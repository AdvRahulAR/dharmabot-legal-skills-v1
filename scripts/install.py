#!/usr/bin/env python3
"""Install Dharmabot Legal Skills into Claude Code, Codex or Antigravity by
copying the skill folders. Works on Windows, macOS and Linux; standard library only.
(Claude Code users can also use the plugin marketplace; see README.)

  python3 scripts/install.py --claude           ~/.claude/skills/
  python3 scripts/install.py --codex            ~/.agents/skills/
  python3 scripts/install.py --antigravity      ~/.gemini/config/skills/
  python3 scripts/install.py --antigravity-cli  ~/.gemini/antigravity-cli/skills/ (path unconfirmed)
  python3 scripts/install.py --project DIR      DIR/.claude/skills and DIR/.agents/skills
  python3 scripts/install.py --all              Claude Code, Codex and Antigravity user locations
  python3 scripts/install.py --dest DIR         any other skills folder

On Windows use `py -3` (or `py`) in place of `python3`.
Add --pack NAME (repeatable) to install only some packs; --list-packs shows them.
"""

import argparse
import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "plugins" / "dharmabot-legal-skills" / "skills"
REGISTRY = ROOT / "plugins" / "dharmabot-legal-skills" / "skill-registry.yaml"

USER_TARGETS = {
    "claude": (".claude", "skills"),
    "codex": (".agents", "skills"),
    "antigravity": (".gemini", "config", "skills"),
    # Reported by third-party sources only; confirm against the Antigravity CLI's own docs.
    "antigravity_cli": (".gemini", "antigravity-cli", "skills"),
}


def read_registry(path=REGISTRY):
    """Return ([(skill_id, pack)], {pack_id: title}) without needing PyYAML.

    In the registry each skill's "- id:" line is followed by its "pack:" line,
    and each pack's "- id:" line by its "title:" line.
    """
    skills, packs, current = [], {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*-\s+id:\s*(\S+)\s*$", line)
        if m:
            current = m.group(1)
            continue
        if current is None:
            continue
        m = re.match(r"^\s*pack:\s*(\S+)\s*$", line)
        if m:
            skills.append((current, m.group(1)))
            current = None
            continue
        m = re.match(r"^\s*title:\s*(.+?)\s*$", line)
        if m:
            packs[current] = m.group(1)
            current = None
    return skills, packs


def select(skills, wanted_packs):
    if not wanted_packs:
        return [s for s, _ in skills]
    return [s for s, p in skills if p in wanted_packs]


def install(skill_ids, dest, src=SRC):
    dest = pathlib.Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    for sid in skill_ids:
        target = dest / sid
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(src / sid, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    return len(skill_ids)


def targets_from(args, home):
    out = []
    for key in ("claude", "codex", "antigravity", "antigravity_cli"):
        if getattr(args, key):
            out.append(home.joinpath(*USER_TARGETS[key]))
    if args.all:
        out += [home.joinpath(*USER_TARGETS[k]) for k in ("claude", "codex", "antigravity")]
    for d in args.project:
        out += [pathlib.Path(d) / ".claude" / "skills", pathlib.Path(d) / ".agents" / "skills"]
    out += [pathlib.Path(d) for d in args.dest]
    unique = []
    for t in out:
        if t not in unique:
            unique.append(t)
    return unique


def main(argv=None, home=None):
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                     formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    parser.add_argument("--claude", action="store_true", help="~/.claude/skills")
    parser.add_argument("--codex", action="store_true", help="~/.agents/skills")
    parser.add_argument("--antigravity", action="store_true", help="~/.gemini/config/skills")
    parser.add_argument("--antigravity-cli", dest="antigravity_cli", action="store_true",
                        help="~/.gemini/antigravity-cli/skills (path unconfirmed)")
    parser.add_argument("--all", action="store_true", help="Claude Code, Codex and Antigravity user locations")
    parser.add_argument("--project", action="append", default=[], metavar="DIR",
                        help="DIR/.claude/skills and DIR/.agents/skills (repeatable)")
    parser.add_argument("--dest", action="append", default=[], metavar="DIR", help="any skills folder (repeatable)")
    parser.add_argument("--pack", action="append", default=[], metavar="NAME", help="install only this pack (repeatable)")
    parser.add_argument("--list-packs", action="store_true", help="list pack ids and exit")
    args = parser.parse_args(argv)
    home = pathlib.Path(home) if home else pathlib.Path.home()

    skills, packs = read_registry()
    if args.list_packs:
        for pid, title in packs.items():
            count = sum(1 for _, p in skills if p == pid)
            print(f"{pid:32} {count:3}  {title}")
        return 0
    unknown = set(args.pack) - set(packs)
    if unknown:
        parser.error(f"unknown pack(s): {', '.join(sorted(unknown))}; see --list-packs")
    targets = targets_from(args, home)
    if not targets:
        parser.print_help()
        return 2

    chosen = select(skills, set(args.pack))
    for dest in targets:
        n = install(chosen, dest)
        print(f"Installed {n} skill(s) into {dest}")
    if args.antigravity_cli:
        print("Note: the Antigravity CLI skills path is unconfirmed; check the CLI's documentation.")
    print("Restart your agent (or reload skills) to pick them up.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
