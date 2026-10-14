---
name: roc-secretarial-compliance-checker
description: Checks recurring and event-based compliance of companies and LLPs under the Companies Act 2013 and the LLP Act 2008, covering annual returns, financial statements, DIR-3 KYC, director disclosures, statutory registers, significant beneficial ownership, charges, auditor appointment and MSME and deposit returns. Use when a client asks what ROC filings are due or overdue, wants a secretarial audit-style gap list, or faces late fees, compounding or adjudication. Do not use to draft the resolutions themselves; use board-meeting-documents-drafter instead.
---

# ROC and Secretarial Compliance Checker

Every output is a review for an advocate, company secretary or chartered accountant in India to check.

## Purpose

Produce an evidence-based list of what the entity has filed, what is due and what is overdue, with the exposure for each gap and the route to cure it.

## Jurisdiction gate

- Confirm the entity is an Indian company or LLP, and its class (private, public, listed, OPC, small company, Section 8, LLP).
- Note the ROC jurisdiction from the registered office.
- For listed companies, add SEBI LODR items through `sebi-lodr-disclosure-checker`.

## Temporal gate

Record the financial year under review. Forms, fees and thresholds change; check which version applied on each due date. Check whether any recent amendment (including decriminalisation changes) altered the penalty for a default.

## Required inputs

- **Blocking:** CIN or LLPIN, and the financial year or period to review.
- **Blocking:** the MCA master data and filing history (the V3 portal download or a CS's list). Without evidence, the skill lists items as "not evidenced", not as "filed".
- Useful: board and general meeting minutes, statutory registers, auditor appointment papers, charge documents, loans and deposits, MSME vendor dues, and the SBO declarations received.

## Method

1. Retrieve the current official text of the Companies Act 2013, the LLP Act 2008, the relevant rules, and the current e-form list and fee rules from the MCA portal. Record the version and date.
2. Build the annual calendar for the entity's class. Typical items: AGM; financial statements and annual return filings; DIR-3 KYC; director disclosures of interest and non-disqualification at the first board meeting of the year; auditor appointment filing; MSME and deposit-related returns; LLP Form 8 and Form 11. Confirm each form, trigger and deadline from the source.
3. Add event-based items found in the record: allotments, transfers, director and KMP changes, registered-office shifts, charges created or satisfied, SBO declarations, alteration of MOA or AOA, and resolutions that must be filed.
4. Check statutory registers and records for existence and currency: members, directors and KMP, charges, contracts with interested parties, loans and investments, and minutes books.
5. Match each item against evidence. Grade it: complied, complied late, overdue, not evidenced.
6. For each gap state the exposure: additional fees, penalty or adjudication, director disqualification risk, strike-off risk, and whether compounding or condonation is available. Cite the retrieved provision.
7. Propose a cure sequence, starting with items that block others (for example pending annual filings that block other forms).

## Output

1. Compliance status table: item · source · due date · status · evidence · exposure.
2. Cure plan in order, with owner and documents.
3. A list of documents to request from the client.
4. A recurring calendar handed to `compliance-calendar-builder`.

## Guardrails and hand-offs

- Do not mark anything as filed without evidence.
- Do not state a late fee or penalty figure without citing the current rule; otherwise tag `[verify]`.
- Do not file forms or certify; a practising professional does that.
- Resolutions and minutes needed for a cure go to `board-meeting-documents-drafter`.
