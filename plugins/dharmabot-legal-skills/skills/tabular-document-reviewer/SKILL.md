---
name: tabular-document-reviewer
description: Runs a structured review over a set of documents of any type (notices, FIRs, judgments, invoices, correspondence, KYC and due-diligence files), with one row per document and one column per question, every cell citing the document page or paragraph or marked not found, and output as CSV or XLSX for spot-checking. Use when a lawyer says "put these in a spreadsheet", "extract the same fields from all these files" or "review this bundle as a table". Do not use for contract term abstraction (use contract-summariser) or a foreign firm's coding protocol (use lpo-document-review-coder).
---

# Tabular Document Reviewer

Every output is a draft review table for the supervising advocate to spot-check.

## Purpose

Turn a pile of documents into a sortable table where every answer can be traced to a page or paragraph, so a lawyer can check it fast and rely on it.

## Jurisdiction gate

The method is neutral. Record the jurisdiction and statute behind any legal question in a column (for example whether a notice meets a statutory requirement), because the column definition must follow that law. Where a column needs a legal test, state the test in the column note and flag it for the advocate.

## Required inputs

Mark as **blocking**:
- the document set, readable (searchable text or OCR of acceptable quality);
- the questions, one per column, each with its answer type (date, amount, yes/no, text, choice list);
- the output format (CSV or XLSX).

Also useful: a document index, sample answers for two or three documents, and confidentiality rules for the set.

## Method

1. Retrieve the current official text of any statute, rule or form a column tests against, and record version and date. Put the test in the column note.
2. Build the column schema: question, answer type, allowed values, "not found" rule, and source-citation field. Confirm it with the user on a sample of two or three documents before running the full set.
3. Index the documents: assign a stable document ID, file name, page count and document type. Flag unreadable, duplicate, password-protected or non-English documents.
4. For each document and column, find the answer in the text. Record:
   - the answer in normalised form (dates as DD-MM-YYYY, amounts in figures with currency);
   - the citation as file name, page and paragraph, with a short quoted snippet;
   - a confidence flag (high, medium, low) and a note for anything inferred.
5. If the answer is not in the document, write NOT FOUND. Never fill a cell from another document or from assumption.
6. Run quality checks: blank cells, conflicting answers within a document, amounts in words and figures that differ, dates out of sequence, and low-confidence cells.
7. Draw a spot-check sample (all low-confidence cells, plus a random sample of the rest) for human checking.
8. Write the table with the csv module or openpyxl. Freeze the header row and keep a column-notes sheet.

## Output

1. The CSV or XLSX: document ID, file name, type, then for each question an answer column, a citation column and a confidence column.
2. A column-notes sheet with each question, answer type and legal test.
3. An exceptions list: unreadable, duplicate and conflicting documents.
4. The spot-check sample and a short method note.

## Guardrails and hand-offs

- No legal conclusions across the set. The table records what each document says.
- Every cell has a citation or NOT FOUND. No exceptions.
- Keep client data inside the agreed environment; use `client-data-redaction-checker` before an external AI tool.
- Contract abstraction goes to `contract-summariser`; chronologies to `litigation-chronology-builder`; foreign review protocols to `lpo-document-review-coder`; deal diligence reports to `ma-due-diligence-analyst`.
