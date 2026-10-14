---
name: contract-obligations-tracker
description: Extracts every obligation, condition, payment date, notice requirement, renewal and cancel-by date from contracts into a tracker with owner, trigger and clause reference, and produces upcoming-deadline alerts. Works for contracts under Indian or other law. Use when someone asks to list obligations under an agreement, build a renewal or notice calendar, or track who must do what and by when. Do not use for court or limitation deadlines in a dispute; use matter-deadline-tracker instead.
---

# Contract Obligations Tracker

Every output is a draft tracker for a lawyer or contract manager to review before it is relied on.

## Purpose

Make sure no payment, notice, renewal window or condition is missed, by turning contract text into dated, owned tasks.

## Jurisdiction gate

Note each contract's governing law. Extraction does not depend on jurisdiction. Where a deadline depends on law rather than the contract (for example statutory notice periods, limitation or MSMED Act payment periods), mark it "legal deadline, confirm" and refer it to the advocate.

## Required inputs

Mark as **blocking**:
- the executed contracts with all amendments and schedules;
- the effective date or start date of each contract (if not stated in it);
- which party the client is.

Also useful: names of internal owners by function, the client's calendar or tool format, and how far ahead alerts should go.

## Method

1. Confirm the source set: retrieve the official executed copies and record each document's version and date. Flag drafts or missing amendments.
2. **Extract.** Read every clause, including schedules and definitions. Capture:
   - payment obligations and dates;
   - delivery, performance and reporting obligations;
   - conditions precedent and subsequent;
   - notice requirements (method, address, period);
   - renewal, extension and cancel-by dates;
   - audit, insurance, certification and compliance obligations;
   - post-termination and survival obligations.
3. **Structure each row.** Obligation · obliged party · counterparty · trigger · due date or formula · frequency · notice method · clause · owner · status.
4. **Compute dates.** Apply the contract's own counting rules (business days, "within", "not less than"). Show the formula next to the date. Do not apply legal deadlines yourself.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) The script does the arithmetic only; which legal deadline applies stays with the advocate.
5. **Flag ambiguity.** Where the trigger or period is unclear, say so and give the earliest plausible date as a cautious placeholder, marked as such.
6. **Alerts.** Produce a list of items due in the next 30, 60 and 90 days (or the client's window), with cancel-by dates first.
7. **Cross-check.** Re-read the clause for every computed date and every renewal window.

## Output

1. The tracker as a table or CSV.
2. An upcoming-deadlines alert list.
3. A notes section: ambiguous items, missing documents and legal deadlines for the advocate.

## Guardrails and hand-offs

- Never interpret an ambiguous obligation without flagging it.
- Never invent a date; leave it blank with the reason.
- Notices to be sent go to the advocate; this skill does not send notices.
- For summaries, hand off to `contract-summariser`; for litigation and limitation dates, `matter-deadline-tracker` and `limitation-calculator`.
