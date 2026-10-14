---
name: criminal-compounding-application-drafter
description: Drafts compounding applications under the Bharatiya Nagarik Suraksha Sanhita, 2023, distinguishing offences compoundable by the victim alone from those needing the court's permission, with the settlement deed, party affidavits and identification, and compounding of cheque-dishonour cases under the Negotiable Instruments Act. Use when complainant and accused have settled a compoundable case and want it closed in the trial or appellate court. Do not use for quashing on settlement of non-compoundable offences; use fir-quashing-petition-drafter.
---

# Criminal Compounding Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Close a criminal case lawfully on settlement, using the right route for each offence, with a record that shows the victim's free consent.

## Jurisdiction gate

Confirm the case is before an Indian court and record the State, court and stage (investigation, trial, appeal, revision). Check whether the State has amended the compounding table. If any offence is not compoundable, stop and route to `fir-quashing-petition-drafter`.

## Temporal gate

Record the date of offence. If it falls before 1 July 2024, the IPC and CrPC tables may apply; map offences with `ipc-bns-concordance-mapper` and check with `crpc-bnss-transition-analyst`.

## Required inputs

Mark as **blocking**:
- the FIR or complaint particulars and every offence charged;
- the court, case number and stage;
- the identity of the person entitled to compound (the victim, or the legal heir or guardian where the law allows);
- the agreed settlement terms.

## Method

1. Retrieve the current official text of the BNSS compounding provision and its tables (believed to be section 359; confirm), any State amendment, the BNS offence sections, and for cheque cases the Negotiable Instruments Act compounding provision. Record the source and date.
2. Classify each offence: compoundable without permission, compoundable with permission of the court, or not compoundable. A single non-compoundable offence changes the route.
3. Check any bar, for example where the accused has a prior conviction or the offence carries an enhanced punishment.
4. Draft a settlement deed: parties, the case, terms, payment schedule, and a clear statement that consent is free and not induced.
5. Draft affidavits of the victim and the accused, with identification by counsel. A minor or incapable victim needs a guardian, and the court's permission.
6. Draft the compounding application, joint or by the victim, with the court's permission where needed. State the effect: compounding amounts to acquittal.
7. For cheque cases, apply the cost guidelines the Supreme Court set (for example Damodar S. Prabhu v. Sayed Babalal H., 2010; confirm current treatment and later modifications). Hand the case details to `cheque-dishonour-case-drafter` if the complaint itself needs work.
8. Search for current authority and tag anything unread `[verify]`.

## Output

1. An offence-wise compounding table with source.
2. Settlement deed, affidavits and compounding application.
3. A note on costs, payment proof and court appearance.

## Guardrails and hand-offs

- Never treat a non-compoundable offence as compoundable.
- Watch for coercion; if the victim appears pressured, flag it to the advocate.
- FEMA or regulatory compounding goes to `fema-regularisation-drafter` or `regulator-notice-reply-drafter`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
- Tag [verify] on every case cited and every offence row in the compounding table that was not read in the official text, not only some; say plainly in the table's source column when the official table was not retrieved, and do not present such a classification as settled.
- If a blocking input is missing, ask for each one by name before drafting or giving a substantive answer.
