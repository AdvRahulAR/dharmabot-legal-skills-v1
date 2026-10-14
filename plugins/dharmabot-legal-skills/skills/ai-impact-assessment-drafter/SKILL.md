---
name: ai-impact-assessment-drafter
description: Runs a structured AI impact assessment of a proposed AI system or use case under Indian law, covering DPDP Act compliance, bias and discrimination risk under constitutional, labour and disability laws, transparency, human oversight, IP and training data, security, sector rules (RBI, SEBI, ICMR, CDSCO), and classifies the use as approve, approve with conditions or reject. Use when a client asks whether to deploy AI for hiring, credit scoring, claims, customer chat, medical triage or an AI agent. Do not use for a company-wide AI policy; use ai-governance-policy-drafter instead.
---

# AI Impact Assessment Drafter

Every output is a draft review for an advocate enrolled in India and the client's decision-makers to check. The decision belongs to the client.

## Purpose

Test one AI use case against the law and the organisation's risk appetite, and record a reasoned recommendation with conditions.

## Jurisdiction gate

- Confirm where the system is deployed and whose data and interests it affects.
- If affected people are in the EU, flag possible high-risk classification under the EU AI Act and hand to `eu-ai-digital-regulation-analyst`.
- Identify the sector regulator and retrieve its rules on AI, models or outsourcing.

## Temporal gate

Record the assessment date. DPDP duties are phased (most reported from 13 May 2027), and AI rules and guidelines change often. Note which requirements are in force, which are coming, and which are guidance only.

## Required inputs

**Blocking**:
- what the system does, the decision it supports or makes, and who is affected;
- the model and vendor, whether it is built, fine-tuned or bought, and what data trains and feeds it;
- the human role: who reviews outputs, and whether the system can act on its own (send, pay, approve, reject).

Also useful: vendor documentation, testing and accuracy results, bias testing, and the business case.

## Method

1. Retrieve the current official text of the DPDP Act and Rules, the IT Act and Rules, and sector rules in play (for example RBI guidance on models and outsourcing, SEBI circulars on AI use by intermediaries, ICMR guidance on AI in health, CDSCO rules on software as a medical device). Record version and date.
2. Describe the use case: purpose, decision, affected people, scale, and harm if wrong.
3. Personal data: ground for processing, notice, children's data, rights handling, retention, and processor contracts. Hand gaps to `dpdp-compliance-gap-analyst`.
4. Bias and discrimination: identify protected characteristics under applicable laws (for example the Rights of Persons with Disabilities Act, 2016, the Transgender Persons (Protection of Rights) Act, 2019, the Labour Codes and, for State bodies, Articles 14 to 16). Ask for bias test results by group; if none, make testing a condition.
5. Transparency: whether affected people must or should be told AI is used, and how they can seek human review.
6. Human oversight: who reviews, with what authority and training, and how overrides are recorded.
7. Agentic actions: if the system can act, set authority limits (value caps, approvals, logging, kill switch) and record them.
8. IP and training data: rights to training data, output ownership, and vendor indemnities.
9. Security: prompt injection, data leakage, model access, and logs.
10. Contracts: hand vendor terms to `ai-vendor-contract-reviewer`.
11. Rate each risk (likelihood and impact), propose mitigations, and classify: approve, approve with conditions, or reject.

## Output

1. AI impact assessment report: description, legal analysis by head, risk register, mitigations.
2. Recommendation with conditions and owners.
3. Authority-limits table for agentic systems.
4. Monitoring and re-assessment triggers.

## Guardrails and hand-offs

- Never fill in accuracy, bias or test results; mark them "not provided".
- Never approve a fully automated decision with legal or similarly significant effect without flagging it for senior review.
- Policy-level changes go to `ai-governance-policy-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
