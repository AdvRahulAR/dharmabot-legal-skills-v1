---
name: internal-investigation-planner
description: Triages whistleblower complaints and plans internal investigations for Indian companies, covering the vigil mechanism under the Companies Act, 2013 and SEBI listing rules, auditor fraud reporting, independence and privilege, preservation, interviews, DPDP Act limits on employee data, and regulator reporting. Use when a company receives a whistleblower or anonymous complaint, suspects kickbacks or fraud, or asks how to run an investigation. Do not use for writing up findings; use investigation-report-drafter.
---

# Internal Investigation Planner

Every output is a draft plan for supervising counsel to check.

## Purpose

Turn an allegation into a scoped, independent and lawful investigation plan before anyone reaches a conclusion.

## Jurisdiction gate

Confirm the company, the subjects and the data are in India. Record the company type (listed, unlisted public, private, LLP, branch of a foreign company) and the regulators (SEBI, RBI, IRDAI, others). If data, employees or conduct are abroad, flag foreign anti-bribery and data laws for counsel qualified in that jurisdiction.

## Temporal gate

The DPDP Act, 2023 and the DPDP Rules are being brought into force in phases. Check which provisions are in force on the date of processing, and from when, before relying on them.

## Required inputs

**Blocking**: the complaint or allegation as received; the company type and regulators; who the subjects are and their reporting lines; and who instructs the investigation (board, audit committee, management).

Also useful: the whistleblower policy, code of conduct, employment terms, IT and device policies, and any earlier complaints on the same subject.

## Method

1. Retrieve the current official text of the Companies Act provisions on vigil mechanism and auditor fraud reporting (believed ss.177 and 143(12); confirm), the related rules, SEBI listing and insider trading provisions on whistleblowers if listed, the DPDP Act and Rules as in force, and the company's own policies. Record source and date.
2. Triage: is the complaint specific and credible; does it involve senior management or directors (route to the audit committee); is there urgency (ongoing loss, evidence destruction, safety).
3. Independence: decide who investigates. Where privilege matters, engage external counsel to direct the work. Note that legal professional privilege under the BSA is narrower than in some foreign systems; confirm its scope.
4. Preservation: trigger a legal hold with `legal-hold-preservation-planner` before interviews.
5. Scope and hypotheses: list allegations as questions; plan document review and funds tracing with `fraud-funds-flow-analyst`.
6. Interviews: order (witnesses before subject), notice, a support person where policy allows, notes, no coercion. Give the subject a fair chance to respond.
7. Data limits: process employee data only as the DPDP Act and policies allow; avoid personal devices without consent or lawful basis.
8. Reporting duties: auditor reporting, regulator or stock exchange disclosures, police complaint, and insurer notification. Check each against its current text.
9. Whistleblower protection: confidentiality, no retaliation, and a record of protective steps.
10. Keep an investigation log from day one.

## Output

1. A triage note and recommended forum.
2. An investigation plan: scope, team, timeline, evidence sources, interview list and reporting duties.
3. A log template and a whistleblower protection checklist.

## Guardrails and hand-offs

- Never reach or state conclusions before evidence.
- Never suggest surveillance, device access or recording that the law or policy does not allow.
- Never disclose the whistleblower's identity without consent and need.
- For disciplinary action, use `disciplinary-inquiry-drafter`; for the report, `investigation-report-drafter`.
