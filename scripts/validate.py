#!/usr/bin/env python3
"""Lint every skill against the Dharmabot skill standard. Exit 1 on any error.

Checks:
  * SKILL.md frontmatter has exactly name + description; name matches folder,
    is lowercase-hyphen and <= 64 chars; description <= 1024 chars and says
    when NOT to use the skill.
  * Body has the required sections, a jurisdiction gate, and a draft notice.
  * Every skill is in skill-registry.yaml and has generated metadata that is
    up to date (run scripts/build.py).
  * Relative links in SKILL.md resolve; manifests are valid JSON with matching versions.
  * No obvious personal data (Indian mobile numbers, Aadhaar-like numbers) in skills or evals.
"""

import json
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "dharmabot-legal-skills"
SKILLS = PLUGIN / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
REQUIRED_SECTIONS = ["## Purpose", "## Jurisdiction gate", "## Required inputs", "## Method", "## Output", "## Guardrails"]
PII_RES = [
    (re.compile(r"(?<!\d)[6-9]\d{9}(?!\d)"), "possible Indian mobile number"),
    (re.compile(r"(?<!\d)\d{4}\s\d{4}\s\d{4}(?!\d)"), "possible Aadhaar number"),
]

errors = []


def err(path, msg):
    errors.append(f"{path.relative_to(ROOT)}: {msg}")


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if not text.startswith("---") or len(parts) < 3:
        err(path, "missing YAML frontmatter")
        return None, text
    try:
        data = yaml.safe_load(parts[1])
    except yaml.YAMLError as e:
        err(path, f"frontmatter YAML error: {e}")
        return None, text
    return data, parts[2]


def main():
    registry = yaml.safe_load((PLUGIN / "skill-registry.yaml").read_text(encoding="utf-8"))
    reg_ids = [s["id"] for s in registry["skills"]]
    if len(reg_ids) != len(set(reg_ids)):
        err(PLUGIN / "skill-registry.yaml", "duplicate skill ids")

    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for folder in folders:
        skill = folder / "SKILL.md"
        if not skill.exists():
            err(folder, "no SKILL.md")
            continue
        data, body = frontmatter(skill)
        if data is None:
            continue
        if set(data) != {"name", "description"}:
            err(skill, f"frontmatter must have only name and description, found {sorted(data)}")
        name, desc = data.get("name", ""), str(data.get("description", ""))
        if name != folder.name:
            err(skill, f"name {name!r} does not match folder {folder.name!r}")
        if not NAME_RE.match(name or "") or len(name) > 64:
            err(skill, "name must be lowercase-hyphen, at most 64 characters")
        if not 80 <= len(desc) <= 1024:
            err(skill, f"description length {len(desc)} outside 80-1024")
        if "Do not use" not in desc:
            err(skill, "description must say when not to use the skill ('Do not use ...')")
        for section in REQUIRED_SECTIONS:
            if section not in body:
                err(skill, f"missing section {section!r}")
        if "draft" not in body.split("## Purpose")[0].lower() and "review" not in body.split("## Purpose")[0].lower():
            err(skill, "first lines must say the output is a draft or review for a human to check")
        for link in re.findall(r"\]\((?!https?://|#)([^)]+)\)", body):
            if not (folder / link).resolve().exists():
                err(skill, f"broken link {link}")
        for ref in re.findall(r"`((?:references|scripts)/[^`\s]+)`", body):
            if not (folder / ref).exists():
                err(skill, f"mentions {ref} but the file does not exist")
        for other in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+){2,})`", body):
            if other.endswith(("-drafter", "-analyst", "-calculator", "-checker", "-reviewer", "-formatter",
                               "-screener", "-verifier", "-planner", "-mapper", "-coder", "-orchestrator")) and not (SKILLS / other).is_dir():
                err(skill, f"hands off to unknown skill {other}")
        if name not in reg_ids:
            err(skill, "not listed in skill-registry.yaml")
        for generated in ["skill.meta.yaml", "agents/openai.yaml"]:
            if not (folder / generated).exists():
                err(folder, f"missing {generated}; run scripts/build.py")
        meta_path = folder / "skill.meta.yaml"
        if meta_path.exists():
            meta = yaml.safe_load(meta_path.read_text(encoding="utf-8"))
            if meta.get("version") != registry["release"]:
                err(meta_path, "out of date; run scripts/build.py")

    for rid in reg_ids:
        if not (SKILLS / rid).is_dir():
            err(PLUGIN / "skill-registry.yaml", f"lists {rid} but no folder exists")

    versions = {}
    for manifest in [
        ROOT / ".claude-plugin" / "marketplace.json",
        ROOT / ".agents" / "plugins" / "marketplace.json",
        PLUGIN / ".claude-plugin" / "plugin.json",
        PLUGIN / ".codex-plugin" / "plugin.json",
    ]:
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            err(manifest, f"invalid JSON: {e}")
            continue
        if "version" in data:
            versions[manifest] = data["version"]
        for p in data.get("plugins", []):
            if "version" in p:
                versions[manifest] = p["version"]
    for manifest, v in versions.items():
        if v != registry["release"]:
            err(manifest, f"version {v} does not match registry release {registry['release']}")

    for wf in sorted((ROOT / "workflows").glob("*.md")):
        for ref in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", wf.read_text(encoding="utf-8")):
            if ref.endswith(("-drafter", "-analyst", "-calculator", "-checker", "-reviewer", "-formatter", "-screener",
                             "-verifier", "-planner", "-mapper", "-coder", "-builder", "-tracker", "-summariser",
                             "-advisor", "-router", "-orchestrator")) and not (SKILLS / ref).is_dir():
                err(wf, f"names unknown skill {ref}")
    for img in ["banner", "pack-map", "skill-anatomy", "workflow-civil-suit", "install"]:
        if not (ROOT / "docs" / "images" / f"{img}.png").exists():
            err(ROOT / "docs" / "images", f"missing {img}.png referenced by README")

    kinds = {}
    for f in sorted((ROOT / "evals").glob("*.yaml")):
        try:
            cases = (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("cases", [])
        except yaml.YAMLError as e:
            err(f, f"YAML error: {e}")
            continue
        seen = set()
        for c in cases:
            if c.get("id") in seen:
                err(f, f"duplicate case id {c.get('id')}")
            seen.add(c.get("id"))
            if c.get("skill") not in reg_ids:
                err(f, f"case {c.get('id')} names unknown skill {c.get('skill')}")
            kinds.setdefault(c.get("skill"), set()).add(c.get("kind"))
    for rid in reg_ids:
        if not {"output", "gate"} <= kinds.get(rid, set()):
            err(SKILLS / rid, "needs at least one output and one gate eval case in evals/")

    for path in list(SKILLS.rglob("*.md")) + list((ROOT / "evals").rglob("*.yaml")):
        text = path.read_text(encoding="utf-8")
        for pattern, label in PII_RES:
            if pattern.search(text):
                err(path, label)

    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s) found")
        return 1
    print(f"OK: {len(folders)} skills validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
