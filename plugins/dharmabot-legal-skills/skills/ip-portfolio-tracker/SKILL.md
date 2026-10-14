---
name: ip-portfolio-tracker
description: Audits and tracks an Indian IP portfolio of trademarks, patents, designs and copyrights by office and class, covering status, renewals and annuities, statements of working, oppositions, licences and encumbrances, and chain-of-ownership gaps, and produces upcoming-deadline alerts. Use when a client asks for a trademark or patent docket, a renewal schedule, an IP audit before a fundraise, or a list of ownership gaps. Do not use for filing a new trademark; use trademark-application-drafter instead.
---

# IP Portfolio Tracker

Every output is a draft tracker for an advocate or IP agent in India to review.

## Purpose

Give the client one reliable record of what IP it owns, what is due, and what must be fixed.

## Jurisdiction gate

Confirm the portfolio covers Indian filings. Foreign filings can be listed, but their dates and status must be confirmed by local counsel or the foreign office record.

## Required inputs

Mark as **blocking**:
- the list of rights to track, with application or registration numbers, or the client's documents from which to build it;
- the legal name of the current owner of each right, and of the client group entities.

Also useful: licences, assignments, security interests, pending oppositions and litigation, and the client's own docket export.

## Method

1. Retrieve the current status of each right from the official records (Trade Marks Registry, Patent Office, Design Office, Copyright Office), and the current Rules on renewal and annuity periods and fees. Record the date each record was checked.
2. Build the tracker row for each right: type · number · mark or title · class or field · owner on record · status · filing and registration dates · next deadline · action.
3. Compute deadlines from the official dates and the Rules: trademark renewals, patent annuities, statements of working, design renewals, and pending response or opposition deadlines. Confirm each period from the Rules and use `limitation-calculator` where helpful.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. Compare the owner on record with the actual owner. Flag gaps: rights in a founder's or former entity's name, unrecorded assignments, name changes after merger, and missing licences.
5. Flag encumbrances and licences, and any rights at risk (non-use, lapsed, abandoned).
6. Flag coverage gaps: core brands not filed in key classes, or unregistered logos.
7. Produce alerts sorted by date, with lead time.

## Output

1. The portfolio tracker as a table (or CSV on request).
2. An upcoming-deadlines list for the next 6 and 12 months.
3. An ownership-gap list with fixes.

## Guardrails and hand-offs

- Record only what the registers or client documents show; mark anything unconfirmed.
- Never invent registration numbers or dates.
- For new filings, hand off to `trademark-application-drafter`.
- For licence obligations, hand off to `contract-obligations-tracker`.
