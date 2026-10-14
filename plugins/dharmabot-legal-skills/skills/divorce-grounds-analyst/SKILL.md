---
name: divorce-grounds-analyst
description: Identifies the law governing a marriage in India (Hindu Marriage Act, 1955, Special Marriage Act, 1954, Divorce Act, 1869, Dissolution of Muslim Marriages Act, 1939, Parsi Marriage and Divorce Act, 1936, a State uniform civil code or custom) and assesses grounds and bars for divorce, judicial separation or nullity, with the evidence needed. Use when a lawyer asks whether a client can get a divorce for cruelty or desertion, which Act applies, or how strong a nullity case is. Do not use to draft the petition; use matrimonial-petition-drafter.
---

# Divorce Grounds Analyst

Every output is a draft assessment for an advocate enrolled in India to check.

## Purpose

Tell the advocate which law governs, which grounds the facts support, what bars or defences apply, and what evidence must be gathered.

## Jurisdiction gate

Ask, never assume: each spouse's religion at marriage and now, the form and place of marriage, whether it was registered and under which Act, and the parties' domicile and residence. Check whether a State uniform civil code applies: Uttarakhand's code is in force; Gujarat and Assam passed codes in 2026 (check assent, commencement and coverage); Goa has its own civil law. If either spouse lives abroad or a foreign decree exists, hand off to `nri-matrimonial-dispute-analyst`.

## Temporal gate

Record the dates of marriage, separation and each key event. Grounds, waiting periods and talaq rules depend on the law in force at the time (for example the Muslim Women (Protection of Rights on Marriage) Act, 2019 on instant triple talaq). Check whether a State code or amendment applies to these dates.

## Required inputs

Mark as **blocking**:
- religion of each spouse and form of marriage;
- date and place of marriage, and registration details;
- date of separation and current living arrangements;
- the facts relied on, in dated sequence;
- children, and any pending cases between the parties (maintenance, DV, criminal, custody).

Also useful: messages, medical records, police complaints, witness names, and the other side's likely stand.

## Method

1. Retrieve the current official text of the governing Act and any State code or amendment, and the Family Courts Act, 1984. Record the version and date.
2. Map each fact to a ground under that Act: cruelty, desertion for the statutory period, adultery, conversion, mental disorder, venereal disease, renunciation, presumed death, non-resumption after a decree, and the wife's special grounds where the Act gives them. For Muslim marriages, consider the 1939 Act grounds for the wife, and talaq, khula and mubarat as recognised now.
3. Check bars: the minimum period after marriage before a petition (where the Act imposes one), condonation, connivance, collusion, delay, and taking advantage of one's own wrong.
4. Nullity: void versus voidable grounds and time limits.
5. Irretrievable breakdown is not a statutory ground for most Acts. The Supreme Court may dissolve a marriage under Article 142 (Shilpa Sailesh v. Varun Sreenivasan, Constitution Bench, 2023; confirm current treatment). Note this is not a remedy the Family Court can grant.
6. Consider mutual consent as an alternative; hand off to `mutual-consent-divorce-drafter`.
7. List evidence for each ground and the likely defences.
8. Search for and read current Supreme Court and jurisdictional High Court authority; tag anything not read in full `[verify]`.

## Output

1. Governing law note with reasons.
2. Ground-by-ground table: ground · facts · evidence held · evidence needed · strength.
3. Bars and risks, alternatives, and next steps (petition, maintenance via `maintenance-petition-drafter`, custody).

## Guardrails

- Never predict that a decree will be granted.
- Never assume religion or marriage form; ask.
- Never suggest fabricating allegations or evidence, or filing false criminal complaints as leverage.
- Keep the client's and children's details confidential.
