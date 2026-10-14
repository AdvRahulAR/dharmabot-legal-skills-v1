---
name: cestat-appeal-drafter
description: Drafts appeals to the Customs, Excise and Service Tax Appellate Tribunal under the Customs Act, 1962 and the Central Excise Act, 1944 (including legacy service tax under the Finance Act, 1994), in the prescribed forms with statement of facts, grounds, the mandatory pre-deposit working, and applications for early hearing, condonation and additional evidence under the CESTAT Procedure Rules, 1982. Use when a Commissioner or Commissioner (Appeals) has confirmed a customs, excise or service tax demand and the client wants to go to CESTAT. Do not use for GST appeals; use tax-appeal-grounds-drafter.
---

# CESTAT Appeal Drafter

Every output is a draft for an advocate or authorised representative to check and sign.

## Purpose

Produce a complete, maintainable CESTAT appeal, with the right form, bench, pre-deposit and limitation, and grounds tied to the order and the record.

## Jurisdiction gate

Confirm the impugned order is under the Customs Act, the Central Excise Act or Chapter V of the Finance Act, 1994, and passed by an authority whose orders are appealable to CESTAT. Some orders (for example certain baggage or drawback matters) go to the Central Government in revision instead; check the current exclusions. Identify the regional bench by the location of the adjudicating authority, and whether a single member or division bench hears it (monetary limits; confirm).

## Temporal gate

Record the date of the order and the date of its communication. Pre-deposit rules depend on when the appeal is filed and the Finance Act amendments then in force. Legacy service tax disputes are governed by transitional provisions after GST; confirm they still apply.

## Required inputs

Mark as **blocking**:
- the impugned order-in-original or order-in-appeal, with its date of communication;
- the show cause notice and the reply filed;
- the amounts of duty, interest, penalty and fine confirmed, and any amount already paid or deposited.

Also useful: the record before the lower authority, relevant invoices, test reports, and any earlier CESTAT or court orders on the same issue.

## Method

1. Retrieve the current official text of the appeal provisions (believed to be section 129A of the Customs Act and section 35B of the Central Excise Act), the pre-deposit provisions (believed to be sections 129E and 35F), the CESTAT Procedure Rules, 1982, the appeal forms, the fee schedule, and CESTAT's current e-filing notices. Record the source and date.
2. Check limitation from the date of communication with `limitation-calculator`. If late, draft a condonation application with a day-by-day explanation.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Work out the pre-deposit: the percentage of duty or penalty in dispute and the statutory cap, set against amounts already paid. Show the arithmetic and the source of each figure.
4. Choose the form (for example the customs, excise or service tax appeal forms) and the bench, and compute the fee from the current schedule.
5. Draft the statement of facts from the record only, then grounds: jurisdiction and limitation of the demand, extended period and suppression, classification or valuation errors, natural justice, penalty and interest. Merits analysis of classification or valuation from scratch goes to `customs-trade-remedy-analyst`.
6. Search for current CESTAT, High Court and Supreme Court authority on each ground. Read it; tag anything unread `[verify]`.
7. Draft miscellaneous applications as needed: early hearing, additional evidence, change of cause title.

## Output

1. Appeal in the prescribed form, with statement of facts and grounds.
2. Pre-deposit working and proof list.
3. Miscellaneous applications.
4. Filing checklist: fee, copies, authorisation, e-filing steps.

## Guardrails and hand-offs

- Never state a pre-deposit percentage, cap, fee or period as settled without the current source.
- Never promise a waiver or a result.
- GST appeals go to `tax-appeal-grounds-drafter`; layout to `court-pleading-formatter`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
