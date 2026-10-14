---
name: ibc-application-drafter
description: Tests and drafts applications to the NCLT under the Insolvency and Bankruptcy Code, 2016, covering the operational creditor demand notice and application, financial creditor and corporate applicant petitions, and personal guarantor insolvency, with checks on default threshold, limitation and pre-existing dispute. Use when a lawyer asks for an IBC demand notice, a section 7 or section 9 petition, or whether IBC is the right route for an unpaid debt. Do not use for steps after admission; use cirp-ppirp-timeline-checker.
---

# IBC Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Decide whether an IBC application is maintainable and wise, and if so draft it in the prescribed form with the evidence the NCLT will look for.

## Jurisdiction gate

Confirm the debtor is a corporate person (or a personal guarantor to one) registered in India, and identify the NCLT bench by the registered office. Partnerships, individuals other than personal guarantors, and financial service providers have separate or excluded regimes; confirm. Note any parallel proceedings against the same debtor.

## Temporal gate

The IBC and its regulations are amended often. The Insolvency and Bankruptcy Code (Amendment) Act, 2026 is reported to have received assent on 6 April 2026, with provisions brought into force from 26 May 2026 by notification; confirm from the eGazette which provisions are in force and any transitional rule. It is reported to change admission timelines, withdrawal under section 12A (believed to be the section; confirm against the official text) and to add a creditor-initiated insolvency route. Check which amendments, notifications and forms are in force on the filing date. Also check the default threshold in force on the date of default, since it has changed before.

## Required inputs

Mark as **blocking**:
- the creditor's role (financial, operational, corporate applicant, personal guarantor);
- the debt documents: agreements, invoices, ledgers, acknowledgments;
- the date of default and the amount in default;
- for an operational creditor, any correspondence showing a dispute before the demand notice.

Also useful: information utility records, the debtor's master data, earlier recovery proceedings, and the creditor's authorisation.

## Method

1. Retrieve the current official text of the IBC, the Insolvency (Application to Adjudicating Authority) Rules, the relevant forms, the default threshold notification and the NCLT Rules. Record versions and dates. Section numbers are orientation only.
2. Confirm the debt is financial or operational debt as defined, and that default exceeds the notified threshold.
3. Compute limitation from the date of default with `limitation-calculator`, counting acknowledgments in the balance sheet or otherwise only where documented.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
4. Operational creditor: test for a pre-existing dispute under Mobilox Innovations v. Kirusa Software (Supreme Court, 2017; confirm current treatment). If a real dispute exists, advise against IBC.
5. Draft the demand notice (or invoice route) and track service and the debtor's reply period.
6. Draft the application in the prescribed form, with the default record (from an information utility where available), the proposed IRP's consent, and fee proof.
7. Personal guarantor: check Part III provisions in force, the interim moratorium, and the resolution professional's report stage.
8. For an eligible financial creditor, compare the NCLT application with the creditor-initiated route reported to be added by the 2026 amendment; confirm eligibility from the official text.
9. Flag when the creditor seeks recovery against a solvent debtor, since the NCLT may treat this as misuse and costs may follow. Suggest alternatives where better.
10. Search for and read current authority; tag unread authority `[verify]`.

## Output

1. A maintainability note: debt type, default, threshold, limitation, dispute, recommendation.
2. The draft demand notice and application with annexure list.
3. A filing checklist and what happens at admission.

## Guardrails and hand-offs

- Never use IBC as a threat to extract payment of a genuinely disputed claim.
- Never invent invoices, dates or acknowledgments.
- Strategy choices go to `litigation-strategy-planner`; post-admission timelines to `cirp-ppirp-timeline-checker`.
- Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
