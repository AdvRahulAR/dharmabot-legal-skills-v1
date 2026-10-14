---
name: share-purchase-agreement-reviewer
description: Drafts and reviews Indian-law acquisition documents, including share purchase agreements, business transfer and slump-sale agreements, warranties and indemnities, limitations, escrow and holdbacks, W&I insurance, conditions precedent and non-compete clauses, with deal-structure, stamp duty and tax flags. Use when a lawyer asks to review or mark up an SPA or BTA, negotiate indemnity caps and escrow, or compare share and asset deals. Do not use for foreign-law governed documents; use cross-border-contract-reviewer instead.
---

# Share Purchase Agreement Reviewer

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Produce a markup or first draft of an acquisition agreement that protects the client's side, reflects the due diligence findings, and is enforceable under Indian law.

## Jurisdiction gate

- Confirm the governing law is Indian and identify the dispute forum (courts or arbitration seat). If the agreement is governed by foreign law, hand off to `cross-border-contract-reviewer`.
- Record the State of execution and of the target's registered office for stamp duty.
- Any non-resident buyer or seller brings FEMA pricing and reporting; flag for `india-entry-fema-structuring-analyst`.

## Required inputs

- **Blocking:** which side the client is on; the agreement or term sheet; the deal type (shares, business transfer, slump sale, asset purchase).
- **Blocking for warranty and indemnity work:** the due diligence findings or red-flag report.
- Useful: price mechanics (locked box or completion accounts), escrow agreement, disclosure letter, W&I policy terms, and the target's listing status.

## Method

1. Retrieve the current official text of the laws that bite on the deal: the Indian Contract Act 1872 (including the restraint-of-trade provision), the Specific Relief Act 1963, the Companies Act 2013 transfer provisions, the applicable State stamp law, and FEMA rules if relevant. Record the version and date.
2. Check structure: share deal versus business transfer or slump sale. Note transfer of licences, contracts, employees and property in each, and flag tax and stamp consequences for a tax adviser.
3. Review clause by clause, from the client's side:
   - parties, recitals and definitions (Business, Losses, Knowledge, Material Adverse Change);
   - price, adjustments, escrow and holdback, and earn-out mechanics;
   - conditions precedent and long-stop date, including CCI, SEBI, sectoral and lender consents;
   - conduct of business between signing and closing;
   - closing deliverables;
   - warranties (fundamental, business, tax), disclosure standard and knowledge qualifiers;
   - indemnities: general and specific, de minimis, basket, caps, time limits, exclusions, conduct of claims, and remoteness;
   - non-compete and non-solicit: test reasonableness and the sale-of-goodwill exception under the Contract Act;
   - termination, governing law and dispute resolution.
4. Map each red-flag item from diligence to a contractual protection.
5. Check the enforceability points: penalty versus liquidated damages; indemnity and limitation interplay; FEMA limits on deferred consideration and indemnity payments by non-residents (confirm current rules).
6. Compute stamp duty with `state-stamp-duty-calculator`.
7. Draft a negotiation issues list with fallback positions.

## Output

1. Tracked markup or clean draft with comments.
2. Issues list: clause · risk · proposed position · fallback.
3. Diligence-to-protection map.
4. CP list for `closing-checklist-builder`.

## Guardrails and hand-offs

- Do not add warranties or disclosures that are not supported by the facts supplied.
- Do not state market norms as figures without a source; describe ranges as "commonly negotiated" and tag `[verify]`.
- Listed targets go to `takeover-code-trigger-analyst`; open diligence to `ma-due-diligence-analyst`.
- Run `citation-verifier` on any authority cited.
