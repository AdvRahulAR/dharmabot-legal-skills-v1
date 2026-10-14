---
name: nclt-nclat-appeal-drafter
description: Drafts interlocutory applications before the NCLT and appeals to the NCLAT under the Insolvency and Bankruptcy Code, 2016 and the Companies Act, 2013, including oppression and mismanagement matters, with grounds tied to the order and a strict limitation check from the date the order was available. Use when a lawyer asks for an NCLAT appeal against an admission or rejection order, an IA in a CIRP, or an appeal in an oppression case. Do not use for the original IBC petition; use ibc-application-drafter.
---

# NCLT NCLAT Appeal Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce an appeal or application that is within time, attacks the right findings, and asks for relief the tribunal can grant.

## Jurisdiction gate

Confirm the order is of an NCLT bench in India and identify the statute under which it was made (IBC or Companies Act). Identify the NCLAT bench (Principal Bench or Chennai) by the NCLT that passed the order; confirm the current allocation. Note that a further appeal to the Supreme Court lies on questions of law; confirm the provision.

## Temporal gate

Record the date of pronouncement, the date the order was uploaded, the date a certified copy was applied for and received, and the filing date. Limitation is short and condonation is narrow under both statutes.

## Required inputs

Mark as **blocking**:
- the order appealed or the proceeding in which the IA is filed;
- all dates above;
- the client's role and standing (party, creditor, shareholder, aggrieved person);
- the record before the NCLT.

Also useful: the NCLT pleadings, transcripts or notes of hearing, and related orders.

## Method

1. Retrieve the current official text of the IBC appeal provision (believed to be section 61), the Companies Act appeal provision (believed to be section 421), the NCLT Rules, the NCLAT Rules and any NCLAT practice directions on e-filing and certified copies. Record versions and dates.
2. Compute limitation with `limitation-calculator`. Do not assume the period; confirm the base period and the maximum condonable period from the text. Search for and read current Supreme Court authority on when time runs and the need to apply for a certified copy; tag unread authority `[verify]`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. If late, draft a condonation application with day-by-day reasons supported by documents, and state if the delay is beyond the condonable limit.
4. Identify the findings appealed. Tie each ground to a paragraph of the order and the record. Typical heads: error of law, ignoring material, natural justice, jurisdiction, and perversity.
5. For oppression and mismanagement matters, check standing and the thresholds (or waiver) for the petitioners, and frame relief the tribunal may grant.
6. Draft any stay application with prima facie case, balance of convenience and irreparable harm from the record.
7. Prepare the synopsis, list of dates, index, affidavit and fee note.

## Output

1. The draft appeal or IA with grounds and prayer.
2. Any condonation and stay applications.
3. A limitation note and filing checklist.

## Guardrails and hand-offs

- Never promise admission of an appeal or a stay.
- Never raise facts outside the record without flagging them as new.
- Formatting goes to `court-pleading-formatter`; deadline computation to `limitation-calculator`.
- Never invent case law. Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
