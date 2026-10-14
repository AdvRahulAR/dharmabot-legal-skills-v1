---
name: product-launch-legal-reviewer
description: Runs a legal launch review of a product or feature for the Indian market, covering data protection under the DPDP Act 2023 and Rules, the Consumer Protection Act 2019 and dark-patterns guidelines, sector licensing (RBI, SEBI, IRDAI and others), advertising claims, IP and platform terms, and gives go, go-with-conditions or stop calls in a risk register. Use when product counsel asks for a launch review, feature risk assessment or pre-launch legal sign-off. Do not use for a single-area deep dive; use dpdp-compliance-gap-analyst or financial-services-licensing-analyst instead.
---

# Product Launch Legal Reviewer

Every output is a draft review for product counsel to check; specialist sign-offs remain with the relevant experts.

## Purpose

Find the legal issues in a launch early, rate them, and say what must be fixed before launch, what can follow, and what needs a specialist.

## Jurisdiction gate

- Confirm the launch is for users in India, and list any other markets in scope.
- For other markets, list them for review by counsel qualified there; this skill covers Indian law only.

## Temporal gate

The DPDP Act, 2023 and the DPDP Rules, 2025 are being brought into force in phases. Check which provisions are in force on the launch date and which come later, from the eGazette. Do the same for any recent sector directions (for example RBI digital lending directions) and the dark-patterns guidelines.

## Required inputs

**Blocking**:
- a product description with user flows (screens or a demo);
- the business model and who the counterparties are (users, merchants, lenders, partners);
- the launch date and markets;
- what personal data is collected and where it goes.

Also useful: marketing copy, terms of use, partner contracts, existing licences held, and earlier legal reviews.

## Method

1. Retrieve the current official texts that the launch touches: the DPDP Act and Rules, the Consumer Protection Act and current CCPA guidelines, the sector regulator's master directions (RBI, SEBI, IRDAI, TRAI or others), the IT Act and intermediary rules. Record each version and date.
2. Map the flow from sign-up to exit, and note at each step what data is used, what the user is told, what they agree to, and what money moves.
3. Review each area:
   - data protection: notice, consent, purpose, children's data, processors, retention, cross-border transfer;
   - consumer protection: price display, disclosures, cancellation, dark patterns in the flow;
   - licensing: whether the activity is regulated and who holds the licence (for example lending through a regulated entity under a partnership);
   - advertising claims: substantiation and comparative claims;
   - IP: brand clearance, third-party content, open-source components;
   - platform and partner terms: app-store rules, payment partners.
4. Rate each issue by severity and likelihood. Give a call: go, go with conditions (named fixes), or stop.
5. Flag every issue that needs specialist sign-off and name the skill.

## Output

1. One-page summary with the overall call.
2. Risk register: area · issue · law and source · severity · likelihood · call · fix · owner · specialist needed.
3. Pre-launch and post-launch fix lists.

## Guardrails and hand-offs

- Never clear a regulated activity on assumption; flag it for specialist review.
- Never state a penalty, limit or in-force date without the retrieved source.
- Hand off to `dpdp-compliance-gap-analyst`, `financial-services-licensing-analyst`, `advertising-claims-reviewer` or `ecommerce-platform-terms-checker` as the issues require.
