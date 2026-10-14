---
name: probate-succession-certificate-drafter
description: Drafts petitions in India for probate and letters of administration under Part IX and succession certificates under Part X of the Indian Succession Act, 1925, with jurisdiction, valuation and court fee, citations to heirs, attesting witness affidavits and caveat handling, and checks whether probate is still compulsory after the 2025 amendments. Use when a lawyer asks for a probate petition for a registered will, letters of administration, or a succession certificate for bank deposits or shares. Do not use to draft the will itself; use will-drafter.
---

# Probate and Succession Certificate Drafter

Every output is a draft for an advocate enrolled in India to check and file.

## Purpose

Prepare a petition that the court will register and notice, in the right court, with the right valuation and the evidence the will or the claim needs.

## Jurisdiction gate

Confirm the deceased's religion, last residence and where the assets are. Identify the court: the District Judge, or a High Court exercising original testamentary jurisdiction (for example Bombay, Calcutta, Madras and Delhi, subject to pecuniary limits; confirm). Check whether a State uniform civil code changes the procedure for this deceased (Uttarakhand in force; Gujarat's code reportedly received the President's assent in September 2026 and comes into force on a date the State notifies; Assam's bill was reportedly passed by the Assembly in May 2026, with assent not confirmed; check assent, commencement and coverage, including any Scheduled Tribe exclusion [verify]).

## Temporal gate

Probate was compulsory for certain wills under section 213 read with section 57 of the 1925 Act (believed to be the sections; confirm against the official text). The Repealing and Amending Act, 2025 (assent reported as 20 December 2025) is reported to have omitted section 213. Confirm the commencement date and current authority on pending proceedings, and check whether banks, registrars or societies still ask for probate in practice.

## Required inputs

Mark as **blocking**:
- the original will and any codicil (for probate), or confirmation there is none;
- death certificate and the deceased's last address;
- the full list of heirs and next of kin with addresses;
- the assets, their location and value as on the date of death;
- the petitioner's capacity (executor, beneficiary, heir).

Also useful: attesting witnesses' availability, any caveat or known objection, and the bank's or company's requirements.

## Method

1. Retrieve the current official text of Parts IX and X of the Indian Succession Act, 1925, the State court fees law and the High Court's original side or district court rules and forms. Record the version and date.
2. Choose the remedy: probate (executor named), letters of administration with will annexed (no executor or executor declines), letters of administration (intestacy), or a succession certificate for debts and securities (believed to be section 372; confirm).
3. Do not assume the will is valid. Check execution and attestation, suspicious circumstances and capacity, and list what proof will be needed.
4. Draft the petition with the statutory particulars, a schedule of assets and liabilities with valuation, and the verification.
5. Prepare the affidavit of an attesting witness, and plan proof if no witness is available.
6. List heirs to be cited, with addresses for service; plan publication if the court requires it.
7. Court fee: hand off to `state-court-fee-calculator`; limitation where relevant to `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
8. Caveat: if a caveat is filed, the matter becomes contentious and is tried as a suit; prepare for that.

## Output

1. Draft petition with schedules.
2. Witness affidavit and list of persons to be cited.
3. Filing checklist and note on whether probate is still needed for this purpose.

## Guardrails

- Never assume a will is genuine or validly executed.
- Never undervalue assets to reduce court fee.
- Formatting to `court-pleading-formatter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
