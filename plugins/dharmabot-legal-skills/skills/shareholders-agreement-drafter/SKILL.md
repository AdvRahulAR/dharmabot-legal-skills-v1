---
name: shareholders-agreement-drafter
description: Drafts and reviews share subscription agreements, shareholders' agreements and joint venture agreements under Indian law, covering subscription mechanics and conditions precedent, investor rights, transfer restrictions, governance and reserved matters, exits, deadlock and alignment with the articles of association under the Companies Act 2013, with FEMA pricing and reporting flags. Use when a lawyer needs an SSA, SHA or JV agreement drafted or marked up after a term sheet. Do not use to review the term sheet itself; use vc-term-sheet-reviewer instead.
---

# Shareholders Agreement Drafter

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Turn agreed commercial terms into definitive SSA, SHA or JV documents that are enforceable against the shareholders and, through the articles, against the company.

## Jurisdiction gate

- Confirm the company is Indian and the agreements are governed by Indian law. Foreign-law side letters or holding-company documents are marked "to be confirmed by counsel qualified in [jurisdiction]".
- Identify non-resident parties. FEMA pricing, permitted instruments, sectoral caps and reporting apply; flag for `india-entry-fema-structuring-analyst`.
- Record the State of execution for stamp duty.

## Required inputs

- **Blocking:** the signed or agreed term sheet; the parties and which one the client is; the instrument and amount.
- **Blocking:** the current AOA, cap table and any existing SHA that must be amended or terminated.
- Useful: due diligence findings, ESOP pool terms, investor's standard form, and the investor's regulatory status (for example AIF, FVCI, foreign corporate).

## Method

1. Retrieve the current official text of the Companies Act provisions on issue and transfer of shares, the Share Capital Rules, the FEMA Non-Debt Instruments Rules, and the applicable State stamp law. Record the version and date.
2. **SSA:** subscription mechanics, CPs (approvals, valuation report, AOA adoption, key employee agreements, diligence fixes), closing actions and deliverables, warranties from the company and founders, indemnity with limits, use of proceeds, and post-closing covenants (allotment and filings within the prescribed time).
3. **SHA or JV:** board composition and quorum; reserved matters at board and shareholder level; information rights; pre-emption; transfer restrictions (lock-in, ROFR or ROFO, tag, drag); anti-dilution; liquidation preference; exit (IPO, strategic sale, put or call options, with FEMA limits); founder vesting and non-compete during engagement; deadlock; events of default; termination; dispute resolution and seat.
4. Check enforceability: transfer restrictions in a public company; whether rights against the company must be in the AOA; FEMA bar on assured returns to non-residents; and the Contract Act restraint-of-trade limit.
5. Draft the AOA amendments that mirror the SHA and a conflict clause.
6. List corporate and regulatory steps for closing; hand issue mechanics to `securities-issuance-compliance-checker`.
7. Compute stamp duty on the agreements and the shares with `state-stamp-duty-calculator`.

## Output

1. SSA draft.
2. SHA or JV agreement draft.
3. Restated AOA or amendment schedule.
4. CP and closing list, and an open-issues list.

## Guardrails and hand-offs

- Do not change agreed commercial terms; flag drafting conflicts as questions.
- Do not value the shares; a registered valuer does that.
- Do not draft put options or guaranteed returns for non-residents without flagging FEMA pricing rules.
- Term-level negotiation goes back to `vc-term-sheet-reviewer`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
