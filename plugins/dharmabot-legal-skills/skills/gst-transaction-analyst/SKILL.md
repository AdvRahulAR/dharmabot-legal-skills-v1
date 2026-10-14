---
name: gst-transaction-analyst
description: Analyses the GST treatment of a transaction under the CGST, IGST and State GST Acts, covering supply and composite or mixed supply, classification and rate, time and place of supply, export of services and zero-rating, reverse charge, input tax credit and blocked credits, and e-invoicing. Use when a client asks how GST applies to a sale, service, export, import of service or bundled offer, or whether ITC is available. Do not use to reply to a GST notice; use gst-notice-reply-drafter.
---

# GST Transaction Analyst

Every output is a draft analysis for an advocate or chartered accountant in India to check.

## Purpose

Give a reasoned view of how GST applies to a defined transaction, with each conclusion tied to the provision and the live rate notification.

## Jurisdiction gate

Confirm the supplier or recipient is in India, and identify the States or UTs involved and whether either side is outside India or in a special economic zone. For cross-border services, foreign tax is outside scope; mark it for local advisers.

## Required inputs

Mark as **blocking**:
- a clear description of what is supplied, by whom, to whom, and how it is delivered;
- the locations of supplier and recipient, and the place of performance;
- contract terms on pricing, bundling and payment currency.

Also useful: GSTINs, invoices, existing classification, and any advance ruling or notice on the issue.

## Method

1. Retrieve the current official text of the CGST Act, IGST Act, the relevant State GST Act, rules, rate notifications and CBIC circulars. Record versions and dates. Never state a rate or exemption from memory; mark every rate "check live".
2. Decide whether there is a supply, and whether it is a composite or mixed supply.
3. Classify the goods (HSN) or services (SAC) and identify the rate notification and any exemption entry.
4. Determine time of supply and value, including inclusions and exclusions.
5. Determine place of supply under the IGST Act and whether the supply is inter-State or intra-State.
6. For services to a recipient abroad, test each condition for export of services, including the rule on consideration in convertible foreign exchange and the bar on supply between establishments of the same person. Note the options of export under LUT or with payment of IGST and refund.
7. Check whether reverse charge applies.
8. Check ITC for the recipient: eligibility, blocked credits, apportionment and conditions.
9. Note e-invoicing and e-way bill duties if thresholds are met (confirm current thresholds).
10. Where the point is uncertain, suggest an advance ruling and note its binding scope. Search for and read authority; tag unread authority `[verify]`.

## Output

1. A short answer on the treatment.
2. A reasoned table: issue, provision, conclusion, confidence, check-live items.
3. Compliance steps (invoice, return reporting, LUT) and open questions.

## Guardrails and hand-offs

- Never design arrangements to evade tax.
- Do not give a final rate without the live notification.
- Notices go to `gst-notice-reply-drafter`; treaty and withholding questions to `dtaa-withholding-analyst`.
- Run `citation-verifier` before delivery.
