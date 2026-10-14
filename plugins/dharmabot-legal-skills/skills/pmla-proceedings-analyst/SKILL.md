---
name: pmla-proceedings-analyst
description: Analyses proceedings under the Prevention of Money-laundering Act, 2002, covering the link to a scheduled offence, ED summons and statements, arrest and written grounds, provisional attachment and its confirmation before the Adjudicating Authority, appeals to the Appellate Tribunal and High Court, and the twin conditions for bail. Use when the ED has issued a summons, recorded an ECIR, attached property or arrested a client, or a PMLA bail is being planned. Do not use for general summons handling across agencies; use enforcement-summons-response-planner.
---

# PMLA Proceedings Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Map a client's position and options at each stage of a PMLA matter, with the deadlines that matter.

## Jurisdiction gate

Confirm the proceedings are by the Directorate of Enforcement under the PMLA in India. Record the ED zone, the Special Court, the Adjudicating Authority bench and the jurisdictional High Court. If foreign assets or a foreign request are involved, flag mutual legal assistance and foreign-law issues for counsel qualified there.

## Temporal gate

Record the dates of the scheduled offence, the ECIR, each summons, attachment and arrest. The PMLA and the schedule have been amended several times; the version in force on each date matters. For procedure on the predicate offence before 1 July 2024, check with `crpc-bnss-transition-analyst`.

## Required inputs

**Blocking**: the summons, attachment order or arrest papers received; the scheduled offence (FIR or complaint) and its current status (pending, closed, quashed, acquitted); and the client's role (accused, witness, company officer, owner of attached property).

Also useful: the property details, source-of-funds documents, earlier statements, and any order in the predicate case.

## Method

1. Retrieve the current official text of the PMLA provisions on summons, arrest, attachment and confirmation, appeals and bail (believed ss.50, 19, 5, 8, 26, 42 and 45; confirm), the schedule, and the relevant rules. Record source and date.
2. Read Vijay Madanlal Choudhary v. Union of India (Supreme Court, 2022) and check the status of review or reference proceedings on it. Search for later Supreme Court rulings on written grounds of arrest, arrest after cognizance and bail. Read before citing; tag anything unread `[verify]`.
3. Predicate offence: confirm its status. If closed, quashed or ended in acquittal, assess the effect on the PMLA case under current authority.
4. Summons: who is summoned and as what; documents sought; whether the client may be arrested; prepare with `enforcement-summons-response-planner`.
5. Attachment: check the reasons recorded, the period of provisional attachment and the deadline for filing before the Adjudicating Authority; plan the reply on source of funds and the "proceeds of crime" link; compute dates with `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
6. Appeals: the Appellate Tribunal against confirmation, and then the High Court, with limitation and any stay.
7. Arrest and bail: written grounds, production, remand; apply the twin conditions and any exceptions (the proviso to s.45(1) is believed to cover a person under sixteen, a woman, the sick or infirm, and an accused of money-laundering below a threshold believed to be Rs 1 crore; the Supreme Court is understood to treat the benefit as discretionary, not automatic [verify]; confirm against the official text); consider long custody and trial delay as current authority treats them. Draft bail via `bnss-bail-application-drafter`.

## Output

1. A stage map: where the matter stands, options, deadlines and owners.
2. An attachment reply plan or an arrest and bail note, as the stage needs.
3. Risks and documents to collect.

## Guardrails and hand-offs

- Never advise moving, layering or concealing assets after notice.
- Never advise false statements to the ED; statements may be used against the maker.
- Never promise bail or release of property.
- For AML programme questions, use `aml-sanctions-compliance-checker`.
