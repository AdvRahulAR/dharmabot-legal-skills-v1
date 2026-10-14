---
name: labour-dispute-claim-drafter
description: Drafts pleadings in Indian labour disputes for workers or employers, covering conciliation applications, statements of claim and written statements before Industrial Tribunals and legacy Labour Courts, recovery of money due under the Industrial Relations Code, wage and bonus claims, and EPF and ESI appeals. Use when an advocate needs a claim for reinstatement and back wages, a reply to an industrial dispute, or a money-recovery application. Do not use for deciding the lawful route for an exit; use termination-retrenchment-analyst instead.
---

# Labour Dispute Claim Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce a pleading for the right forum, built on the record, with the reliefs and documents the forum expects.

## Jurisdiction gate

Identify the State or UT, the appropriate government (Central or State) for the establishment, and the forum. Under the IR Code, Industrial Tribunals replace Labour Courts, but legacy Labour Courts and Tribunals are reported to continue until the new Tribunals function. Check which forum is currently hearing matters in that State and district.

## Temporal gate

The IR Code is reported to be in force from 21 November 2025. If the termination, dues or dispute arose before that date, check the savings provisions and whether the Industrial Disputes Act route, or a pending reference, continues. Record the dates of termination, demand and conciliation.

## Required inputs

Mark as **blocking**:
- the party represented and the opposite party's correct legal name;
- the date and manner of termination or the dues claimed, with the period;
- the worker's designation, duties, wages and length of service;
- whether conciliation was sought, and its outcome or failure report;
- the documents available (appointment letter, pay slips, termination letter, attendance).

Also useful: the standing orders, any domestic inquiry record, and the worker's employment since termination.

## Method

1. Retrieve the current official text of the IR Code chapters on dispute resolution and recovery of money, the central or State rules, the forum's procedural rules and forms, and the EPF and ESI appeal provisions. Record the version and date.
2. Check limitation and pre-conditions: the period for raising an individual dispute, conciliation and the option of approaching the Tribunal directly, and the time for recovery applications. Compute deadlines with `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
3. Establish worker status and the "industry" question from the facts.
4. For a worker: draft the claim with facts, illegality of termination (no inquiry, no notice or compensation, last-in-first-out breach, victimisation), and reliefs (reinstatement, continuity, back wages). Plead non-employment since termination only on instructions.
5. For an employer: draft the written statement, preliminary objections (maintainability, limitation, non-worker status), and the case on merits, including any request to lead evidence on misconduct if no proper inquiry was held.
6. For money recovery: list each head, the period and the computation basis from the record.
7. For EPF and ESI appeals: identify the order, the appellate forum, any pre-deposit, and the grounds.
8. Search for and read current authority on back wages, reinstatement and gainful employment. Tag anything not read in full `[verify]`.

## Output

1. The draft pleading with verification and a list of documents.
2. A limitation and forum note.
3. A short note for the advocate on weak points and missing evidence.

## Guardrails and hand-offs

- Never invent wage records, attendance, dates or admissions.
- Never promise reinstatement or a back-wages percentage.
- For the underlying exit analysis, hand off to `termination-retrenchment-analyst`.
- Format the pleading with `court-pleading-formatter` if the forum's format is not supplied.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
