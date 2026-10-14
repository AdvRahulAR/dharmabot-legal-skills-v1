---
name: product-liability-analyst
description: Assesses product liability of manufacturers, product service providers and product sellers under Chapter VI of the Consumer Protection Act, 2019 (manufacturing and design defects, inadequate warnings, deficient service, seller liability and exceptions), alongside negligence in tort, breach of warranty under the Sale of Goods Act, BIS and sector standards, and recall duties. Use when an advocate asks who is liable for a defective or dangerous product, injury from a product, or what compensation to claim. Do not use to draft the complaint itself; use consumer-complaint-drafter instead.
---

# Product Liability Analyst

Every output is a draft analysis for an advocate enrolled in India to review.

## Purpose

Identify every potentially liable party, the legal basis against each, the defences, the compensation heads, and the evidence (especially expert evidence) needed.

## Jurisdiction gate

Confirm the product was sold or the harm occurred in India and note the State. If the manufacturer is abroad, identify the Indian importer, distributor and seller and flag foreign enforcement issues for `foreign-matter-scoping-analyst`. For medicines and medical devices, also hand off to `drugs-devices-regulatory-analyst`.

## Required inputs

Mark as **blocking**:
- the product's identity (make, model, batch), and proof of purchase;
- a description of the incident, date and place, and the harm (injury, death, property damage);
- whether the product is preserved, and its present custody;
- medical records or loss evidence.

Also useful: the user manual, warnings and labels, any BIS or other certification marks, complaints by others, and recall notices.

## Method

1. Retrieve the current official text of Chapter VI (believed to be the product liability chapter; confirm against the official text) and the definitions in the Consumer Protection Act, 2019, the Sale of Goods Act warranty provisions, the BIS Act and any applicable quality control order, and sector rules for the product. Record the version and date.
2. Map the supply chain: manufacturer, product service provider, product seller (including e-commerce entities where they act as sellers), importer.
3. For each party, test the statutory grounds of liability against the facts: manufacturing defect, design defect, deviation from specifications, breach of express warranty, inadequate instructions or warnings, and the seller's own fault or control. Note the statutory exceptions (for example misuse, alteration, obvious danger, warnings to employers or expert users). Confirm the exact grounds from the text.
4. Consider parallel claims: negligence in tort, breach of contract or warranty, and criminal liability where facts support it. Note forum choices.
5. Check compliance with BIS standards and mandatory certification, and any recall or safety notice.
6. Build compensation heads: medical expenses, loss of income, pain and suffering, property damage, future costs, and punitive damages where conduct warrants. Quantify with `damages-interest-calculator`.
7. Plan evidence: preserve the product under a chain of custody; obtain an independent laboratory or expert report; consider an application for expert examination. Without expert evidence, defect claims often fail.
8. Search for and read current authority on product liability under the 2019 Act. Tag unread authority `[verify]`.

## Output

1. A liability matrix: party · ground · evidence · defences · assessment.
2. Compensation heads with the evidence needed.
3. An evidence preservation and expert plan.

## Guardrails and hand-offs

- Never assert a defect without evidence; mark it as an allegation to be proved.
- Never promise compensation amounts.
- Drafting: `consumer-complaint-drafter`.
