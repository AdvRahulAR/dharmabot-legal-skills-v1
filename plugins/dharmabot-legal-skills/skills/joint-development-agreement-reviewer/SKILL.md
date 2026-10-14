---
name: joint-development-agreement-reviewer
description: Drafts and reviews joint development and development agreements between landowners and developers in any Indian State or UT, covering area or revenue sharing, approvals, timelines, refundable deposits, the linked GPA, the landowner's promoter status under RERA, defaults, step-in rights, and stamp duty, GST and capital gains flags. Use when a lawyer asks to review a JDA for a landowner, negotiate a 60-40 area share, or draft a development agreement for a developer. Do not use to draft the GPA itself; use power-of-attorney-drafter.
---

# Joint Development Agreement Reviewer

Every output is a draft or review for an advocate enrolled in India to check.

## Purpose

Protect the client's side of a joint development, landowner or developer, by testing the economics, security, timelines and exits, and by flagging stamp, tax and RERA consequences early.

## Jurisdiction gate

Record the State or UT and the city or planning authority. Several States charge stamp duty on development agreements at conveyance or special rates, especially where possession passes; confirm the State rule. Identify the parties' tax residence; an NRI landowner also needs `nri-property-transaction-checker`.

## Temporal gate

Note the dates of signing, approval and completion. Capital gains timing for JDAs has specific provisions; the Income-tax Act, 2025 is reported to apply from 1 April 2026. Check which law governs each event and confirm the provision from the official text with a tax adviser.

## Required inputs

Mark as **blocking**:
- the draft JDA and the draft GPA, or the term sheet;
- which side the client is on;
- the land title documents or a title report;
- the sharing model (area or revenue), deposit and timelines.

Also useful: zoning and FSI details, approvals status, the developer's track record and RERA history, existing mortgages, and tenants or occupants.

## Method

1. Retrieve the current official text of the Transfer of Property Act, 1882 (including part performance), the Registration Act, 1908, the State stamp law entry for development agreements, the Real Estate (Regulation and Development) Act, 2016 and State rules, and the relevant GST and income-tax provisions. Open `references/india-state-statutes.md` as a starting point. Record the version and date.
2. Economics: sharing ratio, allocation method for units (which floors, which facing), car parks, common areas, sale of developer's share before completion, revenue-share accounting and audit rights.
3. Security for the landowner: refundable deposit, phased GPA, no mortgage of the landowner's share, escrow, bank guarantee, completion deadline with grace and penalties, and termination with reversion of land.
4. Developer protections: clean title warranties, approvals cooperation, no revocation of GPA without cause, step-in on landowner default.
5. RERA: the landowner may be treated as a promoter for their share; allocate registration, escrow and liability duties. Hand off to `rera-project-compliance-checker`.
6. GPA linkage: ensure the GPA's powers mirror and do not exceed the JDA. Hand off drafting to `power-of-attorney-drafter`.
7. Tax and stamp flags: stamp duty and registration (hand off to `state-stamp-duty-calculator`); GST on construction services exchanged for land; capital gains timing. Flag clauses handing over possession that may attract conveyance duty.
8. Dispute resolution, arbitration seat, and force majeure.

## Output

1. Clause-by-clause review table with redlines, or a full draft JDA.
2. Risk summary for the client, with the five most important negotiating points.
3. Tax and stamp issue list for the client's tax adviser.

## Guardrails

- Never give tax or stamp figures from memory.
- Never structure a JDA to hide a sale from stamp duty or tax.
- Do not certify title or approvals not supplied.
