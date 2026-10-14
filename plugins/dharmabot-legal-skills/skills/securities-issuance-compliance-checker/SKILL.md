---
name: securities-issuance-compliance-checker
description: Maps approvals, eligibility, pricing and filings for issuing securities by private placement, rights issue or preferential allotment under the Companies Act 2013 and its Share Capital and Prospectus rules, and for listed entities the SEBI ICDR Regulations 2018, with FEMA reporting flags for non-resident subscribers. Use when a client plans a private placement, rights issue, preferential allotment or bonus and needs the steps and documents. Do not use to choose between convertible instruments; use convertible-instrument-analyst instead, and leave valuation to a registered valuer.
---

# Securities Issuance Compliance Checker

Every output is a draft for an advocate or company secretary in India to check.

## Purpose

Lay out the correct route, sequence, documents and filings for an issue of securities, and flag defects that make the allotment invalid or the money a deposit.

## Jurisdiction gate

- Confirm the issuer is an Indian company and its class (private, public unlisted, listed, startup). Listed issuers also follow ICDR and LODR.
- Any non-resident subscriber, or a resident subscriber with foreign ownership, brings FEMA pricing and reporting: hand off to `india-entry-fema-structuring-analyst`.

## Temporal gate

Record the proposed board, shareholder and allotment dates. Check recent amendments to the private placement rules, ICDR and FEMA reporting, and apply the text in force on each step.

## Required inputs

- **Blocking:** issuer class; instrument and terms; number, identity and residency of proposed allottees; amount and price; the route (private placement, rights, preferential, bonus, ESOP).
- **Blocking:** the current authorised capital and the AOA provisions on issue and pre-emption.
- Useful: the SHA (pre-emption and investor consent), the valuation report, earlier offers in the same year, and the cap table.

## Method

1. Retrieve the current official text of the Companies Act provisions on private placement and further issue (believed to be sections 42 and 62; confirm), the Share Capital and Debentures Rules, the Prospectus and Allotment of Securities Rules, the Deposits Rules, and for listed issuers ICDR. Record the version and date.
2. Choose the route and confirm its conditions. For private placement check: the cap on the number of offerees in a financial year (excluding exempted classes), the minimum investment size, the offer letter in PAS-4, the record of offers in PAS-5, and the separate bank account.
3. Check pricing: valuation by a registered valuer where the rules require it; ICDR pricing for listed preferential issues; FEMA floor or ceiling for non-residents.
4. Check approvals: board; special resolution where required, with the prescribed explanatory statement; investor consent under the SHA; increase in authorised capital if needed.
5. Sequence the steps: board approval, valuation, shareholder approval, offer, money received only from the allottee's own bank account, allotment within the prescribed time, PAS-3 and other filings, share certificates or demat credit.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
6. Flag defects that commonly go wrong: money received before the offer, cash, third-party payments, allotment after the deadline, utilisation before allotment, and offerees beyond the cap. State the consequences under the retrieved text.
7. For convertibles, check the conversion terms are fixed or determinable at issue; hand deeper analysis to `convertible-instrument-analyst`.
8. For listed issuers, add in-principle approval, lock-in and listing steps under ICDR.

## Output

1. Route recommendation and eligibility check.
2. Step plan with dates, responsible person and form.
3. Document list: resolutions, offer letter, registers, valuation report, FEMA forms.
4. Defect and risk table.

## Guardrails and hand-offs

- Do not value the securities or fix the price; a registered valuer or merchant banker does that.
- Do not state limits, minimum amounts or deadlines from memory; cite the rule or tag `[verify]`.
- Resolutions and notices go to `board-meeting-documents-drafter`.
