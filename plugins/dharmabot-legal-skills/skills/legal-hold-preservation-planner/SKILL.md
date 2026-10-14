---
name: legal-hold-preservation-planner
description: Plans preservation of documents and data in India when litigation, an investigation or regulatory action is anticipated, covering custodians, hold notices, suspension of auto-deletion, CERT-In log retention, forensic imaging, chain of custody for Bharatiya Sakshya Adhiniyam certificates, and release of holds. Use when a suit, complaint or regulator inquiry is expected and someone asks for a legal hold notice or a WhatsApp and email preservation plan. Do not use to draft the s.63 BSA certificate itself; use bsa-electronic-evidence-certificate-drafter.
---

# Legal Hold and Preservation Planner

Every output is a draft for supervising counsel to check before issue.

## Purpose

Preserve relevant data early and defensibly, so that it can be proved later and no one can allege destruction.

## Jurisdiction gate

Confirm the anticipated matter is in India or the data sits with an Indian entity. Record where data is stored (on premises, Indian cloud, foreign cloud, personal devices). For foreign proceedings or data held abroad, flag disclosure and transfer rules for counsel qualified in that jurisdiction.

## Required inputs

**Blocking**: the anticipated matter and the trigger date (letter, notice, incident); the subject matter and period; the likely custodians; and the data systems in use (email, chat, WhatsApp, ERP, shared drives, devices).

Also useful: the retention policy, IT contact, backup schedules, BYOD policy, and any notice already received from the other side or a regulator.

## Method

1. Retrieve the current official text of the BSA provisions on electronic records and certificates, the CERT-In directions on log retention, the DPDP Act and Rules as in force (to limit and secure personal data), and any regulator record-keeping rules for the sector. Record source and date.
2. Fix the trigger date and the scope (subjects, period, custodians, data types). Keep it proportionate.
3. Map data sources per custodian, including mobile chats, personal devices used for work, and third-party vendors.
4. Suspend deletion: auto-delete, mailbox purges, device recycling and exit wipes for custodians. Record each change with date and who made it.
5. Draft the hold notice: plain language, what to keep, what not to do, who to ask, and an acknowledgment. Plan reminders and new-joiner custodians.
6. Collection: decide where forensic imaging is needed; use qualified examiners; record device details, method, tools and hash values as produced by the tool (never invented); keep originals sealed.
7. Chain of custody: a log for every transfer, with dates, people and purpose, designed so a certificate can later be given under the BSA via `bsa-electronic-evidence-certificate-drafter`.
8. Spoliation risk: flag data already lost and record the explanation.
9. Release: when the matter ends, confirm in writing and resume normal retention.

## Output

1. A preservation plan with a custodian and data-source matrix.
2. The legal hold notice and acknowledgment form.
3. A chain-of-custody log template and an IT action checklist.

## Guardrails and hand-offs

- Never advise deleting or altering data after the trigger.
- Never invent hash values, dates or tool outputs.
- Collect personal data only as needed and secure it.
- For a wider investigation, use `internal-investigation-planner`.
