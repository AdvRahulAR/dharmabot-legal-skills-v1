---
name: esop-scheme-drafter
description: Drafts employee stock option schemes, grant letters, exercise forms and approval resolutions under the Companies Act 2013 and the Share Capital and Debentures Rules, or the SEBI (Share Based Employee Benefits and Sweat Equity) Regulations 2021 for listed companies, with tax notes on perquisite taxation and the eligible-startup deferral, plus SARs and phantom stock. Use when a client wants an ESOP pool, vesting and cliff, leaver terms or a grant letter. Do not use to model pool dilution; use cap-table-calculator instead.
---

# ESOP Scheme Drafter

Every output is a draft for an advocate enrolled in India to check, with tax points for a chartered accountant.

## Purpose

Draft an ESOP scheme and its supporting documents that the company can lawfully adopt, grant and administer, and that employees can understand.

## Jurisdiction gate

- Confirm the issuer is an Indian company and whether it is private, unlisted public, listed, or a DPIIT-recognised startup.
- Grants to employees of a foreign holding or subsidiary, or to non-resident employees, bring FEMA and foreign securities and tax law: flag for `india-entry-fema-structuring-analyst` and counsel qualified there.
- An LLP cannot issue ESOPs; suggest a phantom or profit-share plan instead.

## Temporal gate

The Income-tax Act 2025 is reported to replace the Income-tax Act 1961 from 1 April 2026; check whether it is in force and from when. Apply the law in force on the grant, vesting, exercise and sale dates, and map renumbered provisions.

## Required inputs

- **Blocking:** company class and listing status; pool size; vesting schedule and cliff; exercise price basis; and the categories of proposed grantees (employees, directors, promoters, consultants, group company staff).
- Useful: DPIIT recognition and its date, the AOA, the SHA (investor consent to the pool), the latest valuation, and the HR policy on exits.

## Method

1. Retrieve the current official text of the Companies Act provision on issue to employees (believed to be section 62(1)(b); confirm), the Share Capital and Debentures Rules on ESOPs, the SBEB Regulations for listed companies, and the current income-tax provisions on ESOP perquisites and startup deferral. Record the version and date.
2. Check eligibility of each grantee category under the retrieved rules. Flag promoters, promoter-group members and directors holding large stakes, and independent directors; their eligibility depends on company type and age (confirm from the text).
3. Check the mandatory scheme contents and the minimum vesting period from the rules.
4. Draft the scheme: definitions; pool and administration; eligibility; grant; vesting (time and performance), cliff and acceleration; exercise period and method (cash, cashless, net settlement where lawful); good and bad leaver and death or disability; corporate actions and adjustment; lock-in; buy-back or liquidity windows; tax withholding; and amendment.
5. Draft the grant letter, exercise form, nomination form and an employee FAQ.
6. Draft the special resolution and explanatory statement disclosures; hand formatting to `board-meeting-documents-drafter`. Note any SHA investor consent.
7. Add tax notes for the CA: perquisite at exercise, the eligible-startup deferral and its conditions, and capital gains on sale. State that the CA confirms.
8. For SARs or phantom stock, draft a cash-settled plan and note that it is not an issue of shares.

## Output

1. ESOP scheme.
2. Grant letter, exercise form and nomination form.
3. Resolution and explanatory statement inputs.
4. Tax and FEMA note with open points.

## Guardrails and hand-offs

- Do not promise employees any tax outcome.
- Do not set the exercise price or fair value; a registered valuer or merchant banker does that.
- Do not state the minimum vesting period or eligibility limits without citing the rule or tagging `[verify]`.
- Pool sizing and dilution go to `cap-table-calculator`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
