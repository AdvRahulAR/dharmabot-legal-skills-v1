---
name: commercial-suit-filing-checker
description: Checks whether a dispute is a commercial dispute under the Commercial Courts Act, 2015 and whether a commercial suit is ready to file, covering specified value, the correct Commercial Court or Commercial Division, pre-institution mediation under section 12A or a case for urgent interim relief, statement of truth, document disclosure and High Court practice directions. Use when an advocate asks whether a matter is commercial or whether a commercial plaint is ready. Do not use to draft the plaint; use plaint-drafter instead.
---

# Commercial Suit Filing Checker

Every output is a review for an advocate enrolled in India to check before filing.

## Purpose

Give a go or no-go list for filing a commercial suit, so it is not returned, rejected or delayed on threshold grounds.

## Jurisdiction gate

Confirm Indian law governs and identify the State and district. Note whether the High Court has original civil jurisdiction (for example Delhi, Bombay, Calcutta, Madras, Himachal Pradesh) and whether a Commercial Division or a Commercial Court at district level is competent.

## Temporal gate

Check the current state of pre-institution mediation: the Commercial Courts (Pre-Institution Mediation and Settlement) Rules, the Mediation Act, 2023 and any amendment to section 12A. Check whether each relevant provision is in force and from when, and record the date checked. Also check the current specified value as notified.

## Required inputs

Mark as **blocking**:
- the draft plaint or a summary of the claim and reliefs;
- the transaction documents, to classify the dispute;
- the claim value and how it is computed;
- whether mediation under section 12A was attempted, with the non-starter or failure report if any;
- whether urgent interim relief is sought, and why.

## Method

1. Retrieve the current official text of the Commercial Courts Act, 2015, its schedule amendments to the CPC, the pre-institution mediation rules, the specified-value notification and the High Court's commercial practice directions. Record the version and date. Confirm every section, order and rule number used in this skill against that text.
2. Classify: does the dispute fall within a listed category of "commercial dispute" in the Act? Explain the category and the documents showing it.
3. Value: compute the specified value under the Act's own valuation rules, not just the principal claim.
4. Forum: identify the correct court by value, territory and the State's notification.
5. Section 12A: either mediation was exhausted (attach the report), or the plaint genuinely seeks urgent interim relief. Test urgency on the facts. Courts look through artificial urgency. For example, see Patil Automation Pvt Ltd v Rakheja Engineers Pvt Ltd (Supreme Court, 2022) on the mandatory nature of section 12A; confirm current treatment and later authority.
6. Pleading checks: statement of truth in the prescribed form; documents disclosure affidavit; list of documents in power and possession; verification; Order VII particulars.
7. Court fee and limitation: confirm with `state-court-fee-calculator` and `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
8. Practice directions: e-filing format, page limits, case management hearing preparation, and any High Court-specific annexures.

## Output

1. A go or no-go table: requirement · status (met, not met, unclear) · evidence · fix.
2. A list of defects in priority order.
3. A short recommendation: file, mediate first, or reframe as an ordinary suit.

## Guardrails and hand-offs

- Do not draft or redraft the plaint; send defects to `plaint-drafter`.
- Mediation steps: `pre-institution-mediation-advisor`.
- Never certify that a filing will be accepted.
- Tag any authority not read in full `[verify]`.
