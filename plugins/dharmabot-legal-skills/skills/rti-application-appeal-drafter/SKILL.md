---
name: rti-application-appeal-drafter
description: Drafts applications under the Right to Information Act, 2005 to the right public authority and PIO, and first appeals, second appeals and complaints to the Central or a State Information Commission, testing exemptions (including the personal information exemption as amended by the DPDP Act, 2023), third-party procedure and deemed refusal, and tracking timelines. Use when someone wants records from a government department, municipality or public body, or the PIO refused or did not reply. Do not use for challenging an Information Commission order in court; use writ-petition-drafter.
---

# RTI Application and Appeal Drafter

Every output is a draft for the applicant or an advocate to check before filing.

## Purpose

Ask for records in a way the PIO cannot easily refuse, and pursue appeals on time when they do.

## Jurisdiction gate

Confirm the body is a public authority under the RTI Act (Union, State or UT body, or a substantially financed body). Identify whether the Central or a State Information Commission has jurisdiction, and the State's RTI rules (fee, mode of payment, word limit, BPL exemption, online portal). Jammu and Kashmir and Ladakh now follow the central framework; confirm.

## Temporal gate

The DPDP Act, 2023 amended the personal information exemption in the RTI Act. Check whether that amendment is in force, and from when, before relying on it. Record the dates of application, receipt, any reply and any appeal.

## Required inputs

**Blocking**: the public authority and the records wanted; the applicant's citizenship (the Act gives the right to citizens); and, for an appeal, the application, any reply and the dates.

Also useful: file numbers, dates, project names, and why the records matter (not required to be stated, but helps a public-interest argument).

## Method

1. Retrieve the current official text of the RTI Act, the applicable Central or State RTI rules, the authority's PIO and First Appellate Authority details, and the commission's rules. Record source and date.
2. Frame the request as records: name files, registers, approvals, inspection reports, with dates. Avoid questions asking "why" or seeking opinions.
3. Keep within any word or subject limits in the State rules; split requests if needed.
4. Address the PIO correctly; include the fee and mode of payment; ask for inspection where volume is large.
5. Time limits: compute the reply period (believed 30 days, shorter for life and liberty matters, longer when third parties are involved; confirm). Note deemed refusal. Use `limitation-calculator` for appeal deadlines.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
6. First appeal: list each point, the PIO's reply, and why it is wrong (exemption misapplied, no reasons, partial disclosure, delay, transfer not made).
7. Exemptions: test each claimed exemption against its text and current authority; argue severability and public interest override where the Act allows.
8. Second appeal or complaint: choose the remedy, and seek penalty and compensation where the Act permits.
9. Read authority before citing; tag anything unread `[verify]`.

## Output

1. The RTI application, ready to sign.
2. A timeline sheet with reply and appeal deadlines.
3. First or second appeal, or complaint, as needed.

## Guardrails and hand-offs

- Never seek records for harassment or a private person's personal data without a public-interest basis.
- Never state that a record exists if not known.
- For a version in an Indian language, use `regional-language-legal-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
