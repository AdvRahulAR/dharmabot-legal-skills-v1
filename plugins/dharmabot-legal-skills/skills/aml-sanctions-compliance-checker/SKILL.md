---
name: aml-sanctions-compliance-checker
description: Checks reporting-entity duties under the Prevention of Money-laundering Act, 2002 and the PML (Maintenance of Records) Rules, 2005 (KYC, beneficial ownership, FIU-IND reports, records, VDA service providers), and documents sanctions and export-control screening against UN lists implemented in India, the SCOMET list and, for cross-border exposure, OFAC, EU and UK lists, including adjudication of screening hits. Use when a client asks to screen a counterparty, clear a sanctions hit or check PMLA duties. Do not use for ED proceedings; use pmla-proceedings-analyst.
---

# AML and Sanctions Compliance Checker

Every output is a draft review for an advocate enrolled in India and the client's compliance officer to check.

## Purpose

Tell the client whether it is a reporting entity and what it must do, and document a defensible screening decision on a counterparty.

## Jurisdiction gate

- Indian duties apply to reporting entities under the PMLA and to exporters under Indian export-control law.
- Foreign sanctions apply where there is a nexus with that country (persons, currency, goods, or entities owned or controlled by listed persons). Read `references/foreign-jurisdictions.md`. Mark every foreign-law point "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

**Blocking**:
- for PMLA duties: the client's activities and its regulator, and whether it handles virtual digital assets or acts as a designated business or profession;
- for screening: the counterparty's full legal name, aliases, country, registration details, and owners and controllers with their shareholdings;
- the transaction: goods or services, value, currency, routing and end use.

Also useful: the client's KYC policy, screening tool output, and previous alerts.

## Method

1. Retrieve the current official text of the PMLA, the PML (Maintenance of Records) Rules, FIU-IND guidelines for the client's sector, the notification bringing VDA service providers into the PMLA (reported March 2023), orders implementing UN sanctions in India, the SCOMET list, and the current OFAC, EU and UK lists. Record versions and dates.
2. Reporting entity status: test the client's activities against the definitions. If covered, list duties: registration with FIU-IND, a designated director and principal officer, customer due diligence and beneficial ownership, enhanced due diligence, record retention, and reports (cash, suspicious and other reports with their timelines; confirm each).
3. Screening: run each name and owner against every relevant list. Record the list version and date screened.
4. Adjudicate hits: compare name, date of birth or incorporation, nationality, address and identifiers. Classify as true match, false positive or unresolved, with reasons.
5. Ownership tests: check foreign aggregation rules (for example OFAC's 50 percent rule, and EU and UK ownership and control tests), marked for foreign counsel.
6. Export controls: check whether goods, software or technology are on the SCOMET list or foreign control lists, and end-use and end-user red flags.
7. Decide escalation: true or unresolved matches go to the compliance officer, with a recommendation to freeze, reject or seek a licence, and whether a suspicious transaction report is needed.
8. Document the file so a regulator can follow it.

## Output

1. PMLA duties checklist with status.
2. Screening memo: lists searched · date · hits · adjudication · decision.
3. Escalation note, where needed.
4. KYC and screening policy gaps.

## Guardrails and hand-offs

- Never help structure a transaction around sanctions, export controls or reporting thresholds.
- Never tip off a customer about a suspicious transaction report.
- Never clear a hit without written reasons.
- Licensing of the business goes to `financial-services-licensing-analyst`; ED action to `pmla-proceedings-analyst`.
