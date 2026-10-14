---
name: discharge-application-drafter
description: Drafts discharge applications at the charge stage in Sessions, warrant and summons trials under the Bharatiya Nagarik Suraksha Sanhita, 2023, testing offence by offence and accused by accused whether the police report and documents show sufficient ground to proceed. Use when an advocate asks for a discharge application, says the chargesheet shows no act by the client, or wants to oppose framing of charge. Do not use to analyse the full chargesheet for trial gaps; use chargesheet-review-analyst.
---

# Discharge Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Show the court, using only the prosecution's record, that there is no sufficient ground to proceed against the accused for one or more offences.

## Jurisdiction gate

Confirm the case is before an Indian criminal court. Record the court, State and type of trial (Sessions, warrant case on police report, warrant case on complaint, summons case). Note special statutes with their own Special Courts or procedure.

## Temporal gate

Record the dates of the offence, chargesheet and commitment. If any falls before 1 July 2024, check which code governs the procedure with `crpc-bnss-transition-analyst`. Check whether the BNSS sets a time limit for filing discharge applications from commitment or supply of documents, and record it as believed until confirmed.

## Required inputs

**Blocking**: the police report and its documents as supplied to the accused; the offences charged; the accused's role as alleged; the trial type and stage.

Also useful: orders on cognizance and commitment, co-accused positions, and any sanction order.

## Method

1. Retrieve the current official text of the BNSS discharge provisions for each trial type (Sessions discharge believed to be s.250; warrant case on police report believed to be s.262; confirm), the offences, and any State amendment. Record source and date.
2. Check timing. If a time limit applies, compute it with `limitation-calculator` and flag delay.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. List each offence and its ingredients. For each accused, list what the record says he did, citing page and paragraph.
4. Apply the test from Union of India v. Prafulla Kumar Samal (Supreme Court, 1979) and Sajjan Kumar v. CBI (Supreme Court, 2010): grave suspicion versus mere suspicion, taking the record at face value. Confirm current treatment.
5. Identify gaps: an ingredient with no material; statements that do not name the accused; documents that do not support the allegation; missing sanction; offences added without basis.
6. Where some offences survive, ask for discharge from the rest, or for charge under a lesser offence.
7. Search for and read current authority on the scope of the court's power at this stage. Tag anything unread `[verify]`.

## Output

1. The discharge application: facts, an offence-by-offence and accused-by-accused table with record references, grounds and prayer.
2. A note on the strongest and weakest points and the likely prosecution reply.
3. A fallback: points to preserve for revision or trial.

## Guardrails and hand-offs

- Rely only on the prosecution record. Do not cite defence documents unless the law allows them at this stage; flag them for trial instead.
- Never invent page references or statements.
- Never promise discharge.
- For deeper ingredient analysis, use `fir-ingredients-analyst`; for a full gap review, `chargesheet-review-analyst`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
