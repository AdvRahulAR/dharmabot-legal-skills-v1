---
name: contract-summariser
description: Produces a neutral one-page summary of a single contract for business teams, or a tabular abstraction across many contracts with one row per document and agreed columns, each cell pinned to the clause relied on and blanks or ambiguities marked. Works for contracts under Indian or other law. Use when someone asks to summarise a contract, abstract leases or vendor agreements into a table, or pull key terms from a batch of documents. Do not use to give advice or propose redlines; use playbook-contract-reviewer instead.
---

# Contract Summariser

Every output is a draft summary for a lawyer or reviewer to check against the source documents before anyone relies on it.

## Purpose

Tell a reader accurately what a contract says, or let a team compare many contracts at a glance, without interpretation creeping in.

## Jurisdiction gate

Note the governing law of each contract. The skill summarises text and does not apply law, so it works for any jurisdiction. Where a column needs a legal judgment (for example "is the lock-in enforceable"), stop and refer that column to `playbook-contract-reviewer`, or to `cross-border-contract-reviewer` for foreign-law contracts.

## Required inputs

Mark as **blocking**:
- the contracts, complete with schedules, amendments and side letters;
- for a table, the columns wanted (or agreement to the default set below);
- the audience (business team, lawyer, board).

Also useful: a naming convention for documents, the date for "current" status, and whether amendments should be consolidated.

## Method

1. Confirm the source set: retrieve the official or executed copies (signed, stamped versions, not drafts) and record each file name, version and date. If only drafts are given, label every output "based on unsigned draft".
2. **Inventory.** List each document, its parties, date and type. Flag missing pages, unsigned copies, illegible scans and missing schedules.
3. **Amendments.** Link each amendment to its base agreement. Summarise the current position and note what changed. For complex histories, hand off to `contract-amendment-drafter`.
4. **Single contract summary.** One page: parties; purpose; term and renewal; price and payment; key obligations of each side; termination rights and notice; liability and indemnity; governing law and disputes; unusual clauses.
5. **Table abstraction.** Default columns: document · parties · date · term · renewal · price · escalation · payment terms · lock-in · termination notice · governing law. Use one row per document. Each cell carries a clause reference.
6. **Quoting rule.** Quote short operative words where paraphrase could mislead (for example "may" versus "shall"). Do not normalise dates or amounts without showing the source.
7. **Blanks and ambiguity.** Use "Not stated" when the contract is silent and "Ambiguous, see clause X" when wording conflicts. Never fill a blank by inference.
8. **Quality check.** Re-read a random sample of cells against the source, and every cell for high-value columns (price, term, notice).

## Output

1. A one-page summary per contract, or a table (Markdown or CSV as asked).
2. A notes section listing missing documents, ambiguities and conflicts.
3. A coverage line: documents received, abstracted and excluded with reasons.

## Guardrails and hand-offs

- Summarise only; do not advise, recommend or rank risk.
- Never invent a term or fill a blank by assumption.
- Keep client documents confidential; do not include them in public examples.
- For dates and obligations to track, hand off to `contract-obligations-tracker`; for large review pods, `lpo-document-review-coder`.
