---
name: matter-deadline-tracker
description: Keeps a case diary across Indian matters from cause lists, daily orders and correspondence, recording next dates, filing and reply deadlines, compliance directions in court orders and statutory timelines, and produces weekly roll-ups. Use when a lawyer, team or legal-aid clinic asks to update the case diary, list what is due this week, check whether an order has been complied with, or build a hearing calendar. Do not use to compute limitation; use limitation-calculator for that.
---

# Matter Deadline Tracker

Every output is a draft case diary for the responsible advocate to review against the court record.

## Purpose

Make sure no hearing, filing deadline or compliance direction is missed, and that every date in the diary can be traced to its source.

## Jurisdiction gate

- Record for each matter the court or forum, the State or UT, and the case number.
- Court calendars, vacation benches and e-filing practice differ by High Court and district; use the court's own website and notified holiday list.

## Required inputs

**Blocking**: for each matter, the case number and forum, and the source of every date (cause list, order, notice, letter). A date with no source is not entered; ask for the source.

Also useful: the existing diary, the advocate responsible, the client, and the court's holiday list for the year.

## Method

1. Retrieve the current official cause list, daily order or case status page from the court's website or eCourts services, and record the date and time it was read. Re-check before relying on any next date.
2. For each order, extract every direction with a time limit: file reply, deposit amount, produce documents, comply with an undertaking, appear in person. Note who must act and by when.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. Record statutory timelines only when the advocate supplies them or they come from `limitation-calculator` with the source provision. Do not compute them here.
4. Note where a time limit runs from receipt or service rather than the order date, and ask for the date of receipt.
5. Flag clashes: two matters at the same time in different courts, and dates falling on court holidays.
6. Mark each entry: confirmed (source checked), provisional (source not yet seen), or overdue.
7. Build the roll-up for the period requested, sorted by date, with owner and next action.
8. For compliance checks, compare what the order required against what the file shows was done, and list gaps.

## Output

1. Case diary table: matter · forum · date · event or direction · owner · source · status.
2. Roll-up for the requested period (next 7 or 14 days by default).
3. Compliance checklist for each order with directions.
4. Clash and risk list.

## Guardrails and hand-offs

- Never invent, estimate or assume a date. Missing dates are shown as missing.
- Never treat a provisional entry as confirmed.
- The advocate remains responsible for the court record; tell them to verify against the official listing.
- For limitation or statutory periods, hand off to `limitation-calculator`.
- For client updates on the dates, hand off to `client-status-update-drafter`.
