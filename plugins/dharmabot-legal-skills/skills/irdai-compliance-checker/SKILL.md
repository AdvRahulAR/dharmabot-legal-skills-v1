---
name: irdai-compliance-checker
description: Checks compliance with the Insurance Act 1938 and IRDAI regulations and master circulars for insurers, brokers, corporate agents, web aggregators, insurance marketing firms, POSPs and insurtechs, covering distribution models, commission and remuneration, product filing, policyholder protection, outsourcing, advertisements, and data and cyber requirements. Use when a client asks whether it needs an IRDAI registration, how to sell embedded insurance, or whether a referral model is allowed. Do not use for non-insurance financial licences; use financial-services-licensing-analyst.
---

# IRDAI Compliance Checker

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Tell the client which IRDAI category its model falls into, what registration and conduct rules follow, and where its current model has gaps.

## Jurisdiction gate

Confirm the business solicits or services insurance for risks or persons in India. Foreign insurers and reinsurers, GIFT City IFSC entities (regulated by IFSCA) and pure technology vendors need separate treatment. Flag if the client is also RBI- or SEBI-regulated.

## Temporal gate

IRDAI consolidated many regulations in 2024 and issued master circulars, and the Insurance Act was amended by a 2025 amendment Act (including foreign investment and intermediary provisions); check which parts have commenced. Record the date of every regulation and circular relied on.

## Required inputs

Mark as **blocking**:
- a description of the business model: who the customer is, what the client does in the sale, who collects premium, and how the client is paid;
- the client's entity type and existing registrations;
- the insurer partners and product lines.

Also useful: draft agreements with insurers, user journeys and screenshots, marketing copy, and data flows.

## Method

1. Retrieve the current official text of the Insurance Act, the IRDAI regulations on intermediaries, corporate agents, web aggregators or their successor, insurance marketing firms, point-of-sales persons, commission and expenses of management, outsourcing, advertisements, policyholder protection, and the cyber security guidelines, and every master circular in force. Record versions and dates.
2. Classify the model. Ask: does the client solicit, procure or advise? Does it display comparative quotes? Does it collect premium or receive commission? A pure lead or referral model may still be solicitation. Compare against each intermediary definition and state which fits and why.
3. For the chosen category, list registration conditions: net worth, principal officer, training, certification, fit and proper, and limits on tie-ups with insurers.
4. Check remuneration. Payments to unregistered entities and payments above what the rules and the insurer's board policy allow are common defects. Do not state limits from memory.
5. Check conduct rules: disclosures, product suitability, free-look, consent for embedded or bundled cover, no forced bundling, claims assistance, grievance redressal.
6. Check advertisements and digital journeys against the advertisement rules and the insurer's approval.
7. Check outsourcing, data sharing, KYC and cyber security duties, and DPDP obligations.
8. Search for and read IRDAI orders and penalties on similar models. Tag anything not read in full `[verify]`.

## Output

1. A classification note with reasons and alternatives.
2. A compliance table: requirement · source · status · gap · fix.
3. Recent amendments and draft regulations to check live.

## Guardrails and hand-offs

- Never advise structuring payments to disguise commission.
- Never state that IRDAI has approved or will approve a model.
- For advertisement copy, hand off to `advertising-claims-reviewer`.
- For RBI, SEBI or IFSCA licensing, hand off to `financial-services-licensing-analyst`.
- Before delivery, send citations to `citation-verifier`.
