---
name: mediation-brief-drafter
description: Prepares a party for mediation in India, whether under the Mediation Act, 2023, court-annexed, pre-institution under the Commercial Courts Act or private, by drafting a confidential brief to the mediator, an opening statement, an interests map, a caucus disclosure plan and walk-away points. Use when a lawyer asks for a mediation brief, a mediation opening statement, or a plan for what to say in joint session and caucus. Do not use to decide whether an offer is worth accepting; use settlement-strategy-planner instead.
---

# Mediation Brief Drafter

Every output is a draft for an advocate enrolled in India, or the party's representative, to check.

## Purpose

Help the party walk into mediation knowing what it wants, what it will reveal, and when it will stop.

## Jurisdiction gate

Identify the kind of mediation (court-referred, court-annexed centre, pre-institution, community, online, or private institutional) and the State. Confirm whether the Mediation Act, 2023 applies to this mediation and which of its provisions are in force on the session date. If a party or the mediation is abroad, note that foreign rules may govern confidentiality and enforcement, to be confirmed by counsel qualified there.

## Required inputs

Mark as **blocking**:
- the dispute summary and the key documents;
- who the client is and who will attend with authority to settle;
- the type of mediation, the mediator's name or centre, and the date;
- the client's instructions on settlement range (or a statement that none exist yet).

Also useful: the other side's pleadings or notices, earlier offers, relationship history, and any deadline pressure.

## Method

1. Retrieve the current official text of the law and rules that govern this mediation (for example the Mediation Act, 2023 and its notifications, the court's mediation rules, or the centre's rules), especially on confidentiality and admissibility. Record the version and date.
2. **Case snapshot.** One page: parties, dispute, amounts, procedural status, and the strongest and weakest points for each side.
3. **Interests behind positions.** For each party, list commercial, financial, reputational and relationship interests. Note who outside the room influences the decision (board, lender, family).
4. **Confidential brief to the mediator.** Background, issues, what the client needs, obstacles to settlement, and options that might work. Mark what the mediator may and may not share.
5. **Opening statement.** Two to four minutes, non-adversarial, acknowledging the other side, signalling willingness, and stating the client's core need without revealing the bottom line.
6. **Caucus plan.** For each item of information, decide: share in joint session, share in caucus only, or hold back. Plan concessions in order and what to ask for in return.
7. **Walk-away points.** Record the client's limits and the alternative if mediation fails. Hand off valuation of options to `settlement-strategy-planner`.
8. **Logistics.** Authority letters, documents to carry, and a draft heads of terms template for use in the room.

## Output

1. Confidential brief to the mediator.
2. Opening statement script.
3. Interests map and caucus disclosure plan.
4. Internal negotiation sheet with opening, target and walk-away (for the client only).

## Guardrails and hand-offs

- Never draft anything that misleads the mediator or the other side about facts.
- Keep the internal negotiation sheet separate from anything shared with the mediator.
- Respect mediation confidentiality; do not plan to use mediation communications later in court.
- Never invent authority; tag unread authority `[verify]`.
- When terms are agreed, hand off to `mediated-settlement-agreement-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
