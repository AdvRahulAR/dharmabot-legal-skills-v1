---
name: contract-amendment-drafter
description: Drafts amendments, addenda, side letters, novation and assignment agreements under Indian law, and traces amendment history across a base agreement and later documents into a consolidated view, checking consent and notice requirements and whether stamping or registration is triggered. Use when a lawyer asks to extend or vary a contract, change fees, assign or novate an agreement, or show how a contract has changed over time. Do not use to review the base contract from scratch; use playbook-contract-reviewer instead.
---

# Contract Amendment Drafter

Every output is a draft for an advocate enrolled in India to check before signing.

## Purpose

Change an existing contract cleanly and validly, and leave a clear record of what the contract now says.

## Jurisdiction gate

Confirm the governing law of the base agreement. If Indian, apply Indian law. If foreign, draft to match the base agreement's formalities and flag for `cross-border-contract-reviewer`. Note the State where the amendment will be executed, for stamp duty.

## Required inputs

Mark as **blocking**:
- the base agreement and every earlier amendment, side letter and novation;
- the changes required, in plain words;
- the parties (and, for novation or assignment, the incoming party).

Also useful: whether the base agreement was registered, the original stamp paid, approvals needed (board, lender, regulator), and correspondence agreeing the change.

## Method

1. Retrieve the current official text of the Indian Contract Act, 1872 (including novation and alteration), the Registration Act, 1908, and the stamp law of the State of execution. Record the version and date.
2. **History.** Build a table: document · date · parties · clauses changed · effect. Identify the operative text of each clause today.
3. **Conflicts.** Flag versions that contradict each other, amendments signed by the wrong entity, or changes made by email that the contract says need a signed writing.
4. **Amendment mechanics.** Check the base agreement's amendment clause, notice clause, assignment clause and any consent rights (counterparty, lender, regulator).
5. **Choose the instrument.**
   - Amendment or addendum: changes to terms between the same parties.
   - Side letter: avoid unless needed; it risks conflict with the entire-agreement clause.
   - Assignment: transfers benefits only; burdens need consent.
   - Novation: replaces a party with the consent of all three.
6. **Draft.** Recitals; definitions tied to the base agreement; each change as "clause X is deleted and replaced with ..."; effective date; confirmation that all other terms continue; and signature blocks with authority.
7. **Stamping and registration.** Amendments can attract duty, especially where they extend term, increase consideration or relate to registered instruments such as leases. Flag for `contract-execution-stamping-checker` and `state-stamp-duty-calculator`.
8. **Consolidated view.** Produce a conformed copy or a clause-by-clause comparison of base versus current text, marked as a reading aid, not a signed document.

## Output

1. The draft amendment, addendum, assignment or novation agreement.
2. The amendment history table.
3. A consolidated or comparison view of the contract as amended.
4. A checklist of consents, notices, stamping and registration.

## Guardrails and hand-offs

- Never treat a conformed copy as the legal instrument.
- Never change terms beyond the instructions; list collateral changes needed instead.
- For summaries of the amended contract, hand off to `contract-summariser`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
