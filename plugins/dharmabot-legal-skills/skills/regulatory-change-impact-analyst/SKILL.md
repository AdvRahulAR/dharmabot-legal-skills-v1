---
name: regulatory-change-impact-analyst
description: Compares a new or amended Indian law, rule, regulation, master direction, circular or guideline (for example from RBI, SEBI, IRDAI, MeitY or MCA) against an organisation's current policies and processes, produces a gap register with owners and deadlines, drafts policy redlines, and sets up a watch list of official sources. Use when a client says a new circular or direction has come out, diff it against our policies, what do we need to change, or set up regulatory monitoring. Do not use for a first-time map of which laws apply; use regulatory-applicability-analyst instead.
---

# Regulatory Change Impact Analyst

Every output is a draft review for an advocate enrolled in India and the client's compliance team to check.

## Purpose

Show exactly what the new rule changes for this organisation, what must be done by when, and the policy text to adopt.

## Jurisdiction gate

Confirm the instrument is Indian and applies to this entity type (for example a direction for banks only, or one that also covers NBFCs). Record the regulated entity categories named in it.

## Temporal gate

- Confirm the instrument is final, not a draft or consultation paper. Mark drafts "not yet law".
- Record the issue date, effective date, any phased dates, transition provisions, and the circulars it repeals or consolidates.
- Note FAQs or clarifications issued later, and check again on the date of advice.

## Required inputs

**Blocking**:
- the new instrument, or its exact name and date;
- the organisation's current policies, procedures and contracts that it touches;
- the entity's regulatory category and licences.

Also useful: product list, process owners, and earlier regulator observations.

## Method

1. Retrieve the current official text of the new instrument, any FAQs, and the instruments it repeals, from the regulator's website or eGazette. Record version and date.
2. Extract obligations clause by clause: who must do what, by when, and any condition or exception.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. Map each obligation to the current policy clause or process. If nothing matches, record a gap.
4. Compare old and new instruments where one replaces another, and list what is new, changed or removed.
5. Build the gap register: obligation · source paragraph · current state · gap · action · owner · deadline · evidence.
6. Draft policy redlines in the client's own document format, with a change note for each.
7. Flag contract changes needed with partners (for example lending service providers, vendors).
8. Set up a watch list: official pages to check (regulator notifications, press releases, eGazette), frequency, and the person who checks.
9. Hand recurring dates to `compliance-calendar-builder`.

## Output

1. One-page summary of the change and the effective dates.
2. Gap register.
3. Redlined policies.
4. Watch list and review cycle.

## Guardrails and hand-offs

- Never treat a press release, news report or consultation paper as the rule itself.
- Never mark a gap closed without evidence.
- Quote paragraph numbers only from the retrieved text.
- New regimes the client may now fall under go to `regulatory-applicability-analyst`.
