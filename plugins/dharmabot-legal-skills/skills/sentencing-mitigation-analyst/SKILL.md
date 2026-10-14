---
name: sentencing-mitigation-analyst
description: Analyses the lawful sentence range under the Bharatiya Nyaya Sanhita or a special law, aggravating and mitigating factors, probation under the Probation of Offenders Act, 1958, community service, set-off of detention, plea bargaining under the BNSS and victim compensation, and drafts a mitigation note for the hearing on sentence. Use when a client has been convicted, a hearing on sentence is listed, or plea bargaining is being considered. Do not use to draft the appeal against conviction; use criminal-appeal-revision-drafter.
---

# Sentencing Mitigation Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Give the court a lawful, documented basis for the lowest appropriate sentence, without predicting the result.

## Jurisdiction gate

Confirm the conviction or plea is before an Indian court. Record the court, State and offence. Check whether the State has a probation rule set or a victim compensation scheme that changes the options. Note special statutes with minimum sentences or bars on probation.

## Temporal gate

Record the date of the offence. Punishment is fixed by the law in force on that date (Article 20(1) of the Constitution). If the offence is before 1 July 2024, the IPC range may apply; use `ipc-bns-concordance-mapper` and `crpc-bnss-transition-analyst`.

## Required inputs

**Blocking**: the judgment of conviction or the offence for which a plea is proposed; the date of offence; the convict's age at the time of offence; and time already spent in custody.

Also useful: antecedents, family, health, employment, conduct in custody or on bail, victim's loss, any compensation paid or settlement, and character material.

## Method

1. Retrieve the current official text of the punishment provision, any minimum sentence, the BNS provision on community service, the Probation of Offenders Act, 1958 and State rules, the BNSS provisions on hearing on sentence, set-off, plea bargaining and compensation. Record source and date.
2. State the lawful range: minimum, maximum, fine, and whether community service or probation is available for this offence.
3. Check bars: minimum sentences, special-statute exclusions, and offences not eligible for plea bargaining (confirm the current exclusions).
4. List aggravating factors the prosecution will raise from the record.
5. List mitigating factors, each tied to a document: age, first offence, conduct, family dependence, health, remorse, restitution, delay in trial, time in custody.
6. In capital-eligible cases, flag the need for mitigation investigation and expert reports, following Supreme Court guidance (for example Bachan Singh v. State of Punjab, 1980; confirm current treatment and later directions).
7. Compute set-off of detention against any term from the custody dates given.
8. Propose compensation to the victim where it may weigh in mitigation, but never as a price for a lower sentence.
9. Search for current Supreme Court sentencing guidance for this offence. Read it; tag anything unread `[verify]`.

## Output

1. A sentencing range table with sources.
2. The mitigation note: background, mitigating factors with annexures, response to aggravating factors, and the specific order sought.
3. A document checklist for mitigation evidence.

## Guardrails and hand-offs

- Never predict a precise sentence.
- Never assert facts about the convict that are not documented.
- Never suggest probation or plea bargaining where the law bars it.
- For an appeal or suspension of sentence, use `criminal-appeal-revision-drafter`.
