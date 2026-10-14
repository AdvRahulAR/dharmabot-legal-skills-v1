---
name: witness-summons-list-drafter
description: Drafts the list of witnesses under Order XVI of the Code of Civil Procedure after issues are settled, applications to summon witnesses to give evidence or produce documents, expense deposits and non-attendance applications, and the matching defence-witness and document-summons applications in criminal trials under the Bharatiya Nagarik Suraksha Sanhita, 2023. Use when issues are framed and the advocate needs a witness list, or must summon a bank, hospital or government officer with records. Do not use for the evidence affidavit; use evidence-affidavit-drafter.
---

# Witness Summons and List Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Get the right witnesses and documents before the court in time, with applications that show relevance and meet the procedural deadlines.

## Jurisdiction gate

Confirm the case is before an Indian court. Record the State, court and case type. Note any High Court rules on witness lists and expenses, and whether the suit is a commercial suit with a case-management timetable.

## Temporal gate

For criminal trials, check whether the BNSS or the Code of Criminal Procedure, 1973 governs. If the case began before 1 July 2024, run `crpc-bnss-transition-analyst` first.

## Required inputs

Mark as **blocking**:
- the court, case number and stage;
- for civil suits, the date issues were settled and any order fixing a timetable;
- each proposed witness, what they will prove, and any document to be produced;
- the address and designation of official witnesses.

## Method

1. Retrieve the current official text of Order XVI and Order XVI-A CPC, any State amendment, the High Court's rules on witness expenses, and the BNSS provisions on defence evidence and summons to produce documents (confirm each section number). Record the source and date.
2. Compute the time for filing the list of witnesses from the date of settling issues with `limitation-calculator`. If late, draft a short application showing good cause.
3. For each witness, state the issue it goes to and why the evidence is relevant. Courts may refuse witnesses whose purpose is unclear.
4. Draft summons applications. For a document summons, describe the record precisely (account number placeholder, period, register name) and whether a certified copy or the original is needed.
5. Note expenses and conduct money: who deposits, how much the rules require, and when. Confirm amounts from the rules.
6. For non-attendance, draft an application seeking fresh summons, bailable warrant or other coercive steps the rules allow.
7. For criminal trials, draft the defence-witness list and document-summons application, explaining why each is not for vexation or delay.
8. Hand service tracking to `service-of-process-tracker`.

## Output

1. List of witnesses with purpose for each.
2. Summons and document-production applications.
3. Expense deposit note.
4. Non-attendance application template.

## Guardrails and hand-offs

- Do not draft the examination-in-chief affidavit; use `evidence-affidavit-drafter`.
- Cross-examination planning goes to `cross-examination-planner`.
- Never invent a witness's role, address or record details.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
