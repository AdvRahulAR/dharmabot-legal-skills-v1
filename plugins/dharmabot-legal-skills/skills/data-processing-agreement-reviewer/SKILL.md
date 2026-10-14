---
name: data-processing-agreement-reviewer
description: Drafts and reviews data processing agreements between data fiduciaries and processors under the Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025, covering instructions, security safeguards, breach notice, sub-processing, erasure, audits and liability, with a GDPR Article 28 overlay for EU personal data. Use when a client says review this DPA, mark up the vendor's data processing addendum, or draft a DPA for our processors. Do not use for choosing a transfer mechanism; use cross-border-data-transfer-analyst, and vendor-saas-agreement-reviewer for commercial terms.
---

# Data Processing Agreement Reviewer

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Make sure the DPA lets the fiduciary meet its own DPDP duties through the processor, and allocates risk sensibly, with ready fallbacks for negotiation.

## Jurisdiction gate

- Record the governing law and seat of disputes. If not Indian law, mark points of that law "to be confirmed by counsel qualified in [jurisdiction]".
- Identify whose data is processed. If EU personal data is involved, apply the GDPR Article 28 overlay. For UK data, flag UK GDPR for UK counsel.
- Note sector rules on outsourcing and data (RBI outsourcing of IT services, SEBI cloud framework, IRDAI) and retrieve them where the client is regulated.

## Temporal gate

Most fiduciary duties under the DPDP Rules are believed to start on 13 May 2027. Confirm from the Gazette. Draft the DPA now so it already meets those duties, and state any interim reliance on the SPDI Rules.

## Required inputs

**Blocking**:
- the DPA and the main agreement it attaches to;
- which side the client is on, and its role (fiduciary, processor, or both for different data);
- a description of the processing: data categories, data principals, purposes, locations and sub-processors.

Also useful: the client's negotiation playbook, security schedule, insurance, and any regulator expectations.

## Method

1. Retrieve the current official text of the DPDP Act and Rules, any sector direction, and for EU data the GDPR and the current Standard Contractual Clauses. Record version and date.
2. Fix the roles on the facts. A vendor that decides purposes is not a mere processor; flag it.
3. Check processing only on documented instructions, and the processor's duty to say if an instruction appears unlawful.
4. Security: reasonable safeguards matching the Rules (encryption or masking, access control, logs and their retention period, back-ups), with a schedule of measures, not just "industry standard".
5. Breach: notice to the fiduciary without delay and in time for the fiduciary to meet the Board and data principal deadlines in the Rules (a detailed Board report is reported to be due within 72 hours; confirm). Require the facts the fiduciary must report and cooperation thereafter.
6. Sub-processors: prior approval or notice and objection, written flow-down, and full liability for sub-processors.
7. Assistance with data principal requests, DPIAs, audits and regulator queries.
8. Erasure: on end of purpose, withdrawal of consent, or termination, with certification. Carve out only retention required by law.
9. Audit rights and certifications; regulator access where sector rules require it.
10. Data location and onward transfers. Hand the mechanism to `cross-border-data-transfer-analyst`.
11. Liability, indemnity and caps: check whether data breaches sit inside or outside the cap, and that insurance supports it.
12. GDPR Article 28(3) overlay: each mandatory item present.
13. Prepare redlines and a fallback ladder for each issue.

## Output

1. Redlined DPA, or a fresh draft if asked.
2. Issues table: clause · issue · risk · preferred position · fallback · walk-away.
3. Missing schedules list (processing description, security measures, sub-processors).
4. A short cover note for the client.

## Guardrails and hand-offs

- Never accept "industry standard" security wording as meeting the Rules without a schedule.
- Do not state GDPR or foreign-law positions as settled; mark them for local counsel.
- Commercial and service-level terms go to `vendor-saas-agreement-reviewer`; AI-specific terms to `ai-vendor-contract-reviewer`.
