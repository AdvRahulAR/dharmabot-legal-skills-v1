---
name: sale-deed-drafter
description: Drafts agreements to sell and sale deeds for land, houses and flats in any Indian State or UT under the Transfer of Property Act, 1882 and the Registration Act, 1908, with a State-format property schedule, title recitals, consideration and buyer TDS, possession, title covenants and indemnities. Use when a lawyer asks for a sale agreement, conveyance deed, sale deed for a flat with a bank loan, or a check of a developer's draft conveyance. Do not use for gifts, releases or partitions within a family; use family-conveyance-deed-drafter.
---

# Sale Deed Drafter

Every output is a draft for an advocate enrolled in India to check before execution and registration.

## Purpose

Produce an agreement to sell and a sale deed that match the title documents, the payment plan and the State's registration practice.

## Jurisdiction gate

Confirm the property is in India and record the State or UT, district and Sub-Registrar office. Stamp duty, registration fees, the format of the schedule, and rules for flats (apartment ownership laws, co-operative society transfers) differ by State. For an NRI or foreign party, also run `nri-property-transaction-checker`.

## Temporal gate

Record the expected date of each payment and of registration. Check which income-tax law governs the buyer's TDS on that date: the Income-tax Act, 2025 is reported to apply from 1 April 2026, replacing the 1961 Act. Confirm the provision, rate and threshold from the official text. Also check whether any new central registration law or State amendment is in force.

## Required inputs

Mark as **blocking**:
- full names, ages and addresses of sellers and buyers, and whether any is a company, minor, NRI or acting through a POA;
- the title documents or a title report;
- the property schedule as it appears in the title deed and revenue or municipal records;
- the price, payment schedule and any bank loan (with the lender's draft requirements);
- possession date and what is included (parking, undivided share, fittings).

Also useful: encumbrance certificates, society NOC, tax receipts, and the occupancy certificate for flats.

## Method

1. Retrieve the current official text of the Transfer of Property Act, 1882 (sale and part performance provisions), the Registration Act, 1908, the State stamp law and registration rules, and the income-tax provision on TDS on immovable property. Open `references/india-state-statutes.md` as a starting point. Record the version and date of each.
2. Confirm title is examined. If not, hand off to `property-title-diligence-analyst` first.
3. Agreement to sell: parties, recitals, price and instalments, earnest money and its forfeiture, seller's title obligations, deadline for sale deed, default and specific performance, possession, and loan-condition clauses. Note that an agreement with possession may need registration and stamping as a conveyance in some States; confirm.
4. Sale deed: recitals tracing title, consideration and mode of payment (bank details as supplied), TDS deduction recital, conveyance words, schedule with boundaries and measurements, covenants for title and quiet enjoyment, indemnity, delivery of documents, and handover of possession.
5. Flats: add the undivided share in land, common areas, parking, association or society membership and maintenance dues. Check the State apartment ownership law and society bye-laws.
6. Loan: add the lender's tripartite or NOC clauses and the payment flow from the lender.
7. Stamp duty and fees: hand off to `state-stamp-duty-calculator`. For a regional-language version, hand off to `regional-language-legal-drafter`.

## Output

1. Draft agreement to sell.
2. Draft sale deed with schedule.
3. Execution and registration checklist (identity, photos, PAN or Form 60, witnesses, stamp, e-registration, mutation after registration).
4. Notes for counsel on open issues and assumptions.

## Guardrails

- Never fill in extents, survey numbers, prices or bank details not supplied; use bracketed blanks.
- Never draft to show a lower price than actually paid or to split consideration to cut stamp duty or tax.
- Do not state a TDS rate or stamp figure from memory.
- The advocate attends execution and registration; this skill does not.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
