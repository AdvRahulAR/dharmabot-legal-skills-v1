---
name: matter-plan-builder
description: Builds a working plan for a legal matter in India or abroad, with stages, tasks, owners, dependencies, critical path, a stage-wise cost estimate and a risks, assumptions, issues and decisions log, and records scope changes against a baseline. Use when a lawyer asks for a matter plan, case plan, work plan, project plan, budget or cost estimate for a suit, arbitration, transaction or compliance project. Do not use to decide strategy or merits; use litigation-strategy-planner for that.
---

# Matter Plan Builder

Every output is a draft plan for the responsible advocate or supervising counsel to review.

## Purpose

Turn an agreed scope into a plan the team can run: who does what, by when, in what order, at what cost, and what could derail it.

## Jurisdiction gate

- Record the governing law, forum and seat (court, tribunal, arbitral institution or regulator) and the State or UT.
- Stages differ by forum. A commercial suit, a writ, a consumer complaint and an arbitration each have their own sequence; take it from the procedural law for that forum, not from a generic template.
- For foreign-law workstreams, mark the steps as to be confirmed by counsel qualified in that jurisdiction.

## Required inputs

**Blocking**:
- the agreed scope (engagement letter or scope note);
- the forum and the current stage of the matter;
- the team and their roles.

Also useful: known dates (next hearing, filing deadlines), fee model and budget cap, client approvals needed, and similar past matters for cost benchmarks.

## Method

1. Retrieve the current official procedural text for the forum (for example the CPC as amended by the Commercial Courts Act, the High Court's original side rules, the arbitral institution's rules) and record the version and date. Use it to list the stages.
2. Break each stage into tasks with a deliverable, an owner and an effort estimate.
3. Mark dependencies (for example no written statement before receipt of documents) and identify the critical path.
4. Add dates only where they are given or computed by `limitation-calculator`. Otherwise show durations, not dates.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
5. Build the cost estimate stage by stage: professional fees, counsel fees, court fees (from `state-court-fee-calculator`), stamp duty, expert, travel and translation. Give a range and state the assumptions behind it.
6. Build the RAID log:
   - Risks: event, likelihood, impact, mitigation, owner.
   - Assumptions: what the estimate depends on.
   - Issues: problems already present.
   - Decisions: what was decided, by whom, on what date.
7. Record the baseline. When scope changes, add a change entry with the effect on tasks, dates and cost, and note that client approval is needed.

## Output

1. Plan table: stage · task · owner · depends on · effort · due (if known).
2. Critical path summary in five lines or fewer.
3. Stage-wise cost estimate with assumptions and a range.
4. RAID log.
5. Change log (empty at baseline).

## Guardrails and hand-offs

- Do not decide strategy, merits or settlement value; record decisions made by the advocate.
- Never invent a hearing date, deadline or fee figure; mark unknowns.
- Cost estimates are estimates, not quotations; say so.
- Send dates and deadlines to `matter-deadline-tracker`.
- Send client-facing summaries to `client-status-update-drafter`.
