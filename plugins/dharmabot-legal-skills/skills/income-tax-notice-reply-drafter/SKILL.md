---
name: income-tax-notice-reply-drafter
description: Reads Indian income-tax notices (scrutiny, information requests, reassessment, penalty, TDS defaults and faceless assessment) and drafts replies, checking jurisdiction, limitation, sanction and procedure under the Income-tax Act, 1961 for earlier years and the Income-tax Act, 2025 from its commencement. Use when a client has received a reassessment notice, scrutiny notice, show-cause notice or penalty notice and wants validity checked and a reply drafted. Do not use for appeals against assessment orders; use tax-appeal-grounds-drafter.
---

# Income Tax Notice Reply Drafter

Every output is a draft for an advocate or chartered accountant in India to check.

## Purpose

Test the notice for validity, decide between a reply and a writ, and draft a reply that answers on the merits while keeping all objections alive.

## Jurisdiction gate

Confirm the notice is from the Indian income-tax department and identify the issuing authority (jurisdictional or faceless unit), the PAN holder's status (resident, non-resident, company, individual), and any treaty issue. Treaty points go to `dtaa-withholding-analyst`.

## Temporal gate

The Income-tax Act, 2025 came into force on 1 April 2026; confirm from the official notification. Identify the assessment year or tax year and the date of the notice. Check from the transition provisions which Act and procedure govern this proceeding. For reassessment, the procedure and time limits changed in 2021 and again later; apply the version in force for the year and the notice date.

## Required inputs

Mark as **blocking**:
- the full notice with DIN, date, provision invoked and any annexures;
- the assessment year or tax year;
- the return filed for that year and its computation;
- for reassessment, any prior notice, the information relied on, and the approval or sanction recorded.

Also useful: earlier assessment orders, books of account, bank statements, and correspondence.

## Method

1. Retrieve the current official text of the applicable Act, rules, CBDT notifications and instructions, and the faceless scheme. Record versions and dates. Hand off section mapping to `income-tax-act-2025-concordance-mapper`.
2. Check validity: DIN, correct authority, service, time limit, approval or sanction from the right authority, and the pre-notice inquiry and opportunity where required.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. For reassessment, test whether the information relied on meets the statutory standard, and whether the monetary and time conditions for older years are met.
4. Decide whether a writ is stronger than a reply (for example notice barred by limitation, or no valid sanction). Search for and read current Supreme Court and jurisdictional High Court authority; tag unread authority `[verify]`.
5. Draft the reply: preliminary objections, then point-wise answers with documents.
6. Ask for the material relied on, cross-examination where witnesses are relied on, and a personal hearing through video conference where allowed.
7. Prepare a document index cross-referenced to the reply.

## Output

1. A validity note: each check, pass or fail, and the writ or reply recommendation.
2. The draft reply and document index.
3. The reply deadline and next steps.

## Guardrails and hand-offs

- Never suggest backdated documents or concealment of income.
- Never promise the notice will be dropped.
- Appeals go to `tax-appeal-grounds-drafter`; deadlines to `limitation-calculator`.
- Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
