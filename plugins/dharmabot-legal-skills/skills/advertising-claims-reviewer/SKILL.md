---
name: advertising-claims-reviewer
description: Reviews advertisements, influencer posts and marketing claims against the Consumer Protection Act, 2019, the CCPA Guidelines for Prevention of Misleading Advertisements and Endorsements, 2022, the ASCI Code and influencer guidelines, sector rules (Drugs and Magic Remedies Act, FSSAI, SEBI, RBI, IRDAI norms), comparative advertising and trademark use. Use when an advocate or marketing team asks to vet an ad, a campaign claim, an influencer brief or disclosure. Do not use for food label compliance; use food-product-labelling-compliance-checker instead.
---

# Advertising Claims Reviewer

Every output is a review for an advocate enrolled in India, or in-house counsel, to check before the campaign goes live.

## Purpose

Find claims that are misleading, unsubstantiated or prohibited, and suggest compliant wording and disclosures, before regulators or competitors do.

## Jurisdiction gate

Confirm the ad targets consumers in India and note the media (TV, print, digital, influencer, packaging). Identify the sector, as sector regulators add rules. For ads also aimed abroad, flag that foreign rules need local counsel.

## Temporal gate

CCPA guidelines, ASCI codes and sector advertising rules change often. Retrieve the current versions and check whether any new guideline (for example on dark patterns or on specific sectors) is in force and from when.

## Required inputs

Mark as **blocking**:
- the full creative or copy, including fine print and the format it will run in;
- the product or service and its sector;
- the substantiation held for each claim (test reports, studies, certifications);
- for endorsements, the brief and the endorser's relationship with the advertiser.

## Method

1. Retrieve the current official text of the Consumer Protection Act, 2019 provisions on misleading advertisements, the CCPA guidelines, the ASCI Code and its influencer guidelines, and the sector rules. Record the version and date.
2. Break the ad into individual claims, express and implied, including visuals and overall impression.
3. For each claim, test truth, substantiation, qualification and context. Absolute claims ("kills 99.9% germs", "best", "No. 1") need strong, current and relevant evidence matching the test conditions. Professional endorsement claims ("doctor recommended") need verifiable basis and may be restricted by professional or sector rules.
4. Check prohibited claims under special statutes (for example remedies for listed diseases under the Drugs and Magic Remedies Act, health claims under FSSAI rules, return claims for financial products).
5. Disclaimers must not contradict the main claim and must be legible in the format used.
6. Endorsements: disclose material connection clearly and prominently; endorsers must have used the product where the guidelines require due diligence. Check celebrity and influencer obligations.
7. Comparative advertising: no disparagement, truthful and fair comparison; check trademark use of the competitor's mark.
8. Flag surrogate or indirect advertising of prohibited products.
9. Assess exposure: CCPA action, ASCI complaint, competitor suit, sector regulator.

## Output

1. A claims table: claim · issue · rule · evidence held · risk (high, medium, low) · suggested wording.
2. An influencer brief checklist with required disclosures.
3. A list of substantiation still needed.

## Guardrails and hand-offs

- Never approve a claim that lacks evidence; mark it "hold until substantiated".
- Never help disguise surrogate advertising.
- E-commerce listings: `ecommerce-platform-terms-checker`. Food labels: `food-product-labelling-compliance-checker`. Trademark clearance: `trademark-clearance-analyst`.
