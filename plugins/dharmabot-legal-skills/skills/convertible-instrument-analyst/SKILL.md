---
name: convertible-instrument-analyst
description: Compares convertible instruments for Indian startups, namely CCPS, CCDs (and the Companies Deposits Rules), iSAFE notes and convertible notes for DPIIT-recognised startups under FEMA, with conversion formulae, valuation caps and discounts, Companies Act issue steps, FEMA pricing and reporting, and the current tax position on share premium. Use when founders ask whether to raise on CCPS, CCDs, iSAFE or a convertible note, or how a cap and discount will convert. Do not use for the issue procedure itself; use securities-issuance-compliance-checker instead.
---

# Convertible Instrument Analyst

Every output is a draft for an advocate enrolled in India to check, with tax points for a chartered accountant.

## Purpose

Recommend the instrument that fits the round and the investor mix, explain how it converts, and flag where it may be treated as a deposit, debt or a FEMA breach.

## Jurisdiction gate

- Confirm the issuer is an Indian company and whether it holds DPIIT startup recognition (some instruments depend on it).
- List each investor's residency and type (resident individual, AIF, non-resident individual, foreign entity, FVCI). FEMA governs every non-resident; hand detailed structuring to `india-entry-fema-structuring-analyst`.
- A foreign "SAFE" on a US template is not an Indian instrument; it must be recast.

## Temporal gate

- The tax on share premium received by unlisted companies (often called angel tax) was reported to have been withdrawn by the Finance (No. 2) Act 2024; confirm and record from which year.
- The Income-tax Act 2025 is reported to apply from 1 April 2026; check whether it is in force and map the provisions.
- Check recent changes to the Deposits Rules and the FEMA convertible note conditions.

## Required inputs

- **Blocking:** company status (DPIIT recognition and date); investors and their residency; round size; and whether the price is agreed now or deferred.
- Useful: the current cap table, any existing investor rights, the proposed cap and discount, and expected next-round timing.

## Method

1. Retrieve the current official text of the Companies Act provisions on preference shares and debentures, the Share Capital and Debentures Rules, the Companies (Acceptance of Deposits) Rules, the FEMA Non-Debt Instruments Rules and Debt Instruments Regulations, the RBI master direction on foreign investment, and the DPIIT startup notification. Record the version and date.
2. Build a comparison table for the instruments in play:
   - **CCPS:** equity instrument for FEMA; conversion formula or price must be fixed upfront within FEMA pricing; preference rights; voting limits.
   - **CCDs:** equity for FEMA if compulsorily convertible; check the deposit exemption conditions (conversion period, security, issuer type); interest and TDS.
   - **iSAFE:** a market label, usually issued as a CCPS-style instrument; read the actual terms.
   - **Convertible note:** issued by DPIIT-recognised startups. From residents, check the deposit exemption conditions in the Deposits Rules; from non-residents, the FEMA conditions (minimum amount, conversion period, sectoral rules) and reporting. Confirm all figures.
3. Explain conversion mechanics with a worked example: cap, discount, the lower-of rule, and the conversion ratio. Hand numbers to `cap-table-calculator`.
4. Check FEMA pricing for each non-resident: price at issue not below fair value, and conversion not below fair value at issue (confirm the current rule). Note reporting forms.
5. Flag risks: instruments that may be deposits; optionally convertible instruments treated as debt (ECB) for non-residents; assured-return features.
6. Set out the Companies Act issue steps and hand them to `securities-issuance-compliance-checker`.
7. Note the tax position for the CA to confirm.

## Output

1. Instrument comparison table.
2. Recommendation with reasons.
3. Worked conversion example.
4. FEMA and deposit risk list, and next steps.

## Guardrails and hand-offs

- Do not state FEMA minimums, periods or tax rates as settled without the current text; tag `[verify]`.
- Do not recommend an instrument to avoid regulation or tax.
- Do not value the company.
