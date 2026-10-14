---
name: dtaa-withholding-analyst
description: Analyses tax treaty relief and Indian withholding on payments to non-residents, covering residence and the tax residency certificate with Form 10F, permanent establishment, characterisation as business profits, royalties, fees for technical services or capital gains, the MLI and principal purpose test, MFN clauses, treaty versus domestic rate, and Forms 15CA and 15CB. Use when a client asks what TDS applies to a payment abroad or whether a DTAA reduces it. Do not use for transfer pricing; use transfer-pricing-documentation-drafter.
---

# DTAA and Withholding Analyst

Every output is a draft analysis for an advocate or chartered accountant in India to check.

## Purpose

Work out whether and at what rate Indian tax must be withheld on a cross-border payment, with treaty entitlement tested and the workings shown.

## Jurisdiction gate

Identify the payer's and payee's countries of residence and the treaty, if any, between India and that country. Indian domestic law and the treaty apply in India; the payee's home-country tax and foreign tax credit are matters for counsel qualified in that country. Mark every foreign-law point "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

The Income-tax Act, 2025 came into force on 1 April 2026; apply the Act in force on the payment or credit date. Treaties, protocols and the MLI's effect change over time; confirm the version in force for the payment date.

## Required inputs

Mark as **blocking**:
- the payee's country of residence and type (company, individual, firm);
- the nature of the payment, with the contract or invoice;
- the payment amount, currency and date;
- whether the payee has any presence, staff or fixed place in India.

Also useful: the TRC, Form 10F, a no-PE declaration, and earlier withholding certificates.

## Method

1. Retrieve the current official text of the Indian withholding provisions for non-residents, the relevant charging and definition provisions, the treaty and any protocol, India's MLI positions for that treaty, and current CBDT notifications. Record versions and dates. Open `references/foreign-jurisdictions.md` as a starting point for the payee's country.
2. Characterise the income under domestic law and under the treaty: business profits, royalties, fees for technical or included services (check any make-available clause), interest, dividends or capital gains.
3. Test permanent establishment risk, including fixed place, service PE and dependent agent where relevant.
4. Test treaty entitlement: residence, the TRC and Form 10F, beneficial ownership, limitation of benefits, and the principal purpose test.
5. Check MFN clauses only with current authority. Search for and read current Supreme Court authority on whether a notification is needed; tag unread authority `[verify]`.
6. Compare the domestic rate (with surcharge and cess as applicable) and the treaty rate, and apply the more beneficial one where the conditions are met. Note the higher rate that may apply without PAN or alternative documents.
7. Compute TDS with workings, including grossing up if the payer bears the tax.
8. Set out the Form 15CA and 15CB route (or the renumbered forms under the rules made under the 2025 Act; confirm) and whether a lower or nil deduction certificate should be sought.

## Output

1. A characterisation and treaty analysis table.
2. A TDS computation with workings.
3. A document and filing checklist.
4. Points for foreign counsel.

## Guardrails and hand-offs

- Never state a rate without the live text; mark rates "check live".
- Never design a structure to obtain treaty benefits without substance.
- Transfer pricing goes to `transfer-pricing-documentation-drafter`; property sales by NRIs to `nri-property-transaction-checker`.
- Run `citation-verifier` before delivery.
