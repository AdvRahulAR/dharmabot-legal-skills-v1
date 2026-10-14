---
name: dpdp-compliance-gap-analyst
description: Assesses an organisation's readiness under the Digital Personal Data Protection Act, 2023 and the DPDP Rules, 2025, covering grounds for processing, notice and consent, children's data, data principal rights, security safeguards, breach readiness and Significant Data Fiduciary duties, and produces a prioritised gap register. Use when a client asks for a DPDP readiness assessment, privacy gap analysis, data protection impact assessment or "are we DPDP compliant". Do not use for drafting notice or consent text; use privacy-notice-consent-drafter, or gdpr-compliance-gap-analyst for EU GDPR.
---

# DPDP Compliance Gap Analyst

Every output is a draft review for an advocate enrolled in India or the client's privacy counsel to check.

## Purpose

Map what the organisation actually does with personal data against the DPDP Act and Rules, and list each gap by priority with the date the obligation bites.

## Jurisdiction gate

- The Act covers digital personal data processed in India, and processing outside India connected with offering goods or services to data principals in India. Record which limb applies.
- If EU or UK individuals are involved, note the overlap and hand GDPR points to `gdpr-compliance-gap-analyst`.
- List sector regulators whose rules add to or override the Act for this client (RBI, SEBI, IRDAI, health, telecom, education boards).

## Temporal gate

- The DPDP Rules, 2025 were notified on 13 November 2025 with phased commencement. Reported phasing: Board provisions at once; the consent manager rule after 12 months (13 November 2026); most fiduciary duties after 18 months (13 May 2027). Confirm from the Gazette.
- Check for later changes: amendments, removal-of-difficulties orders (one was reported in October 2026), SDF notifications, and any MeitY move to shorten the 18-month window.
- Record the assessment date. Tag every gap "in force", "in force from [date]" or "awaiting notification".
- Until the DPDP repeal provisions commence, check whether the IT Act compensation provision for sensitive personal data (believed to be section 43A) and the SPDI Rules, 2011 still bind the client.

## Required inputs

**Blocking**:
- what the business does, who its users are, and whether children or persons with disability use the service;
- a data inventory, or enough facts to build one (data categories, sources, purposes, systems, recipients, processors, storage locations, retention);
- whether the client is, or expects to be, notified as a Significant Data Fiduciary.

Also useful: current privacy policy and consent screens, vendor list and DPAs, security certifications, incident history and sector licences.

## Method

1. Retrieve the current official text of the DPDP Act, 2023, the DPDP Rules, 2025, and every later amendment, order or SDF notification (eGazette, MeitY website). Record version and date.
2. Build a processing register with one row per purpose. Do not merge purposes.
3. For each purpose, identify the ground: consent, or a legitimate use listed in the Act. Test each legitimate use against its exact words; do not stretch it.
4. Notice and consent: standalone and itemised notice; consent that is free, specific, informed and unambiguous; withdrawal as easy as giving consent; availability in English and Eighth Schedule languages; consent manager integration if planned.
5. Children and persons with disability: age assurance, the method of verifiable parental or guardian consent, and the bar on tracking, behavioural monitoring and targeted advertising aimed at children. Check whether the client falls in an exempt class in the Rules, and for which purposes only. Edtech and school products need particular care here.
6. Data principal rights: access, correction, completion, erasure, nomination and grievance. Check the published contact point, process and response period against the Rules.
7. Security safeguards: encryption or masking, access control, logging and the log-retention period in the Rules, back-ups, processor obligations, and a tested breach intimation process for the Board and data principals.
8. Retention and erasure: purpose-based retention, any time-based erasure for specified classes in the Rules with prior notice to the principal, and longer retention required by other laws (RBI, tax, PMLA, Companies Act).
9. Processors and transfers: hand processor contracts to `data-processing-agreement-reviewer` and transfers abroad to `cross-border-data-transfer-analyst`.
10. SDF duties, if applicable: India-based DPO, independent data auditor, periodic DPIA and data audit, algorithmic due diligence, and any localisation direction.
11. Governance: accountable owner, training, records of processing, grievance officer and evidence for the Board.
12. Score each gap high, medium or low by exposure (penalty band in the Schedule, confirmed from the text), effective date and effort.

## Output

1. Processing register: purpose · data · ground · notice · retention · processors · transfer.
2. Gap register: obligation · provision (to confirm) · current state · gap · priority · effective date · owner · fix.
3. A children's data note, where relevant.
4. A roadmap up to each commencement date.
5. Open questions for the client.

## Guardrails and hand-offs

- Never certify the client "compliant". This is a review of gaps on the facts supplied.
- Never quote a penalty, timeline or rule number without checking the official text.
- Mark consultation drafts and press reports as not law.
- Notice text goes to `privacy-notice-consent-drafter`; breach plans to `data-breach-response-planner`; citations to `citation-verifier`.
