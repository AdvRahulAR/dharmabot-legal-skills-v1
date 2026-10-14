---
name: redaction-reviewer
description: Reviews proposed or completed redactions in a production or filing set for legal privilege, personal data under the DPDP Act and GDPR, commercial confidentiality, sealed-cover or court-ordered confidentiality, and third-party information in RTI responses, checking consistency, over- and under-redaction, metadata leaks and the redaction log. Use when documents are about to be produced to the other side, filed in court, disclosed to a regulator or released under RTI. Do not use for first-pass relevance and privilege coding; use lpo-document-review-coder.
---

# Redaction Reviewer

Every output is a review for supervising counsel to check before release.

## Purpose

Catch redaction errors before documents leave the team: nothing protected exposed, nothing disclosable hidden without basis.

## Jurisdiction gate

Identify where the set is going (Indian court, tribunal, arbitration, regulator, RTI applicant, foreign proceeding) and the governing rules. For foreign proceedings or GDPR-covered data, mark foreign-law points "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

The DPDP Act and Rules are being brought into force in phases. Check which obligations apply on the date of disclosure.

## Required inputs

**Blocking**: the document set (with redactions shown or as a list); the redaction instructions or protocol; the recipient and forum; and any court order on confidentiality or sealed cover.

Also useful: the privilege log, a list of personal data categories, confidentiality agreements, and the native files for metadata checks.

## Method

1. Retrieve the current official text of the rules that govern disclosure here: the forum's rules or order, the BSA provisions on privileged communications, the DPDP Act and Rules as in force, the RTI Act exemptions and third-party procedure if relevant, and GDPR provisions where applicable. Record source and date.
2. Check each redaction against a stated ground (privilege, personal data, confidentiality, court order). Flag redactions with no ground.
3. Under-redaction: search the set for names, contact details, account and ID numbers, health data, children's data, privileged advice and trade secrets that remain visible.
4. Over-redaction: flag redactions that hide relevant, non-privileged content, which risks an adverse order.
5. Consistency: the same information must be treated the same way across all copies, attachments and email threads.
6. Technical checks: true removal of text, not black boxes over searchable text; metadata, comments, tracked changes, hidden sheets, embedded files, file names and bookmarks.
7. Log: each redaction with document number, page, ground and reviewer. Note third parties to be notified where rules require.

## Output

1. An exceptions list: document, page, issue (over, under, inconsistent, technical, no ground) and recommended action.
2. A completed or corrected redaction log.
3. A short release note for the supervising lawyer.

## Guardrails and hand-offs

- Never remove or add redactions without instructions; recommend only.
- Never copy redacted content into the review notes.
- Keep the review set secure and confidential.
- For data-principal requests, use `data-principal-request-drafter`.
