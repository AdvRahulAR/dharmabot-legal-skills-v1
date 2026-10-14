---
name: settlement-strategy-planner
description: Builds a settlement strategy for a dispute in any forum, mapping each party's interests, BATNA and WATNA, opening, target and walk-away figures, a concession plan, and a risk-weighted comparison of an offer against likely litigation or arbitration outcomes including time, cost, interest and enforceability. Use when a client asks whether to accept a settlement offer, what to counter-offer, or how to plan a without-prejudice negotiation. Do not use for the mediation papers themselves; use mediation-brief-drafter instead.
---

# Settlement Strategy Planner

Every output is a draft analysis for the advocate to review with the client; the client decides.

## Purpose

Give the client a clear, numbers-based view of an offer and a negotiation plan, without deciding for them.

## Jurisdiction gate

Identify the forum and governing law (Indian court, Indian-seated arbitration, foreign forum). Where outcomes depend on Indian procedure, apply Indian law and practice. Where a foreign forum or law is involved, mark those assumptions "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the claim and counterclaim amounts and their basis;
- the offer on the table (amount, timing, conditions) or the client's goal;
- the forum and stage of proceedings;
- the client's priorities (cash now, relationship, precedent, confidentiality).

Also useful: the advocate's view of merits by issue, costs incurred and expected, the opponent's financial position and assets, and any security held.

## Method

1. Retrieve the current official text of any law that drives the numbers, such as interest provisions, costs rules, the Commercial Courts Act, 2015 on costs, or the MSMED Act, 2006 for supplier claims. Record the version and date.
2. **Interests.** For each party, list what it needs beyond money. Identify decision-makers and their constraints.
3. **Issue-by-issue merits.** Take the advocate's probability for each issue. If none is given, ask; do not supply your own as fact. Use ranges, not single points.
4. **Outcome model.** For each scenario (win, partial, lose), estimate the award, interest, costs recovered or paid, and time to recovery including appeals and execution. Hand off interest and quantum to `damages-interest-calculator`.
5. **Discount for time and risk.** Apply a client-chosen discount rate and an enforceability discount reflecting the opponent's assets and solvency.
6. **BATNA and WATNA.** State the realistic best and worst alternatives to settlement.
7. **Positions.** Recommend an opening, target and walk-away figure, with reasons. Plan concessions in shrinking steps and what to ask in return (timing, security, confidentiality, non-monetary terms).
8. **Communications.** Mark all offers "without prejudice"; note that this protection has limits, and that settlement terms may need court recording. Check current authority if relying on privilege.
9. **Pressure-test.** List the three assumptions that most change the answer and show how the answer moves.

## Output

1. A one-page decision summary: offer versus risk-weighted value, with ranges.
2. A scenario table: scenario · probability · net amount · time · notes.
3. A negotiation plan: opening, target, walk-away, concession sequence and trade-offs.
4. A draft without-prejudice counter-offer letter, if asked.

## Guardrails and hand-offs

- Never present a probability as certain or as the AI's own legal opinion; use the advocate's figures.
- Never recommend misrepresenting facts or the client's position.
- Do not decide for the client; present options and trade-offs.
- Broader case strategy goes to `litigation-strategy-planner`; mediation papers go to `mediation-brief-drafter`.
