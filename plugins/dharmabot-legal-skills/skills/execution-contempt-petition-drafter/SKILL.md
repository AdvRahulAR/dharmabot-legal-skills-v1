---
name: execution-contempt-petition-drafter
description: Drafts execution petitions under Order XXI of the Code of Civil Procedure (attachment, sale, arrest, garnishee and delivery of possession), including execution of domestic arbitral awards as decrees under section 36 of the Arbitration and Conciliation Act, and civil contempt petitions under the Contempt of Courts Act, 1971 for wilful disobedience. Use when an advocate asks to execute a decree, attach bank accounts, enforce an award, or file contempt for breach of an order or undertaking. Do not use for foreign decrees or awards; use foreign-judgment-award-enforcement-analyst instead.
---

# Execution and Contempt Petition Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Turn a decree, award or order into recovery or compliance, by choosing the executing court and the most effective modes, or by drafting a focused contempt petition.

## Jurisdiction gate

Confirm the decree, award or order is from an Indian court or an India-seated arbitration. Note the State. Identify the executing court: the court that passed the decree, or the court to which it is transferred where the property or judgment-debtor is located. For awards, check current authority on filing where assets are (for example Sundaram Finance Ltd v Abdul Samad, Supreme Court, 2018; confirm current treatment).

## Required inputs

Mark as **blocking**:
- the decree, award or order, with its date and certified copy;
- the amount due or act ordered, and payments received;
- known assets of the judgment-debtor (bank accounts, immovable property, receivables) with particulars;
- for an award, whether any challenge is pending and whether a stay was granted;
- for contempt, proof that the contemnor knew of the order, and the acts of disobedience.

## Method

1. Retrieve the current official text of Order XXI and the execution sections of the CPC, the Limitation Act articles on execution, section 36 of the Arbitration Act, the Contempt of Courts Act and the relevant High Court rules. Record the version and date.
2. Check limitation with `limitation-calculator`. Execution of a decree is subject to an outer limit (believed to be twelve years under the Limitation Act; confirm the article and its start date). Contempt has its own short limit (believed to be one year from the act; confirm).
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Choose modes of execution in the order most likely to recover: attachment of bank accounts and debts (garnishee), attachment and sale of property, delivery of possession, and arrest and detention only where the law's conditions are met.
4. Draft the execution application in the prescribed tabular form, with the schedule of property and the prayer for each mode.
5. Plan for resistance: objections under the CPC execution provisions, third-party claims, and corporate debtors under moratorium. Check for any IBC moratorium before filing.
6. For contempt: identify the specific order and clause breached, show knowledge and wilfulness, and seek compliance and punishment. Note that contempt is discretionary and is not a substitute for execution of money decrees.
7. Search for and read current authority on any contested point. Tag unread authority `[verify]`.

## Output

1. The draft execution petition with schedules, or the contempt petition with affidavit.
2. An asset and mode table: asset · particulars · mode · evidence available.
3. A note: limitation, likely objections, and next steps.

## Guardrails and hand-offs

- Never list assets that have not been verified.
- Never use contempt to pressure payment of a simple money decree.
- Formatting: `court-pleading-formatter`. Insolvency route: `ibc-application-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
