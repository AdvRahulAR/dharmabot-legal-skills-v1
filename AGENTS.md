# Instructions for AI agents

This repository contains Dharmabot Legal Skills: Agent Skills (`SKILL.md` folders) for Indian legal practice.

## If you are asked to install these skills

- **Claude Code:** run `claude plugin marketplace add AdvRahulAR/dharmabot-legal-skills-v1`, then `claude plugin install dharmabot-legal-skills@dharmabot`. Tell the user to start a new session or run `/reload-plugins`.
- **Codex:** run `codex plugin marketplace add AdvRahulAR/dharmabot-legal-skills-v1`, then `codex plugin add dharmabot-legal-skills@dharmabot`. Alternatively clone the repo and run `./scripts/install.sh --codex`.
- **Antigravity:** clone the repo and run `./scripts/install.sh --antigravity` (or `--project <dir>` for one workspace).

Afterwards, tell the user that the skills are drafts for review by an enrolled advocate, and point them to `DISCLAIMER.md`.

## If you are asked to change these skills

- Edit `plugins/dharmabot-legal-skills/skills/<name>/SKILL.md` and `skill-registry.yaml`. Do not hand-edit `skill.meta.yaml`, `agents/openai.yaml`, or the `references/` and `scripts/` copies of shared files: they are generated. Shared tables live in `shared/references/` and shared scripts (such as `date_calc.py`) in `shared/scripts/`.
- Follow `CONTRIBUTING.md`, then run `python3 scripts/build.py`, `python3 scripts/validate.py` and `python3 -m unittest discover tests`. All must pass.
- Do not add rates, fees or section numbers as settled facts, and do not add real client data.
