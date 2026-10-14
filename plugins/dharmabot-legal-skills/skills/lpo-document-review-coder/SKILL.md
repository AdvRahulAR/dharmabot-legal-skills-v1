---
name: lpo-document-review-coder
description: Codes documents in a review for foreign litigation, arbitration, investigations or due diligence run by a US, UK or other foreign law firm, as done in Indian LPO and document-review teams. Applies the review protocol for responsiveness, issue tags, privilege (US attorney–client and work product; UK legal advice and litigation privilege), confidentiality and personal data redaction, and builds privilege-log entries. Use when an Indian reviewer or team is coding documents under a foreign firm's protocol, or needs a protocol turned into coding rules. Do not use to give the end client advice.
---

# LPO Document Review Coder

Every output is first-level review work for supervising counsel to check.

## Purpose

Apply the instructing firm's review protocol consistently and explain each coding decision briefly, so supervising lawyers can quality-check quickly.

## Jurisdiction gate

Identify the instructing firm, the matter, the forum (for example a US federal court, the English Business and Property Courts, an arbitral tribunal or a regulator), and the protocol version. The protocol always prevails over this skill's defaults. If no protocol is supplied, stop and ask for it, or offer to draft one for counsel's approval.

## Required inputs

Mark as **blocking**:
- the review protocol (issues, definitions, coding fields, privilege instructions, list of attorneys and law firms, date range, custodians);
- the documents or batch;
- the confidentiality and data-handling rules for the engagement.

## Method

1. Turn the protocol into a coding checklist: fields, allowed values, and decision rules. Ask counsel to approve it before the first batch.
2. For each document, record:
   - **Responsiveness** under the protocol's definitions.
   - **Issue tags**, with the key sentence quoted.
   - **Privilege:**
     - US: attorney–client privilege needs a communication with a lawyer, for legal advice, and kept confidential; work product needs material prepared in anticipation of litigation.
     - UK: legal advice privilege and litigation privilege.
     - Flag the document if a third party was copied (possible waiver), if it has mixed business and legal purposes, or if in-house counsel is involved, since EU competition investigations treat in-house advice differently.
     - Code as the protocol directs: privileged, partially privileged (redact) or not privileged.
   - **Confidentiality designation**, if the protective order requires one.
   - **Personal data** to redact (for example under GDPR or the DPDP Act) where the protocol directs.
   - **Hot-document** flags.
3. For privileged documents, draft a privilege-log entry: date, author, recipients, document type, privilege basis, and a description that does not reveal the advice. Use the format of the forum's rules or the protocol. In US federal court, see FRCP 26(b)(5) and the case-management order, and check the December 2025 amendments to FRCP 16(b) and 26(f) on privilege-log timing and method. In the English Business and Property Courts, privilege claims are made in the list of documents and Disclosure Review Document under Practice Direction 57AD, as the protocol directs. Retrieve the current rules if the protocol does not specify.
4. Note any document that is unclear, in a foreign language (hand off to `legal-translation-verifier`), or needs escalation, with a reason.

## Output

1. A coding table: document ID · responsive · issues · privilege · confidentiality · redactions · notes.
2. Privilege-log entries.
3. An escalation list for supervising counsel.

## Guardrails

- Follow the protocol over any default here, and note any conflict for counsel.
- Treat all documents as confidential; never copy them outside the review platform or session.
- Never contact the client or opposing parties, or give legal advice on the matter.
