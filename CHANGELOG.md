# Changelog

## Unreleased

Fixes from a stress test on 2 November 2026 (static audit of all 318 skills, bundled-script edge cases, and seven adversarial prompts run through headless Claude Code).

- **Default bail counting corrected.** `bnss-bail-application-drafter` no longer treats "does the remand day count?" as an open point. It is settled by the three-judge bench in *Enforcement Directorate v. Kapil Wadhawan* (2023 INSC 723): the period runs from the first remand and the remand day is day one. The skill now always passes `--include-start`, states that the right accrues on day 61 (or 91) and is defeated only by a charge sheet filed before the application, and tells the advocate to file at the first moment the court is open that day, before the duty magistrate on a holiday, never to wait for the next working day. In testing, the old wording led to advice to "file Monday in practice" when the right accrued on a Sunday. `arrest-rights-advisor` and `undertrial-release-screener` carry the same rule.
- **Commencement dates stated as fact.** Eighteen skills said laws were "reported to" be in force. The Income-tax Act, 2025 (1 April 2026), the four Labour Codes (21 November 2025), the DPDP Rules, 2025 phases (13 November 2025, 13 November 2026, 13 May 2027), the IBC (Amendment) Act, 2026 (assent 6 April 2026, phased commencement) and the omission of s.213 of the Indian Succession Act by the Repealing and Amending Act, 2025 (assent 20 December 2025) are now stated plainly with their source. Hedges stay only where the position is genuinely open (State rules under the Labour Codes, IBC commencement notifications, s.213 and pending proceedings, Assam's code).
- **`date_calc.py` hardened.** A bad date, a `--to` before `--start` or a missing holiday file now gives a one-line `date_calc.py: error:` message and exit code 2 instead of a traceback. Zero and negative periods are rejected. When the last day falls on a Saturday or Sunday and no holiday rule was applied, the working carries a WARNING line. Five new unit tests.
- **Install guidance.** With all 318 skills loaded, the agent answered six of seven adversarial prompts without loading any skill; with one 21-skill pack it loaded the right skill at once. README, `AGENTS.md` and `install.py` now steer users to `--pack` installs and warn on a full install.
- **New `evals/adversarial.yaml`** (7 cases): prompt injection inside a contract clause, a request to drop [verify] tags on a time-barred s.138 notice, a false affidavit, naming a POCSO victim, a fabricated SCC citation, the default-bail remand-day count, and a Kerala rent-control trigger. Run with `python3 scripts/run_evals.py --file adversarial.yaml`.
- `scripts/build.py --check` rebuilds and fails if any generated file changed; CI uses it. `--help` no longer rebuilds. Plugin manifests now say 318 skills, matching the catalogue.

- New `legal-workflow-orchestrator` (core pack) runs an approved multi-skill plan end to end: matter ledger, STOP checkpoints, hand-off checks after each skill, parallel steps where inputs are independent, re-planning and resume. `legal-task-router` now hands approved plans to it. `-orchestrator` is a new allowed role suffix.

## 0.1.1 (2026-10-15), alpha

Fixes from live testing. Every legal point added is hedged or tagged [verify] and needs review by an enrolled advocate.

- `bnss-bail-application-drafter` now runs a default-bail gate before drafting any grounds. The gate counts custody from the first remand order, takes the limit from BNSS s.187(3) (both limits are shown where the 60-day or 90-day reading is disputed), and computes the days with `date_calc.py`. If the limit has passed and no charge sheet has been filed, the output leads with a **DEFAULT BAIL MAY HAVE ACCRUED** flag and hands off to `undertrial-release-screener`. The first remand date, charge-sheet status and maximum punishment are now blocking inputs.
- 137 skills that turn on a time period now compute it from the actual dates with `scripts/date_calc.py`. Where the user's stated count disagrees with the dates, they flag it and ask which is right.
- `date_calc.py` has moved to `shared/scripts/`. The build now copies it into each skill that lists it under `shared_scripts`. A new `--to` option counts the days elapsed between two dates, both with and without the start day.
- `foreign-judgment-award-enforcement-analyst` now has two separate tracks: A for foreign court judgments (s.44A and s.13 CPC) and B for foreign arbitral awards (Part II, the s.44 notified countries). It never uses one list to answer a question about the other.
- Section numbers, thresholds and status claims that were stated as settled are now hedged across the skills.
- `foreign-judgment-award-enforcement-analyst` and the shared foreign-jurisdictions table now warn that Explanation 2 to s.44A CPC is believed to exclude arbitration awards from "decree". Executing a seat-court judgment on an award under s.44A is therefore presented only as a contested option [verify].
- `arbitral-proceedings-drafter` notes that, for an international commercial arbitration, the twelve-month award period is believed to be only a target under the proviso to s.29A(1).
- Seven family and succession skills now give the reported status of the Gujarat and Assam uniform civil codes: Gujarat assent reported September 2026, commencement awaiting State notification; Assam passed by the Assembly May 2026, assent not confirmed [verify].
- `pmla-proceedings-analyst` now lists all four classes believed to be covered by the proviso to s.45(1), and notes that the benefit is discretionary [verify].
- `date_calc.py` now handles periods in hours (`--start 2026-10-15T14:30 --period 6h`). `data-breach-response-planner`, `it-rules-intermediary-compliance-checker` and `pocso-case-analyst` now use it. `registry-letter-drafter` still hands all time computation to `limitation-calculator`, by design.
- Hedged further statements that were given as settled: Railway Claims Tribunal exclusivity, post-exit non-competes under s.27 of the Contract Act, and the Gazette part for name changes.
- 373 eval cases have been added since 0.1.0 (1012 in total).

## 0.1.0 (2026-10-14), alpha

First public release. Law as of 14 October 2026. Every skill was reviewed for legal accuracy after drafting; none has yet been signed off by an enrolled advocate.

**317 skills in 39 packs**, covering the full range of Indian legal work, all 36 States and Union Territories, Indian languages, and cross-border work with the US, UK, UAE, EU and Singapore. The full list is in [docs/CATALOGUE.md](docs/CATALOGUE.md).

**Coverage**
- Mapped against more than 700 skills in published legal skill collections:
  - Anthropic's claude-for-legal and knowledge-work legal plugin;
  - Rohas Nagpal's Legal AI Skills;
  - Lawve and Lawvable;
  - UK, US and Indian repositories.
- A second gap analysis (October 2026) covered daily court practice, tribunals and recent regulation. From 117 suggestions, 54 new skills were added and 57 were already covered.
- New packs:
  - court craft (cause lists, e-filing defects, vakalatnama, adjournment, condonation, restoration, amendment, substitution, compromise, caveat, mentioning, hearing-day briefs);
  - tribunal practice;
  - client documents;
  - sectoral regulatory (RBI digital lending and Master Directions, FEMA compounding, SEBI AIFs and others);
  - emerging technology and climate (DPDP consent managers, dark patterns, carbon credits, deepfake remedies);
  - AI practice safeguards;
  - review and analysis (tabular review, pleadings matrix).

**Safeguards**
- `pre-filing-verification-checker` checks every authority and quotation against an official source and keeps a log. Every drafting skill hands off to it, following the Supreme Court's ruling in *Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd.* (2026 INSC 668) that citing unverified AI-generated judgments is misconduct.
- `client-data-redaction-checker` pseudonymises client data before AI processing.
- Temporal gates handle recent changes:
  - the IBC (Amendment) Act, 2026;
  - the Income-tax Act, 2025;
  - the Labour Codes;
  - the DPDP Rules phasing;
  - the 2026 IT Rules amendment;
  - the Online Gaming Act;
  - the Press Note 3 relaxation;
  - the omission of compulsory probate.

**Workflows and profile**
- Ten matter recipes in `workflows/`, each with STOP checkpoints for the advocate.
- `legal-task-router` chooses skills and recipes.
- A practice profile template in `templates/dharmabot-profile.md`.

**Reference tables**
- `shared/references/india-state-statutes.md`: court fees, stamp, tenancy, High Court, rules of practice and official languages for every State and UT. Unverified rows are marked.
- `shared/references/foreign-jurisdictions.md`: India's treaty position with the US, UK, UAE, EU and Singapore, official sources, professional rules and data-protection regimes.

**Tooling**
- Plugin manifests for Claude Code and Codex.
- An install script for Codex, Antigravity and Claude Code that can install single packs.
- A build script that generates metadata, the catalogue and copies of shared references.
- A validator that checks:
  - the skill standard;
  - hand-offs, and the skills named in workflows;
  - eval coverage;
  - personal data.
- Unit tests for the bundled scripts, and 639 behavioural eval cases.
- README images in `docs/images/`.
