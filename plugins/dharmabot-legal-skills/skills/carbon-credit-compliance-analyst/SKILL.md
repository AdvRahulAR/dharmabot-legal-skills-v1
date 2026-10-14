---
name: carbon-credit-compliance-analyst
description: Maps duties and opportunities under the Carbon Credit Trading Scheme, 2023 made under the Energy Conservation Act, 2001 (obligated entities, GHG intensity targets, MRV, BEE and Grid Controller roles, the offset mechanism), the Green Credit Programme and Article 6, and reviews carbon credit purchase and sale agreements. Use when a plant is notified as an obligated entity, or a client wants to buy, sell or generate carbon credits in India. Do not use for BRSR reporting (use csr-esg-brsr-compliance-checker) or green ad claims (use advertising-claims-reviewer).
---

# Carbon Credit Compliance Analyst

Every output is a draft analysis for an advocate enrolled in India to check.

## Purpose

Tell an entity what the Indian carbon market requires of it, what it can earn, and where its carbon contracts carry risk.

## Jurisdiction gate

Confirm the plant or project is in India. For credits sold abroad or under Article 6, flag that host-country authorisation and corresponding adjustments are needed, and mark buyer-country rules "to be confirmed by counsel qualified in [jurisdiction]". Voluntary registries (for example Verra or Gold Standard) are private schemes; note their rules separately from Indian law.

## Temporal gate

- The scheme has been built through several notifications: the CCTS 2023, amendments including the offset mechanism, BEE procedures, and MoEFCC's Greenhouse Gases Emission Intensity Target Rules, 2025 (reported as effective 8 October 2025, initially for aluminium, cement, chlor-alkali and pulp and paper, with a further amendment reported around January 2026). Confirm each instrument and its date from the eGazette, BEE and MoEFCC websites.
- Targets apply by compliance year. Record the compliance year in issue and the baseline year.
- Check whether trading on power exchanges has begun and under which approved procedure.

## Required inputs

Mark as **blocking**: the entity's sector and plant details; the notification naming it (if obligated) with its target; production and emissions data for the baseline and current years; and, for contract review, the agreement itself.

Also useful: energy audit reports, PAT scheme history, MRV plan, accredited carbon verification agency details, and any registry account.

## Method

1. Retrieve the current official text of the Energy Conservation Act, the CCTS and amendments, the GHG Emission Intensity Target Rules and Schedule, BEE detailed procedures, the Green Credit Rules and any Article 6 notification. Record versions and dates.
2. **Obligated entity.** Confirm coverage, target (intensity per unit of output), compliance years and trajectory.
3. **MRV.** List monitoring plan, reporting format and timeline, verification by an accredited agency, and data retention.
4. **Compliance outcomes.** Over-achievement earns credit certificates; shortfall requires surrender of certificates. Reports say environmental compensation applies to unmet shortfall; confirm the formula and procedure, including the hearing right.
5. **Offset mechanism.** For non-obligated projects: eligible methodologies, registration, additionality, crediting period and issuance.
6. **Green Credit Programme.** Explain how it differs from carbon credits and whether credits can be used for any compliance purpose.
7. **Contract review.** For ERPAs and credit sale agreements, test: credit type and vintage; registry and transfer mechanics; delivery risk and make-good; price and adjustment; Article 6 authorisation and corresponding adjustment risk; tax and GST treatment (mark for tax adviser); warranties on additionality and no double counting; termination; dispute resolution and governing law.
8. Hand off energy project terms to `infrastructure-energy-contract-reviewer`.

## Output

1. Obligations map: requirement · source · deadline · owner.
2. Shortfall or surplus scenarios using the client's data, labelled as estimates.
3. Contract issues table with suggested drafting.

## Guardrails and hand-offs

- Never state a target, price or compensation multiple from memory.
- Never suggest double counting or claiming the same reduction twice.
- Mark tax and accounting points for specialist advice.
- For marketing claims like "carbon neutral", hand off to `advertising-claims-reviewer`.
- Run `citation-verifier` before delivery.
