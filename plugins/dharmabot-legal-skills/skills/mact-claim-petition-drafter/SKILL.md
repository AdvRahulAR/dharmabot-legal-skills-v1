---
name: mact-claim-petition-drafter
description: Drafts claim petitions before the Motor Accident Claims Tribunal under the Motor Vehicles Act 1988 as amended in 2019, and computes compensation with workings using the multiplier method, future prospects and conventional heads for death and injury, disability and loss of earning capacity. Covers the Detailed Accident Report process, insurer defences and the limitation period. Use when a lawyer asks for a MACT petition, a compensation calculation or a reply to an insurer's defence. Do not use for an employee's compensation claim against an employer; use labour-dispute-claim-drafter.
---

# MACT Claim Petition Drafter

Every output is a draft for an advocate enrolled in India to check and file.

## Purpose

Produce a claim petition and a transparent compensation computation that a Tribunal can follow line by line.

## Jurisdiction gate

Confirm the accident involved a motor vehicle in a public place in India. Identify the State and the Tribunal with jurisdiction: where the accident occurred, where the claimant resides or carries on business, or where the defendant resides (confirm from the current Act). State MV rules govern forms, the Detailed Accident Report procedure and court fees.

## Temporal gate

The 2019 amendments changed claims procedure, the hit-and-run scheme and limitation, and the rules were amended in 2022 for the accident report process. Record the accident date. If it falls before the relevant amendments commenced, check which version applies.

## Required inputs

Mark as **blocking**:
- date, time and place of the accident, and the vehicles involved with registration numbers;
- FIR or DAR details;
- for death: the deceased's age, occupation, proof of income and the dependants with ages;
- for injury: medical records, disability certificate and treatment bills.

Also useful: insurance policy, driving licence, permit, eyewitness details, salary slips or tax returns.

## Method

1. Retrieve the current official text of the Motor Vehicles Act, the State MV rules, the central rules on the Detailed Accident Report, and any Supreme Court directions on the claims process. Record versions and dates.
2. Check limitation. The 2019 amendment is believed to set six months from the accident; confirm the text and current authority on its application. Compute with `limitation-calculator`.
3. Build the facts from the record. Identify the owner, driver and insurer as respondents.
4. Compute compensation in a table:
   - income from proof only;
   - future prospects by age and employment type, following National Insurance Co v Pranay Sethi (Supreme Court, 2017; confirm current treatment);
   - deduction for personal expenses by number of dependants, and the multiplier by age, following Sarla Verma v DTC (Supreme Court, 2009; confirm current treatment);
   - conventional heads (loss of estate, consortium, funeral) at current figures from the latest authority;
   - for injury, functional disability, loss of earning capacity, medical expenses, attendant charges, pain and suffering.
   Show each step. Mark any figure taken from authority `[verify]` until read.
5. Anticipate insurer defences: licence or permit breach, contributory negligence, gratuitous passenger, collusion, income not proved. Note pay-and-recover.
6. Draft the petition in the State form with interest and interim relief prayers.

## Output

1. The draft claim petition with annexure list.
2. The compensation table with workings and sources.
3. A note on evidence gaps and defences.

## Guardrails and hand-offs

- Never inflate income or add heads without proof.
- Never promise an award amount.
- For a client who may qualify for free legal aid, hand off to `legal-aid-eligibility-screener`.
- For a petition in the Tribunal's language, hand off to `regional-language-legal-drafter`.
- Before delivery, send citations to `citation-verifier`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
