---
name: pocso-case-analyst
description: Analyses cases under the Protection of Children from Sexual Offences Act, 2012 for the defence or the victim, covering age determination under the Juvenile Justice Act, 2015, mandatory reporting, recording of the child's statement, Special Court procedure, statutory presumptions, in-camera trial, support persons and compensation. Use when a POCSO chargesheet needs review, the victim's age is disputed, the statement was recorded late, or a family needs to know the child's rights. Do not use for drafting the bail application itself; use bnss-bail-application-drafter.
---

# POCSO Case Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Test a POCSO case for legal and procedural compliance, and protect the child's identity and welfare throughout.

## Jurisdiction gate

Confirm the case is before an Indian Special Court or police station. Record the State: POCSO Rules, victim compensation schemes, support-person panels and Special Court notifications vary. If the accused may be a child, flag the Juvenile Justice Act route and the Juvenile Justice Board.

## Temporal gate

Record the dates of the alleged acts, report and statements. Punishments for some POCSO offences were raised by the 2019 amendment; the law on the date of the act governs punishment. For procedure, check IPC/CrPC versus BNS/BNSS from 1 July 2024 with `crpc-bnss-transition-analyst`.

## Required inputs

**Blocking**: the FIR and police report or complaint; whom the user acts for; the alleged acts and their dates; the age documents on record (school records, birth certificate, medical age estimation); and the chargesheet.

Also useful: statements recorded by police and Magistrate, medical examination report, forensic reports, Child Welfare Committee orders and the Special Court's orders.

## Method

1. Retrieve the current official text of the POCSO Act, 2012, the POCSO Rules in force (2020 Rules believed current; confirm), the Juvenile Justice Act age-determination provision, the BNSS provisions on statements and medical examination, and the State compensation scheme. Record source and date.
2. Map each charged POCSO section to its ingredients and the evidence.
3. Age: apply the JJ Act order of documents (school certificate, birth certificate, then medical estimation) as confirmed from the text. Note the margin of error debates and current Supreme Court treatment; read before citing.
4. Procedure: who reported and when; police recording by a woman officer at the child's place where required; Magistrate statement; medical examination by the prescribed doctor; support person; information to the Child Welfare Committee and Special Court within the prescribed times.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates. Run the script even for a period in hours: do not add hours by hand. For a period in hours, give `--start` with a time, for example `--start 2026-10-15T14:30 --period 6h`.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
5. Trial safeguards: in-camera proceedings, no aggressive questioning, questions through the court, no disclosure of identity, and time limits for evidence and disposal.
6. Presumptions: identify which statutory presumptions apply (believed ss.29 and 30; confirm), when the foundational facts must first be proved, and what rebuttal standard current authority applies.
7. Compensation: interim and final compensation under the rules and scheme.
8. Search for current Supreme Court and High Court authority on any disputed point. Read it; tag anything unread `[verify]`.

## Output

1. A compliance table: each statutory step, done or not, with record reference.
2. An age analysis note.
3. A defence or victim-side issue list with next steps (bail, discharge, trial, compensation, protection).

## Guardrails and hand-offs

- If a blocking input is missing, ask for each one by name before giving a substantive answer; do not produce an analysis or draft with blanks first. Ask for the age documents and the chargesheet by name.
- Mark every section, article, rule number, period and last date as believed and to be confirmed against the official text, in tables, headlines and bold lines as well as in notes, and tag [verify] anything not checked against a primary source. A closing disclaimer alone is not enough. This covers every prescribed reporting and other time limit, including the 24-hour reporting period.
- If the user's stated count and the dates disagree, put the question "which is right?" to the user in plain words, and show both results as conditional until they reply.
- Never name the child or include details that could identify the child, family, school or locality in any output. Use initials or "the child".
- Never suggest pressure on the child or family, or out-of-court settlement of a POCSO offence.
- Never comment on the child's character or past.
- For trial, use `criminal-trial-readiness-checker`; for a record review, `chargesheet-review-analyst`.
