---
name: matter-closure-retention-checker
description: Runs the closure checklist for an Indian legal matter, covering the final bill and unclaimed client money, return of original documents with acknowledgement, a retention period set against limitation for professional claims and client instructions, deletion of personal data no longer needed under the DPDP Act, 2023, an archive index and conflict-register update. Use when a lawyer says "close this file", "what do we keep and for how long" or "return the originals to the client". Do not use to draft the client closure report; use client-status-update-drafter instead.
---

# Matter Closure and Retention Checker

Every output is a draft checklist for the advocate in charge of the matter to review.

## Purpose

Close a matter cleanly: nothing owed or held for the client is left behind, originals go back, records are kept for as long as needed and no longer.

## Jurisdiction gate

Confirm the practice is in India and note the State or UT and the State Bar Council. Note any client located abroad whose data law may also apply.

## Temporal gate

DPDP Act, 2023 duties on erasure and retention are being brought into force in phases under the DPDP Rules, 2025. Check which apply on the closure date.

## Required inputs

Mark as **blocking**:
- the matter's final status (decreed, executed, settled, withdrawn, transferred, instructions withdrawn) and the final order;
- the list of original documents held, with who supplied them;
- the client's instructions on return, retention or destruction, if any.

Also useful: the ledger of client money and fees, the engagement letter's retention clause, linked matters, and any pending appeal or limitation for appeal.

## Method

1. Retrieve the current official text of the BCI Rules on professional conduct (client money, accounts, documents), the DPDP Act and Rules on erasure and retention, and any tax or other law that sets record-keeping periods for the practice. Record version and date.
2. Confirm the matter is really closed: no appeal, review or execution window still open. Compute remaining windows with `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Finance: final bill, fees received, unbilled time, and any client money or court deposit to refund or account for. Hand narratives to `time-billing-narrative-drafter`.
4. Originals: list each original, its location, and return it against signed acknowledgement. Do not hold originals against unpaid fees without checking current authority on an advocate's lien (for example R.D. Saxena v. Balram Prasad Sharma, Supreme Court, 2000; confirm current treatment).
5. Retention: set a retention period for the file copy that covers limitation for any claim against the practice, tax and record-keeping laws, and client instructions. Record the reason for the period chosen.
6. Personal data: identify data no longer needed for any purpose, including copies in email, AI tools and shared drives. Schedule secure deletion and log it.
7. Archive: build an index of what is kept, where and until when. Update the conflict register with parties and the closure date.

## Output

1. Closure checklist with status and owner for each item.
2. Originals return schedule with acknowledgement form.
3. Retention and deletion schedule: record · location · retain until · reason · deletion method.
4. Archive index and conflict-register entry.

## Guardrails and hand-offs

- Never destroy anything while an appeal, claim or legal hold is possible.
- Never state a retention period as mandatory unless the retrieved text says so.
- The client closure letter goes to `client-status-update-drafter`; a client's erasure request goes to `data-principal-request-drafter`.
