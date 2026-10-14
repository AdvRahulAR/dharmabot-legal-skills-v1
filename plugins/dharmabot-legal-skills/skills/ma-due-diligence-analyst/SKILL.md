---
name: ma-due-diligence-analyst
description: Plans and performs legal due diligence on Indian targets for acquisitions and investments, covering request lists, virtual data room review by workstream (corporate, contracts, employment, property, IP, litigation, regulatory, tax, data protection), issue extraction with severity, material contract and disclosure schedules, and a red-flag report with conditions precedent and indemnity asks. Use when a lawyer asks for a DD request list, a VDR review or a red-flag report. Do not use to draft the SPA itself; use share-purchase-agreement-reviewer instead.
---

# M&A Due Diligence Analyst

Every output is a review for supervising counsel to check before it goes to the client.

## Purpose

Find the legal risks in a target that affect price, structure, conditions or protection, and present them so the deal team can act on them.

## Jurisdiction gate

- Confirm the target and its material subsidiaries are Indian, and list the States where they operate, own property or employ staff. Property, labour, stamp and local licences vary by State.
- Foreign subsidiaries or foreign-law contracts need counsel qualified there; mark those items.

## Required inputs

- **Blocking:** the deal type (share purchase, business transfer, investment), the target entities, and the scope and materiality threshold agreed with the client.
- **Blocking for review:** access to the data room or the documents; the review cannot report on what it has not seen.
- Useful: the buyer's concerns, the sector, the cut-off date, and any management presentation.

## Method

1. Retrieve the current official text of the statutes and regulator portals relevant to the sector, and check MCA master data, charge records and court and tribunal case-status portals for the target. Record each source and the date checked.
2. Prepare the request list by workstream, sized to the sector and deal. Include: constitutional and cap table records; ROC filings; approvals and licences; material contracts with change-of-control clauses; borrowings and security; employees, ESOPs and labour registrations; property titles and leases; IP; litigation and notices; tax (flag for a tax adviser); data protection and cyber; and anti-bribery.
3. Review the data room by workstream. For each document record: what it is, parties, date, term, key clauses (change of control, assignment, exclusivity, termination, liability caps), and gaps (unsigned, unstamped, expired).
4. Extract issues into a log: issue · document · severity (red, amber, green) · consequence · recommended action (price, CP, specific indemnity, covenant, walk-away).
5. Build the material contracts schedule and the disclosure schedule cross-reference.
6. Run public checks: litigation searches, charges, director disqualification, regulatory orders. Record what was searched and when.
7. Write the red-flag report: executive summary, top issues, structure implications, CPs and indemnity asks.
8. Record every request not answered and every document not provided.

## Output

1. DD request list (tracker format).
2. Issue log with severity.
3. Material contracts schedule.
4. Red-flag report with CPs, covenants and indemnity asks.
5. List of open requests and limitations of the review.

## Guardrails and hand-offs

- Never treat an unprovided document as clean.
- Do not quote figures, holdings or dates not shown in the documents.
- Keep data room content confidential and within the review team.
- Property titles go to `property-title-diligence-analyst`; contract summaries at scale to `contract-summariser`; findings feed `share-purchase-agreement-reviewer`.
