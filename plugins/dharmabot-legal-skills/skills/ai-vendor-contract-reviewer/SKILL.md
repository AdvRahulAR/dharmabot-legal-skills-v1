---
name: ai-vendor-contract-reviewer
description: Reviews AI terms in vendor agreements, model API and model-as-a-service contracts and AI feature terms of service for Indian clients, covering training on customer data, output ownership and IP indemnities, confidentiality, data location, accuracy disclaimers, acceptable-use limits, audit, security, regulatory cooperation under RBI outsourcing rules, SEBI and the DPDP Act, and exit. Use when a client asks to review a generative AI API agreement, an AI vendor contract, or the AI terms in a SaaS renewal. Do not use for general SaaS commercial terms; use vendor-saas-agreement-reviewer instead.
---

# AI Vendor Contract Reviewer

Every output is a draft review for an advocate enrolled in India to check.

## Purpose

Show the client what it gives up and what it gets under the AI vendor's terms, and what to negotiate, with fallbacks.

## Jurisdiction gate

- Record governing law and dispute forum. Many AI terms choose US or other foreign law. Mark points of that law "to be confirmed by counsel qualified in [jurisdiction]" and use `foreign-law-contract-support-reviewer` where needed.
- Identify the client's regulator and its outsourcing, cloud and data rules (for example RBI IT outsourcing directions, SEBI cloud framework, IRDAI).

## Required inputs

**Blocking**:
- the full contract set: order form, master terms, data processing addendum, acceptable use policy, service terms and any linked documents, with their version dates;
- the intended use, and the data the client will send (personal, customer, confidential, regulated);
- whether the client is regulated, and by whom.

Also useful: the client's AI policy, security requirements and playbook.

## Method

1. Retrieve the current official text of the DPDP Act and Rules and each sector direction in play, and save the vendor's linked online terms as they stand on the review date. Record version and date.
2. List every document incorporated by reference and every clause letting the vendor change terms unilaterally. Flag each.
3. Customer data: is it used to train or improve models, by default or opt-in? Retention of prompts and outputs, abuse-monitoring access by vendor staff, and zero-retention options.
4. Confidentiality and data location: where data is processed and stored, sub-processors, transfers abroad (hand to `cross-border-data-transfer-analyst`).
5. Outputs: ownership or licence of outputs, restrictions on use, and similarity of outputs across customers.
6. IP indemnity: scope, exclusions (modified outputs, filters turned off), caps and conditions.
7. Accuracy and liability: disclaimers, caps, carve-outs for data breach and confidentiality, and suitability for regulated decisions.
8. Acceptable use: prohibited uses that could catch the client's planned use (for example legal, medical or credit decisions without human review).
9. Security and audit: certifications, penetration test reports, breach notice period, and audit or regulator access rights required by sector rules.
10. Regulatory cooperation: access for RBI, SEBI or other regulators, business continuity, and records.
11. Exit: data return and deletion, transition support, notice of model deprecation.
12. Hand the DPA to `data-processing-agreement-reviewer`.

## Output

1. Issues list: clause · issue · risk rating · ask · fallback · walk-away.
2. Redlines or a negotiation letter.
3. A one-page summary for the business: what data may go in, and conditions for use.

## Guardrails and hand-offs

- Never assume online terms are static; record the version date reviewed.
- Never treat a vendor's marketing statement as a contractual commitment.
- Do not state foreign-law enforceability as settled.
- Wider SaaS terms go to `vendor-saas-agreement-reviewer`.
