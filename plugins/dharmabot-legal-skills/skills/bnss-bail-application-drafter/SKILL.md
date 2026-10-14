---
name: bnss-bail-application-drafter
description: Drafts regular bail and anticipatory bail applications under the Bharatiya Nagarik Suraksha Sanhita, 2023 for a Magistrate, Sessions Court or High Court in India, with a chronology, grounds, proposed conditions and annexure list. Use when an advocate needs a bail or anticipatory bail draft, or wants grounds tested against the FIR and case diary extracts. Do not use where the CrPC still governs the proceeding; run crpc-bnss-transition-analyst first if any date is before 1 July 2024.
---

# BNSS Bail Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce a court-ready draft bail or anticipatory bail application, built only on the record supplied, with grounds the advocate can argue. For an applicant in custody, first check whether default bail may already have accrued.

## Jurisdiction gate

Confirm the matter is before an Indian court and note the State, district and court (Magistrate, Sessions, High Court). Ask whether the offence falls under a special statute with its own bail conditions (for example NDPS, UAPA, PMLA, POCSO). If it does, say so at the top of the draft and retrieve those conditions before drafting.

## Temporal gate

Record the date of the offence, FIR, arrest and first remand. If any falls before 1 July 2024, or the user is unsure which code governs, run `crpc-bnss-transition-analyst` first.

## Required inputs

Mark as **blocking**: copy or particulars of the FIR or complaint; the offences and sections alleged; custody status (arrested, apprehending arrest, in judicial or police custody) with dates; the court the application is for; and any earlier bail application and its result.

For an applicant in custody, also **blocking** (the default-bail gate cannot run without them):
- the date of the first remand order (and the arrest date, if different);
- whether the charge sheet (police report) has been filed, and if so on what date (ask for both, the status and the date);
- the maximum punishment for each offence alleged (and any minimum), taken from the official text, or from the user and then checked against it. If the user has not given it, ask for it by name and say which figure you have assumed and why, tagged [verify]; never assert it silently.

Also useful: the applicant's age, occupation, residence and family; criminal antecedents; health; status of the investigation and recovery; and conditions the applicant can offer (surety, reporting, passport, not contacting witnesses).

## Method

1. Retrieve the current official text of the BNSS provisions on bail, anticipatory bail and the period of investigation in custody, any State amendment, any special statute in play, and the First Schedule entry for each offence. The bail chapter is believed to start at section 478 (anticipatory bail believed to be section 482), and the custody limit is believed to be in section 187(3), but confirm every number and its wording from the source.
2. **Default-bail gate.** Run this for every applicant in custody, before any ground is drafted. (For anticipatory bail where the applicant is not in custody, say the gate does not apply and why.)
   a. **When custody began.** Take the start date from the first remand order, not the arrest date if they differ. Ask the user in the response to confirm which date the court will count from [verify], and show the result for each candidate date until they reply.
   b. **The statutory limit.** For each offence alleged, record its maximum punishment (and any minimum) from the official text. Take the limit from BNSS s.187(3), believed to be 90 days where the investigation relates to an offence punishable with death, imprisonment for life or imprisonment for a term of ten years or more, and 60 days for any other offence; confirm against the official text and check whether any special statute extends the period (for example NDPS, UAPA) [verify]. Courts have differed on whether "ten years or more" turns on the maximum or the minimum punishment: the Karnataka High Court in State of Karnataka v. Kalandar Shafi (2024) is understood to have read it as a minimum, following Rakesh Kumar Paul v. State of Assam (2017) on the CrPC wording [verify]. Where an offence's maximum is ten years or more but its minimum is below ten years, show both the 60-day and the 90-day dates, mark the point [verify], and leave the choice to the advocate.
   c. **Count the days.** Compute with the bundled script, never by mental arithmetic:

      ```
      python3 scripts/date_calc.py --start <first remand date> --to <today> --period 60d
      ```

      On Windows, use `py -3` in place of `python3`.

      Use `--period 90d` where the 90-day limit is in play. Run it both with and without `--include-start` and show both results, since whether the remand day itself counts is a point to confirm [verify]. Do not pass `--holidays` or `--weekends-closed` (they apply the Limitation Act holiday rule); if the advocate thinks a holiday rule applies, flag it [verify]. Paste the script's working into the output.
   d. **Check the user's count.** Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. For example, "40 days in custody" against remand dates that give about 73 days must be flagged, not relied on. Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead. Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
   e. **Limit passed, no charge sheet.** If the limit has passed and the charge sheet (police report) has not been filed, put a prominent **DEFAULT BAIL MAY HAVE ACCRUED** flag at the very top of the output, above any draft. Explain that the right is generally treated as lost once the charge sheet is filed before the application is made [verify], so the application should be made immediately. Hand off to `undertrial-release-screener`, and to `arrest-rights-advisor` where the arrest or remand itself is in question.
   f. **Limit close.** If the limit has not yet passed, state the date on which it will run out (each candidate date, where the period or the counting rule is open).
3. Classify each offence from the statute: bailable or non-bailable, maximum punishment, triable by which court. Check whether the application is premature or barred (for example a pending application elsewhere).
4. Choose the provision and forum, and set out in one line why this court has jurisdiction.
5. Build a dated chronology from the record only.
6. Draft grounds in order of strength. Typical heads, used only where the record supports them: nature of the accusation and the gaps in it; role attributed to the applicant; period already in custody and its relation to the maximum sentence; investigation status and recovery; antecedents; roots in the community and flight risk; health, age, sex or family circumstances; parity with co-accused already on bail; and conditions offered.
7. Search for and cite current Supreme Court and jurisdictional High Court authority on bail principles only after reading it. Tag anything not read in full `[verify]`.
8. Draft the prayer and proposed conditions. Add an annexure list and an affidavit or verification as the forum's rules require.

## Output

1. If the default-bail gate found the limit passed with no charge sheet, the **DEFAULT BAIL MAY HAVE ACCRUED** flag first, with the start date, the limit applied, the days counted and the script's working, followed by the question asking the user to confirm the start date.
2. If a special statute is in play (for example NDPS, UAPA, PMLA, POCSO), a one-line notice of its bail conditions straight after the default-bail flag and before any draft, naming the provision believed to apply and tagging it [verify].
3. The default-bail gate result in every custody case: dates, limit (both limits where disputed), days in custody, the date the limit runs out, and any discrepancy with the user's stated count.
4. The draft application: cause title, facts, chronology, grounds, authorities, prayer, verification.
5. Annexure list.
6. A short note for the advocate: the strongest and weakest points, documents still missing, and any special-statute bar.

## Guardrails and hand-offs

- Never draft a regular-bail application without first running the default-bail gate.
- If a blocking input is missing, ask for each one by name before drafting or giving a substantive answer; do not produce a draft with blanks first.
- When the limit has passed and no charge sheet is filed, name `undertrial-release-screener` in the response (and `arrest-rights-advisor` where the arrest or remand itself is in question), and name `pre-filing-verification-checker` before anything is filed.
- Mark every section number and period (including the 60-day and 90-day limits) as believed and to be confirmed against the official text, in tables and headings as well as notes, and tag [verify].
- Never state or imply that bail will be granted.
- Never add facts, antecedents or medical grounds that are not in the record.
- Never invent a case name, citation, paragraph number or section number.
- Use the court's format if the advocate supplies one; otherwise hand off formatting to `court-pleading-formatter`.
- For a version in an Indian language, hand off to `regional-language-legal-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
