---
name: contract-negotiation-planner
description: Builds a negotiation plan for a commercial contract, with an issues list, opening, fallback and walk-away positions, trade-offs across issues, counter-proposals with drafting, and an escalation path, using Indian market practice where known and labelling assumptions. Use when a lawyer asks how to negotiate liability, IP, indemnity or payment clauses, wants fallback positions, or needs a counter-proposal plan for a customer or vendor. Do not use for settling a dispute; use settlement-strategy-planner instead.
---

# Contract Negotiation Planner

Every output is a draft plan for the advocate or in-house counsel to review with the client; it plans and does not represent the client.

## Purpose

Help the client enter a contract negotiation knowing what it must win, what it can trade, and when to walk away.

## Jurisdiction gate

Identify the governing law and each party's location. Use Indian market practice and Indian-law enforceability where Indian law governs. For foreign-law contracts, label positions as commercial only and refer legal points to `cross-border-contract-reviewer`.

## Required inputs

Mark as **blocking**:
- the contract draft and the counterparty's markup or comments;
- which party the client is;
- the client's priorities and red lines (or the playbook).

Also useful: deal value and duration, the client's leverage (alternatives, timing, relationship), the counterparty's known constraints (regulator, procurement policy, insurer), and who has authority to approve concessions.

## Method

1. Retrieve the current official text of any law that limits what can be agreed (for example the Indian Contract Act, 1872 on penalties and restraints, the DPDP Act, 2023 for data terms, sector rules for regulated customers such as banks). Record the version and date.
2. **Issues list.** From the markup, list every open point. Group them: legal risk, commercial, operational, drafting only.
3. **Leverage and interests.** For each side, note what it needs and why. Regulated customers often cannot move on audit, data location or termination rights; note which of their asks are likely non-negotiable.
4. **Positions per issue.** Opening, target, fallback and walk-away, with the reason for each. Label any "market practice" claim as an observation to confirm, not a rule.
5. **Trade-offs.** Pair issues so a concession on one buys a gain on another (for example a higher cap for a narrower indemnity; IP assignment for a broad licence back).
6. **Counter-proposals.** Draft the clause wording for each fallback so the team can respond in the same round.
7. **Sequencing.** Decide which issues to settle first, which to park, and which to escalate together.
8. **Escalation path.** Who approves each fallback internally, and when to take an issue to senior business contacts.
9. **Risk check.** For each walk-away, state the business consequence of losing the deal.

## Output

1. A negotiation grid: issue · their ask · our opening · target · fallback · walk-away · trade · approver.
2. Counter-proposal wording for each issue.
3. A round plan: order of issues, talking points and escalation triggers.

## Guardrails and hand-offs

- Never recommend misrepresenting facts, authority or competing offers.
- Never present an assumed market standard as fact.
- The client decides concessions; the plan does not commit the client.
- Clause-level review goes to `playbook-contract-reviewer`.
