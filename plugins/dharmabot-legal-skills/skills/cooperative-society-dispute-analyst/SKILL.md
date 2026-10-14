---
name: cooperative-society-dispute-analyst
description: Analyses disputes in co-operative housing societies under the State co-operative societies law (for example the Maharashtra Co-operative Societies Act, 1960), covering membership and transfer, nomination and heirs, NOC refusal, maintenance and transfer premium, committee elections and supersession, redevelopment approvals, and the route to the Registrar, co-operative court and appellate court. Use when a society refuses transfer, membership or NOC, or members dispute charges or redevelopment. Do not use to review the redevelopment agreement; use joint-development-agreement-reviewer.
---

# Co-operative Society Dispute Analyst

Every output is a draft analysis for an advocate enrolled in India to review.

## Purpose

Identify the member's rights under the State law and bye-laws, the correct forum, and the fastest lawful remedy.

## Jurisdiction gate

Identify the State and confirm the society is registered under that State's co-operative societies law (not a company, an apartment owners' association or a multi-State society). Housing co-operative law varies widely by State. If the building is governed by an apartment ownership law instead, flag it and stop the co-operative analysis there.

## Temporal gate

State co-operative laws are amended often (for example Maharashtra added a separate chapter for housing societies in 2019; confirm). Record the dates of the disputed acts and check which version of the Act and bye-laws applied.

## Required inputs

Mark as **blocking**:
- the State, the society's name and registration, and the bye-laws it has adopted;
- the dispute: what was refused or done, when, and by whom;
- the member's documents (share certificate, allotment, nomination, sale deed, correspondence).

Also useful: committee resolutions, general body minutes, demand notices, and the Registrar's earlier orders.

## Method

1. Retrieve the current official text of the State co-operative societies Act and Rules, the society's registered bye-laws, and any government directions on transfer premium or redevelopment. Record the source and date. Open `references/india-state-statutes.md` as a starting point.
2. Classify the dispute: membership or transfer, nomination and heirs, NOC, charges, elections or supersession, redevelopment, or misconduct by the committee.
3. For death of a member, separate the nominee's position from the heirs' ownership. Search for current authority on whether a nominee takes membership as owner or trustee in that State. Hand heirship shares to `intestate-succession-share-calculator`.
4. Test the society's refusal against the Act and bye-laws: time limits for deciding applications, deemed membership, permissible grounds, and caps on transfer premium or charges (confirm figures from source).
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
5. Map the forum: Registrar (for statutory directions, inquiry, audit), co-operative court (for disputes touching the business of the society), appellate court, and a writ only where no adequate remedy exists. Check limitation with `limitation-calculator`.
6. For redevelopment, check the general body approvals, quorum and the government's directions. Leave contract review to `joint-development-agreement-reviewer`.
7. Search for and read current High Court authority; tag anything unread `[verify]`.

## Output

1. An issues and rights note.
2. A forum and remedy map, with limitation.
3. A document checklist and suggested first step (for example a representation to the committee or an application to the Registrar).

## Guardrails and hand-offs

- Do not guarantee transfer or membership.
- Never state premium caps, time limits or section numbers from memory.
- Writs go to `writ-petition-drafter`.
