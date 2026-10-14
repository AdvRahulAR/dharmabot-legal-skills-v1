---
name: litigation-strategy-planner
description: Assesses whether to sue, defend or settle an Indian dispute and compares routes, including civil suit, Order XXXVII summary suit, arbitration, IBC insolvency, SARFAESI and DRT, the MSME Facilitation Council, consumer commissions and cheque dishonour complaints, on merits, evidence, cost, time, enforceability and settlement windows. Use when an advocate asks for litigation strategy, should we sue, which forum, recovery options, or the strength of a claim or defence. Do not use for drafting a specific pleading; use plaint-drafter or the relevant drafting skill instead.
---

# Litigation Strategy Planner

Every output is a draft assessment for an advocate enrolled in India to review with the client.

## Purpose

Give the client a realistic options paper: the strength of the case, the routes available, what each costs and delivers, and a recommended sequence.

## Jurisdiction gate

Confirm Indian law governs the dispute and note the State and parties' locations. Check for an arbitration clause, exclusive jurisdiction clause, or foreign element. If a foreign party or law is involved, hand off to `foreign-matter-scoping-analyst` first.

## Required inputs

Mark as **blocking**:
- the client's objective (money, performance, protection, leverage, exit);
- the core documents (contract, invoices, correspondence, cheques, security);
- the amount at stake and the counterparty's identity and status (company, individual, government, MSME);
- the key dates, to test limitation.

Also useful: the counterparty's assets and solvency, the client's budget and appetite for time, and any related proceedings.

## Method

1. Retrieve the current official text of each statute behind the routes considered (CPC, Commercial Courts Act, Arbitration Act, IBC and its default threshold, SARFAESI, RDB Act, MSMED Act, Consumer Protection Act, Negotiable Instruments Act) and record the version and date. Confirm any threshold from the current notification.
2. Assess the merits: elements of each claim and defence, evidence for each, and gaps.
3. Check limitation for every route with `limitation-calculator`.
4. Map routes and test eligibility for each. Examples: IBC needs an operational or financial debt above the notified threshold and no pre-existing dispute for operational creditors; MSME reference needs a registered micro or small supplier; cheque dishonour needs a valid notice within time; SARFAESI needs secured debt held by a covered lender.
5. Compare in a table: route · eligibility · time to first relief · cost · enforceability · leverage · risks.
6. Note interactions: parallel routes, moratorium effects, and the risk of abuse-of-process findings.
7. Identify settlement windows (notice stage, pre-institution mediation, first hearing, after interim orders) and hand off to `settlement-strategy-planner`.
8. Quantify the claim with `damages-interest-calculator`.
9. Search for and read current authority on any route-determining point. Tag unread authority `[verify]`.

## Output

1. A merits assessment with evidence gaps.
2. The route comparison table and a recommended sequence.
3. A next-steps list with owners and dates.

## Guardrails and hand-offs

- Never promise or estimate an outcome as certain; express risk qualitatively, with reasons.
- Never recommend using criminal process to pressure a civil debt.
- Hand off to `msme-delayed-payment-claim-drafter`, `ibc-application-drafter`, `summary-suit-order-xxxvii-drafter`, `cheque-dishonour-case-drafter` or `plaint-drafter` once the route is chosen.
