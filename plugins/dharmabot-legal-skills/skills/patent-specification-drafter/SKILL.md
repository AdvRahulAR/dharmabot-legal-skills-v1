---
name: patent-specification-drafter
description: Supports a registered patent agent in drafting provisional and complete specifications under the Patents Act 1970 and Patents Rules 2003 (title, field, background, summary, detailed description, claims, abstract) and the accompanying forms such as Forms 1, 2, 3, 5 and 26, including PCT national phase entry and request-for-examination timelines. Use when a client asks to draft a provisional or complete patent specification or prepare Indian patent filing forms. Do not use for screening whether an invention is patentable; use invention-disclosure-screener instead.
---

# Patent Specification Drafter

Every output is a draft for a registered Indian patent agent to review, sign and file.

## Purpose

Produce a specification that fully describes the invention, supports claims of varying scope, and meets Indian formal requirements.

## Jurisdiction gate

Confirm the filing is at the Indian Patent Office and record the appropriate office (based on the applicant's residence, place of business or address for service). For PCT national phase or Convention filings, record the international or priority application details.

## Required inputs

Mark as **blocking**:
- the invention disclosure with drawings, data and embodiments;
- the applicant(s) and inventor(s) with nationality and addresses;
- whether this is a provisional, complete, Convention or PCT national phase filing;
- for priority or PCT, the earliest priority date and the international application details.

Also useful: the screening report, known prior art, preferred claim scope, commercial embodiments, and applicant category for fees (startup, small entity, education institution).

## Method

1. Retrieve the current official text of the Patents Act and Rules, the forms and fee schedule from the Patent Office website, and the Manual of Patent Office Practice and Procedure. Record the version and date.
2. Compute key dates from the priority date: complete specification after a provisional, Convention deadline, PCT national phase entry, and request for examination. Confirm each period from the Rules and use `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. Draft the specification: title, field, background (without admitting prior art unnecessarily), objects, summary, brief description of drawings, detailed description with best method and multiple embodiments, and abstract.
4. Draft claims in tiers: broad independent claims, narrower independent claims in other categories (process, system, apparatus, use where allowed), and dependent claims with fallback features. Check every claim is supported by the description.
5. Check section 3 risk (believed to be the section; confirm against the official text) in claim wording (for software, tie claims to technical features and hardware).
6. Prepare the forms: application (Form 1), specification (Form 2), statement and undertaking on foreign filings (Form 3), declaration of inventorship (Form 5), and authorisation of agent (Form 26). Confirm current form numbers and contents.
7. List the documents needed: priority documents, proof of right, translations, and the startup or small-entity proof.

## Output

1. The draft specification with claims and abstract.
2. Draft forms data sheets.
3. A date schedule and filing checklist.

## Guardrails and hand-offs

- Filing, signing and prosecution are done by the applicant or a registered patent agent. An advocate who is not a registered patent agent is believed to be limited to appearing at hearings (confirm from the Patents Act chapter on patent agents).
- Never add data, results or embodiments the inventors have not supplied.
- Never state a deadline or fee from memory; confirm from the Rules.
- For the screening stage, hand off to `invention-disclosure-screener`.
- For examination, hand off to `patent-fer-reply-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
