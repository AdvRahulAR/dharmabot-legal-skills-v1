---
name: carriage-goods-claim-analyst
description: Analyses cargo loss, damage and delay claims within India under the Carriage by Road Act 2007 (common carrier liability, notice of loss), the Railways Act 1989 and the Railway Claims Tribunal, the Multimodal Transportation of Goods Act 1993, and warehousing and logistics contracts, including insurance subrogation, and drafts notices and claims. Use when goods were damaged, lost or delayed in transit by a transporter, railway or logistics provider. Do not use for sea carriage or vessel arrest; use admiralty-shipping-claim-analyst.
---

# Carriage Goods Claim Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Identify who is liable for the cargo loss, preserve the claim with timely notice, and choose the forum.

## Jurisdiction gate

Confirm the carriage was in India, or the Indian leg of a multimodal movement. Identify the mode (road, rail, multimodal, warehouse), the origin and destination States, and the contract terms on jurisdiction and arbitration.

## Required inputs

Mark as **blocking**:
- the consignment note, goods receipt, railway receipt or multimodal transport document;
- dates of booking, expected delivery and actual delivery (or non-delivery);
- the nature and value of the loss, with invoices;
- whether and when notice of loss or claim was given.

Also useful: survey report, photos, the carrier's contract and terms, insurance policy and any claim paid by the insurer.

## Method

1. Retrieve the current official text of the Carriage by Road Act and Rules, the Railways Act and the Railway Claims Tribunal Act and rules, the Multimodal Transportation of Goods Act, and the contract terms. Record versions and dates.
2. Identify the carrier and its status (registered common carrier, railway administration, multimodal operator, warehouse keeper). Check registration where the law requires it.
3. Test liability:
   - **Road**: common carrier liability, the carrier's defences, declared value and the limit where value was not declared, and the statutory notice of loss. Check the period live.
   - **Rail**: the railway's liability as carrier or bailee, exceptions, the notice of claim to the railway administration within the period in the Act, and the Tribunal's limitation.
   - **Multimodal**: operator liability, limits, notice period and the time to bring a suit or arbitration.
   - **Warehousing**: bailee's duty of care and contract limits.
4. Time bars: notice periods can extinguish a claim. Compute each with `limitation-calculator`, from the date of delivery or expected delivery.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
5. Subrogation: if the insurer paid, check the letter of subrogation and whose name the claim proceeds in.
6. Choose the forum: Railway Claims Tribunal (believed to have exclusive jurisdiction over railway claims; confirm against the official text), civil court, commercial court (by value), consumer commission (if the claimant is a consumer), or arbitration under the contract.
7. Search for and read current authority on disputed points. Tag anything not read in full `[verify]`.
8. Draft the notice of loss or claim.

## Output

1. A liability and time-bar table: party · basis · defences · notice due · suit or claim due.
2. The draft notice of claim.
3. A forum recommendation and evidence list.

## Guardrails and hand-offs

- Never backdate a notice or inflate the value of goods.
- For a formal legal notice or reply, hand off to `legal-notice-drafter`.
- For a consumer forum route, hand off to `consumer-complaint-drafter`.
- If the insurer repudiated the transit claim, hand off to `insurance-claim-repudiation-analyst`.
