---
name: summary-suit-order-xxxvii-drafter
description: Drafts summary suits under Order XXXVII of the Code of Civil Procedure on written contracts, bills of exchange, promissory notes, cheques and acknowledged liquidated debts, and the defendant's application for leave to defend, applying the Supreme Court's tests in IDBI Trusteeship. Use when an advocate asks for an Order 37 suit, summary suit, summons for judgment, or leave to defend. Do not use where the claim is unliquidated or needs an ordinary trial; use plaint-drafter instead.
---

# Summary Suit (Order XXXVII) Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Draft a summary suit only where the claim truly fits Order XXXVII, or a leave-to-defend application that shows a triable defence.

## Jurisdiction gate

Confirm the suit is in an Indian court to which Order XXXVII applies (High Courts and the courts notified by them, and Commercial Courts). Note the State and court, and whether the High Court's original side rules add their own forms. Check any arbitration clause first.

## Required inputs

Mark as **blocking**:
- for the plaintiff: the written contract, negotiable instrument, invoices with written acceptance, or the written acknowledgment of debt;
- the exact liquidated amount and interest basis;
- the parties' details and the place of suing;
- for the defendant: the summons, the summons for judgment and its affidavit, and the date of service of each.

## Method

1. Retrieve the current official text of Order XXXVII CPC, any High Court amendment and original side rules, the Commercial Courts Act amendments and the Limitation Act. Record the version and date. Confirm every section, order and rule number used in this skill against that text.
2. Test eligibility. The claim must be a debt or liquidated demand in money, with or without interest, arising on a written contract, an enactment, a guarantee, or a negotiable instrument as the Order allows. Ledger entries alone, damages, or disputed quantities usually fail. If it fails, say so and recommend an ordinary suit.
3. Check limitation with `limitation-calculator`, using acknowledgments and part-payments.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
4. Plaintiff's draft: the plaint with the mandatory statement that it is filed under Order XXXVII and that no relief outside the Order is claimed; computation of the amount and interest; documents; verification; and, after appearance, the summons for judgment with a supporting affidavit.
5. Defendant's draft: an application for leave to defend with a supporting affidavit. Disclose facts showing a substantial defence or a genuine triable issue. Apply the tests in IDBI Trusteeship Services Ltd v Hubtown Ltd (Supreme Court, 2016); read the judgment and confirm current treatment. Address whether conditions (deposit or security) are likely, and offer reasonable ones.
6. Calendar the strict periods for appearance and leave to defend from the served summons. Confirm each period from the official text.
7. Search for and read current High Court authority on any contested point. Tag unread authority `[verify]`.

## Output

1. The draft plaint or leave-to-defend application with affidavit.
2. An eligibility note: why the claim does or does not fit the Order.
3. A deadline table from service dates.

## Guardrails and hand-offs

- Never force an unliquidated claim into Order XXXVII.
- Never plead a defence the client's documents do not support, and never invent a sham defence.
- If the claim does not fit, hand off to `plaint-drafter`.
- Cheques: consider a parallel complaint via `cheque-dishonour-case-drafter`.
- Formatting: `court-pleading-formatter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
