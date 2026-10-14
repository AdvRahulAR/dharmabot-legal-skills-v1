---
name: bnss-bail-application-drafter
description: Drafts regular bail and anticipatory bail applications under the Bharatiya Nagarik Suraksha Sanhita, 2023 for a Magistrate, Sessions Court or High Court in India, with a chronology, grounds, proposed conditions and annexure list. Use when an advocate needs a bail or anticipatory bail draft, or wants grounds tested against the FIR and case diary extracts. Do not use where the CrPC still governs the proceeding; run crpc-bnss-transition-analyst first if any date is before 1 July 2024.
---

# BNSS Bail Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce a court-ready draft bail or anticipatory bail application, built only on the record supplied, with grounds the advocate can argue.

## Jurisdiction gate

Confirm the matter is before an Indian court and note the State, district and court (Magistrate, Sessions, High Court). Ask whether the offence falls under a special statute with its own bail conditions (for example NDPS, UAPA, PMLA, POCSO). If it does, say so at the top of the draft and retrieve those conditions before drafting.

## Temporal gate

Record the date of the offence, FIR and arrest. If any falls before 1 July 2024, or the user is unsure which code governs, run `crpc-bnss-transition-analyst` first.

## Required inputs

Mark as **blocking**: copy or particulars of the FIR or complaint; the offences and sections alleged; custody status (arrested, apprehending arrest, in judicial or police custody) with dates; the court the application is for; and any earlier bail application and its result.

Also useful: the applicant's age, occupation, residence and family; criminal antecedents; health; status of the investigation and recovery; and conditions the applicant can offer (surety, reporting, passport, not contacting witnesses).

## Method

1. Retrieve the current official text of the BNSS provisions on bail and anticipatory bail, any State amendment, and the First Schedule entry for each offence. The bail chapter is believed to start at section 478 (anticipatory bail believed to be section 482), but confirm every number and its wording from the source.
2. Classify each offence from the statute: bailable or non-bailable, maximum punishment, triable by which court. Check whether the application is premature or barred (for example a pending application elsewhere).
3. Choose the provision and forum, and set out in one line why this court has jurisdiction.
4. Build a dated chronology from the record only.
5. Draft grounds in order of strength. Typical heads, used only where the record supports them: nature of the accusation and the gaps in it; role attributed to the applicant; period already in custody and its relation to the maximum sentence; investigation status and recovery; antecedents; roots in the community and flight risk; health, age, sex or family circumstances; parity with co-accused already on bail; and conditions offered.
6. Search for and cite current Supreme Court and jurisdictional High Court authority on bail principles only after reading it. Tag anything not read in full `[verify]`.
7. Draft the prayer and proposed conditions. Add an annexure list and an affidavit or verification as the forum's rules require.

## Output

1. The draft application: cause title, facts, chronology, grounds, authorities, prayer, verification.
2. Annexure list.
3. A short note for the advocate: the strongest and weakest points, documents still missing, and any special-statute bar.

## Guardrails and hand-offs

- Never state or imply that bail will be granted.
- Never add facts, antecedents or medical grounds that are not in the record.
- Never invent a case name, citation, paragraph number or section number.
- Use the court's format if the advocate supplies one; otherwise hand off formatting to `court-pleading-formatter`.
- For a version in an Indian language, hand off to `regional-language-legal-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
