---
name: land-acquisition-compensation-calculator
description: Computes land acquisition compensation under the Right to Fair Compensation and Transparency in Land Acquisition, Rehabilitation and Resettlement Act, 2013 and special statutes such as the National Highways Act, 1956, covering market value, the State multiplier, structures and trees, solatium and interest, with arithmetic shown, and plans objections, references and appeals. Use when a lawyer asks to compute acquisition compensation, challenge a low award, or object to a highway acquisition. Do not use for a constitutional challenge to the acquisition itself; use writ-petition-drafter.
---

# Land Acquisition Compensation Calculator

Every output is a draft calculation and plan for an advocate enrolled in India to check.

## Purpose

Show what the landowner should receive, line by line, and set out the procedural steps to contest a low award.

## Jurisdiction gate

Identify the acquiring statute: the 2013 Act, a special central Act (for example National Highways, Railways, Metro, Coal), or a State law or State amendment to the 2013 Act. The State sets the rural multiplier and may have exempted projects or adopted consent-based purchase schemes. Record the State, district and village.

## Required inputs

Mark as **blocking**:
- the notifications issued so far (preliminary, declaration, award) with dates;
- the statute under which they were issued;
- the land's extent, classification and location (rural or urban, distance from the urban area);
- the award, if made, with its computation.

Also useful: sale deeds of comparable lands, the State guideline value, crops, trees, structures and wells, tenants and livelihood losers, and any SIA report.

## Method

1. Retrieve the current official text of the acquiring statute, its compensation schedule and the State's notifications and rules (multiplier factor, guideline values, R&R schemes). Open `references/india-state-statutes.md` as a starting point. Record the version and date.
2. Market value: the 2013 Act uses the highest of specified measures (guideline value, average of a top set of sale deeds, consented compensation for PPP or private projects; confirm the provision, believed to be section 26). Work out each measure from documents supplied.
3. Apply the multiplier for rural land as notified by the State (the Act allows a range; confirm). Urban land uses a factor of one.
4. Add the value of assets attached: buildings, trees, crops, wells.
5. Add solatium (believed to be 100% of the total under the 2013 Act; confirm) and additional amount or interest for the period stated in the Act.
6. Compute R&R entitlements under the Act's schedules or the State scheme.
7. For National Highways and other special statutes, apply that statute's own procedure, including the arbitrator appointed by the Central Government for disputed amounts, and note the extent to which the 2013 Act's compensation principles now apply to it (confirm current notification and authority).
8. Show every step as a table with the source of each number. Mark assumptions.
9. Remedies: objections at the notification stage, reference to the Authority or arbitrator, appeals, and limitation. Hand off dates to `limitation-calculator`. Hand off challenges to the acquisition process to `writ-petition-drafter`.

## Output

1. Compensation computation table, with sources and assumptions.
2. Comparison with the award, if any, showing the gap.
3. Draft objections or reference grounds outline, and a timeline of steps.

## Guardrails

- Never present a computed figure as what the authority or court will award.
- Never invent sale instances, guideline values or multipliers.
- Never state percentages, factors or deadlines as settled without the official text.
