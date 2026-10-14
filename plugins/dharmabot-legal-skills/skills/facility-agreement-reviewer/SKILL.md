---
name: facility-agreement-reviewer
description: Drafts and reviews Indian term loan, working capital, inter-corporate and NBFC facility agreements under the Indian Contract Act and RBI fair practices and interest-rate directions, covering conditions precedent, covenants, events of default, cross-default, prepayment and set-off, and builds a covenant tracker. Use when a lawyer asks to review a loan agreement, mark up a facility agreement for a borrower or lender, or check whether an event of default has occurred. Do not use for the security documents themselves; use security-guarantee-document-drafter.
---

# Facility Agreement Reviewer

Every output is a draft or review for an advocate enrolled in India to check.

## Purpose

Review or draft a facility agreement from one side's point of view, find the clauses that create real risk, and test any alleged default against the actual wording.

## Jurisdiction gate

Confirm Indian law governs the agreement and note the lender type: scheduled bank, NBFC (and its layer under the scale-based framework), co-operative bank, or a foreign lender. If the lender is non-resident or the loan is in foreign currency, flag External Commercial Borrowing and FEMA issues and hand off to `financial-services-licensing-analyst` or a FEMA specialist. If foreign law governs, review only the Indian-law points and mark the rest for counsel qualified in that jurisdiction.

## Required inputs

Mark as **blocking**:
- the agreement (or term sheet for a draft), with schedules and any sanction letter;
- which party the client is (borrower, guarantor, lender, agent);
- for a default question, the alleged default, the dates, and any notices exchanged.

Also useful: the borrower's latest financials, related security documents, the lender's key fact statement, and the client's commercial priorities.

## Method

1. Retrieve the current official text of the RBI directions that bind the lender (fair practices code, key fact statement, interest-rate and penal-charges rules, prepayment directions, and NBFC master directions), and record each version and date. Do not state any rate, cap or charge from memory.
2. Map the document: definitions, facility terms, pricing and resets, conditions precedent and subsequent, representations, covenants (information, financial, negative, affirmative), events of default, remedies, set-off, assignment, governing law and dispute resolution.
3. Test pricing and charges against RBI rules: whether penal charges are levied as charges rather than penal interest, reset transparency, and prepayment or foreclosure fees for the borrower and loan type.
4. Read every event of default for triggers that are vague, lender-discretionary (material adverse change), cross-default with no threshold, or without a cure period.
5. Check representations that are repeated each period and could create a default from facts outside the borrower's control.
6. Check negative covenants against the borrower's business plan: further borrowing, dividends, change of control, asset disposals, and group restructuring.
7. For a default analysis, take each alleged default, quote the clause, apply the facts, and record whether notice and cure steps were followed. Note any interaction with SARFAESI, IBC or wilful defaulter rules.
8. Build a covenant tracker: covenant, test, frequency, data source, owner, next date, status.
9. Search for and read current authority on any contested point (for example penalty and liquidated damages under the Contract Act, or MAC clauses). Tag anything not read in full `[verify]`.

## Output

1. An issues list: clause, issue, risk rating, proposed redline or fallback position.
2. A marked-up draft or clean drafting language for priority clauses.
3. The covenant tracker as a table.
4. For a default question, a reasoned note: default or not, cure options, and next steps.

## Guardrails and hand-offs

- Do not advise on how to hide a default or misreport financials.
- Do not state stamp duty figures; hand off to `state-stamp-duty-calculator`.
- Security documents go to `security-guarantee-document-drafter`.
- Regulatory questions on the lender's licence go to `financial-services-licensing-analyst`.
- Never invent case law or RBI circular numbers. Run `citation-verifier` before delivery.
