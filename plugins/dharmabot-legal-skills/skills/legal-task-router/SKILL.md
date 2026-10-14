---
name: legal-task-router
description: Reads a lawyer's request, the supplied documents and any practice profile (dharmabot-profile.md with home State, courts, languages, citation style, playbooks and house style), identifies the task, forum and urgency, and selects the skills from the Dharmabot collection in the order they should run, confirming the plan before long chains. Use when a lawyer asks "what do we need to do and in what order", "which skill should I use" or gives a new matter without naming a skill. Do not use for business request triage inside a company; use in-house-request-triage-screener instead.
---

# Legal Task Router

Every output is a draft work plan for the advocate in charge to review and approve before any skill runs.

## Purpose

Turn a loosely worded request into the right chain of skills, in the right order, with the inputs each one needs. Catch urgency and limitation first. Do not do the substantive work here.

## Jurisdiction gate

Identify whether the matter is under Indian law, cross-border, or foreign. Identify the State or UT, the likely forum and the court level. Use the profile's home State only as a default; the facts decide. For foreign-law matters, route to `foreign-matter-scoping-analyst` first.

## Required inputs

Mark as **blocking**:
- the request in the lawyer's words;
- for a matter task, the key document or facts (notice, order, FIR, contract) and the date received or served.

Also read, if present in the working folder:
- `dharmabot-profile.md`: practice areas, home State, courts, languages, citation style, playbooks, house style, setting (firm, chamber, in-house, legal aid), and whether client data must be redacted before AI use.

If the profile is absent, ask only what is needed (State, forum, client side) and proceed.

## Method

1. Retrieve the current official text of any statute, notice provision or rule the request depends on only far enough to confirm the forum, whether the law is in force, and whether a time limit runs (India Code, eGazette, court websites). Record version and date. The routed skills do the full legal work.
2. Read the profile and apply its defaults: language, citation style, house style and playbooks to pass to each skill.
3. Classify the request:
   - task type (advice, drafting, review, research, filing, compliance, tracking, translation);
   - practice area and forum;
   - client side and setting;
   - urgency: a hearing, auction, arrest, limitation or regulatory deadline within days.
4. **Urgency first.** If any time limit may run, put `limitation-calculator` first, and `urgent-mentioning-memo-drafter` where same-day relief is needed.
5. **Intake.** For a new client or matter, start with `client-intake-conflict-screener`.
6. **Data protection.** If the profile requires it, or client identifiers will go to an external AI tool, run `client-data-redaction-checker` before any other skill reads client documents.
7. **Choose the core skills.** Pick only ids that exist in this collection. Examples:
   - SARFAESI demand or possession notice: `sarfaesi-enforcement-planner`, then `drt-application-drafter`;
   - bail: `bnss-bail-application-drafter` (after `crpc-bnss-transition-analyst` if dates precede 1 July 2024);
   - contract review: `playbook-contract-reviewer` with the profile's playbook;
   - unclear law: `legal-research-planner`, then `research-memo-drafter`;
   - vernacular exhibits: `court-exhibit-translation-drafter`, then `legal-translation-verifier`;
   - document bundles: `tabular-document-reviewer`.
8. **Workflow recipes.** The repository may contain matter recipes at workflows/*.md (for example a SARFAESI defence or cheque-dishonour recipe). If one matches, follow it and note any step the facts make unnecessary. If none exists or the folder is absent, plan the chain yourself using steps 4 to 9.
9. **Close every drafting chain** with `pre-filing-verification-checker`, after `citation-verifier`, and with `court-ai-policy-checker` where the forum has AI rules.
10. For each skill in the chain, list the inputs it needs and which earlier skill supplies them.
11. **Confirm before running.** Show the plan. If it has more than two skills, or any step sends client data outside the user's machine, wait for the lawyer's approval. Run one skill at a time and report after each.

## Output

1. A one-line reading of the request: task, forum, State, client side, urgency.
2. The plan as a numbered list: skill id · why · inputs needed · input source · output passed on.
3. Blocking questions for the lawyer.
4. The urgent date, if any, at the top in bold.

## Guardrails and hand-offs

- Never invent a skill. Use only ids in this collection; if no skill fits, say so and suggest a manual step.
- Do not draft, advise or compute here. Hand each task to its skill.
- Never skip the redaction step the profile requires, or the final `pre-filing-verification-checker` on a drafting chain.
- Never start a long chain without the lawyer's confirmation.
- Business requests inside a company go to `in-house-request-triage-screener`.
- Once the lawyer approves a multi-skill plan and wants it run end to end, with a ledger and checkpoints, hand it to `legal-workflow-orchestrator`.
