---
name: tax-appeal-grounds-drafter
description: Drafts appeals against Indian tax orders, covering appeals to the CIT(A) and ITAT, High Court appeals on substantial questions of law, GST first appeals and appeals to the GST Appellate Tribunal, with statement of facts, grounds, stay applications and pre-deposit computation, and plans the litigation route. Use when a lawyer asks to draft grounds of appeal, a stay application or a pre-deposit computation against an assessment or GST order. Do not use to reply to a notice before an order is passed; use income-tax-notice-reply-drafter or gst-notice-reply-drafter.
---

# Tax Appeal Grounds Drafter

Every output is a draft for an advocate or chartered accountant in India to check.

## Purpose

Choose the right remedy against a tax order and draft grounds, facts and stay papers that are complete, in time and properly funded.

## Jurisdiction gate

Confirm the order is from an Indian income-tax or GST authority and identify the forum: CIT(A) or the Joint Commissioner (Appeals), ITAT, GST appellate authority, GSTAT bench, or High Court. Note the State for GST and for the jurisdictional High Court.

## Temporal gate

The Income-tax Act, 2025 came into force on 1 April 2026; confirm which Act governs the appeal. The GSTAT became functional recently and special filing timelines applied to backlog appeals; check the current notified deadlines. Record the order date and date of service.

## Required inputs

Mark as **blocking**:
- the order appealed, with the date of service;
- the notice and reply that preceded it;
- the amount of tax, interest and penalty demanded;
- any tax already paid against the demand.

Also useful: the assessment record, evidence filed below, and earlier appellate orders on the same issue.

## Method

1. Retrieve the current official text of the appeal provisions, rules, forms, fee schedule and pre-deposit rules for the forum, and any CBDT or CBIC instruction on stay. Record versions and dates. Do not state pre-deposit percentages or fees from memory.
2. Compute limitation with `limitation-calculator`. If late, draft a condonation application with documented reasons.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. Choose the route: appeal, revision, rectification, writ, or a dispute-resolution scheme. Explain why in a short table.
4. Draft a neutral statement of facts.
5. Draft grounds: concise, numbered, one issue each, with general and alternative grounds. Cover jurisdiction, limitation, natural justice, merits, and interest and penalty.
6. Flag grounds not raised below. Note whether additional grounds or additional evidence will need permission, and draft that application where needed.
7. Compute the pre-deposit and draft the stay application. Show the arithmetic.
8. For a High Court appeal, frame substantial questions of law tied to the record.
9. Search for and read current authority; tag unread authority `[verify]`.

## Output

1. A route note with recommendation.
2. Draft grounds and statement of facts in the prescribed form.
3. The stay application and pre-deposit computation.

## Guardrails and hand-offs

- Never promise success or a stay.
- Never add facts not on record.
- Notice-stage work goes to `income-tax-notice-reply-drafter` or `gst-notice-reply-drafter`.
- Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
