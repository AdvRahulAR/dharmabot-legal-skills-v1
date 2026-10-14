---
name: evidence-affidavit-drafter
description: Drafts examination-in-chief affidavits under Order XVIII Rule 4 of the Code of Civil Procedure and witness statements for Indian civil, commercial and tribunal proceedings, exhibiting documents in order and proving them under the Bharatiya Sakshya Adhiniyam, 2023, including electronic records. Use when an advocate asks for an evidence affidavit, affidavit in lieu of chief, proof affidavit or witness statement. Do not use for the electronic evidence certificate itself; use bsa-electronic-evidence-certificate-drafter instead.
---

# Evidence Affidavit Drafter

Every output is a draft for an advocate enrolled in India to check, and for the witness to read, correct and swear.

## Purpose

Put the witness's own knowledge into a clear affidavit that proves each document needed for the issues, without overreach.

## Jurisdiction gate

Confirm the proceeding is before an Indian court or tribunal and note the forum and State. Check whether the forum accepts affidavit evidence and in what format.

## Temporal gate

The Bharatiya Sakshya Adhiniyam, 2023 replaced the Indian Evidence Act, 1872 from 1 July 2024. Check from the official text and current authority which statute governs evidence in this proceeding, especially for suits pending on that date, and cite the correct one.

## Required inputs

Mark as **blocking**:
- the pleadings and the issues framed;
- the witness's identity, role and source of knowledge;
- the documents to be proved, with originals or the reason originals are unavailable;
- the witness's own account, from an interview or notes.

## Method

1. Retrieve the current official text of Order XVIII CPC, the Bharatiya Sakshya Adhiniyam provisions on primary and secondary evidence, electronic records and proof of documents, and the forum's practice directions. Record the version and date.
2. Map each issue to the facts this witness can prove and the documents they can identify.
3. Draft in the first person, in plain language the witness understands. Confine each paragraph to facts within personal knowledge, or say clearly the source of information and belief.
4. Exhibit documents in a logical order with proposed exhibit marks. For each, state how the witness knows it (author, recipient, custodian).
5. For secondary evidence, plead the foundation (loss, possession of the other side, and so on). For electronic records, flag the certificate requirement and hand off.
6. Leave out argument, legal submissions and hearsay.
7. Add the verification and jurat in the forum's format, and an index of exhibits.

## Output

1. The draft affidavit of evidence.
2. An exhibit table: exhibit mark · document · date · mode of proof · original available.
3. A note of gaps: documents this witness cannot prove and who can.

## Guardrails and hand-offs

- Never put words in a witness's mouth that the witness has not confirmed. Never coach false testimony.
- Never state that a document is original unless confirmed.
- Electronic evidence certificate: `bsa-electronic-evidence-certificate-drafter`.
- Preparing to meet the other side's witnesses: `cross-examination-planner`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
