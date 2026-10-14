---
name: pollution-consent-compliance-checker
description: Checks an Indian unit's compliance with the Water Act 1974 and Air Act 1981 as amended (consent to establish and operate, conditions, environmental compensation) and the waste rules (hazardous, bio-medical, plastic, e-waste, battery, construction and demolition) with Extended Producer Responsibility registration and targets. Use when a client asks about CTE or CTO, consent conditions, a State board inspection, hazardous waste authorisation or EPR filings. Do not use for EIA or forest clearance; use environmental-clearance-analyst.
---

# Pollution Consent Compliance Checker

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Produce a gap list showing where the unit's consents, conditions and waste obligations stand, and what to fix first.

## Jurisdiction gate

Confirm the unit is in India and identify the State or UT. The State Pollution Control Board (or Pollution Control Committee in a UT) sets the industry category (red, orange, green, white), consent fees, validity and online procedure. Note if the unit is in a notified industrial estate or critically polluted area.

## Temporal gate

The Air Act was amended by the Jan Vishwas (Amendment of Provisions) Act, 2023 and the Water Act by an amendment Act of 2024, which applies in a State only after adoption. Check whether a later Jan Vishwas amendment has changed penalties. Waste rules and EPR targets are replaced or amended often. Record the date of each document reviewed.

## Required inputs

Mark as **blocking**:
- the State and the unit's activity, products and capacity;
- copies of the current consent to establish and consent to operate, with their conditions and validity;
- the waste streams generated and any authorisations held.

Also useful: the last board inspection report, show-cause or closure notices, monitoring reports, annual returns, EPR registrations and the unit's role (producer, importer, brand owner, recycler).

## Method

1. Retrieve the current official text of the Water Act, Air Act, Environment (Protection) Act, the relevant waste rules and the CPCB category list, and the State board's consent manual and circulars. Record versions and dates. Open `references/india-state-statutes.md` for the State's starting points.
2. Confirm the industry category and whether the consents held match actual capacity, products and location. Expansion or product-mix change without fresh consent is a common defect.
3. Read every consent condition. Mark each: complied, partly complied, not complied, or no evidence. Watch effluent and emission standards, online monitoring, stack height, ZLD conditions, groundwater and bank guarantees.
4. Check each waste stream against its rules: authorisation, storage period, manifest system, annual return, and disposal through an authorised facility.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
5. Check EPR. Identify which regimes apply (plastic packaging, e-waste, batteries, tyres, used oil), registration on the CPCB portal, targets, certificates bought, and filing deadlines. Mark each target "to be checked live".
6. Check exposure: environmental compensation assessed by the board, penalties after decriminalisation, adjudicating officer procedure, and closure or utilities-disconnection powers.
7. Note pending NGT or court orders affecting the area or industry. Search for and read current authority; tag anything not read in full `[verify]`.

## Output

1. A gap table: obligation · source · status · evidence · risk (high, medium, low) · fix · owner.
2. A list of State board circulars and CPCB notices to check live.
3. A 30-60-90 day remediation plan.

## Guardrails and hand-offs

- Never certify a unit as compliant; this is a review of documents supplied.
- Never suggest bypassing monitoring, diluting samples or backdating records.
- For a show-cause or closure notice, hand off to `regulator-notice-reply-drafter`.
- For new projects or expansions needing EIA or forest clearance, hand off to `environmental-clearance-analyst`.
- Before delivery, send citations to `citation-verifier`.
