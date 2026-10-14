---
name: drt-application-drafter
description: Drafts proceedings before the Debts Recovery Tribunals and DRAT under the Recovery of Debts and Bankruptcy Act, 1993 and the SARFAESI Act, 2002, covering lender original applications, borrower securitisation applications, written statements, counterclaims, interim stay applications and DRAT appeals with pre-deposit. Use when a lawyer asks for a DRT OA, a section 17 SARFAESI application, a stay of auction, or an appeal to the DRAT. Do not use for overall enforcement strategy; use sarfaesi-enforcement-planner.
---

# DRT Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce a filing-ready draft before the DRT or DRAT, built on the record, with jurisdiction and limitation checked first.

## Jurisdiction gate

Confirm the debt is owed to a bank or financial institution covered by the RDB Act, and the claim meets the pecuniary minimum notified for the DRT. Identify the correct DRT by territorial rules (where the defendant resides or works, or where the cause of action or secured asset lies). Confirm the current DRT territorial notification. For a securitisation application, the DRT with jurisdiction over the secured asset's location usually applies; confirm.

## Required inputs

Mark as **blocking**:
- the proceeding type (lender OA, borrower securitisation application, written statement, interim application, DRAT appeal);
- the notices or order challenged, with dates of issue and receipt;
- the loan and security documents and account statement;
- for an appeal, the order appealed and the amount of debt determined.

Also useful: the auction notice, valuation reports, prior replies, and any OTS correspondence.

## Method

1. Retrieve the current official text of the RDB Act, the SARFAESI Act, the DRT (Procedure) Rules, the DRAT procedure rules, the fee rules and the pecuniary jurisdiction notification. Record versions and dates. Section numbers here are orientation only.
2. Compute limitation with `limitation-calculator`. A securitisation application has a short period from the measure challenged (believed to be 45 days; confirm). A DRAT appeal also has a short period and a pre-deposit requirement; confirm both from the text.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. For a lender OA: plead the debt, the account, acknowledgments that extend limitation, the security, and the guarantors. Attach a certified statement of account under the Bankers' Books Evidence Act.
4. For a borrower securitisation application: plead each defect in the steps taken (NPA classification, demand notice, reply to objections, possession, valuation, sale notice). Seek stay, interim relief and restoration of possession only where the record supports it.
5. For a written statement and counterclaim: deal with each paragraph, plead limitation and set-off where available, and file within the time allowed.
6. For a DRAT appeal: grounds tied to findings in the order, pre-deposit computation and any waiver or reduction prayer.
7. Note the limits on writ petitions where a statutory remedy exists. Search for and read current Supreme Court authority; tag unread authority `[verify]`.
8. Prepare the index, synopsis and list of dates, affidavit, fee computation note and annexures.

## Output

1. The draft application, appeal or written statement.
2. An interim application for stay where needed.
3. Index, list of dates, annexure list and fee note.
4. A short note for counsel: limitation status, strongest points, missing documents.

## Guardrails and hand-offs

- Never promise a stay or waiver of pre-deposit.
- Never plead facts or defects not supported by documents.
- Overall strategy goes to `sarfaesi-enforcement-planner`; formatting to `court-pleading-formatter`.
- Never invent case law. Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
