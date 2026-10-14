---
name: undertrial-release-screener
description: Screens undertrial prisoners for release under section 479 of the Bharatiya Nagarik Suraksha Sanhita, 2023 (half the maximum sentence, one-third for first-time offenders, exclusions for death or life offences and multiple pending cases), and for default bail and plea of guilt routes, using custody dates and case status, and prepares notes for the Undertrial Review Committee and the jail superintendent. Use when a legal-aid clinic, LADC or jail visitor has a list of undertrials and asks who qualifies for release. Do not use to draft the bail application; use bnss-bail-application-drafter.
---

# Undertrial Release Screener

Every output is a draft screening for a legal-aid lawyer or advocate enrolled in India to review.

## Purpose

Find undertrials who have overstayed what the law allows, sort them by route to release, and give the UTRC and jail authorities clear, verifiable notes.

## Jurisdiction gate

Confirm the prisoners are in an Indian prison and record the State and prison. Note the District and State Legal Services Authority. Check whether any prisoner is held under a special law with its own bail bar (for example NDPS, UAPA, PMLA) and flag the interaction with section 479 BNSS (believed to be the section; confirm against the official text).

## Temporal gate

Record the date of each FIR and arrest. The Supreme Court reportedly directed that section 479 applies to undertrials in cases registered before 1 July 2024 (In re Inhuman Conditions in 1382 Prisons, 2024; confirm current position). For cases under the CrPC, check the corresponding provision with `crpc-bnss-transition-analyst`.

## Required inputs

Mark as **blocking**, for each prisoner:
- name or prison number (synthetic in examples), offences and sections;
- date of arrest and total custody, with any period of release;
- whether a first-time offender, and whether other cases are pending;
- the stage of each case.

If custody dates are unverified, mark the prisoner "unverified" and do not decide eligibility.

## Method

1. Retrieve the current official text of section 479 BNSS (believed to be the section; confirm the number), the BNSS provisions on default bail and plea bargaining, the First Schedule entries, and NALSA's current UTRC standard operating procedure. Record the source and date.
2. For each offence, find the maximum punishment from the statute, not from memory. Exclude offences punishable with death or life imprisonment.
3. Compute custody against one-half of the maximum, and one-third for first-time offenders. Show the arithmetic.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
4. Apply the bar on multiple pending cases, and read the current authority on its scope. Tag unread authority `[verify]`.
5. Screen other routes: default bail where the charge sheet was late, plea bargaining, compounding, and bailable offences where the prisoner cannot furnish surety.
6. Sort prisoners into: eligible, likely eligible pending verification, not eligible, and other route.
7. Draft UTRC notes and the jail superintendent's application to the court, which the superintendent signs.

## Output

1. A screening table: prisoner · offences · max sentence · custody · threshold · route · status.
2. UTRC notes per eligible prisoner.
3. Draft superintendent's application.
4. A list of records to obtain.

## Guardrails and hand-offs

- Mark every section, article, rule number, period and last date as believed and to be confirmed against the official text, in tables, headlines and bold lines as well as in notes, and tag [verify] anything not checked against a primary source. A closing disclaimer alone is not enough.
- If a blocking input is missing, ask for each one by name before giving a substantive answer; do not produce an analysis or draft with blanks first. If no prisoner list or custody dates are supplied, ask for them and screen no one.
- Never compute eligibility on unverified custody dates.
- Keep prisoners' data confidential; use only what the clinic needs.
- Bail applications go to `bnss-bail-application-drafter`; file tracking to `ladcs-case-file-tracker`; eligibility for free legal aid to `legal-aid-eligibility-screener`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`.
