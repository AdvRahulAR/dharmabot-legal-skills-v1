---
name: uk-pre-action-letter-drafter
description: Drafts English letters before claim and responses that follow the Practice Direction on Pre-Action Conduct and any relevant pre-action protocol under the Civil Procedure Rules, without-prejudice settlement letters and claim summaries for UK solicitors, with notes on enforcing an English judgment back in India under s.44A CPC. Use when an Indian client is owed money by, or is in dispute with, an English or Welsh party and its UK solicitors want a first draft. Do not use for enforcement analysis itself; use foreign-judgment-award-enforcement-analyst.
---

# UK Pre Action Letter Drafter

Every output is a draft for an authorised UK lawyer to review, adopt and send. It is not advice on English law.

## Purpose

Give the UK solicitor a well-organised first draft that tracks the pre-action rules and the client's evidence, saving time without taking their judgement.

## Jurisdiction gate

Confirm the dispute will be pursued in England and Wales (Scotland and Northern Ireland have separate systems). Check the contract's governing-law and jurisdiction clauses; if they point to arbitration or another court, stop and flag. Mark every English-law point "to be confirmed by counsel qualified in [jurisdiction]". Indian law governs the enforcement-in-India note.

## Required inputs

Mark as **blocking**:
- the parties, with the debtor's correct legal name and status (company, LLP, sole trader or individual);
- the contract and invoices, or the basis of the claim;
- the amount claimed and how it is calculated;
- the name of the UK solicitor who will review and send.

Also useful: correspondence, acknowledgements of debt, any dispute raised by the debtor, and earlier without-prejudice offers.

## Method

1. Retrieve the current official text of the Practice Direction on Pre-Action Conduct and Protocols, any specific protocol that may apply, the relevant CPR parts, and, for interest, the Late Payment of Commercial Debts (Interest) Act 1998 and current base rate. Record versions and dates. Open `references/foreign-jurisdictions.md` for UK sources and the India enforcement position.
2. Choose the protocol. The Pre-Action Protocol for Debt Claims is believed to apply where the debtor is an individual (including a sole trader); for a company debtor, the general Practice Direction usually applies. The solicitor confirms.
3. Draft the letter before claim: parties; the basis of the claim; a clear summary of facts; what is claimed and how it is calculated (principal, contractual or statutory interest, compensation); key documents enclosed or offered; a reasonable response period; the ADR invitation; and the consequences of non-response.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
4. For a response, address each allegation: admitted, denied with reasons, or not known, and list documents relied on.
5. Draft any without-prejudice letter separately, clearly marked, so it is not mixed with open correspondence.
6. Add a one-page claim summary for the solicitor: chronology, evidence, limitation (to be confirmed), likely defences, and enforcement options.
7. Add an India note: the United Kingdom is believed to be a reciprocating territory (confirm from the current Gazette notification [verify]), so an English superior court money judgment may be executed in India under s.44A CPC, subject to s.13 CPC (believed to be the sections; confirm against the official text). Hand off detail to `foreign-judgment-award-enforcement-analyst`.

## Output

1. The draft letter before claim or response.
2. A separate without-prejudice letter, if asked.
3. The claim summary and India enforcement note.

## Guardrails and hand-offs

- Never send the letter or address the debtor directly.
- Never threaten consequences the rules do not support.
- For service of English proceedings on a party in India, hand off to `cross-border-service-evidence-planner`.
- For a research point on English law, hand off to `foreign-law-research-memo-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
- In the letter and the table, mark each English statute, section, period and rate (for example the 1998 Act and its interest and compensation provisions, s.35A Senior Courts Act 1981, s.69 County Courts Act 1984) as believed and to be confirmed by the UK solicitor, with the current base rate checked and dated.
- Keep without-prejudice settlement content out of the open letter; say in the response that any offer is in a separate without-prejudice letter.
