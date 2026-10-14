---
name: limitation-calculator
description: Calculates limitation periods and procedural deadlines for Indian proceedings under the Limitation Act, 1963 and special statutes, using a bundled date-arithmetic script that excludes the first day, applies excluded periods (such as time to obtain certified copies) and moves a last day that falls on a court holiday. Use when an advocate asks "what is the last date to file", "is this appeal in time", "is this within time", "when must we reply", "how many days have passed since", or gives a deadline in hours (for example a reply due within 48 hours), or needs a deadline table for a matter. Do not use to decide which limitation article applies when that is disputed; flag it for the advocate.
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

   On Windows, use `py -3` in place of `python3`.

   - `--period` takes `30d`, `3m` or `1y`, or `6h` for a period in hours (then `--start` needs a time, such as `2026-10-15T14:30`).
   - The start date is excluded by default (`--include-start` to change).
   - `--exclude` (repeatable) adds excluded spans, inclusive, such as time taken to obtain copies.
   - `--holidays` is a file of `YYYY-MM-DD` dates when the court is closed, taken from that court's published calendar. If the last day falls on one, the date moves to the next open day. Use `--weekends-closed` only if that court does not sit on any Saturday or Sunday; many courts sit on some Saturdays, so prefer the court's own calendar.
   - Section 4 extends only the prescribed period. Do not use it to extend a condonation window or a period a special statute treats differently (for example the further 30 days believed to be under section 34(3) of the Arbitration and Conciliation Act, 1996; confirm against the official text). Check current authority for the statute in question.
   - `--to` counts the days elapsed between `--start` and that date, both with the start day excluded and with it counted.
   - The script prints its working. Paste the working into the output.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.

4. Check conditions on any extension or exclusion relied on (for example whether a copy application was made within time).
5. State whether delay condonation is available for this proceeding and on what test, citing the provision retrieved, if the date has passed.

## Output

1. A deadline table: proceeding · provision · start event and date · period · exclusions · computed last date · basis.
2. The script's working.
3. Assumptions and open questions (disputed start date, missing holiday list, competing articles).

## Guardrails

- If the user's stated count and the dates disagree, say so before giving any date.
- If the court's holiday list was not supplied, say the date was not adjusted for holidays.
- Never present a computed date without the provision and the working.
- When a deadline is within 7 days, put that first, in bold.
