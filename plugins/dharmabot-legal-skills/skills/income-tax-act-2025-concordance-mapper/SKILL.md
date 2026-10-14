---
name: income-tax-act-2025-concordance-mapper
description: Maps provisions, rules and forms of the Income-tax Act, 1961 and Income-tax Rules, 1962 to the Income-tax Act, 2025 and its rules, noting wording changes, the tax-year concept, and which Act governs a given year or proceeding under the transition provisions, working from the official concordance where available. Use when a lawyer asks what the new section is for an old one, whether a 1961 Act citation still works, or which Act applies to a pending assessment. Do not use to draft a notice reply; use income-tax-notice-reply-drafter.
---

# Income-tax Act 2025 Concordance Mapper

Every output is a draft research note for an advocate or chartered accountant in India to check.

## Purpose

Give a reliable old-to-new (or new-to-old) map of income-tax provisions, with the wording differences that matter and a clear statement of which Act governs.

## Jurisdiction gate

Confirm the question concerns Indian income tax. Treaty provisions are not mapped here; route treaty questions to `dtaa-withholding-analyst`.

## Temporal gate

The Income-tax Act, 2025 came into force on 1 April 2026, with new rules from the same date; confirm both from the Gazette and the department's website. Record the year (assessment year or tax year) and the date of the proceeding. Apply the repeal and savings provisions to say which Act governs. Later amendments to either Act may change a mapping; note the Finance Act version used.

## Required inputs

Mark as **blocking**:
- the provisions, rules or forms to map, exactly as cited;
- the year and proceeding they relate to.

Also useful: the order or notice in which they appear, and the purpose of the mapping (reply, appeal, opinion, internal training).

## Method

1. Retrieve the official text of both Acts, both sets of rules, and the official concordance or navigator tables published by the income-tax department or CBDT. Record the version and date of each.
2. For each provision, find the corresponding provision in the official table. If none exists, search both texts for the operative words and propose a mapping marked unverified.
3. Compare wording side by side. Note changes in scope, conditions, thresholds, defined terms and the move from previous year and assessment year to tax year.
4. Check whether rules and forms changed number or content, and whether old forms remain valid for pending matters.
5. State which Act governs the year or proceeding under the savings provisions, with the reasoning.
6. Note any early CBDT circular, FAQ or ruling on the new provision. Search for and read it; tag unread material `[verify]`.

## Output

1. A concordance table: 1961 provision, 2025 provision, source of mapping (official or proposed), key wording changes, confidence.
2. A short note on which Act governs the matter and why.
3. A list of mappings marked unverified.

## Guardrails and hand-offs

- Never present a proposed mapping as official.
- Never paraphrase a provision as if quoting it; quote only from the retrieved text.
- Run `citation-verifier` on the final table; notice replies go to `income-tax-notice-reply-drafter`.
