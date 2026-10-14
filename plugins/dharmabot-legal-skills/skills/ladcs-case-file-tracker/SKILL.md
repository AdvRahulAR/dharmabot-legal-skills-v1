---
name: ladcs-case-file-tracker
description: Maintains case files for Legal Aid Defence Counsel offices under NALSA's Legal Aid Defence Counsel System scheme, covering assignment details, custody status, remand and bail history, hearing log, jail visits, client communication, and monthly and quarterly reports to the DLSA and SLSA. Use when a Chief, Deputy or Assistant LADC wants to set up case files, update hearing logs, or prepare the monthly report. Do not use to screen eligibility for legal aid; use legal-aid-eligibility-screener.
---

# LADCS Case File Tracker

Every output is a draft record for the Legal Aid Defence Counsel to review before it is relied on or sent.

## Purpose

Keep each assigned case in one consistent file, spot custody and hearing risks early, and produce DLSA reports without retyping.

## Jurisdiction gate

Confirm the office is an LADCS office attached to a District Legal Services Authority in India. Record the State, district, and the SLSA's current reporting formats. If the user is a panel lawyer outside LADCS, adapt the tracker but say the report formats may differ.

## Required inputs

Mark as **blocking**:
- the list of assigned cases with the assignment date and the assigning authority;
- for each case, the court, case number, offences and the client's custody status;
- the DLSA or SLSA report format, or confirmation to use a neutral format.

Also useful: remand and bail orders, jail visit notes, next dates, and the names of co-accused and their counsel.

## Method

1. Retrieve the current official NALSA LADCS scheme, any SLSA circular on reporting, and NALSA's formats for legal aid case records. Record the source and date.
2. Build one file per case with fixed fields: assignment, client details (minimum needed), court and case, offences, custody, arrest date, remand history, bail applications and results, charge-sheet date, stage, next date, and last action.
3. Keep a dated hearing log: date, court, what happened, next step, who acts.
4. Log jail visits and client communications. Record consent where the client shares information meant for family.
5. Run risk flags each week: custody beyond default-bail periods, long custody relative to the maximum sentence (refer to `undertrial-release-screener`), missed hearing dates, no bail application on record, and pending copies.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
6. Prepare the monthly report in the SLSA format: cases assigned, disposed, bail obtained, pending, and remarks. Prepare quarterly summaries if required.
7. Export upcoming dates to `matter-deadline-tracker`.

## Output

1. A case register (one row per case) and individual case files.
2. The hearing log and jail-visit log.
3. The monthly report and, if due, the quarterly report.
4. A weekly risk list.

## Guardrails and hand-offs

- Keep client data confidential. Do not include personal details in reports beyond what the format requires.
- Never fill gaps with assumed dates or outcomes; mark them "to verify".
- Bail drafts go to `bnss-bail-application-drafter`; legal aid eligibility to `legal-aid-eligibility-screener`.
- Before any report is sent, hand off to `pre-filing-verification-checker`.
