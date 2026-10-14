---
name: legal-workflow-orchestrator
description: Runs a multi-skill legal matter end to end. Calls the right Dharmabot skills in order (in parallel where inputs are independent), passes each output on, keeps a matter ledger of facts, dates and approvals, enforces STOP checkpoints, re-plans when facts change and resumes a half-finished matter. Use when a lawyer says "run this matter", "take it from notice to filing", "handle all of this" or "carry on from where we stopped". Do not use only to pick skills; use legal-task-router. Do not use for one task one skill covers.
---

# Legal Workflow Orchestrator

Every output is a draft for the advocate in charge to review and approve. The orchestrator moves work between skills; it never replaces the advocate's decisions.

## Purpose

Carry a matter through several skills without losing facts, dates or approvals between them. `legal-task-router` decides what should run. This skill runs it: it calls each skill, checks what came back, records it, stops where the advocate must decide, and picks the matter up again in a later session.

## Jurisdiction gate

- Fix the governing law, forum, State or UT and client side once, at the start, and write them in the ledger. Every skill called inherits them.
- If the facts later point to another forum, State or a foreign element (a foreign party, seat, document or asset), stop, update the ledger, and re-plan before the next call. For foreign-law points, call `foreign-matter-scoping-analyst` first.
- Use the profile's home State only as a default; the facts decide.

## Temporal gate

Before any step that drafts, files or sends, confirm in the ledger that every limitation, notice and hearing date has been computed by `limitation-calculator` (or `scripts/date_calc.py` for a plain count) and logged with `matter-deadline-tracker`. Where the facts straddle a change in the law (for example events before and after 1 July 2024 under the criminal codes), run the relevant transition skill before drafting. Never carry a date forward from a skill's output without its working.

## Required inputs

**Blocking**:
- the lawyer's goal in their own words;
- the key documents or facts, and the date each was received or served;
- confirmation of who the client is and which side they are on.

Also read, if present in the working folder:
- `dharmabot-profile.md` (State, courts, languages, citation style, playbooks, house style, redaction rule);
- `matter-ledger.md`, if the matter was started earlier. If it exists, resume from it (step 12) instead of starting again.

## Method

1. **Retrieve and confirm the basics.** Confirm from the official source (India Code, eGazette, the court's website) only what the plan depends on: that the law in question is in force and the forum is right. Record the version and date in the ledger. The called skills do the full legal retrieval.
2. **Open the ledger.** Create `matter-ledger.md` in the working folder using the layout under Output. It holds no client names, addresses or identifiers if the profile requires redaction; use short matter codes instead.
3. **Get a plan.** If the lawyer has not given an approved plan or a recipe, call `legal-task-router`. If a recipe in `workflows/` fits, use it and note the steps the facts make unnecessary. For cost, staffing and a critical path on a long matter, also call `matter-plan-builder`. Number the steps in the ledger.
4. **Check the plan against the collection.** Use only skills that exist in the installed collection. Read each skill's own description and required inputs before calling it. If no skill fits a step, mark it **manual** in the ledger and tell the lawyer; do not improvise a skill.
5. **Get approval to run.** Show the plan: step, skill, input needed, source of that input, output passed on, STOP or not. Wait for the lawyer's approval if the chain has more than two skills, if any step sends client data outside the lawyer's machine, or if any step will produce something that leaves the firm.
6. **Run in a fixed order.**
   1. Intake and conflict (`client-intake-conflict-screener`) for a new matter.
   2. Redaction (`client-data-redaction-checker`) if the profile requires it, before any other skill reads client documents.
   3. Limitation and deadlines (`limitation-calculator`, then `matter-deadline-tracker`).
   4. Facts and issues (for example `litigation-chronology-builder`, `issue-spotting-analyst`).
   5. Substantive analysis, then drafting.
   6. Verification: `citation-verifier`, `court-ai-policy-checker` where the forum has AI rules, then `pre-filing-verification-checker`.
7. **Call one skill at a time unless inputs are independent.** Skills that need only the same upstream facts (for example a research memo and a chronology) may be given to separate subagents at once. A step that needs another step's output waits. Give each subagent only the ledger extract and documents it needs, the skill's name, and the instruction to return a draft and its open points. Never let parallel steps edit the same document.
8. **Hand-off check after every skill.** Before the next step, read the output and ask:
   - did it ask a blocking question that has not been answered;
   - did it flag a discrepancy, a missing document, a gate failure or a date that may have run;
   - does it contradict a fact or date already in the ledger.

   If yes to any, stop and put the point to the lawyer. Do not pass a flagged output on as if it were clean.
9. **STOP checkpoints.** Stop and wait for the advocate's approve, edit or reject at: the end of intake; after the limitation computation; after issue-spotting and before choosing a course; before any draft is finalised; and before anything is filed, sent, signed or paid. A silent or ambiguous reply is not approval. Record the decision, the date and the version approved in the ledger.
10. **Pass outputs forward by reference.** Give the next skill the approved version of the earlier output, with its date and the ledger's fact table, not a recollection of it. If the lawyer edited a draft, use the edited version.
11. **Re-plan on change.** When new facts, an order, a notice, a hearing or a settlement offer arrives, add it to the ledger with its date, then decide which completed steps are now stale. Mark them **superseded**, add the steps that follow, and show the lawyer the revised plan before continuing. Re-run `limitation-calculator` if any date moved.
12. **Resume.** On a later session, read the ledger first. Report: where the matter stands, the next three dates, the steps done, the steps waiting for the advocate, and what is blocked. Confirm nothing has changed since the last entry before running the next step.
13. **Close.** When the chain ends, check that every drafting step passed through `pre-filing-verification-checker` and that every approval is recorded. Offer `client-status-update-drafter` for the client note, and `matter-closure-retention-checker` if the matter is ending.

## Output

At each turn, a short status in this order:

1. **Next urgent date**, in bold, with the skill that computed it.
2. Where the matter stands: step number, what was just done, what the advocate must decide now.
3. The result of the hand-off check for the step just finished.
4. The next step and the skill it will call, or the question blocking it.

The ledger `matter-ledger.md` has these sections: matter code, forum, State and client side; fact table (fact, date, source document); deadline table (event, date, computed by, in tracker yes/no); step table (number, skill, status: pending, running, waiting for advocate, approved, superseded, manual; output location; approval date); open questions; and a change log.

## Guardrails and hand-offs

- Never invent a skill, a date, a hearing, a fee or an authority. Mark unknowns.
- Do not do the substantive work here. Hand each task to its skill, and each date to `limitation-calculator`.
- Never skip a STOP, the redaction step the profile requires, or the final `pre-filing-verification-checker` on a chain that ends in a filing, notice or signed document.
- Never file, send, sign, pay or contact anyone on the lawyer's or client's behalf. The advocate does that.
- Never run a long or parallel chain without the lawyer's approval of the plan.
- Do not put rates, fees or section numbers in the ledger as settled facts; copy them only from the skill that retrieved them, with its source.
- If two skills give conflicting answers on the same point, show both and the reason for the difference, and ask the advocate. Do not choose silently.
- If a skill's output fails its own gate or the lawyer rejects it, stop that branch, record why, and re-plan; do not retry the same call unchanged.
- Choosing skills without running them goes to `legal-task-router`; a costed plan goes to `matter-plan-builder`.
