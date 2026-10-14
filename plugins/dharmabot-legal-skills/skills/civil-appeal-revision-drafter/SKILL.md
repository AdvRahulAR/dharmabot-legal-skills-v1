---
name: civil-appeal-revision-drafter
description: Drafts memoranda of first appeal under section 96 and Order XLI of the Code of Civil Procedure, second appeals under section 100 with substantial questions of law, commercial appeals under section 13 of the Commercial Courts Act, revisions under section 115 CPC or Article 227, and review petitions under Order XLVII, with stay applications. Use when an advocate asks to appeal a decree, draft grounds of appeal, a civil revision, review petition or stay of a decree. Do not use for Supreme Court petitions; use special-leave-petition-drafter instead.
---

# Civil Appeal and Revision Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Pick the correct remedy and forum against a civil order or decree, and draft grounds that match the record.

## Jurisdiction gate

Confirm the order is from an Indian civil or commercial court and note the court, State and the nature of the order (decree, appealable order, interlocutory order, commercial court order). Identify the appellate or revisional forum from the pecuniary limits of the State's civil courts law and the Commercial Courts Act.

## Required inputs

Mark as **blocking**:
- the impugned judgment, decree or order;
- the date of the order and the date of applying for and receiving the certified copy;
- the pleadings, issues and evidence relevant to the grounds;
- the client's instructions on which findings to challenge.

## Method

1. Retrieve the current official text of the CPC provisions on appeals, revision and review, the Commercial Courts Act, the Limitation Act, the State's civil courts act on forum, and the High Court's appellate rules. Record the version and date.
2. Choose the remedy. First appeal on facts and law; second appeal only on a substantial question of law; commercial appeal under the Commercial Courts Act and only against orders it allows; revision against a case decided where no appeal lies; Article 227 supervision; review on an error apparent on the record or new evidence. State why the chosen remedy fits and the others do not.
3. Compute limitation with `limitation-calculator`, excluding the time for certified copies as the law allows. If late, prepare a condonation application.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. Compute court fee with `state-court-fee-calculator`.
5. Draft grounds: each ground specific, tied to the finding and the record page, and not argumentative. For a second appeal, frame the substantial questions of law precisely.
6. Check whether each point was raised below. Flag new points; new pleas of fact usually cannot be raised for the first time.
7. Draft a stay application with grounds, and offer security or deposit where a money decree is involved, as the Order XLI rules usually require (confirm the rule against the official text).
8. Search for and read current authority on the remedy and the main grounds. Tag unread authority `[verify]`.

## Output

1. The draft memorandum of appeal, revision or review.
2. The stay application and affidavit.
3. A note: remedy reasoning, limitation, court fee, and points not raised below.

## Guardrails and hand-offs

- Never misstate a finding or the record.
- Never invent authority.
- If the remedy or forum is wrong, say so first.
- Formatting: `court-pleading-formatter`. Supreme Court: `special-leave-petition-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
