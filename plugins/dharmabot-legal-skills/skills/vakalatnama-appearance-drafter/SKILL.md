---
name: vakalatnama-appearance-drafter
description: Drafts vakalatnamas under Order III Rule 4 of the Code of Civil Procedure and in criminal courts, memos of appearance (including under the Supreme Court Rules, 2013), no-objection letters and applications to change or discharge an advocate, with State stamp and welfare-fund requirements. Use when a client is engaging new counsel, the earlier advocate refuses NOC, or a memo of appearance or vakalat is needed for a forum. Do not use for general or litigation powers of attorney; use power-of-attorney-drafter.
---

# Vakalatnama and Appearance Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce appearance papers that the registry accepts first time, and handle a change of advocate cleanly and professionally, including where NOC is refused.

## Jurisdiction gate

Confirm the forum is an Indian court or tribunal. Record the State, district and court, because vakalat format, stamps and welfare-fund requirements vary by State and by High Court rules. Note whether the forum needs an advocate-on-record (for example the Supreme Court).

## Required inputs

Mark as **blocking**:
- the forum, case type, case number and stage;
- the party represented and who signs for it (individual, company through an authorised signatory, minor through guardian);
- the advocate's name, enrolment number and Bar Council;
- for a change of advocate, the name of the existing advocate and whether NOC is given or refused.

Also useful: board resolution or authority letter, client identity proof, and the court's own vakalat form.

## Method

1. Retrieve the current official text of Order III CPC, the High Court's civil and criminal rules of practice on appearance, the Supreme Court Rules, 2013 where relevant, and the State Advocates' Welfare Fund law. Record the source and date. Open `references/india-state-statutes.md` as a starting point for the State law.
2. Fix the format: the court's prescribed form if one exists, otherwise a standard vakalat with the cause title, the powers given, and acceptance by the advocate.
3. Check signature formalities: client signature or thumb impression with identification, authority for corporate or representative signatories, and the advocate's acceptance with enrolment details.
4. List the stamps needed (court-fee stamp on vakalat, welfare-fund stamp) and confirm the current amounts from the State source. Never state amounts from memory.
5. For a memo of appearance, use the forum's format and note who may file it.
6. For a change of advocate:
   - with NOC, draft the NOC letter and the new vakalat;
   - without NOC, draft a courteous request for NOC, then an application seeking leave to file a fresh vakalat, stating that the earlier advocate was informed and that dues, if any, are not a ground to block appearance (confirm the current Bar Council position).
7. Draft any discharge application where the advocate withdraws, with notice to the client.

## Output

1. Vakalatnama or memo of appearance.
2. NOC letter, request for NOC, or application for change or discharge.
3. A stamp and signature checklist with sources.

## Guardrails and hand-offs

- Do not draft general or litigation powers of attorney; use `power-of-attorney-drafter`.
- Fee disputes or conduct questions between advocates go to `professional-conduct-advisor`.
- Never invent enrolment numbers, stamp values or rule numbers.
- Layout goes to `court-pleading-formatter`; covering letters to `registry-letter-drafter`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
