# Contributing

Thank you for helping. This project is most useful when practising advocates check and improve it.

## Ways to help

- **Review a skill.** Check its method against the current statute, rules and practice in your court. Open an issue with what is wrong or missing, citing the source. If you are an enrolled advocate and want to sign off a skill, say so in the issue; we record reviewers in `skill-registry.yaml`.
- **Report a law change.** Use the "Law changed" issue template: what changed, the notification or amendment, and its date.
- **Add a skill.** Open an issue first describing the task, the jurisdiction and why existing skills do not cover it.
- **Fix the State or foreign-jurisdiction tables.** `shared/references/india-state-statutes.md` and `shared/references/foreign-jurisdictions.md` hold starting points marked "unconfirmed" where they could not be verified. A correction with an official source is very welcome.
- **Add eval cases.** Synthetic facts only (see `evals/README.md`).

## Writing or editing a skill

1. Create `plugins/dharmabot-legal-skills/skills/<name>/SKILL.md`. Use lowercase-hyphen names ending in a role: `-drafter`, `-reviewer`, `-analyst`, `-calculator`, `-checker`, `-planner`, `-formatter`, `-screener`, `-verifier`, `-mapper`, `-coder`, `-builder`, `-tracker`, `-summariser`, `-advisor` or `-router`.
2. Frontmatter has only `name` and `description`. The description has three parts: what the skill does; when to use it, in the words a lawyer would type; and "Do not use ..." with the skill to use instead. Keep it under about 600 characters.
3. Body sections in this order: draft notice line, `## Purpose`, `## Jurisdiction gate`, `## Temporal gate` (criminal and procedure skills), `## Required inputs` (mark **blocking** inputs), `## Method` (step 1 retrieves the current official text), `## Output`, `## Verification` (optional), and `## Guardrails` (or `## Guardrails and hand-offs`).
4. Never put rates, fees, income ceilings or section numbers in a skill as settled facts. If you mention a number to help orientation, say "believed to be ... confirm from the source".
5. Every drafting skill's guardrails must hand off to `pre-filing-verification-checker` before anything is filed or sent.
6. Put any calculation in a script under `scripts/` with unit tests in `tests/`. Use only the Python standard library and no network access.
7. If the skill needs a shared reference table, list it under `shared_refs` in `skill-registry.yaml`; the build copies it into the skill's `references/` folder so the skill works when installed on its own. Edit the file in `shared/references/`, never the copies.
8. Add the skill to `skill-registry.yaml`, then run:

   ```bash
   pip install pyyaml
   python3 scripts/build.py
   python3 scripts/validate.py
   python3 -m unittest discover tests
   ```

9. Add at least one output case and one gate case to `evals/` (the validator checks this).

## Rules

- Never include real client information in skills, evals or issues.
- No advertising of any advocate or firm (Bar Council of India Rules, Rule 36).
- Sign off your commits (`git commit -s`) to certify you have the right to contribute them under the MIT licence (Developer Certificate of Origin).
