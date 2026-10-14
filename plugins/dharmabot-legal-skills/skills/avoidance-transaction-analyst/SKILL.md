---
name: avoidance-transaction-analyst
description: Analyses a corporate debtor's transactions under the avoidance provisions of the Insolvency and Bankruptcy Code, 2016, covering preferential, undervalued, defrauding-creditors and extortionate credit transactions, and fraudulent or wrongful trading, and drafts the avoidance application to the NCLT. Use when an RP or liquidator asks to review bank statements or related-party payments for avoidance transactions, or a counterparty wants to defend one. Do not use for general fund-flow forensics; use fraud-funds-flow-analyst.
---

# Avoidance Transaction Analyst

Every output is a draft review for an insolvency professional or advocate in India to check.

## Purpose

Screen the debtor's transactions in the look-back periods, classify each suspect one under the right head, and set out the evidence needed before any application.

## Jurisdiction gate

Confirm a CIRP or liquidation is under way before an NCLT in India and identify the insolvency commencement date. Note the client's role: RP, liquidator, CoC member, or the counterparty defending.

## Temporal gate

The IBC (Amendment) Act, 2026 (provisions reported in force from 26 May 2026) is reported to add a definition of avoidance transactions and to let creditors apply where the RP or liquidator does not. Confirm the text in force on the application date and any transitional rule.

## Required inputs

Mark as **blocking**:
- the insolvency commencement date;
- bank statements, ledgers and the transaction audit report (if any) for the look-back periods;
- the list of related parties with the basis for each;
- the client's role.

Also useful: board minutes, valuation reports, loan documents, and correspondence explaining the transactions.

## Method

1. Retrieve the current official text of the IBC avoidance provisions (believed to be sections 43 to 51 and 66; confirm), the regulations requiring the RP to form an opinion and file by set dates, and IBBI guidance. Record versions and dates.
2. Fix the look-back periods from the commencement date. The Code sets a longer period for related parties than for others; confirm the periods from the text and compute them.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Screen transactions for heads: preference to a creditor or surety for an antecedent debt; undervalue (gift or significantly less than value, not in the ordinary course); intent to defraud creditors; extortionate credit; and fraudulent or wrongful trading by those in charge.
4. For each suspect transaction, record date, parties, amount, relationship, head, the ordinary-course or other exception, and the evidence held and missing.
5. Separate weak suspicion from evidenced findings. Only evidenced findings go in the application.
6. Note the remedies the NCLT may order and who bears them, including third parties who received benefits in good faith.
7. Search for and read current Supreme Court and NCLAT authority on look-back computation, ordinary course and whether avoidance applications survive the end of the CIRP. Tag unread authority `[verify]`.
8. If acting for the counterparty, build the defence on the same table.

## Output

1. A transaction table: date, parties, amount, head, exception, evidence, assessment.
2. A short findings memo for the CoC or liquidator.
3. A draft avoidance application with grounds and prayer, where the evidence supports one.

## Guardrails and hand-offs

- Never allege fraud or intent without documentary evidence.
- Never name individuals as wrongdoers in the memo without the basis stated.
- Detailed fund tracing goes to `fraud-funds-flow-analyst`; appeals to `nclt-nclat-appeal-drafter`.
- Never invent case law. Run `citation-verifier` before delivery.
