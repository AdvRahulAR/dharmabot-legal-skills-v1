---
name: gst-detention-release-drafter
description: Drafts replies and release requests when goods or vehicles are detained in transit under the detention provision of the CGST Act, 2017 and the e-way bill rules, through the GST MOV forms, building the bona fide technical lapse case, provisional release and a defence against confiscation. Use when a truck is stopped for an expired, missing or defective e-way bill or invoice and a detention order or MOV notice has issued. Do not use for demand notices (use gst-notice-reply-drafter) or the appeal against the penalty order (use tax-appeal-grounds-drafter).
---

# GST Detention Release Drafter

Every output is a draft for an advocate enrolled in India or the client's GST practitioner to check.

## Purpose

Get the goods and vehicle released quickly, and keep the record clean for any appeal.

## Jurisdiction gate

Confirm the interception is under the CGST Act and the State or UT GST Act (or IGST Act for inter-State movement). Identify the State where goods are detained and the proper officer's designation. If the officer has moved to confiscation proceedings, flag the shift and the higher stakes at the top of the draft.

## Temporal gate

The detention and penalty provision was substantially amended (believed by the Finance Act, 2021, from 1 January 2022), changing penalty computation and removing the earlier link to tax demand. Record the date of interception, and confirm the version of the section, the e-way bill rule and the MOV forms in force then.

## Required inputs

Mark as **blocking**: the MOV forms served (with dates and reference numbers); the invoice, e-way bill (with validity period and any extension), and lorry receipt; the nature of the alleged defect; whether the owner of goods has come forward; and whether goods are perishable.

Also useful: GSTR-1 and books showing the supply was reported, transporter's explanation for delay (breakdown, traffic, strike), GPS logs, and past compliance record.

## Method

1. Retrieve the current official text of the CGST Act provisions on detention and confiscation, the e-way bill rule, the MOV forms, and CBIC circulars on interception and on minor discrepancies. Record versions and dates.
2. Check procedure first: was physical verification recorded in the right form, within time; was the detention order served; was the notice issued within time; was a hearing given. Note each lapse.
3. Classify the defect: technical or clerical (for example a minor error in pin code or vehicle number, an expiry by a short time due to breakdown) versus no document or goods not matching.
4. Collect CBIC guidance treating certain discrepancies as minor, and current High Court authority on bona fide lapses and intention to evade. Read before citing; tag unread items `[verify]`.
5. Draft the reply to the notice: facts, chronology, defect explained, evidence that tax was not evaded, procedural objections, and prayer.
6. Draft a release request: pay under protest or furnish security as the provision allows, with a reservation of rights. Explain the trade-off of paying under protest.
7. If goods are perishable or hazardous, add an urgent release prayer.
8. Calculate the penalty exposure under the current text; show the working and label it an estimate.

## Output

1. Reply to the MOV notice with annexures.
2. Release request letter.
3. Advice note: procedural defects, exposure, appeal route and deadline (via `limitation-calculator`).

## Guardrails and hand-offs

- Never fabricate breakdown or traffic evidence.
- Never advise moving goods without a valid document.
- Do not state penalty percentages from memory.
- For the appeal against the penalty order, hand off to `tax-appeal-grounds-drafter`; for a writ against an illegal detention, `writ-petition-drafter`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`.
