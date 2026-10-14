---
name: criminal-appeal-revision-drafter
description: Plans and drafts criminal appeals, revisions and victim appeals against acquittal under the Bharatiya Nagarik Suraksha Sanhita, 2023, with grounds tied to the trial record, applications for suspension of sentence and bail pending appeal, and criminal transfer petitions, identifying the correct forum and limitation. Use when a client is convicted or acquitted and wants to appeal, challenge an interlocutory order in revision, get sentence suspended, or transfer a criminal case to another court. Do not use for the hearing on sentence in the trial court; use sentencing-mitigation-analyst.
---

# Criminal Appeal and Revision Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Choose the right remedy and forum, compute the deadline, and draft grounds that the record supports.

## Jurisdiction gate

Confirm the order was passed by an Indian court. Record the court, State and type of order (conviction, acquittal, sentence, interlocutory, final). Identify the appellate or revisional forum (Sessions Court, High Court, Supreme Court). Note special statutes with their own appeal routes (for example NIA Act, POCSO, NDPS).

## Temporal gate

Record the dates of the offence, judgment and receipt of the certified copy. For proceedings that began before 1 July 2024, check whether CrPC or BNSS appeal provisions apply using `crpc-bnss-transition-analyst`.

## Required inputs

**Blocking**: the judgment and order under challenge; the date of pronouncement and of the certified copy application; whom the user acts for (convict, State, victim, complainant); and custody status.

Also useful: the trial record (depositions, exhibits), earlier bail orders, and the sentence served.

## Method

1. Retrieve the current official text of the BNSS chapters on appeals and revision, the provisions on suspension of sentence pending appeal, the victim's right of appeal, leave requirements for appeals against acquittal, and the Limitation Act articles. Record source and date. Confirm all section numbers.
2. Classify the order and pick the remedy: appeal as of right, appeal by leave, revision, or a petition to the High Court. Note that revision does not lie against interlocutory orders; check the current test.
3. Compute limitation with `limitation-calculator`, excluding time for certified copies as the law allows. Prepare a delay condonation application if needed.
4. Read the judgment and record. List findings and the evidence relied on.
5. Draft grounds: misreading or non-reading of evidence, wrong burden, inadmissible evidence relied on, defective charge, defects in the accused's examination, wrong law on ingredients, sentence errors. Tie each ground to page and paragraph.
6. Flag points not raised below and whether they can be raised now (pure questions of law usually can; confirm).
7. For transfer of a criminal case, retrieve the BNSS transfer provisions (believed to be sections 446 to 450, for the Supreme Court, High Court and Sessions Judge; confirm from the official text). Pick the lowest competent forum. Ground the petition in record facts showing a reasonable apprehension of injustice, not mere suspicion, and add an affidavit and any stay of trial sought.
8. For suspension of sentence and bail, set out sentence length, time served, appeal hearing delay, conduct on bail and arguable points.
9. Search for current Supreme Court and High Court authority on each ground. Read it; tag anything unread `[verify]`. Hand off to `citation-verifier`.

## Output

1. A remedy and deadline note.
2. The memorandum of appeal or revision petition with grounds and prayer.
3. An application for suspension of sentence and bail, any delay condonation application, or a transfer petition with affidavit.
4. A list of record documents to file.

## Guardrails and hand-offs

- Never misquote the judgment or depositions.
- Never promise acquittal or suspension.
- For layout, use `court-pleading-formatter`; for sentence arguments, `sentencing-mitigation-analyst`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has reportedly held that citing unverified AI-generated judgments is advocate misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank, 2026 INSC 668; reported; confirm).
