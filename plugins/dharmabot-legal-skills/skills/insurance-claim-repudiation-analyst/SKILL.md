---
name: insurance-claim-repudiation-analyst
description: Analyses repudiation of Indian insurance claims (health, life, motor, property, marine, liability) under the Insurance Act 1938 and IRDAI policyholder rules, reviews corporate covers such as D&O, cyber and CGL for gaps, and drafts complaints to the insurer's grievance cell, Bima Bharosa, the Insurance Ombudsman under the Insurance Ombudsman Rules 2017, or a consumer commission. Use when a claim is rejected for non-disclosure, late intimation, an exclusion or a surveyor's report. Do not use for consumer pleadings in full; use consumer-complaint-drafter.
---

# Insurance Claim Repudiation Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Decide whether a repudiation can be challenged, on what grounds and in which forum, and draft the first complaint.

## Jurisdiction gate

Confirm the policy was issued by an insurer registered in India and identify the insured's State and district. The Ombudsman's territorial office depends on the insurer's branch or the complainant's residence; confirm from the current Rules and the Council for Insurance Ombudsmen's list. Marine cargo or reinsurance with foreign elements may need `cross-border-contract-reviewer`.

## Temporal gate

The Insurance Act was amended in 2015 and again by a 2025 amendment Act; check what has commenced. IRDAI replaced many regulations with consolidated 2024 regulations and master circulars, including on health moratorium and claim timelines. Record the policy start date, renewal history, date of loss and date of repudiation; the version in force on each date matters.

## Required inputs

Mark as **blocking**:
- the policy schedule and wording, including exclusions and endorsements;
- the proposal form, if non-disclosure is alleged;
- the claim documents and the repudiation letter;
- key dates: policy inception, renewals, loss or admission, intimation, repudiation.

Also useful: surveyor or investigator report, medical records, earlier grievance correspondence, and portability or migration records.

## Method

1. Retrieve the current official text of the Insurance Act, the Insurance Ombudsman Rules 2017 as amended, the IRDAI regulations and master circulars on policyholder protection and health insurance, and the policy wording filed with IRDAI. Record versions and dates.
2. State the ground for repudiation in one line. Map it to the clause relied on.
3. Test the ground:
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - **Non-disclosure.** Was the question asked in the proposal form? Was the fact material and known to the insured? Has the moratorium or look-back period for the policy type run? Retrieve the current period; do not state it from memory. For life policies, check the statutory bar on questioning a policy after a set period (believed to be section 45; confirm).
   - **Exclusion.** Is it clear, disclosed and applied correctly? Ambiguity is read against the insurer; search for current authority.
   - **Late intimation.** Was the delay explained, and did it prejudice the insurer?
   - **Surveyor report.** Was it shared, reasoned and within licence?
4. For corporate covers, compare the loss against insuring clauses, definitions, exclusions, retroactive dates and notice conditions.
5. Choose the forum: the insurer's grievance cell first, then Bima Bharosa, the Ombudsman (check monetary limit and time limit live), or a consumer commission. Compute deadlines with `limitation-calculator`.
6. Search for and read current Supreme Court and NCDRC authority on the ground in issue. Tag anything not read in full `[verify]`.
7. Draft the complaint in the forum's format.

## Output

1. A repudiation analysis: ground · clause · facts · counter-argument · evidence · strength.
2. A forum recommendation with deadlines and monetary limits to confirm.
3. The draft grievance or Ombudsman complaint, with an annexure list.

## Guardrails and hand-offs

- Never advise concealing facts, altering records or misrepresenting a claim.
- Never guarantee settlement or an amount.
- For a full consumer complaint, hand off to `consumer-complaint-drafter`.
- For regulatory complaints against the insurer, hand off to `regulator-notice-reply-drafter`.
- Before delivery, send citations to `citation-verifier`.
