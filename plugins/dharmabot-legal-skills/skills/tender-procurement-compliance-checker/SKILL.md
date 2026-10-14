---
name: tender-procurement-compliance-checker
description: Checks bids and tender documents in Indian public procurement against the General Financial Rules, 2017, procurement manuals, CVC guidelines, the Make in India public procurement order and State transparency in tenders laws, assesses challenges to eligibility, evaluation, blacklisting and cancellation by judicial review, and reviews Government and PSU contracts. Use when a client is bidding for a government tender, was disqualified or blacklisted, or wants to challenge a clause. Do not use for private-sector commercial contracts; use infrastructure-energy-contract-reviewer.
---

# Tender Procurement Compliance Checker

Every output is a draft review for an advocate enrolled in India to check.

## Purpose

Make a bid compliant before the deadline, and assess whether a tender decision can be challenged and where.

## Jurisdiction gate

Identify the procuring entity (Union ministry, State department, PSU, local body, statutory authority) and the State. Central entities follow the GFR and their manuals; States have their own rules and, in several States, a transparency in tenders Act; PSUs have board-approved manuals. Confirm which apply. For multilateral-funded projects, the lender's rules may govern; flag them.

## Required inputs

**Blocking**: the tender document with all corrigenda; the bid due date and time; the procuring entity; and for a challenge, the impugned decision and its date.

Also useful: the client's draft bid, pre-bid queries and replies, integrity pact, earlier contracts, and the evaluation results.

## Method

1. Retrieve the current official text of the rules that govern this procurement (GFR, the relevant manual, CVC guidance, the Public Procurement (Preference to Make in India) Order and any land-border restriction, MSE preference policy, and the State's tenders law and rules). Record source and date.
2. Bid compliance: build a matrix of every eligibility, technical and commercial requirement against the client's documents. Flag missing documents, unsigned pages, wrong formats, EMD or bid security, local content certificates and declarations.
3. Deadlines: bid submission, pre-bid query date, validity, and any grievance window under the State law or tender. Flag them prominently.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. Restrictive clauses: test whether a clause is tailored to one bidder, disproportionate to the work, or contrary to the governing rules. Plan pre-bid queries first.
5. Challenges: apply judicial review limits from Tata Cellular v. Union of India (Supreme Court, 1994) and Michigan Rubber (India) Ltd. v. State of Karnataka (Supreme Court, 2012); confirm current treatment. Courts intervene only for arbitrariness, mala fides, irrationality or breach of rules. Check internal grievance or appeal mechanisms first.
6. Blacklisting and debarment: check notice, hearing, reasons, period and proportionality.
7. Contract review: one-sided clauses on termination, liquidated damages, payment, price variation, indemnity and dispute resolution. Use `arbitration-clause-reviewer` for the dispute clause.
8. Read authority before citing; tag anything unread `[verify]`.

## Output

1. A bid compliance matrix with gaps and owners.
2. A challenge note: forum, grounds, prospects and timing.
3. A list of contract risks and suggested pre-bid queries or deviations.

## Guardrails and hand-offs

- Never suggest cartel conduct, bid rigging, false certificates or contact with evaluators outside the process.
- Never promise a challenge will succeed; courts defer to the employer.
- For a writ, use `writ-petition-drafter`.
