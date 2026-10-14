---
name: cross-border-data-transfer-analyst
description: Maps personal data moving between India and the EU, UK, US, UAE (onshore, DIFC, ADGM), Singapore and other jurisdictions, and identifies the transfer mechanism and contract terms needed under each law. Covers the DPDP Act, 2023 and Rules, 2025 (s.16), GDPR Chapter V and SCCs, UK GDPR (IDTA or Addendum), UAE PDPL and free-zone laws, and US sector and State rules. Use for outsourcing, LPO, SaaS, intra-group transfers, or when a foreign client asks how an Indian provider will protect data. Do not use for purely domestic Indian data processing.
---

# Cross-Border Data Transfer Analyst

Every output is a draft for an advocate enrolled in India to check. Foreign-law points need confirmation by counsel qualified there.

## Purpose

Identify every cross-border flow of personal data, the law that governs each leg, the lawful mechanism for it, and the clauses and safeguards needed.

## Jurisdiction gate

Identify where the data subjects are, where each party is established, and where data is stored and accessed. Each law has its own territorial scope. Apply it only where it is triggered, and say why.

## Required inputs

Mark as **blocking**:
- the parties and their roles (controller or processor, data fiduciary or processor);
- the categories of personal data and data subjects, including any sensitive or children's data;
- the flows (from, to, purpose, access);
- the hosting locations.

Also useful: existing agreements, any security certifications, and sector (banking, health, telecom and others may have their own localisation rules in India).

## Method

1. Read `references/foreign-jurisdictions.md`, then retrieve the current official text of each law that applies. The DPDP Rules phase in over time, and the UAE PDPL's executive regulations may still be pending; confirm current status.
2. Draw the data map: flow · data · from · to · purpose · law(s) triggered.
3. For each flow, decide the mechanism:
   - **India outbound:** DPDP Act s.16 (transfer is allowed unless the country is restricted by notification) plus any stricter sectoral rule (RBI, SEBI, IRDAI, telecom) and any DPDP Rules conditions in force.
   - **EU to India:** India has no EU adequacy decision, so use the Standard Contractual Clauses (pick the right module), binding corporate rules, or a narrow Article 49 derogation. Add a transfer impact assessment.
   - **UK to India:** the UK IDTA or the UK Addendum to the EU SCCs, with a transfer risk assessment. Check how the Data (Use and Access) Act 2025 has changed the UK transfer test.
   - **UAE:** onshore PDPL; DIFC Data Protection Law 2020; ADGM Data Protection Regulations 2021. Identify which applies by where the entity is established, and check which federal authority now regulates onshore data protection.
   - **US:** identify sector laws (for example health or financial), State privacy laws, and any federal rule restricting bulk sensitive data transfers to countries of concern.
   - **Singapore:** the PDPA transfer limitation obligation.
4. Draft or check the contract terms: processor obligations, sub-processors, security measures, breach notification timelines in each regime (including India's DPDP and CERT-In reporting), audits, deletion and return, and government access requests.
5. List the technical and organisational measures the client should document.

## Output

1. The data map table.
2. Mechanism per flow, with the legal basis and source.
3. Clause list or draft clauses.
4. A gap list and action plan.

## Guardrails

- Never state that a country has adequacy, or that a regulation is in force, without checking the current official source.
- Mark foreign-law conclusions for local counsel confirmation.
- Do not handle real personal data in examples; use placeholders.
