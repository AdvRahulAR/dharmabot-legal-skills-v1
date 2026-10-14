---
name: service-law-matter-analyst
description: Analyses Indian public service disputes on recruitment, seniority, promotion, sealed-cover procedure, transfer, disciplinary proceedings under the CCS (CCA) Rules, 1965 and State equivalents, Article 311 protections, and pension and retiral benefits, and drafts original applications before the Central or a State Administrative Tribunal or the Armed Forces Tribunal, or writs. Use when a government employee is denied promotion, faces a chargesheet or dismissal, or has a pension or seniority grievance. Do not use for private-sector employment disputes; use labour-dispute-claim-drafter.
---

# Service Law Matter Analyst

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Identify the right service rule, the right forum and the time limit, and set out the employee's or employer's strongest case.

## Jurisdiction gate

Identify the employer: Union, State, UT, PSU, statutory body, or armed forces. That decides the rules and the forum: the Central Administrative Tribunal, a State Administrative Tribunal (where one exists; confirm whether the State has one), the Armed Forces Tribunal, or the High Court. Under L. Chandra Kumar v. Union of India (Supreme Court, 1997) the tribunal is usually the first forum, with the High Court above it; confirm current treatment.

## Required inputs

**Blocking**: the employer and the employee's post, service and cadre; the impugned order or inaction and its date; the service rules that apply; and any representation or departmental appeal made and its outcome.

Also useful: recruitment rules, seniority lists, DPC minutes, APARs, the chargesheet and inquiry record, and orders in similar cases.

## Method

1. Retrieve the current official text of the applicable service rules (for example CCS (CCA) Rules, 1965, CCS (Conduct) Rules, Pension Rules, or State equivalents), the recruitment rules, relevant DoPT or State government office memoranda, and the Administrative Tribunals Act, 1985 or Armed Forces Tribunal Act, 2007. Record source and date.
2. Classify the grievance: recruitment, seniority, promotion, transfer, discipline, pension, pay.
3. Exhaustion: check whether statutory departmental remedies must be used first, and their periods.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. Limitation: compute the tribunal's limitation and any delay condonation needed with `limitation-calculator`. Note continuing-wrong arguments for pay and pension.
5. Merits by type. For promotion and sealed cover, check DPC procedure and the conditions for sealed cover (for example Union of India v. K.V. Jankiraman, Supreme Court, 1991; confirm current treatment and the current office memorandum). For discipline, check the competent authority, charge memo, inquiry fairness, supply of documents, the inquiry report, representation, reasoned order and proportionality of penalty; check Article 311 for dismissal or removal.
6. Interim relief: stay of transfer, of recovery, or of a penalty, with grounds.
7. Search for and read current Supreme Court and tribunal authority. Tag anything unread `[verify]`.

## Output

1. A forum and limitation note.
2. An issues analysis with strengths and risks.
3. A draft original application (or writ, where the tribunal has no jurisdiction) with facts, grounds, relief and interim relief, or a representation if remedies are not yet exhausted.

## Guardrails and hand-offs

- Never promise reinstatement, promotion or back wages.
- Never invent office memoranda or their dates.
- Keep the employee's APARs and personal records confidential.
- For a writ before the High Court, use `writ-petition-drafter`; for conducting a departmental inquiry, `disciplinary-inquiry-drafter`.
