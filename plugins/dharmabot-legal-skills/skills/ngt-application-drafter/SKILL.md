---
name: ngt-application-drafter
description: Drafts original applications and appeals before the National Green Tribunal under the National Green Tribunal Act 2010, for substantial questions on the environment, restitution and compensation, and appeals against environmental clearances and pollution consents, with limitation and zonal bench checks. Use when a client wants to approach the NGT about illegal mining, pollution, a clearance grant or a consent order. Do not use where only constitutional rights or non-scheduled laws are in issue; use pil-drafter or writ-petition-drafter.
---

# NGT Application Drafter

Every output is a draft for an advocate enrolled in India to check and file.

## Purpose

Draft an NGT application or appeal that fits the Tribunal's jurisdiction, is in time, is filed at the right bench and asks for relief the Tribunal can grant.

## Jurisdiction gate

Confirm the harm or order is in India and identify the State and district. Confirm the dispute arises under a law in the Act's Schedule (for example the Water, Air, Environment Protection, Forest and Biological Diversity Acts). The Wild Life (Protection) Act is believed not to be scheduled; confirm. If the case rests on a non-scheduled law, or attacks the validity of a statute or rule, flag that a writ may be the right route.

Identify the zonal bench (Principal Bench, Delhi, and the zonal benches) from the current NGT rules and notifications.

## Required inputs

Mark as **blocking**:
- what happened, where, and since when (with dates);
- the type of proceeding sought: original application, compensation claim, or appeal;
- for an appeal, the impugned order, its date and the date it was communicated or published;
- the applicant's identity and standing.

Also useful: photographs, RTI replies, board inspection reports, satellite imagery, news reports, earlier complaints and replies, and any pending case on the same subject.

## Method

1. Retrieve the current official text of the NGT Act, the NGT (Practice and Procedure) Rules, the Tribunal's filing instructions and the bench notifications. Record versions and dates.
2. Choose the provision. Original applications on a substantial question relating to the environment, relief and compensation, and appeals against specified orders are believed to sit in sections 14, 15 and 16. Confirm each from the text.
3. Check limitation. The Act is believed to set six months for original applications and 30 days for appeals, each with a limited condonation window. Compute with `limitation-calculator` from the date the cause first arose or the order was communicated. If the delay exceeds the outer limit, say so plainly.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. Check for pending or decided proceedings on the same subject (res judicata, parallel writs).
5. Draft: cause title; jurisdiction and limitation paragraphs; facts in date order from the record; questions of law; grounds (precautionary principle, polluter pays, sustainable development, statutory breaches); and relief. Typical relief includes stopping the activity, a joint inspection committee, restitution, and environmental compensation.
6. Name respondents with care: the operator, the State board, the district collector, the mining department and the Union ministry, as the facts need.
7. Search for and read current NGT and Supreme Court authority on the issue. Tag anything not read in full `[verify]`.
8. Add an annexure index, a verification and affidavit, and any application for condonation or interim relief.

## Output

1. The draft application or appeal.
2. Annexure index and a list of documents still needed.
3. A note for the advocate on jurisdiction, limitation, bench and weaknesses.

## Guardrails and hand-offs

- Never invent site facts, measurements or test results.
- Never promise an outcome or an amount of compensation.
- If clearance status is unclear, run `environmental-clearance-analyst` first.
- If the matter belongs in a High Court, hand off to `pil-drafter` or `writ-petition-drafter`.
- Before delivery, send citations to `citation-verifier`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
