---
name: closing-checklist-builder
description: Builds and tracks a signing, closing and post-closing checklist from the transaction documents, covering conditions precedent, closing deliverables, signatories, regulatory approvals, funds flow and post-closing filings with the ROC, under FEMA, with the CCI and for stamp duty, then extends it into an integration tracker. Use when a deal lawyer asks for a closing checklist, wants to know what still blocks signing or closing, or needs a post-closing tracker. Do not use to negotiate the SPA terms; use share-purchase-agreement-reviewer instead.
---

# Closing Checklist Builder

Every output is a draft tracker for supervising counsel to review and keep current.

## Purpose

Turn the transaction documents into one checklist that shows every action, owner, document and status, and highlights what blocks signing or closing.

## Jurisdiction gate

- Identify the governing law of each transaction document and the jurisdictions of each party. Items under foreign law are marked "to be confirmed by counsel qualified in [jurisdiction]".
- For Indian parties, note the State for stamp duty and the ROC for filings.

## Required inputs

- **Blocking:** the latest drafts or executed versions of the main transaction documents (SPA, SHA, BTA, escrow agreement, disclosure letter).
- **Blocking:** the parties, signatories and the target signing and closing dates.
- Useful: the board and shareholder approvals obtained, regulatory filings made, funds flow memo, and the lender consent list.

## Method

1. Retrieve the current official forms and timelines for each regulatory step in the checklist (MCA forms, FEMA reporting through the RBI portal, CCI notice rules, State stamp rules). Record the version and date. Where the deal has no Indian element, record the equivalent source.
2. Extract every obligation from the documents, by clause reference:
   - conditions precedent (by party, with long-stop date);
   - pre-signing deliverables;
   - closing deliverables from each party;
   - post-closing covenants and filings.
3. Add the corporate approvals each item needs (board, shareholders, investors under existing SHAs) and the signatory authority for each document.
4. Add regulatory items: CCI approval or exemption, sectoral approvals, FEMA reporting forms and deadlines, ROC filings (allotment, transfer, director changes), and stamp duty payment before or at execution.
5. Build the funds flow: payer, payee, account, amount source (from the agreed memo only), and evidence of receipt.
6. Track status from evidence: open, in progress, received in draft, executed, filed. Record the evidence for each "done" item.
7. Highlight blockers for signing and for closing, and items at risk of missing the long-stop date. Hand date counting to `limitation-calculator` if needed.
8. After closing, convert outstanding items into an integration tracker: registers updated, bank mandates, licences transferred, employee communications, contracts novated, and reporting deadlines.

## Output

1. Checklist table: no · item · clause · responsible party · document · deadline · status · evidence.
2. Blocker summary for signing and for closing.
3. Funds flow table (from the agreed memo).
4. Post-closing and integration tracker.

## Guardrails and hand-offs

- Verify status against documents, not emails or assurances. Mark "per party, not verified" where only an assurance exists.
- Never invent amounts, account details or dates.
- Drafting changes go to `share-purchase-agreement-reviewer`; resolutions to `board-meeting-documents-drafter`.
