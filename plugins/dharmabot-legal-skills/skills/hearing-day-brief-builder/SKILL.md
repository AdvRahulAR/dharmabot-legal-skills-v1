---
name: hearing-day-brief-builder
description: Builds a one-page brief for each matter on an Indian court's daily cause list for the appearing advocate, covering stage, last order and compliance due, the relief sought today, key points, authorities with pinpoint paragraphs, likely questions from the bench and a fallback request. Use when an advocate says tomorrow's board has several matters and wants short briefs from the case files, or a junior must appear on a senior's brief. Do not use for full written submissions; use written-submissions-drafter.
---

# Hearing Day Brief Builder

Every output is a draft brief for the appearing advocate to review before the hearing.

## Purpose

Let an advocate walk into court with every listed matter on one page: what happened last, what is wanted today, how to get it, and what to ask for if the bench will not hear it.

## Jurisdiction gate

Confirm each matter is before an Indian court or tribunal. Record the court, court hall, item number and bench. Note matters where the bench composition changed since the last date.

## Required inputs

Mark as **blocking**:
- the cause list or board for the day, with item numbers;
- for each matter, the case file or at least the last two orders and the main pleading.

Also useful: the client's instructions for the day, opposing counsel, pending compliance, and any notes from the last appearance.

## Method

1. Retrieve the court's official cause list and the last orders from the court's website or the eCourts services portal. Record the date and time retrieved. Flag any mismatch with the file.
2. For each matter, read the last order. Extract directions, compliance due and who must comply. Check whether compliance is done.
3. State the stage (admission, notice, pleadings, evidence, arguments, orders, execution) and what is realistically achievable today.
4. Write two or three key points the advocate must make, each tied to a page of the paper book.
5. List authorities already in the file with pinpoint paragraphs. Do not add new ones without reading them. Send every authority to `citation-verifier`.
6. Anticipate two or three questions the bench is likely to ask (delay, maintainability, alternative remedy, compliance) with short answers.
7. Set a fallback: a short date, continued interim protection, or directions for pleadings.
8. Order the briefs by court hall and item number, and flag clashes between halls.

## Output

For each matter, one page:
1. Header: court, item, case number, parties, for whom, opposing counsel.
2. Stage and last order (with date) and compliance status.
3. Relief sought today and key points with page references.
4. Authorities with pinpoint paragraphs.
5. Likely questions and answers.
6. Fallback request.

Then a one-page running order for the day with clashes flagged.

## Guardrails and hand-offs

- Never invent an order, date, page reference or authority. Mark gaps "not in file".
- Every authority goes through `citation-verifier` before use. Citing unverified AI-generated judgments has been reportedly held to be misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank, 2026 INSC 668; reported; confirm).
- Full written submissions go to `written-submissions-drafter`.
- New dates and compliance go to `matter-deadline-tracker`.
- Keep briefs confidential to the chamber.
