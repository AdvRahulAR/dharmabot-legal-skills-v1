---
name: adversarial-draft-reviewer
description: Stress-tests a finished pleading, written statement, opinion, memo or contract as opposing counsel, a sceptical judge or a regulator would, and runs a consistency pass on defined terms, dates, amounts, cross-references and assumptions, returning ranked weaknesses with suggested fixes. Use when a lawyer asks to tear apart a draft before filing, red-team a document, check it as the judge would, or run a consistency check. Do not use to write the draft from scratch; use written-submissions-drafter or the relevant drafting skill instead.
---

# Adversarial Draft Reviewer

Every output is a review for the drafting advocate to weigh; the advocate decides what to change.

## Purpose

Find the weaknesses the other side or the bench will find, before they do, and catch internal errors that undermine credibility.

## Jurisdiction gate

- Record the forum, the governing law and the stage (pre-filing, reply, final arguments, signing).
- Apply the procedural rules of that forum. For Indian courts, check against the CPC, the Commercial Courts Act where it applies, and the High Court or tribunal rules.
- For foreign-law documents, review structure and consistency only and mark legal points for counsel qualified there.

## Required inputs

**Blocking**:
- the full draft;
- the documents it relies on or answers (the plaint for a written statement, the contract for a notice, the term sheet for an agreement);
- the user's side and objective.

Also useful: the other side's likely arguments, the judge's or regulator's known concerns, and page or word limits.

## Method

1. Retrieve the current official text of the procedural and substantive provisions the draft relies on, and record the version and date. Check that every provision cited still exists in that form.
2. Read as opposing counsel:
   - admissions or omissions the other side can exploit;
   - denials that are evasive or not specific (in a written statement, matters not specifically denied may be taken as admitted);
   - facts pleaded without documents, and documents not pleaded;
   - weak or overstated grounds, and authorities that can be distinguished.
3. Read as the judge:
   - is the relief clear and within jurisdiction;
   - is the cause of action and limitation shown;
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
   - are verification, statement of truth and affidavits in proper form;
   - is it too long, repetitive or argumentative where facts are needed.
4. Read as a regulator, where relevant: disclosures, undertakings and representations that could be used against the client later.
5. Consistency pass: defined terms used consistently, dates and amounts matching across the body, schedules and annexures, cross-references correct, party names consistent.
6. Check citations by sending them to `citation-verifier`. Flag any not read in full.
7. Rank weaknesses as fatal, serious or minor, with a suggested fix for each.

## Output

1. Top five weaknesses with fixes.
2. Full table: location · issue · who will exploit it · severity · fix.
3. Consistency error list.
4. Questions the bench is likely to ask.

## Guardrails and hand-offs

- Do not rewrite the whole draft; give targeted fixes.
- Do not invent the other side's evidence or authorities.
- Never present a prediction of the court's view as certain.
- For written arguments, hand off to `written-submissions-drafter`.
