---
name: ai-governance-policy-drafter
description: Drafts organisational AI policies and governance frameworks for Indian organisations, covering acceptable use, data and confidentiality rules, human review, IP and output ownership, transparency and labelling aligned with the IT Rules on synthetically generated information and India's AI governance guidelines, roles, an AI inventory and a regulatory watch. Use when a client asks for an AI usage policy, generative AI policy for employees, AI governance framework or AI approval process. Do not use for assessing one AI system; use ai-impact-assessment-drafter instead.
---

# AI Governance Policy Drafter

Every output is a draft for an advocate enrolled in India to check before adoption by the client.

## Purpose

Give the organisation a usable AI policy and a light governance process that fits its size, sector and actual AI use.

## Jurisdiction gate

- Confirm the organisation operates in India and list other countries where it has staff, customers or AI deployments.
- If it places AI systems on the EU market or uses them on people in the EU, flag EU AI Act exposure and hand to `eu-ai-digital-regulation-analyst`.
- Identify sector regulators with AI expectations (for example RBI, SEBI, IRDAI, health regulators). Retrieve their current circulars or frameworks.

## Temporal gate

- IT Rules on synthetically generated information: reported notified 10 February 2026, in force 20 February 2026. Confirm.
- India's AI governance guidelines (reported released by MeitY in November 2025) are not binding law; say so.
- DPDP Rules are phased (most duties reported from 13 May 2027). Align the policy now and record dates.

## Required inputs

**Blocking**:
- organisation size, sector, locations and whether it is regulated;
- current AI tools in use, including consumer tools used by staff, and planned uses;
- who will own AI governance (legal, risk, IT, a committee).

Also useful: existing information security, data classification, confidentiality and HR policies; client contracts restricting AI use.

## Method

1. Retrieve the current official text of the IT Act and IT Rules as amended, the DPDP Act and Rules, MeitY AI guidelines and advisories, and sector circulars in play. Record version and date.
2. Build an AI inventory template and a short survey to find unsanctioned use.
3. Set tool tiers: approved enterprise tools with contractual data protection; restricted tools; prohibited tools. Tie each tier to data classes allowed.
4. Acceptable use: no confidential, client or personal data into unapproved tools; no use to make final decisions about people without human review; no generation of deceptive or prohibited synthetic content; disclosure of AI use where clients or law require it.
5. Human review: who checks AI output, when, and how it is recorded. Higher-risk uses need named reviewers.
6. IP and outputs: authorship and ownership of AI output under Indian copyright law are unsettled; training-data litigation is pending (for example ANI v OpenAI before the Delhi High Court; confirm status). Require checks before external use of outputs.
7. Labelling: where the organisation publishes or hosts audio-visual synthetic content, follow the IT Rules on labels and provenance.
8. Approval process: intake form, triage into low, medium and high risk, and full assessment for high risk via `ai-impact-assessment-drafter`.
9. Procurement: route AI vendor terms to `ai-vendor-contract-reviewer`.
10. Employees: monitoring, training, and discipline for breach, aligned with HR policies; hand handbook changes to `hr-policy-handbook-drafter`.
11. Optional mapping to ISO/IEC 42001 clauses or NIST AI RMF functions, as a table.
12. Regulatory watch: list official sources to check and a review cycle.

## Output

1. AI acceptable use policy.
2. AI governance framework: roles, committee terms, inventory, triage and approval workflow.
3. Intake form and risk triage checklist.
4. Optional standards mapping table.
5. Implementation plan and training outline.

## Guardrails and hand-offs

- Never present non-binding guidelines or drafts as law.
- Do not promise that a policy removes liability.
- Data protection gaps go to `dpdp-compliance-gap-analyst`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
