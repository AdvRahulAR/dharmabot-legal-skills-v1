---
name: one-time-settlement-proposal-drafter
description: Drafts borrower-side letters to Indian banks and NBFCs, covering one-time settlement proposals under the lender's OTS policy and the RBI compromise settlement framework, MSME restructuring requests, and replies to show-cause notices for wilful defaulter or fraud classification under the RBI Master Directions. Use when a borrower or guarantor wants to propose an OTS, ask for restructuring, or answer a wilful defaulter or fraud notice. Do not use for court filings against the lender; use drt-application-drafter.
---

# One Time Settlement Proposal Drafter

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Draft a credible, accurate approach to the lender that improves the borrower's chance of settlement or protects its right to be heard before classification.

## Jurisdiction gate

Confirm the lender is regulated by the RBI (bank, NBFC, co-operative bank) and note which category. Confirm the account is in India. Identify any pending proceedings (SARFAESI, DRT, IBC, criminal complaint) because they affect the content and tone.

## Temporal gate

Confirm the date of the notice and the version of the RBI directions in force on that date. The wilful defaulter and fraud risk directions were revised in recent years; check the current master directions and from when they apply.

## Required inputs

Mark as **blocking**:
- the loan particulars: lender, facilities, outstanding as per lender, NPA date;
- the borrower's honest current financial position, sources of the settlement amount, and timing;
- for a show-cause reply, the notice, its annexures and the reply deadline.

Also useful: the lender's published OTS scheme, security valuation, MSME registration, the cause of stress, and earlier proposals.

## Method

1. Retrieve the current official text of the RBI compromise settlement framework, the wilful defaulter master directions, the fraud risk management directions, the MSME restructuring framework if applicable, and the lender's board-approved OTS policy. Record versions and dates.
2. For an OTS, compute the proposal against what the lender realistically recovers: security value, time and cost of enforcement, and guarantor means. Show upfront payment and instalments.
3. Explain the cause of default factually. Do not make admissions beyond what is necessary and true.
4. Ask for withdrawal or suspension of recovery steps on acceptance, release of security and guarantors, and a no-dues certificate. Note credit bureau reporting.
5. For a wilful defaulter or fraud notice, check the process the directions and current Supreme Court authority require (for example State Bank of India v. Rajesh Agarwal, Supreme Court, 2023, on the right to be heard before fraud classification; confirm current treatment). Ask for documents relied on, including any forensic audit, and a personal hearing.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
6. Answer each allegation with documents. Distinguish inability to pay from wilful refusal and diversion.
7. Search for and read current authority on any contested point; tag unread authority `[verify]`.

## Output

1. The OTS or restructuring proposal letter, with a payment schedule table.
2. Or the show-cause reply with an annexure index and a request for documents and hearing.
3. A cover note listing risks, admissions to avoid, and next steps.

## Guardrails and hand-offs

- Never overstate assets, understate means, or hide income or transfers. Misstatement can be an offence and worsens classification risk.
- Never promise acceptance of an OTS.
- Enforcement status goes to `sarfaesi-enforcement-planner`; negotiation strategy to `settlement-strategy-planner`.
- Never invent case law. Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
