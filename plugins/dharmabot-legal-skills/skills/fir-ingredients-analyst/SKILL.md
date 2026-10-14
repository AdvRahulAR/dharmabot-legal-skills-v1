---
name: fir-ingredients-analyst
description: Tests the facts alleged in an Indian FIR, complaint or charge-sheet against the statutory ingredients of each offence charged under the BNS (or IPC) and related laws, and shows which ingredients are supported, missing or contradicted. Use when an advocate wants an offence-by-offence analysis for bail, discharge, quashing or a reply, or asks "do these facts make out the offence". Do not use for drafting the application itself; use the drafting skills afterwards.
---

# FIR Ingredients Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Break each alleged offence into its legal ingredients and check each one against what the FIR, complaint or charge-sheet actually says, so the advocate can see where the prosecution case is thin.

## Jurisdiction gate

Confirm the matter is under Indian law and identify the State. Note any special statute charged alongside the general code.

## Temporal gate

Note the offence date. If it is before 1 July 2024, the IPC ingredients may govern; if unsure, run `crpc-bnss-transition-analyst` first.

## Required inputs

Mark as **blocking**: the full text of the FIR or complaint (or the charge-sheet and witness statements, if filed), and the sections invoked.

Also useful: which side the advocate acts for, and the purpose (bail, discharge, quashing, defence, prosecution).

## Method

1. Retrieve the official text of each section invoked, including definitions it relies on (for example "dishonestly", "fraudulently", "public servant") and any explanation or exception.
2. Split each offence into numbered ingredients, including the mental element.
3. For each ingredient, quote the exact words from the record that support it, with a page or paragraph reference. If nothing supports it, say "no allegation". If the record contradicts it, quote the contradiction.
4. Identify sections that appear to be invoked without any supporting allegation, and offences the facts may support but that are not invoked (neutrally, without advising either side to add charges).
5. Note facts that point to a civil dispute presented as a criminal one, delay in lodging the FIR, and internal inconsistencies, but only where the record shows them.
6. Where courts have interpreted an ingredient, search for, read and cite current authority. Tag anything not read in full `[verify]`.

## Output

For each offence, a table: ingredient · supporting words from the record (with reference) · assessment (supported / no allegation / contradicted). Then a short summary ranking the weakest offences, and a list of documents that would change the analysis.

## Guardrails and hand-offs

- Quote the record exactly; never paraphrase an allegation into something stronger or weaker.
- Do not comment on guilt or innocence or on witness credibility beyond what the record shows.
- Hand off to `bnss-bail-application-drafter` for bail, and to the user's preferred skill for discharge or quashing.
