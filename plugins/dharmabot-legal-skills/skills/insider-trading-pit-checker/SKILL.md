---
name: insider-trading-pit-checker
description: Applies the SEBI (Prohibition of Insider Trading) Regulations 2015 to UPSI, designated persons, the structured digital database, trading window closure, pre-clearance, trading plans, contra-trades, disclosures, leak inquiries and reporting of violations, and drafts or reviews the code of conduct and fair disclosure code. Use when an employee or director traded near results, UPSI may have leaked, or a listed company needs its PIT code reviewed. Do not use for event disclosure to exchanges; use sebi-lodr-disclosure-checker instead.
---

# Insider Trading PIT Checker

Every output is a draft for an advocate or the compliance officer of a listed entity to check.

## Purpose

Test a trade or a leak against the PIT Regulations and the company's code, set out the company's obligations and the individual's exposure, and draft the internal and exchange paperwork.

## Jurisdiction gate

- Confirm the securities are listed, or proposed to be listed, in India. The PIT Regulations also reach intermediaries and fiduciaries handling UPSI.
- Note whether the person is an employee, director, promoter, connected person, designated person or immediate relative. Duties differ for each.

## Temporal gate

The PIT Regulations have been amended often (including on trading plans and the definition of UPSI). Record the trade dates and apply the text in force on each date.

## Required inputs

- **Blocking:** the company and its listing status; the person, their role and designation status; trade dates, quantities and direction; the UPSI involved and when it arose and was published.
- **Blocking for a leak inquiry:** the company's leak inquiry policy and the structured digital database entries.
- Useful: the code of conduct, trading window notices, pre-clearance records, any trading plan, and the person's earlier trades (for contra-trade testing).

## Method

1. Retrieve the current official text of the PIT Regulations, their schedules and the current SEBI circulars and FAQs on PIT from sebi.gov.in. Record the version and date.
2. Decide whether the information was UPSI at the trade date: price-sensitive, not generally available, and within the categories listed. Build a timeline: UPSI created, entered in the database, trading window closed, information published.
3. Test the trade:
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
   - Was the window closed? Was pre-clearance required and obtained?
   - Was it under an approved, disclosed trading plan?
   - Is there a contra-trade within the prohibited period?
   - Are disclosure thresholds crossed, and was disclosure made on time?
4. Consider statutory defences the text allows (for example off-market inter se transfers between insiders in possession of the same UPSI, or a trading plan). Apply only those confirmed from the text.
5. State the company's steps: inquiry under the code, disgorgement of contra-trade profit where the code provides, recording, and reporting violations to the stock exchanges in the prescribed format and time.
6. For a leak, plan the inquiry: preserve devices and logs, interview in sequence, report to SEBI as the text requires. Hand a larger inquiry to `internal-investigation-planner`.
7. For code drafting or review, check every mandatory element of Schedule A and Schedule B (believed to be the schedules; confirm against the official text) against the company's documents and list gaps.
8. Flag where the individual or company may need advice on SEBI settlement, the informant mechanism or adjudication; that needs separate counsel.

## Output

1. UPSI and trade timeline.
2. Breach analysis by rule, with evidence for each point.
3. Company action list with deadlines (verified) and draft exchange report.
4. For code work, a redline or gap table.

## Guardrails and hand-offs

- Do not conclude that someone traded "on the basis of" UPSI; state the facts and presumptions.
- Never advise on structuring trades to avoid the window or disclosure.
- Keep the matter confidential; the analysis may itself be UPSI.
- Event disclosure goes to `sebi-lodr-disclosure-checker`.
