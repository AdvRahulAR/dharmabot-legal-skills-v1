---
name: limitation-calculator
description: Calculates limitation periods and procedural deadlines for Indian proceedings under the Limitation Act, 1963 and special statutes, using a bundled date-arithmetic script that excludes the first day, applies excluded periods (such as time to obtain certified copies) and moves a last day that falls on a court holiday. Use when an advocate asks "what is the last date to file", "is this appeal in time", or needs a deadline table for a matter. Do not use to decide which limitation article applies when that is disputed; flag it for the advocate.
---

# Limitation Calculator

Every output is a draft for an advocate enrolled in India to check. Missing a limitation date can end a case; treat every result as needing confirmation.

## Purpose

Identify the period, the date it starts, any time excluded, and the last date, with every step shown.

## Jurisdiction gate

Confirm the proceeding is in India. Identify whether the Limitation Act, 1963 or a special statute (for example the Commercial Courts Act, Arbitration and Conciliation Act, Consumer Protection Act, NI Act, BNSS, rent control or tax laws) fixes the period, and whether the Limitation Act applies to it.

## Required inputs

Mark as **blocking**: the proceeding to be filed (suit, appeal, revision, application, complaint); the event that starts time (date of decree or order, date of knowledge, date of breach, date of notice and so on); and the forum.

Also useful: the date of applying for a certified copy and the date the copy was made ready (notified as ready), not the date it was collected, since courts generally exclude only the time requisite to obtain the copy; periods spent in another forum in good faith; dates of acknowledgment or part payment; the court's holiday list for the relevant year.

## Method

1. Retrieve the current official text of the provision fixing the period (the article of the Schedule to the Limitation Act, or the special statute) and any provision on exclusion or extension (for example sections 4, 12, 14, 18 and 19 of the Limitation Act). Confirm the numbers and wording from the source.
2. State the period and the starting event, and why that article applies. If more than one article could apply, list them and do not choose; flag it.
3. Compute with the bundled script, never by mental arithmetic:

   ```
   python3 scripts/date_calc.py --start 2026-03-10 --period 90d \
       --exclude 2026-03-12:2026-03-30 --holidays holidays.txt --json
   ```

   - `--period` takes `30d`, `3m` or `1y`.
   - The start date is excluded by default (`--include-start` to change).
   - `--exclude` (repeatable) adds excluded spans, inclusive, such as time taken to obtain copies.
   - `--holidays` is a file of `YYYY-MM-DD` dates when the court is closed, taken from that court's published calendar. If the last day falls on one, the date moves to the next open day. Use `--weekends-closed` only if that court does not sit on any Saturday or Sunday; many courts sit on some Saturdays, so prefer the court's own calendar.
   - Section 4 extends only the prescribed period. Do not use it to extend a condonation window or a period a special statute treats differently (for example the further 30 days under section 34(3) of the Arbitration and Conciliation Act, 1996). Check current authority for the statute in question.
   - The script prints its working. Paste the working into the output.

4. Check conditions on any extension or exclusion relied on (for example whether a copy application was made within time).
5. State whether delay condonation is available for this proceeding and on what test, citing the provision retrieved, if the date has passed.

## Output

1. A deadline table: proceeding · provision · start event and date · period · exclusions · computed last date · basis.
2. The script's working.
3. Assumptions and open questions (disputed start date, missing holiday list, competing articles).

## Guardrails

- If the court's holiday list was not supplied, say the date was not adjusted for holidays.
- Never present a computed date without the provision and the working.
- When a deadline is within 7 days, put that first, in bold.
