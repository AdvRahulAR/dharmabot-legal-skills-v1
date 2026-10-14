---
name: vendor-saas-agreement-reviewer
description: Reviews inbound vendor, procurement, SaaS, cloud and SLA terms from the Indian customer's side, covering service levels and credits, data location and security, DPDP Act, 2023 and CERT-In obligations, sub-processors, price changes, auto-renewal, exit and data return, liability and indemnities, with a prioritised issues list and fallbacks. Use when a company in India is buying software, cloud or outsourced services and asks for a review of the vendor's terms or click-through agreement. Do not use when the vendor is supplying an AI model or AI features; use ai-vendor-contract-reviewer instead.
---

# Vendor and SaaS Agreement Reviewer

Every output is a review for in-house counsel or an advocate enrolled in India to check.

## Purpose

Protect the customer's data, continuity and budget in a vendor contract that was written for the vendor.

## Jurisdiction gate

Note the customer's location in India and the vendor's country. Vendor terms often choose foreign law and courts. Review commercial and Indian regulatory points here, and flag foreign-law terms for `cross-border-contract-reviewer`. If the customer is a regulated entity (bank, NBFC, insurer, listed company, government body), identify the regulator's outsourcing or cloud rules that apply.

## Temporal gate

Check which DPDP Act, 2023 and DPDP Rules, 2025 obligations are in force on the review date, and the current CERT-In directions. Record the date checked.

## Required inputs

Mark as **blocking**:
- the full vendor terms, including order form, SLA, DPA, acceptable use policy and any URL-linked terms;
- what the service does and what data it will hold (personal data, financial, health, children's data);
- whether the customer is a regulated entity.

Also useful: contract value and term, how critical the service is, the customer's security requirements and playbook.

## Method

1. Retrieve the current official text of the DPDP Act, 2023 and Rules, the IT Act, 2000 and current CERT-In directions, and any sector regulator's outsourcing or cloud circulars that apply. Record the version and date. Fetch every linked policy and record its version, because vendors change them unilaterally.
2. **Order of precedence.** Check whether linked terms can change without consent; seek notice and a right to terminate.
3. **Service levels.** Uptime definition, exclusions, measurement, credits as the sole remedy, and chronic failure termination rights.
4. **Data.** Location and transfer, encryption, access controls, sub-processor list and change notice, breach notification in time for the customer to meet its own reporting duties, audit rights and certifications. Hand off a detailed DPA to `data-processing-agreement-reviewer`.
5. **Security incidents.** Cooperation and logs needed for CERT-In reporting; confirm current timelines from the directions.
6. **Commercials.** Price increases, auto-renewal, usage overages, suspension rights, and taxes including withholding and GST.
7. **IP and customer data.** Customer owns its data and outputs; vendor licence to data limited to providing the service; no training on customer data without consent.
8. **Risk allocation.** Vendor IP infringement indemnity, data-breach liability, the cap and super-cap, and exclusions.
9. **Exit.** Data export in a usable format, a transition period, deletion certificates, and escrow or continuity for critical services.
10. **Disputes.** Governing law, forum and practical enforceability in India.

## Output

1. A summary: sign, sign with changes, or do not sign without escalation.
2. An issues list: clause · issue · priority (P1, P2, P3) · ask · fallback.
3. A short vendor-facing markup or a list of requested changes.

## Guardrails and hand-offs

- Do not assume a vendor will accept changes to click-through terms; offer an order-form override.
- Never state regulatory timelines from memory; cite the current direction.
- AI products go to `ai-vendor-contract-reviewer`; open-source components go to `open-source-licence-reviewer`.
