---
name: customs-trade-remedy-analyst
description: Analyses Indian customs and trade matters under the Customs Act, 1962 and the Customs Tariff Act, 1975, covering classification under the HSN-based tariff, valuation rules, FTA origin and CAROTAR, exemptions, advance rulings, show-cause replies, anti-dumping and safeguard measures by DGTR, and DGFT foreign trade policy schemes. Use when a client asks how an import is classified, whether an FTA rate is available, or how to answer a customs notice or trade remedy probe. Do not use for GST on domestic supplies; use gst-transaction-analyst.
---

# Customs and Trade Remedy Analyst

Every output is a draft analysis for an advocate or customs specialist in India to check.

## Purpose

Give a reasoned view on classification, valuation, origin and duty for an import or export, and support replies and trade remedy submissions.

## Jurisdiction gate

Confirm the goods are imported into or exported from India. Identify the port of import, the importer's IEC and the country of origin. The FTA partner's rules on certifying origin are for counsel qualified there; mark them.

## Required inputs

Mark as **blocking**:
- a technical description of the goods (composition, function, use) with data sheets;
- the country of origin and supplier, and for FTA claims the certificate of origin and supply chain;
- the invoice value, terms of delivery and any related-party relationship;
- for a notice or DGTR matter, the notice or initiation notification.

Also useful: the bill of entry, earlier assessments, test reports and advance rulings for similar goods.

## Method

1. Retrieve the current official text of the Customs Act, the Customs Tariff Act and its schedules, the valuation rules, the origin rules for the relevant FTA, the CAROTAR rules, the exemption notifications, and current DGTR and DGFT notifications. Record versions and dates. Mark every rate and notification "check live".
2. Classify using the General Rules for Interpretation, section and chapter notes, and the HSN explanatory notes. Explain why rival headings fail.
3. Determine the duty structure: basic customs duty, any exemption, surcharges and cesses, IGST, and any GST compensation cess still levied (largely withdrawn after the 2025 GST changes; confirm). Do not state a rate from memory.
4. Test valuation: transaction value, related-party influence, and additions such as royalties and assists.
5. For FTA claims, test the origin criterion (wholly obtained, value content, change in tariff heading or product-specific rule), direct consignment and documents, and the importer's duties under CAROTAR to hold origin information.
6. Check whether anti-dumping, countervailing or safeguard duty applies to the product and origin, and its period.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
7. For a show-cause notice, test limitation, the extended period, confiscation and penalty, and draft the reply. Consider an advance ruling for future imports.
8. For DGTR matters, outline participation steps and submissions on injury, causation and dumping margin, with data from the client.
9. Note DGFT schemes (for example duty remission or export promotion) that may apply. Search for and read authority; tag unread authority `[verify]`.

## Output

1. A classification and duty note with check-live items.
2. An FTA origin checklist.
3. A draft reply or submission where asked.

## Guardrails and hand-offs

- Never suggest misdeclaration, undervaluation or origin circumvention.
- GST questions go to `gst-transaction-analyst`; sanctions and export-control screening to `aml-sanctions-compliance-checker`.
- Run `citation-verifier` before delivery.
