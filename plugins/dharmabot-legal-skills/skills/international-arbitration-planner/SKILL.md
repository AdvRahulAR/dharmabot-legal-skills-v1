---
name: international-arbitration-planner
description: Plans international commercial arbitration involving an Indian party. Covers choosing seat, institution and rules (SIAC, ICC, LCIA, the Dubai International Arbitration Centre, HKIAC, MCIA, the India International Arbitration Centre and others), drafting or reviewing the clause, Indian court support for foreign-seated arbitrations, emergency and interim relief, enforcement in India and abroad, and a procedural timeline. Use when drafting a dispute clause for a cross-border deal, when a dispute is starting under an arbitration clause, or when advising on seat and enforcement. Do not use for purely domestic arbitration with an Indian seat and Indian parties only.
---

# International Arbitration Planner

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Make sure the arbitration clause and strategy will produce an award that can be enforced where the counterparty's assets are, with interim protection available when needed.

## Jurisdiction gate

Identify the parties' jurisdictions, the seat (or proposed seat), the institution and rules, and where assets are. Indian-law points (Part I and Part II of the Arbitration and Conciliation Act, 1996) are advised on. Seat-law and institution-rule points are checked against the current rules, and foreign seat-law points are marked for local counsel.

## Required inputs

Mark as **blocking**:
- the existing clause, or the deal for which a clause is needed;
- where each party's assets are;
- the likely type and size of dispute.

Also useful: the client's preferences on cost, speed, confidentiality, language and number of arbitrators, and whether emergency relief may be needed.

## Method

1. Read `references/foreign-jurisdictions.md` for New York Convention notification status and courts.
2. **Seat.** Compare candidate seats on:
   - support from local courts;
   - whether the seat is New York Convention-notified by India, which matters for enforcement in India (the UAE was not notified at the last check, so flag a UAE seat);
   - enforceability where the assets are;
   - neutrality, cost and the time zone.
3. **Institution and rules.** Compare the candidates' current rules on emergency arbitrator, expedited procedure, joinder and consolidation, and fees. Retrieve each institution's current rules; rules are revised often.
4. **Indian law points.** Confirm every section number below against the official text of the Act.
   - Party autonomy to choose a foreign seat, especially where both parties are Indian; retrieve current Supreme Court authority.
   - Which Part I provisions apply to foreign-seated arbitrations under the proviso to s.2(2) (ss.9, 27, 37(1)(b) and 37(3)), unless the parties excluded them. The proviso is tied to "international commercial arbitration" under s.2(1)(f). Where both parties are Indian and chose a foreign seat, check current authority (for example PASL Wind Solutions v GE Power, 2021) before assuming s.9 relief is available.
   - Whether an emergency arbitrator's order from a foreign seat is enforceable in India. Current authority supports enforcing it for India-seated arbitrations; foreign-seated orders generally need a fresh s.9 application. Do not rely on draft amendment Bills (such as a proposed emergency-arbitrator provision) unless enacted.
5. **Draft or review the clause.** Cover the institution and rules, seat (distinct from venue), number and appointment of arbitrators, language, governing law of the contract and of the arbitration agreement, confidentiality, interim relief carve-out, and multi-contract or multi-party wording. Remove pathological wording, such as mixing up seat and venue, naming an institution that no longer exists, or giving the parties an "option" to arbitrate.
6. **Timeline.** For a live dispute, set out notice, constitution, statements, hearing and award, with limitation checks via `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)

## Output

1. A seat and institution comparison table, with a recommendation and reasons.
2. A model or revised clause.
3. An interim relief and enforcement plan, by country.
4. A timeline for a live dispute.

## Guardrails

- Confirm every institution rule and India notification from current official sources.
- Do not describe an institution or rule set without checking that it still exists.
- Mark foreign seat-law points for local counsel.
