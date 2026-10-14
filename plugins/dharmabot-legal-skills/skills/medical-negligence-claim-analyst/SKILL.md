---
name: medical-negligence-claim-analyst
description: Assesses medical negligence claims and defences under Indian law, testing duty, breach, causation and damages against the Bolam and Jacob Mathew standards, informed consent and records, and choosing the forum (consumer commission, civil suit, criminal complaint under the BNS with the medical-board requirement, or State Medical Council). Use when a patient's family asks if there is a case after a death or injury in hospital, or a hospital or doctor needs a defence assessment. It gives no clinical opinion. Do not use to draft the complaint itself; use consumer-complaint-drafter.
---

# Medical Negligence Claim Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Give an honest, evidence-led assessment of a medical negligence claim or defence, and the forum and steps that fit it.

## Jurisdiction gate

Confirm the treatment took place in India and identify the State and district. Note the provider type (private hospital, government hospital, individual practitioner, free or paid service), because consumer-law coverage and State Medical Council jurisdiction depend on it.

## Temporal gate

If the treatment or death occurred before 1 July 2024, the offence is under the IPC; on or after, under the BNS. Procedure depends on when the FIR or complaint was registered or the proceeding began (CrPC for proceedings pending on 1 July 2024, generally BNSS after); confirm current authority on the savings clause. Run `crpc-bnss-transition-analyst` if dates straddle. Check whether the consumer-law position on medical services has changed after any pending reference in the Supreme Court.

## Required inputs

Mark as **blocking**:
- whose side the client is on (patient or family, doctor, hospital);
- a chronology of treatment with dates;
- the medical records, or confirmation that they have been requested;
- the outcome (death, injury, disability) and the post-mortem report if any.

Also useful: consent forms, bills, discharge summary, prescriptions, nursing notes, imaging, the hospital's reply, and any second opinion.

## Method

1. Retrieve the current official text of the Consumer Protection Act 2019, the BNS provision on death by negligence including the medical-practitioner proviso (believed to be section 106(1); confirm), the NMC professional conduct regulations in force, and the State Clinical Establishments law. Record versions and dates.
2. Build a timeline from the records only. Mark gaps, overwriting and late entries.
3. Test each element:
   - **Duty**: the relationship and scope of care.
   - **Breach**: the standard of a reasonably competent practitioner in that field, following Jacob Mathew v State of Punjab (Supreme Court, 2005; confirm current treatment). Note where a respectable body of opinion would support the choice made.
   - **Causation**: whether the breach caused the harm, as opposed to the underlying illness.
   - **Damages**: losses and evidence of them.
   - **Consent**: whether it was informed, specific and documented.
4. List the questions an independent expert must answer. Do not answer them.
5. Compare forums: consumer commission (pecuniary jurisdiction, speed, expert evidence), civil suit, criminal complaint (gross negligence threshold and the requirement of a credible medical opinion before prosecution), and the State Medical Council (discipline, not compensation). Compute deadlines with `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
6. Search for and read current Supreme Court and NCDRC authority. Tag anything not read in full `[verify]`.

## Output

1. An element-by-element assessment with evidence and gaps.
2. A list of questions for a medical expert.
3. A forum comparison and recommended first steps (records request, notice, complaint).

## Guardrails and hand-offs

- Never give a clinical opinion or diagnosis.
- Never overstate prospects; grief does not prove breach.
- For a consumer complaint, hand off to `consumer-complaint-drafter`.
- For a criminal complaint, hand off to `criminal-complaint-drafter`.
- Before delivery, send citations to `citation-verifier`.
