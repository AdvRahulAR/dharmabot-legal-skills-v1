---
name: rbi-master-direction-mapper
description: Maps citations to repealed or consolidated RBI circulars and older master directions in policies, contracts and opinions to the entity-wise Master Directions of the November 2025 consolidation, with paragraph-level successors, substantive changes and items with no successor. Use when a bank, NBFC or fintech says its credit or KYC policy or a contract still cites old RBI circulars. Do not use to draft policy redlines (use regulatory-change-impact-analyst) or for licensing advice (use financial-services-licensing-analyst).
---

# RBI Master Direction Mapper

Every output is a draft concordance for supervising counsel or the compliance officer to check.

## Purpose

Turn a list of legacy RBI citations into a verified table of current successors, so documents stop relying on repealed text.

## Jurisdiction gate

Confirm the citations are to the Reserve Bank of India and identify the regulated entity type (commercial bank, small finance bank, payments bank, co-operative bank, NBFC layer, ARC, credit information company, AIFI). The consolidation was entity-wise, so the same old circular may map to different directions for different entity types. SEBI, IRDAI or IFSCA citations are out of scope; list them separately.

## Temporal gate

- In late November 2025 RBI reportedly issued about 240 entity-wise Master Directions (reports give 238 or 244) consolidating more than 9,000 circulars, with a list of withdrawn circulars. Confirm the date, effective date and savings clause from rbi.org.in.
- Reported savings language preserves actions taken under repealed circulars. Check the exact wording before advising on past transactions.
- Record the date of each document being mapped. A 2023 opinion was correct when written; the map shows what has changed since.
- Check for amendments to each Master Direction after issue.

## Required inputs

Mark as **blocking**: the list of citations (circular number, date and subject) or the documents containing them; and the regulated entity type.

Also useful: the purpose of each citation in the document (definition, threshold, process), and whether the entity is in a specific NBFC layer.

## Method

1. Retrieve the current official texts from rbi.org.in: the consolidated Master Direction(s) for the entity type, the list of repealed circulars, and any later amendments. Record version and date.
2. Normalise each citation: circular reference number, date, department, subject. Flag citations that are incomplete or appear wrong.
3. Check whether each item appears on the repealed list. If not, check whether it is still in force on its own.
4. Find the successor paragraph in the consolidated direction by subject, not by assumed numbering. Read the paragraph in full.
5. Compare old and new text. Classify the change: carried over unchanged; reworded only; substantive change (scope, threshold, timeline, approval); or no successor.
6. For "no successor", check whether the requirement was dropped, moved to another direction, or moved to a FAQ or a statute.
7. Note where the consolidated direction cross-refers to another direction (for example KYC or outsourcing).
8. Mark each mapping "verified on rbi.org.in on [date]" or `[verify]` if the text could not be opened.

## Output

1. Concordance table: old citation · subject · status · successor direction and paragraph · change type · note.
2. A list of substantive changes for `regulatory-change-impact-analyst`.
3. A list of items with no successor and what that means for the document.

## Guardrails and hand-offs

- Never guess a paragraph number. If it cannot be read, say so.
- Do not treat secondary summaries as the source; use them only to find the text.
- Do not advise on whether the entity needs a licence; hand off to `financial-services-licensing-analyst`.
- Run `citation-verifier` before delivery.
