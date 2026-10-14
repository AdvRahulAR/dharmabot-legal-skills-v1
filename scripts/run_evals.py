#!/usr/bin/env python3
"""Run eval cases through Claude Code with this plugin loaded, and grade them.

Each case's prompt is sent to a fresh headless Claude Code session
(`claude -p`) started in an empty temporary folder, with the local plugin
loaded through --plugin-dir. The transcript is parsed for the skills used,
shell commands and the final answer. Two checks then decide the result:

  * a deterministic check that the expected skill fired (for `trigger` cases,
    that it fired or did not, as `should_trigger` says);
  * a model grader (a second `claude -p` call returning JSON) that marks each
    `must` and `must_not` line pass or fail with a reason.

A case passes only if both pass. The grader is a model: spot-check its verdicts.

Usage (on Windows use `py -3` in place of `python3`):
    python3 scripts/run_evals.py --dry-run --pack criminal-bnss
    python3 scripts/run_evals.py --pack criminal-bnss --pack cross-border
    python3 scripts/run_evals.py --case bail-date-mismatch --workers 1
    python3 scripts/run_evals.py --out eval-results/run1 --resume --pack core

Runs use --setting-sources project, so your own user-level plugins and settings are not loaded and
cannot compete with these skills. Needs Claude Code on PATH, signed in. Each case costs API usage (roughly
$0.15-0.60 per case plus a few cents to grade); use --dry-run first.
This is a developer tool and uses the network; skill scripts do not.
"""

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "dharmabot-legal-skills"
EVALS = ROOT / "evals"
EST_COST_PER_CASE = 0.36
ALLOWED_TOOLS = ["Skill", "Read", "Glob", "Grep", "WebSearch", "WebFetch", "Bash", "PowerShell"]

GRADE_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "kind": {"type": "string", "enum": ["must", "must_not"]},
                    "text": {"type": "string"},
                    "pass": {"type": "boolean"},
                    "reason": {"type": "string"},
                },
                "required": ["kind", "text", "pass", "reason"],
            },
        }
    },
    "required": ["items"],
}

GRADER_PROMPT = """You are grading one response from an AI legal assistant against a fixed rubric.
Today's date is {today}. Judge only from the response and the tool summary below; do not use outside knowledge to excuse a gap.

Rubric:
- For each MUST line: pass = true only if the response clearly does it (or, where the line is about tools, the tool summary shows it).
- For each MUST NOT line: pass = true only if the response does NOT do the forbidden thing.
- Be strict. A partial or vague attempt fails. Give a one-sentence reason quoting or pointing to the response.
Return one item per rubric line, in order, copying the line text exactly.

CASE: {id} (skill {skill}, kind {kind})
USER PROMPT:
{prompt}

MUST:
{must}

MUST NOT:
{must_not}

TOOL SUMMARY:
skills used: {skills}
shell commands run: {commands}
tool errors: {errors}

RESPONSE:
{answer}
"""


def load_pack_map():
    reg = yaml.safe_load((PLUGIN / "skill-registry.yaml").read_text(encoding="utf-8"))
    return {s["id"]: s["pack"] for s in reg["skills"]}


def load_cases(evals_dir=EVALS):
    cases = []
    for f in sorted(evals_dir.glob("*.yaml")):
        for c in (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("cases", []):
            c = dict(c)
            c["file"] = f.name
            cases.append(c)
    return cases


def select_cases(cases, pack_map, packs=(), skills=(), ids=(), files=()):
    out = []
    for c in cases:
        if packs and pack_map.get(c.get("skill")) not in packs:
            continue
        if skills and c.get("skill") not in skills:
            continue
        if ids and c.get("id") not in ids:
            continue
        if files and c.get("file") not in files:
            continue
        out.append(c)
    return out


def should_trigger(case):
    """Whether the case's own skill is expected to fire."""
    if "should_trigger" in case:
        return bool(case["should_trigger"])
    marker = f"uses {case.get('skill')}"
    if any(marker in str(m) for m in case.get("must_not", []) or []):
        return False
    return True


def parse_transcript(lines):
    """Pull skills, shell commands, tool errors, final answer, cost and turns from stream-json lines."""
    info = {"skills": [], "commands": [], "errors": [], "answer": "", "cost": None, "turns": None, "is_error": None}
    for line in lines:
        try:
            ev = json.loads(line)
        except (json.JSONDecodeError, TypeError):
            continue
        msg = ev.get("message") if isinstance(ev.get("message"), dict) else {}
        content = msg.get("content") if isinstance(msg.get("content"), list) else []
        if ev.get("type") == "assistant":
            for block in content:
                if block.get("type") != "tool_use":
                    continue
                inp = block.get("input") or {}
                if block.get("name") == "Skill":
                    info["skills"].append(str(inp.get("skill") or inp.get("command") or inp))
                elif block.get("name") in ("Bash", "PowerShell"):
                    info["commands"].append(str(inp.get("command", "")))
        elif ev.get("type") == "user":
            for block in content:
                if block.get("type") == "tool_result" and block.get("is_error"):
                    info["errors"].append(str(block.get("content"))[:300])
        elif ev.get("type") == "result":
            info["answer"] = ev.get("result") or ""
            info["cost"] = ev.get("total_cost_usd")
            info["turns"] = ev.get("num_turns")
            info["is_error"] = ev.get("is_error")
    return info


def skill_fired(skills_used, skill):
    return any(s == skill or s.endswith(":" + skill) for s in skills_used)


def claude_bin():
    found = shutil.which("claude")
    if not found:
        sys.exit("Claude Code (`claude`) was not found on PATH.")
    return found


def run_case(case, out, model=None, budget=None, timeout=1200):
    transcript = out / f"{case['id']}.jsonl"
    prompt = " ".join(str(case["prompt"]).split())
    cmd = [claude_bin(), "-p", "--plugin-dir", str(PLUGIN), "--output-format", "stream-json", "--verbose",
           "--no-session-persistence", "--permission-prompts", "none", "--setting-sources", "project",
           "--allowedTools", *ALLOWED_TOOLS]
    if model:
        cmd += ["--model", model]
    if budget:
        cmd += ["--max-budget-usd", str(budget)]
    start = time.time()
    with tempfile.TemporaryDirectory(prefix="dharmabot-eval-") as work:
        try:
            with open(transcript, "w", encoding="utf-8") as fh:
                proc = subprocess.run(cmd, input=prompt, cwd=work, stdout=fh, stderr=subprocess.PIPE, text=True,
                                      encoding="utf-8", errors="replace", timeout=timeout)
            status = proc.returncode
        except subprocess.TimeoutExpired:
            status = "timeout"
    info = parse_transcript(transcript.read_text(encoding="utf-8", errors="replace").splitlines())
    info["status"] = status
    info["seconds"] = round(time.time() - start)
    return info


def grade(case, info, grader_model="sonnet", timeout=600):
    must = case.get("must", []) or []
    must_not = case.get("must_not", []) or []
    if not must and not must_not:
        return [], 0.0
    prompt = GRADER_PROMPT.format(
        today=dt.date.today().isoformat(), id=case["id"], skill=case.get("skill"), kind=case.get("kind"),
        prompt=" ".join(str(case["prompt"]).split()),
        must="\n".join(f"- {m}" for m in must) or "(none)",
        must_not="\n".join(f"- {m}" for m in must_not) or "(none)",
        skills=info["skills"] or "none", commands=info["commands"] or "none", errors=info["errors"] or "none",
        answer=info["answer"] or "(no answer)",
    )
    cmd = [claude_bin(), "-p", "--model", grader_model, "--output-format", "json", "--no-session-persistence",
           "--tools", "", "--json-schema", json.dumps(GRADE_SCHEMA)]
    with tempfile.TemporaryDirectory(prefix="dharmabot-grade-") as work:
        proc = subprocess.run(cmd, input=prompt, cwd=work, capture_output=True, text=True,
                              encoding="utf-8", errors="replace", timeout=timeout)
    try:
        data = json.loads(proc.stdout)
        items = (data.get("structured_output") or {}).get("items", [])
        cost = data.get("total_cost_usd") or 0.0
    except (json.JSONDecodeError, AttributeError):
        items, cost = [], 0.0
    expected = len(must) + len(must_not)
    if len(items) != expected:
        items = [{"kind": "must", "text": "(grader)", "pass": False,
                  "reason": f"grader returned {len(items)} items for {expected} rubric lines"}]
    return items, cost


def evaluate(case, out, pack_map, args):
    result_path = out / f"{case['id']}.result.json"
    if args.resume and result_path.exists():
        return json.loads(result_path.read_text(encoding="utf-8"))
    info = run_case(case, out, model=args.model, budget=args.budget_usd)
    fired = skill_fired(info["skills"], case.get("skill"))
    expect = should_trigger(case)
    trigger_ok = fired == expect
    items, grade_cost = grade(case, info, grader_model=args.grader_model)
    passed = trigger_ok and info["status"] == 0 and all(i.get("pass") for i in items)
    result = {
        "id": case["id"], "file": case["file"], "skill": case.get("skill"), "pack": pack_map.get(case.get("skill")),
        "kind": case.get("kind"), "expected_trigger": expect, "skills_used": info["skills"], "trigger_ok": trigger_ok,
        "status": info["status"], "seconds": info["seconds"], "turns": info["turns"], "commands": info["commands"],
        "tool_errors": len(info["errors"]), "items": items, "passed": passed,
        "cost_run": info["cost"] or 0.0, "cost_grade": grade_cost,
    }
    result_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return result


def summarise(results):
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    by = {}
    for key in ("pack", "skill", "kind"):
        groups = {}
        for r in results:
            g = groups.setdefault(r.get(key) or "?", [0, 0])
            g[0] += 1
            g[1] += 1 if r["passed"] else 0
        by[key] = groups
    return {
        "total": total, "passed": passed, "failed": total - passed,
        "trigger_failures": sum(1 for r in results if not r["trigger_ok"]),
        "cost": round(sum((r.get("cost_run") or 0) + (r.get("cost_grade") or 0) for r in results), 2),
        "by": by,
    }


def report_md(results, summary, meta):
    pct = (100 * summary["passed"] / summary["total"]) if summary["total"] else 0
    lines = [
        "# Eval report", "",
        f"Run {meta['started']} · Claude Code {meta['claude_version']} · run model {meta['model'] or 'default'} · "
        f"grader {meta['grader_model']}", "",
        f"**{summary['passed']} of {summary['total']} cases passed ({pct:.0f}%).** "
        f"Skill-trigger failures: {summary['trigger_failures']}. Cost: ${summary['cost']}.", "",
        "A case passes only if the expected skill fired (or did not, for negative trigger cases) and a model grader "
        "marked every `must` and `must_not` line as met. The grader is a model; its verdicts should be spot-checked.", "",
        "## By pack", "", "| Pack | Passed | Total |", "| --- | --- | --- |",
    ]
    lines += [f"| {k} | {v[1]} | {v[0]} |" for k, v in sorted(summary["by"]["pack"].items())]
    lines += ["", "## By kind", "", "| Kind | Passed | Total |", "| --- | --- | --- |"]
    lines += [f"| {k} | {v[1]} | {v[0]} |" for k, v in sorted(summary["by"]["kind"].items())]
    lines += ["", "## Failures", ""]
    fails = [r for r in results if not r["passed"]]
    if not fails:
        lines.append("None.")
    else:
        lines += ["| Case | Skill | Why it failed |", "| --- | --- | --- |"]
        for r in fails:
            why = []
            if not r["trigger_ok"]:
                why.append("expected skill " + ("did not fire" if r["expected_trigger"] else "fired")
                           + f" (used: {', '.join(r['skills_used']) or 'none'})")
            if r["status"] != 0:
                why.append(f"run status {r['status']}")
            for i in r["items"]:
                if not i.get("pass"):
                    why.append(f"{i.get('kind')}: {i.get('text')} ({i.get('reason')})")
            text = "; ".join(why).replace("|", "/").replace("\n", " ")
            lines.append(f"| {r['id']} | {r['skill']} | {text} |")
    return "\n".join(lines) + "\n"


def main(argv=None):
    p = argparse.ArgumentParser(description="Run and grade eval cases through Claude Code.",
                                formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    p.add_argument("--pack", action="append", default=[])
    p.add_argument("--skill", action="append", default=[])
    p.add_argument("--case", action="append", default=[])
    p.add_argument("--file", action="append", default=[], help="eval file name, e.g. v0.1-cases.yaml")
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--model", help="model for the run (default: Claude Code's default)")
    p.add_argument("--grader-model", default="sonnet")
    p.add_argument("--budget-usd", type=float, help="per-case spending cap passed to claude --max-budget-usd")
    p.add_argument("--out", help="output folder (default eval-results/<timestamp>)")
    p.add_argument("--resume", action="store_true", help="skip cases that already have a result in --out")
    p.add_argument("--dry-run", action="store_true", help="list the selected cases and an estimated cost, then stop")
    args = p.parse_args(argv)

    pack_map = load_pack_map()
    unknown = set(args.pack) - set(pack_map.values())
    if unknown:
        p.error(f"unknown pack(s): {sorted(unknown)}")
    cases = select_cases(load_cases(), pack_map, set(args.pack), set(args.skill), set(args.case), set(args.file))
    if not cases:
        p.error("no cases selected")
    if args.dry_run:
        for c in cases:
            print(f"{c['id']:60} {c.get('kind', '?'):8} {c.get('skill')}")
        print(f"\n{len(cases)} case(s); estimated cost about ${len(cases) * EST_COST_PER_CASE:.0f} (rough).")
        return 0

    out = pathlib.Path(args.out) if args.out else ROOT / "eval-results" / dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    out.mkdir(parents=True, exist_ok=True)
    version = subprocess.run([claude_bin(), "--version"], capture_output=True, text=True).stdout.strip()
    meta = {"started": dt.datetime.now().isoformat(timespec="minutes"), "claude_version": version,
            "model": args.model, "grader_model": args.grader_model}
    results = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(evaluate, c, out, pack_map, args): c for c in cases}
        for fut in cf.as_completed(futures):
            c = futures[fut]
            try:
                r = fut.result()
            except Exception as e:  # keep the batch going; record the failure
                r = {"id": c["id"], "file": c["file"], "skill": c.get("skill"), "pack": pack_map.get(c.get("skill")),
                     "kind": c.get("kind"), "expected_trigger": should_trigger(c), "skills_used": [],
                     "trigger_ok": False, "status": f"error: {e}", "items": [], "passed": False,
                     "cost_run": 0.0, "cost_grade": 0.0}
            results.append(r)
            print(f"[{len(results)}/{len(cases)}] {'PASS' if r['passed'] else 'FAIL'} {r['id']}", flush=True)
    results.sort(key=lambda r: r["id"])
    summary = summarise(results)
    (out / "results.json").write_text(json.dumps({"meta": meta, "summary": summary, "results": results}, indent=2),
                                      encoding="utf-8")
    (out / "report.md").write_text(report_md(results, summary, meta), encoding="utf-8")
    print(f"\n{summary['passed']}/{summary['total']} passed; cost ${summary['cost']}. Report: {out / 'report.md'}")
    return 0 if summary["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
