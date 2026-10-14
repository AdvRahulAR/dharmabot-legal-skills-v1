---
name: maintenance-petition-drafter
description: Drafts maintenance claims in India for spouses, children and parents under the Bharatiya Nagarik Suraksha Sanhita, 2023 (formerly section 125 CrPC), the Hindu Marriage Act, 1955, the Hindu Adoptions and Maintenance Act, 1956, the DV Act and the Senior Citizens Act, 2007, with the Rajnesh v. Neha disclosure affidavit and a transparent quantum model. Use when a lawyer asks for an interim maintenance application, a wife's or child's maintenance petition, a parent's claim against children, or enforcement of arrears. Do not use to assess divorce grounds; use divorce-grounds-analyst.
---

# Maintenance Petition Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Choose the best maintenance route, draft the application and disclosure affidavit, and show a reasoned range for the amount.

## Jurisdiction gate

Confirm the claimant and respondent, their personal law, and where each resides. Identify the available routes and fora: Magistrate under the BNSS, Family Court under personal law, Magistrate under the DV Act, or the Maintenance Tribunal under the Senior Citizens Act. Check whether a State uniform civil code changes the position (Uttarakhand in force; Gujarat's code reportedly received the President's assent in September 2026 and comes into force on a date the State notifies; Assam's bill was reportedly passed by the Assembly in May 2026, with assent not confirmed; check assent, commencement and coverage, including any Scheduled Tribe exclusion [verify]).

## Temporal gate

The BNSS replaced the CrPC from 1 July 2024. The maintenance provision is believed to be section 144 BNSS; confirm. For applications filed before that date, the CrPC provision continues to govern; check with `crpc-bnss-transition-analyst` where dates straddle it.

## Required inputs

Mark as **blocking**:
- the relationship and the marriage or birth particulars;
- date of separation and whether the claimant has been neglected or refused maintenance;
- the claimant's income, assets and needs;
- the respondent's income and assets, with whatever evidence exists (salary slips, ITRs, business records);
- all pending proceedings and any earlier maintenance orders.

## Method

1. Retrieve the current official text of the BNSS maintenance provision, the relevant personal law provisions, the DV Act and the Senior Citizens Act, and the court's format. Record the version and date.
2. Choose routes. Several can run together, but the court must take earlier awards into account (Rajnesh v. Neha, Supreme Court, 2020; confirm current treatment).
3. Draft the application: relationship, neglect or refusal, claimant's inability to maintain herself or himself, respondent's means, and prayer for interim and final maintenance from the date the court fixes (Rajnesh v. Neha addressed the date of award; confirm).
4. Prepare the affidavit of assets and liabilities in the format the Supreme Court prescribed in Rajnesh v. Neha, adapted to the forum.
5. Quantum model: start from net income after statutory deductions, list each dependant's reasonable needs, consider the standard of living during marriage and the claimant's own income. Show two or three scenarios with the arithmetic. Label it a negotiating and pleading aid only.
6. Enforcement: arrears, distress warrants and sentence for wilful default, attachment of salary; check the limitation for recovering arrears with `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
7. Search for and read current authority on quantum and earning spouses; tag anything not read `[verify]`.

## Output

1. Draft application with interim relief.
2. Draft disclosure affidavit.
3. Quantum worksheet with assumptions.
4. Note on parallel remedies and enforcement.

## Guardrails

- Never present a model figure as what the court will award.
- Never invent income figures; mark estimates and their basis.
- Never advise hiding income or assets.
- A regional-language version goes to `regional-language-legal-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
