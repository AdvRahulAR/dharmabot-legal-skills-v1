---
name: matrimonial-petition-drafter
description: Drafts contested matrimonial petitions and written statements before Family Courts or District Courts in India for divorce, restitution of conjugal rights, judicial separation and nullity under the applicable personal law or State code, with forum and venue under the Family Courts Act, 1984, pleaded particulars of cruelty or desertion, and interim maintenance and custody prayers. Use when a lawyer asks for a divorce petition on cruelty, a reply to a husband's petition, or a restitution petition. Do not use for a joint petition; use mutual-consent-divorce-drafter.
---

# Matrimonial Petition Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce a petition or written statement with specific, dated particulars, filed in the right court, and with the interim prayers the client needs.

## Jurisdiction gate

Confirm the governing Act (run `divorce-grounds-analyst` if unclear). Check whether a State uniform civil code applies (Uttarakhand in force; Gujarat and Assam codes passed in 2026, check commencement). Identify the venue: the Act usually allows filing where the marriage was solemnised, where the respondent resides, where the parties last resided together, or where the wife resides, but confirm the exact wording of the governing Act. Confirm whether a Family Court has been set up for that area.

## Required inputs

Mark as **blocking**:
- governing Act, the relief sought and the ground or grounds;
- marriage particulars (date, place, rites, registration);
- residence of each party and where they last lived together;
- the facts, dated, for each ground;
- children's names and ages (to be kept out of public annexures where possible), and all pending cases between the parties.

For a written statement, also the petition and its annexures.

## Method

1. Retrieve the current official text of the governing Act, the Family Courts Act, 1984, the State Family Court rules and the High Court's rules for matrimonial petitions. Record the version and date.
2. Fix the cause title, court and jurisdiction paragraph, citing the venue provision of the Act (confirm the number).
3. Plead facts chronologically with dates, places and specific incidents. Cruelty needs instances, not adjectives. Desertion needs the date of separation, the intention to desert and the absence of reasonable cause.
4. Add the statutory averments the Act requires (no collusion, no condonation, no unnecessary delay, no other proceeding, as applicable).
5. Add interim prayers: maintenance pendente lite and litigation costs (hand off quantum to `maintenance-petition-drafter`), interim custody and visitation (see `child-custody-planner`), and residence or protection where facts support it.
6. For a written statement: admit, deny or explain each paragraph; plead specific defences; add any counter-claim the Act allows.
7. Prepare the verification, affidavit, list of documents and any application for in-camera hearing. Hand off interlocutory applications to `civil-interlocutory-application-drafter`.

## Output

1. The draft petition or written statement.
2. List of documents and witnesses.
3. A note for the advocate: weak points, missing evidence, and mediation or counselling stages to expect.

## Guardrails

- Never add allegations not in the client's instructions.
- Never use children's school or address details beyond what the court needs.
- Never invent case law; tag unread authority `[verify]`.
- Formatting to `court-pleading-formatter`; a regional-language version to `regional-language-legal-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
