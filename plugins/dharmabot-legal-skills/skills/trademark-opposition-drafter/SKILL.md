---
name: trademark-opposition-drafter
description: Drafts trademark opposition pleadings in India under the Trade Marks Act 1999 and Rules 2017, covering notices of opposition, counter-statements, evidence affidavits under the Rules, and rectification or cancellation petitions, on prior rights, deception, bad faith and well-known status, with opposition and evidence deadlines tracked. Use when a competitor's mark has been advertised in the Trade Marks Journal, or a client's mark is opposed, or a registered mark should be removed. Do not use for an examination report reply; use trademark-examination-reply-drafter instead.
---

# Trademark Opposition Drafter

Every output is a draft for an advocate or registered trademark agent in India to check and file.

## Purpose

Prepare the right opposition-stage document, within time, with grounds and evidence that match the client's real rights.

## Jurisdiction gate

Confirm the proceeding is before the Indian Trade Marks Registry, or for rectification before the Registrar or the High Court (after the abolition of IPAB, rectification lies with the High Court; confirm the current IP Division rules). Record the application or registration number and the Journal date.

## Required inputs

Mark as **blocking**:
- the Journal advertisement or registration details of the impugned mark;
- the client's role (opponent, applicant, petitioner, registered proprietor);
- the client's rights relied on (registrations, use evidence with dates, well-known status);
- the date of the Journal publication or of service of the last pleading.

Also useful: evidence of the other party's bad faith, market reports, prior correspondence and any related litigation.

## Method

1. Retrieve the current official text of the Trade Marks Act, the Rules on opposition and evidence, the forms (TM-O and others) and fees, and the High Court IP Division rules where relevant. Record the version and date.
2. Compute deadlines: the opposition window from the Journal date (reported as four months and non-extendable; confirm), and the counter-statement and evidence periods. Use `limitation-calculator`. Flag any missed deadline at the top.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. **Notice of opposition:** set out the opponent's rights and grounds, such as likelihood of confusion with an earlier mark, prior use and passing off, bad faith, deception, lack of distinctiveness, and well-known mark protection. Plead only grounds with factual support.
4. **Counter-statement:** respond paragraph by paragraph, deny unsupported claims, and plead honest adoption, concurrent use, and differences in marks and goods.
5. **Evidence affidavits:** draft the opponent's evidence in support, the applicant's evidence, and evidence in reply, as the Rules require, with exhibits indexed.
6. **Rectification or cancellation:** grounds such as non-use for the statutory period, wrongly remaining on the register, or bad-faith registration; identify the forum.
7. Search for and read current authority on each ground. Tag anything not read in full `[verify]`.
8. Note where a civil suit for infringement or passing off is a better or parallel route, especially if the other party is already using the mark.

## Output

1. The draft pleading or petition.
2. Evidence affidavit and exhibit list.
3. A deadline schedule for the remaining stages.
4. A strategy note comparing opposition, rectification and a suit.

## Guardrails and hand-offs

- Never fabricate use dates, sales or reputation evidence.
- Never invent case law or Registry orders.
- For enforcement against actual use, hand off to `ip-infringement-analyst`.
- For deadlines, use `limitation-calculator`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
