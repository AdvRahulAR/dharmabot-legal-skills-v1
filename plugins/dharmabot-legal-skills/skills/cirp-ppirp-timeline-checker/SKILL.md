---
name: cirp-ppirp-timeline-checker
description: Builds and audits the timeline of a corporate insolvency resolution process, or a pre-packaged process for MSMEs, under the Insolvency and Bankruptcy Code, 2016 and the IBBI CIRP and PPIRP Regulations, and analyses the moratorium's effect on suits, arbitrations, contracts and guarantees. Use when an IRP, RP, CoC member or creditor asks for a regulation-wise timeline, wants to know what deadlines were missed, or asks if a moratorium stops a proceeding. Do not use for drafting claims; use insolvency-claim-drafter.
---

# CIRP and PPIRP Timeline Checker

Every output is a draft review for an insolvency professional or advocate in India to check.

## Purpose

Produce a dated timeline of every step the law requires, mark what is done, late or missing, and advise on the moratorium's reach.

## Jurisdiction gate

Confirm an NCLT bench in India has admitted the process, and note whether it is a CIRP, a PPIRP for an MSME, a fast-track process, or a creditor-initiated process under the 2026 amendment (confirm it is in force). The rules differ for each.

## Temporal gate

The CIRP Regulations are amended frequently. The Insolvency and Bankruptcy Code (Amendment) Act, 2026 is reported to have received assent on 6 April 2026, with provisions brought into force from 26 May 2026 by notification; confirm from the eGazette which provisions are in force and any transitional rule. It is reported to add a creditor-initiated process with its own timelines and to change withdrawal rules. Check which version applied on each step date.

## Required inputs

Mark as **blocking**:
- the admission order and its date of pronouncement and upload;
- the type of process;
- the steps already taken, with dates (public announcement, claims, CoC, valuers, information memorandum, Form G, plans received);
- any exclusion or extension orders from the NCLT.

Also useful: CoC minutes, the list of creditors, and pending applications.

## Method

1. Retrieve the current official text of the IBC, the CIRP Regulations or PPIRP Regulations, and IBBI circulars on timelines and model timelines. Record versions and dates. Do not rely on remembered day counts.
2. Fix the insolvency commencement date from the order, and note any dispute about it.
3. Lay out each step with its regulation, the deadline computed from the commencement date, and the actual date.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
4. Apply the overall time limits and extensions (believed to be section 12; confirm), and exclusions granted by the NCLT or permitted by authority. Search for and read current authority on exclusion of time; tag unread authority `[verify]`.
5. Flag missed or late steps, their effect, and cure options (for example an application to the NCLT).
6. For the moratorium (believed to be section 14), test each affected proceeding or contract: suits and arbitrations against the debtor, enforcement of security, recovery of property, termination of essential supplies or licences, and set-off. Note the carve-outs and that the moratorium usually does not protect guarantors; confirm current law.
7. For PPIRP, check the base resolution plan, the creditors' approval steps, and the shorter overall limit.
8. Highlight risks that could lead to liquidation, such as no plan by the deadline.

## Output

1. A timeline table: step, provision, due date, actual date, status, note.
2. A list of lapses with risk and cure.
3. A moratorium note for each proceeding or contract raised.

## Guardrails and hand-offs

- Never treat a computed date as final without the order dates checked.
- Claims go to `insolvency-claim-drafter`; plan review to `resolution-plan-reviewer`; challenges to `nclt-nclat-appeal-drafter`.
- Never invent case law. Run `citation-verifier` before delivery.
