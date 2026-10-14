---
name: licence-application-drafter
description: Prepares applications for licences, permits, registrations and approvals before Indian central, State and municipal authorities (for example FSSAI, trade licences, shops and establishments, pollution consents, drug licences), with an eligibility checklist, forms, supporting documents, undertakings, covering letters, and post-grant conditions, renewals and amendments. Use when a client asks to prepare the licence application, compile documents for a registration, or renew or amend a licence. Do not use to decide which licences apply; use regulatory-applicability-analyst first.
---

# Licence Application Drafter

Every output is a draft for an advocate enrolled in India or the client's authorised signatory to check. The client or its authorised professional signs and submits.

## Purpose

Produce a complete, consistent application pack the authority can process without queries.

## Jurisdiction gate

- Confirm the authority, the State or UT, and the municipal body, since forms and fees vary. Open `references/india-state-statutes.md` as a starting point for State laws.
- Confirm the licence category applies (for example central versus State FSSAI licence, or registration only). If unclear, run `regulatory-applicability-analyst` first.

## Required inputs

**Blocking**:
- the licence or registration sought, and the authority;
- applicant details: entity documents, authorised signatory and board resolution or authority letter;
- premises details: address, ownership or lease, layout, and occupancy;
- activity details as the form requires (products, capacity, equipment, staff).

Also useful: earlier licences, inspection reports, and any refusal or query from the authority.

## Method

1. Retrieve the current official form, guidance and fee schedule from the authority's portal (for example the FSSAI online portal, State single-window system, municipal portal) and the governing Act and rules. Record version and date.
2. Build an eligibility checklist from the rules and test each item against the client's facts.
3. Prepare the document checklist: entity proof, identity of signatories, premises proof, NOCs (fire, pollution, building), layout plans, technical staff qualifications, test reports, and declarations.
4. Fill a form draft using only facts supplied. Leave gaps marked "[client to supply]".
5. Draft undertakings, declarations and a covering letter.
6. Cross-check consistency: names, addresses, activity description and capacity must match across every document.
7. List common defects for this authority (for example unsigned pages, expired NOCs, a lease not in the applicant's name, unstamped or unregistered leases). Hand stamping questions to `state-stamp-duty-calculator`.
8. Post-grant: list conditions, display duties, returns, inspections and the renewal date. Hand dates to `compliance-calendar-builder`.
9. For renewals or amendments, check the timing window and late fees in the rules.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.

## Output

1. Eligibility checklist with status.
2. Completed form draft with gaps flagged.
3. Document checklist and index.
4. Covering letter and undertakings.
5. Post-grant compliance list.

## Guardrails and hand-offs

- Never fill in facts, numbers or qualifications not supplied.
- Never prepare a false declaration or backdated document.
- Never submit on the client's behalf; the authorised person submits and pays fees.
- Fees are quoted only from the authority's current schedule.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
