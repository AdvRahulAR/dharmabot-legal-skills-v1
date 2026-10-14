---
name: overseas-expansion-legal-planner
description: Builds an implementation plan for an Indian company hiring or expanding abroad, comparing a foreign entity, an employer of record and contractors, flagging which foreign employment laws may apply (US federal and state, UK, UAE, Singapore) for local counsel to confirm, and covering IP and data transfer, tax residence and permanent establishment flags, and ODI reporting under FEMA. Use when an Indian startup wants to hire in the US, open a UK office or set up in Dubai or Singapore. Do not use for FEMA structuring detail; use india-entry-fema-structuring-analyst.
---

# Overseas Expansion Legal Planner

Every output is a draft plan for an advocate enrolled in India to check. Foreign-law points are for counsel in each country.

## Purpose

Turn an expansion idea into a tracked list of legal workstreams, owners and decisions, so nothing is missed in India or abroad.

## Jurisdiction gate

List each target country (and US state, UK nation, UAE free zone or mainland). Indian law governs ODI, FEMA reporting, Indian tax, and transfers of IP and data out of India. Foreign law governs the entity, employment, immigration and local tax there; mark those points "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

ODI rules were overhauled in 2022 and are amended from time to time. The Income-tax Act 2025 replaces the 1961 Act from the date notified; check which Act governs the relevant tax year. Record today's date.

## Required inputs

Mark as **blocking**:
- the target countries and what will happen there (sales, hiring, R&D, holding IP);
- the number and roles of people to be hired, and whether they are local or relocating Indians;
- the Indian company's structure and funding.

Also useful: timeline, budget, existing customer contracts in those countries, and investor requirements.

## Method

1. Retrieve the current official text of the FEMA ODI rules, regulations and RBI directions, the Indian tax provisions on residence and permanent establishment, and the relevant DTAA. For each country, retrieve official guidance on entity formation and employment from government sites. Record versions and dates. Open `references/foreign-jurisdictions.md` for official sources.
2. Compare models for each country: subsidiary or branch, employer of record, or independent contractors. Note misclassification risk and permanent establishment risk for each.
3. Employment: list which laws may apply for counsel to confirm (US federal and state wage, leave and at-will rules; UK employment rights and right-to-work checks; UAE labour law or free-zone rules; Singapore Employment Act). Note contracts, handbooks and benefits to localise.
4. Immigration: work permits for relocating Indians.
5. IP: who owns IP created abroad; intra-group assignments and licences; transfer pricing.
6. Data: transfers from India under the DPDP Act and Rules phasing; inbound duties under GDPR or US state laws.
7. India-side filings: ODI approvals or reporting, annual performance reports, and board and shareholder approvals.
8. Build a workstream tracker with owners and status.

## Output

1. A model comparison per country.
2. A workstream tracker: workstream · country · tasks · owner (India counsel, local counsel, CA) · status · dependency.
3. Questions for local counsel in each country.

## Guardrails and hand-offs

- Never present foreign employment or tax rules as settled.
- Never suggest contractor labels to avoid employment law.
- For FEMA structuring, hand off to `india-entry-fema-structuring-analyst`.
- For engaging foreign counsel, hand off to `foreign-client-engagement-checker`.
- For data transfers, hand off to `cross-border-data-transfer-analyst`.
