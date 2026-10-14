---
name: special-leave-petition-drafter
description: Drafts special leave petitions to the Supreme Court of India under Article 136 following the Supreme Court Rules, 2013, with synopsis and list of dates, questions of law, grounds, the declaration on annexures, interim relief and condonation of delay, and adapts for transfer petitions under Article 139A and section 25 of the Code of Civil Procedure. Use when an advocate asks to draft an SLP, a Supreme Court appeal against a High Court judgment, or a Supreme Court transfer petition. Do not use for High Court appeals; use civil-appeal-revision-drafter instead.
---

# Special Leave Petition Drafter

Every output is a draft for an Advocate-on-Record to check, settle and file.

## Purpose

Produce an SLP that shows why the case needs the Supreme Court's discretionary jurisdiction, in the format the Registry accepts.

## Jurisdiction gate

Confirm the impugned order is from an Indian court or tribunal and that the Supreme Court is the right next forum. Check first whether a review petition, an intra-court appeal (Letters Patent or similar), or a statutory appeal to the Supreme Court must or should be pursued. Note that only an Advocate-on-Record can file.

## Required inputs

Mark as **blocking**:
- the impugned judgment or order and the orders of the courts below;
- the date of the impugned order and of the certified copy (or the date it was made available);
- the pleadings and key documents from the courts below;
- the client's instructions and whether interim relief is needed.

## Method

1. Retrieve the current Supreme Court Rules, 2013, the Registry's current practice directions and notices on format and paper books, and the Limitation Act provisions for SLPs. Record the version and date.
2. Check maintainability: is an alternative remedy pending or available? Is the order final or interlocutory? Explain the choice.
3. Compute limitation with `limitation-calculator`. If late, draft an application for condonation of delay with day-by-day reasons from the client.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
4. Build the synopsis and list of dates with `litigation-chronology-builder`. Keep it neutral and sourced.
5. Frame questions of law that are general and important, not just re-arguments of fact.
6. Draft grounds, each tied to the impugned findings and the record.
7. Draft the declaration that the annexures were part of the record below (believed to be required under the Rules; confirm the current form), the certificate on the facts, and the affidavit.
8. Draft any interim application (stay, exemption from filing certified copy, permission to file additional documents).
9. For a transfer petition, set out grounds of convenience or fair trial and the cases to be transferred.
10. Search for and read current authority. Tag unread authority `[verify]`.

## Output

1. The draft SLP with synopsis and list of dates, questions of law, grounds and prayer.
2. Interim and condonation applications.
3. A note: maintainability, limitation, annexure list and filing checklist.

## Guardrails and hand-offs

- Never annex documents not on record below without a separate application.
- Never invent citations or misstate the record.
- Before delivery, run `citation-verifier`. Formatting: `court-pleading-formatter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
