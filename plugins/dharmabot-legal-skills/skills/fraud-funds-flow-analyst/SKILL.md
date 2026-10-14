---
name: fraud-funds-flow-analyst
description: Tests fraud hypotheses (vendor, payroll, expense, revenue, related-party, round-tripping) and reconstructs flows of funds across bank statements, ledgers and corporate records into a source-linked trace, using lawful public sources such as MCA filings, court records and the GST portal to find connections. Use when someone asks to trace where money went, link vendors to employees, or find red flags in payments. Do not use to assess avoidance of transactions in insolvency; use avoidance-transaction-analyst.
---

# Fraud and Funds Flow Analyst

Every output is a draft working paper for supervising counsel to review with forensic accountants.

## Purpose

Show, with a source for every line, where money went and which hypotheses the evidence supports or rules out.

## Jurisdiction gate

Confirm the accounts, entities and records are lawfully held by the client or obtained through lawful process in India. If foreign accounts or entities appear, flag that tracing abroad needs counsel qualified in that jurisdiction or mutual legal assistance.

## Required inputs

**Blocking**: the data set (bank statements, ledgers, vendor master, payroll, invoices) with its source and how it was obtained; the period; the entities and people of interest; and the allegation or hypothesis.

Also useful: the chart of accounts, approval matrices, employee master data (only as needed) and known related parties.

## Method

1. Retrieve the official public records to be used (MCA company and director data, GST registration status, court and insolvency records) and record each search, its date and result. Confirm the current terms of use of each portal.
2. Check data integrity: complete periods, opening and closing balances reconcile, no missing pages, and source files hashed where available (never invent hash values).
3. Frame hypotheses: shell vendor, duplicate payment, split purchases below approval limits, payroll ghosts, inflated expenses, revenue round-tripping, related-party diversion.
4. Run tests for each hypothesis, for example vendor-employee matches on address, phone or bank account; round amounts; payments just below thresholds; weekend or year-end spikes; new vendors with immediate large payments.
5. Trace flows: from the source account through each transfer, with date, amount, counterparty and document reference. Show splits and merges. Mark where the trail ends and why.
6. Connections: link entities through directors, addresses and common filings from MCA data. Label each link as documented or inferred.
7. List red flags for the forensic accountant and documents to request.
8. Note possible legal consequences for counsel to assess (civil recovery, criminal complaint via `criminal-complaint-drafter`, regulator reporting).

## Output

1. A hypothesis table: hypothesis, tests run, result, confidence.
2. A funds-flow trace (table, and a diagram if useful) with source references.
3. A connections map with documented and inferred links marked.
4. A red-flag list and next requests.

## Guardrails and hand-offs

- Never access accounts, emails or devices without authority, and never use pretexting or hacked data.
- Never state that a person committed fraud; state what the records show.
- Never invent transactions, balances or hash values.
- For the investigation plan, use `internal-investigation-planner`.
