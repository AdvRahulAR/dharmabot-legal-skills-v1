---
name: encumbrance-certificate-analyst
description: Reads encumbrance certificates issued by Sub-Registrar offices in any Indian State or UT, extracts every registered sale, mortgage, lease, release and attachment, and reconciles them with the title chain and loan papers, flagging search-period gaps and charges to check in CERSAI and ROC records. Use when a lawyer asks to read an EC, check an EC against title deeds, spot a missing mortgage release, or confirm a property is free of registered charges. Do not use for a full title opinion; use property-title-diligence-analyst.
---

# Encumbrance Certificate Analyst

Every output is a draft review for an advocate enrolled in India to check.

## Purpose

Turn one or more encumbrance certificates into a clean transaction table, reconcile it with the title documents, and list what the EC cannot show.

## Jurisdiction gate

Confirm the property is in India and record the State or UT and the Sub-Registrar office or offices with jurisdiction over the period. Formats differ (for example Form 15 and Form 16 in some southern States, online ECs in others). Where the jurisdiction of a Sub-Registrar office changed during the period, ECs from each office are needed.

## Required inputs

Mark as **blocking**:
- the EC or ECs, with the search period and the office that issued each;
- the property description used for the search (survey or door number, extent, village);
- the title documents or a list of them for reconciliation.

Also useful: loan sanction and discharge letters, CERSAI search results, ROC charge records where a company held the property, and any court or revenue attachment orders.

## Method

1. Retrieve the current official text of the Registration Act, 1908 and the State registration rules on encumbrance certificates and searches. Open `references/india-state-statutes.md` as a starting point and confirm the State's EC format and online search facility on its official registration portal. Record the version and date.
2. Check the search itself: period requested against period covered, property description used, and any "nil" entry periods. Flag gaps, overlaps and mismatched survey or sub-division numbers.
3. Extract each entry into a table: date, document number, nature, executant, claimant, consideration, extent.
4. Reconcile with the title chain. Every title deed should appear. Every mortgage should have a matching release, reconveyance or discharge. Unexplained entries are flags.
5. List charges the EC may not show: equitable mortgages by deposit of title deeds where no memorandum was registered, agreements to sell not registered, charges on company property (check the ROC charge register), security interests on CERSAI, tax and revenue attachments, and pending suits (lis pendens).
6. Check whether the State requires registration or notice of attachments and lis pendens, and whether those appear.
7. Pass the reconciled table to `property-title-diligence-analyst` for the title opinion.

## Output

1. Transaction table extracted from each EC.
2. Reconciliation table: EC entry · matching document · status (matched, missing, unexplained).
3. Gap and risk list with the further searches needed (CERSAI, ROC, court, revenue, society).
4. A short note that an EC shows only registered transactions in the searched office and period.

## Guardrails

- Never treat a nil EC as proof that the property is free of all charges.
- Never fill in an entry that is illegible; mark it and ask for a clearer copy.
- Do not invent document numbers, dates or office names.
- Recommend fresh ECs up to the date of registration of the sale.
