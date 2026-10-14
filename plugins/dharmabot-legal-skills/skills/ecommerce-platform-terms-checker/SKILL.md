---
name: ecommerce-platform-terms-checker
description: Checks e-commerce entities against the Consumer Protection Act, 2019, the Consumer Protection (E-Commerce) Rules, 2020, the Guidelines for Prevention and Regulation of Dark Patterns, 2023, Legal Metrology display rules, refund and grievance duties and FDI conditions for marketplaces, and drafts or audits terms of use, seller agreements, EULAs and refund policies. Use when a client asks to check our marketplace or app for e-commerce compliance, dark patterns, or to redraft our terms of service, seller terms or EULA. Do not use for advertising copy; use advertising-claims-reviewer instead.
---

# E-commerce Platform Terms Checker

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Find compliance gaps in how an online business sells to Indian consumers, and produce terms that are lawful, clear and fair.

## Jurisdiction gate

- The E-Commerce Rules cover entities offering goods or services to consumers in India, including those set up abroad. Confirm the model: marketplace, inventory, or hybrid.
- Note whether the client is an intermediary for seller content; if so, also run `it-rules-intermediary-compliance-checker`.
- Check FDI status. Foreign-owned marketplaces face conditions under the FDI Policy (for example on inventory control and seller relationships). Hand structuring to `india-entry-fema-structuring-analyst`.

## Temporal gate

The E-Commerce Rules have draft amendments that have not been notified. Record the date of the review and list drafts and CCPA advisories separately from binding rules.

## Required inputs

**Blocking**:
- the business model, who sells, who holds inventory, and who handles payment and delivery;
- current terms of use, seller agreement, refund and return policy, and privacy policy;
- screenshots or a walkthrough of the user journey (listing page, cart, checkout, cancellation, subscription).

Also useful: product categories, grievance data, and CCPA notices received.

## Method

1. Retrieve the current official text of the Consumer Protection Act, 2019, the E-Commerce Rules, the Dark Patterns Guidelines, the Legal Metrology (Packaged Commodities) Rules, relevant CCPA advisories, and the FDI Policy on e-commerce. Record version and date.
2. E-Commerce Rules: entity details, grievance officer and its acknowledgement and redress periods, display of seller details, return, refund, exchange and warranty terms, country of origin, no manipulated prices, no fake reviews, no cancellation charges unless equally borne (these items paraphrase the Rules; confirm each against the official text).
3. Dark patterns: walk through the journey against each listed pattern (for example false urgency, basket sneaking, confirm shaming, forced action, subscription traps, interface interference, drip pricing). Log each instance with a screenshot reference.
4. Legal Metrology: mandatory declarations displayed for packaged goods on the platform.
5. Product rules: BIS Quality Control Orders and sector rules for listed categories; hand food and labels to `food-product-labelling-compliance-checker`.
6. Unfair contract terms: one-sided liability exclusions, unilateral changes without notice, excessive forfeiture, and denial of consumer forum access. The Act lets consumer commissions declare such terms void.
7. Draft or redraft terms of use, seller agreement, EULA and refund policy. Keep consumer-facing text short and plain; keep seller terms aligned with marketplace obligations passed down to sellers.
8. Cross-check the privacy policy with `privacy-notice-consent-drafter`.

## Output

1. Compliance matrix: requirement · source (to confirm) · current state · gap · fix.
2. Dark patterns log with screenshots referenced.
3. Redlined or new terms, seller agreement, EULA and refund policy.
4. A risk note on unfair terms and FDI conditions.

## Guardrails and hand-offs

- Never draft terms designed to deny consumers statutory rights or remedies.
- Never approve a pattern listed in the Guidelines because "competitors do it".
- Advertising and influencer claims go to `advertising-claims-reviewer`; consumer disputes to `consumer-complaint-drafter`.
