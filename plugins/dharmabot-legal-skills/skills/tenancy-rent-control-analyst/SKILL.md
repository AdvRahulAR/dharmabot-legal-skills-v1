---
name: tenancy-rent-control-analyst
description: Analyses a landlord–tenant dispute over a residential or commercial building in any Indian State or Union Territory, under that State's rent control law or its newer Model Tenancy Act-based tenancy law. Covers whether the law applies, eviction grounds, rent revision, deposits, the rent court or controller, and a draft petition or reply. Use when an advocate asks about evicting a tenant, arrears, bona fide need, sub-letting, fair rent, or defending an eviction case. Do not use for agricultural land, or for drafting a new lease; use a contract skill.
---

# Tenancy and Rent Control Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Decide which tenancy law governs the premises, which grounds or remedies are available on the facts, what must be proved and where, and prepare a draft petition or reply.

## Jurisdiction gate

Identify the State or UT and the exact location (municipal area, cantonment, panchayat). Then decide which regime applies, because many States now have two:

- an older **rent control Act** that protects tenants and applies only in specified areas or to specified premises, often with exemptions by rent amount, building age, owner or purpose; and
- a newer **tenancy Act based on the Model Tenancy Act, 2021**, which commonly requires a written, registered or filed tenancy agreement and sets up rent authorities, rent courts and rent tribunals. Many of these come into force only on notification.

Check whether the new law has commenced, whether it applies to this tenancy (for example by date of agreement), and what happens to tenancies and cases under the old law. If neither regime applies, say so and point to the civil court remedy under the Transfer of Property Act, 1882.

## Required inputs

Mark as **blocking**:
- the State and location of the building;
- the tenancy terms (written or oral, registered or not), rent, and when the tenancy began;
- who the landlord and tenant are;
- what the client wants (eviction, arrears, rent revision, deposit refund, defence).

Also useful: an arrears schedule; notices exchanged; evidence of the ground relied on (the landlord's need and other properties owned, sub-letting, damage, non-occupation); and any earlier proceedings.

## Method

1. Open `references/india-state-statutes.md` for the State's rent and tenancy statutes. Treat it as a starting point only.
2. Retrieve the current official text of each potentially applicable law, its Rules, and its commencement, extension and exemption notifications. Record versions and dates. Do not rely on remembered section numbers.
3. Test applicability: area, type of premises, exemptions, date of tenancy, and whether a written agreement or registration with the rent authority is required.
4. For each ground or remedy the facts may support, list its statutory conditions and any proviso protecting the tenant. Mark each condition supported, unsupported or disputed, with the evidence.
5. For arrears, prepare a schedule. Check any requirement to deposit admitted arrears or ongoing rent during the case, and the consequence of default.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
6. Identify the forum (rent controller, rent authority, rent court, civil court), the appeal and revision route, and time limits. Use `limitation-calculator` for the arithmetic.
7. Search for, read and cite current High Court and Supreme Court authority on the disputed points. Tag anything not read in full `[verify]`.
8. Draft the petition or reply, pleading only facts supplied.

## Output

1. Which law applies, and why.
2. A ground-by-ground table: ground · conditions · facts and evidence · assessment.
3. Forum, remedies and time limits.
4. A draft petition or reply, with an annexure list.
5. Evidence still needed.

## Guardrails and hand-offs

- Do not advise self-help eviction, cutting utilities or other unlawful pressure.
- Do not overstate either side's prospects.
- Hand off formatting to `court-pleading-formatter`, a regional-language version to `regional-language-legal-drafter`, and court fee to `state-court-fee-calculator`.
