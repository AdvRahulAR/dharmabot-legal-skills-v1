---
name: compromise-withdrawal-petition-drafter
description: Drafts joint compromise petitions under Order XXIII Rule 3 of the Code of Civil Procedure with terms executable as a decree (instalments, default clauses, property descriptions needing stamp or registration), withdrawal applications with liberty to file afresh under Rule 1, and memos of settlement, flagging the bar in Rule 3A. Use when parties have settled a pending suit or appeal and want a decree in terms, or a party wants to withdraw with liberty. Do not use for out-of-court mediated settlements; use mediated-settlement-agreement-drafter.
---

# Compromise and Withdrawal Petition Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Turn a settlement into a court record that can be executed without fresh litigation, or end a proceeding by withdrawal without losing the right to sue again.

## Jurisdiction gate

Confirm the proceeding is pending before an Indian court and record the State. Stamp duty, registration and court-fee refund rules vary by State. If the matter is before a Lok Adalat, use `lok-adalat-settlement-drafter` instead.

## Required inputs

Mark as **blocking**:
- the case number, court, parties and the reliefs claimed;
- the agreed terms (amounts, dates, property, conduct obligations);
- confirmation that each party, or its authorised signatory, will sign the petition;
- for withdrawal, whether liberty to file afresh is sought and the formal defect or sufficient ground for it.

## Method

1. Retrieve the current official text of Order XXIII CPC (Rules 1, 3, 3A and 3B, with any State amendment), Order XXXII Rule 7 where a minor is involved, the Registration Act, 1908 provisions on compromise decrees, and the State stamp and court-fee law. Record the source and date.
2. Check the compromise is lawful, in writing and signed by the parties. Flag minors, representative suits and any third-party rights.
3. Draft terms so each obligation is certain: who pays what, by when, to which account, and what happens on default (for example the whole balance falls due and is executable). Avoid vague words like "shall co-operate".
4. Describe any immovable property precisely. If the compromise covers property beyond the subject matter of the suit, flag registration and stamp duty and hand off to `state-stamp-duty-calculator`.
5. State whether the decree is to be in terms of the compromise, and list which terms form part of the decree.
6. Check any refund of court fee on settlement under the State law and add a prayer if available.
7. For withdrawal, distinguish abandonment from withdrawal with liberty. State the formal defect or sufficient ground. Warn of the bar on a fresh suit without liberty.
8. Flag the Rule 3A bar on a separate suit to set aside a compromise decree, so the parties know challenges must go to the same court.

## Output

1. Joint compromise petition with annexed terms, or withdrawal application.
2. A default and execution note: how each term would be enforced.
3. A stamp, registration and court-fee checklist.

## Guardrails and hand-offs

- Do not add or soften terms the parties did not agree.
- Never state stamp or fee amounts from memory.
- Enforcement after default goes to `execution-contempt-petition-drafter`.
- Out-of-court mediated settlements go to `mediated-settlement-agreement-drafter`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
