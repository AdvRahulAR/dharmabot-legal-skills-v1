---
name: nri-property-transaction-checker
description: Checks property purchases, sales, gifts and inheritance involving NRIs, OCIs and foreign nationals under FEMA and the Foreign Exchange Management (Non-debt Instruments) Rules, 2019, covering permitted assets, the bar on agricultural land and plantations, payment channels, repatriation and the USD 1 million facility, Form 15CA and 15CB, buyer TDS, and POA and attestation steps. Use when a lawyer asks how an NRI can sell inherited property and repatriate money, or whether an OCI can buy farmland. Do not use for treaty withholding analysis; use dtaa-withholding-analyst.
---

# NRI Property Transaction Checker

Every output is a draft review for an advocate enrolled in India to check, with tax points confirmed by a chartered accountant.

## Purpose

Tell the client whether the transaction is permitted, how money must move, what tax is withheld and what documents to execute abroad.

## Jurisdiction gate

Indian law governs the property and the FEMA position. Record the State where the property is and the person's status: NRI (Indian citizen resident outside India), OCI cardholder, or foreign national, and their country of residence. Tax and succession questions in the country of residence are for counsel qualified there; read `references/foreign-jurisdictions.md` for orientation and mark those points "to be confirmed by counsel qualified in [jurisdiction]". Flag at once if the person is a citizen of, or of origin from, a country for which the rules require prior RBI approval (believed to include certain neighbouring countries; confirm the list).

## Temporal gate

Record the dates of acquisition, inheritance, sale and payment. The Income-tax Act, 2025 is reported to apply from 1 April 2026; check which tax law governs each payment, and the holding period for capital gains.

## Required inputs

Mark as **blocking**:
- the person's residential status and citizenship;
- the transaction (buy, sell, gift, inherit) and the property type (residential, commercial, agricultural, plantation, farmhouse);
- how the property was acquired and with what funds;
- for repatriation, the source of the sale proceeds and earlier repatriations.

Also useful: the title deeds, the will or heirship documents, bank accounts held (NRE, NRO, FCNR), and the buyer's residential status.

## Method

1. Retrieve the current official text of FEMA, 1999, the Non-debt Instruments Rules, 2019, the RBI Master Direction on remittances and on property, and the income-tax provisions on TDS on payments to non-residents and on Forms 15CA and 15CB. Record the version and date.
2. Acquisition: NRIs and OCIs may generally acquire immovable property other than agricultural land, plantation property and farmhouses; foreign nationals resident outside India generally may not, except by inheritance. Confirm each from the Rules.
3. Inheritance: permitted from a person resident in India or from one who acquired it lawfully. Hand off share questions to `intestate-succession-share-calculator`.
4. Payment: inward remittance or NRE, FCNR or NRO accounts only; no traveller's cheques or foreign currency notes.
5. Sale and transfer: to whom each class of property may be sold (agricultural land only to a resident Indian citizen; confirm).
6. Repatriation: purchase price paid in foreign exchange; limits on number of residential properties; the USD 1 million per financial year facility from NRO balances, with Forms 15CA and 15CB (or their renumbered equivalents under the 2025 Act rules) and the chartered accountant's certificate. Confirm current limits and form numbers.
7. Buyer TDS on payment to a non-resident seller: the rate depends on capital gains character; lower-deduction certificates may be sought. Hand off treaty questions to `dtaa-withholding-analyst`.
8. Documents abroad: POA drafting to `power-of-attorney-drafter`; authentication, apostille and stamping on arrival to `document-legalisation-planner`.

## Output

1. Permissibility note with the provision relied on.
2. Step plan: documents, accounts, tax filings, repatriation.
3. Open questions for the chartered accountant and foreign counsel.

## Guardrails

- Never state remittance limits, TDS rates or approval lists from memory.
- Never suggest routing funds through informal channels or a resident nominee.
- Do not advise on foreign tax as if qualified there.
