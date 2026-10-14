---
name: trademark-application-drafter
description: Prepares TM-A trademark applications under the Trade Marks Act 1999 and Trade Marks Rules 2017, covering applicant type and fee category (individual, startup, MSME, others), class selection, specification of goods and services, proposed-to-be-used or user claims with affidavit and evidence, priority claims and Madrid designations. Use when a client wants to file a trademark in India for a word mark, logo or tagline. Do not use for replying to an examination report; use trademark-examination-reply-drafter instead.
---

# Trademark Application Drafter

Every output is a draft for an advocate or registered trademark agent in India to check and file.

## Purpose

Prepare a complete TM-A filing pack with an accurate specification and a user claim that the evidence supports.

## Jurisdiction gate

Confirm the application is for the Indian Trade Marks Registry. Record the applicant's principal place of business in India (or address for service in India for a foreign applicant), which decides the appropriate office. For an international application under the Madrid Protocol, note the extra steps and mark foreign points for local counsel.

## Required inputs

Mark as **blocking**:
- the applicant's exact legal name, entity type, address and nationality or place of incorporation;
- the mark (word, device, colour, sound or shape) and a clean representation;
- the goods and services in plain words;
- the date of first use in India, or that it is proposed to be used;
- evidence for any user claim, and any priority filing (country, number, date).

Also useful: startup recognition or MSME registration (for the fee category), translation or transliteration of non-English words, and any clearance report.

## Method

1. Retrieve the current official text of the Trade Marks Act, the Rules, the current fee schedule and the TM-A form from the Registry website. Record the version and date.
2. Decide the fee category from the documents supplied; never assume startup or MSME status without proof.
3. Choose classes using the current NICE edition. Draft a specification that is precise and covers the real business and near expansion, without being so broad that it invites objection or non-use attack.
4. Decide the filing set. Recommend separate word and device filings where the logo contains a distinctive word, and a multi-class or single-class approach with reasons.
5. For a user claim, draft the user affidavit stating the date of first use with supporting evidence (invoices, advertisements, website archives). Flag gaps between the claimed date and the evidence.
6. Record priority details and check that the priority period has not expired; confirm the period from the Act.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
7. Draft the authorisation of agent (TM-48 or the current form) where an agent files.
8. Note follow-up: examination, advertisement, opposition window and renewal.

## Output

1. A completed TM-A data sheet (field by field).
2. The specification for each class.
3. The draft user affidavit and an evidence index.
4. A filing note: fee category, office, documents and next steps.

## Guardrails and hand-offs

- Never back-date a user claim or fabricate evidence of use.
- Do not state a fee or deadline from memory; confirm from the official schedule.
- For examination objections, hand off to `trademark-examination-reply-drafter`.
- To record the filing in the client's portfolio, hand off to `ip-portfolio-tracker`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
