---
name: arbitration-clause-reviewer
description: Reviews a domestic arbitration clause under the Arbitration and Conciliation Act, 1996 for existence, validity, arbitrability, seat versus venue, arbitrator appointment (including unilateral-appointment problems), institutional rules, pre-arbitration steps, non-signatories and stamping, and proposes repaired wording. Use when a lawyer asks whether an arbitration clause works, what the seat is, or how to fix a clause before signing or invoking. Do not use for clauses with a foreign party or foreign seat; use international-arbitration-planner instead.
---

# Arbitration Clause Reviewer

Every output is a review for an advocate enrolled in India to check before advising the client.

## Purpose

Tell the advocate whether the clause will hold up when invoked, where it will break, and how to repair it.

## Jurisdiction gate

Confirm both parties are Indian and the seat (or intended seat) is in India, so the arbitration is domestic. If any party is incorporated, resident or managed abroad, or the seat is outside India, stop and hand off to `international-arbitration-planner`. Note the State and city named, because the seat fixes the supervisory court.

## Required inputs

Mark as **blocking**:
- the full text of the dispute-resolution clause, and the governing-law clause;
- the agreement it sits in (or at least its title, parties, date and how it was signed);
- whether a dispute has already arisen, and if so its nature.

Also useful: whether either party is a government body or PSU, any institutional rules referred to, related agreements (group contracts, guarantees), and stamping and execution details.

## Method

1. Retrieve the current official text of the Arbitration and Conciliation Act, 1996 with all amendments, any institutional rules named in the clause, and the stamp law of the State of execution. Record the version and date. Check for any amendment Act or notification after your last known version. Confirm every section, rule and article number used in this skill against that official text before relying on it.
2. **Existence and validity.** Is there a written agreement to refer disputes to arbitration, with intent to be bound? Flag optional or "may" wording, clauses that allow either court or arbitration, and expert-determination or "final and binding decision of the engineer" clauses that are not arbitration.
3. **Arbitrability.** Check the subject matter against non-arbitrable categories (for example certain rights in rem, criminal, matrimonial, insolvency, some tenancy and consumer matters). Search for and read current Supreme Court authority; tag anything not read in full `[verify]`.
4. **Seat versus venue.** Decide whether "venue", "place" or "held at" designates the juridical seat, reading the clause as a whole. Note conflicts with an exclusive-jurisdiction clause naming another city. Search for current authority on the seat test.
5. **Tribunal.** Check the number of arbitrators (an even number causes problems), qualifications, the appointment procedure, and fallback to the court under section 11. Flag any clause letting one party alone appoint the sole arbitrator, or curate a panel the other side must pick from. For example, Perkins Eastman (Supreme Court, 2019) and the Constitution Bench decision in CORE (Supreme Court, 2024) address these; confirm current treatment and whether the ruling applies to the appointment date in issue.
6. **Rules and institution.** Ad hoc or institutional (for example MCIA, DIAC, ICA, IIAC)? Check that the institution named exists under that exact name and that its rules fit the dispute size.
7. **Pre-arbitration steps.** Negotiation, escalation or mediation tiers: are they mandatory, time-bound and capable of proof? Flag vague tiers that invite a prematurity objection.
8. **Parties and scope.** Does "arising out of or in connection with" cover tort and related contracts? Identify group companies, guarantors or assignees who may be bound or excluded.
9. **Stamping and execution.** Check whether the main agreement is duly stamped. Explain the effect under the seven-judge Constitution Bench decision of December 2023 on stamping and arbitration agreements (confirm current treatment). Hand off execution and duty to `contract-execution-stamping-checker`.
10. Draft repaired wording for each defect, keeping the parties' commercial intent.

## Output

1. A verdict line: workable, workable with risk, or defective.
2. An issues table: issue · clause text · risk · consequence when invoked · fix.
3. A clean repaired clause, with drafting notes.
4. Points the advocate must confirm with the client (for example the preferred city or institution).

## Guardrails and hand-offs

- Do not guarantee that a court will refer the dispute or uphold the clause.
- Never invent a case name, citation or rule number; run `citation-verifier` before delivery.
- Do not redraft the commercial terms of the contract; flag them only.
- Cross-border clauses go to `international-arbitration-planner`; duty computation goes to `state-stamp-duty-calculator`.
