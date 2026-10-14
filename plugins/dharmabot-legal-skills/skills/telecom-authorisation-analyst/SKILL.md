---
name: telecom-authorisation-analyst
description: Analyses authorisation needs and obligations under the Telecommunications Act, 2023 and the rules made under it, including the 2026 authorisation rules, covering service categories, enterprise and cloud calling, satellite communications, user verification, interception and telecom cyber-security rules, and right of way. Use when a client asks whether it needs a telecom authorisation for VoIP, cloud telephony, SMS or CPaaS, M2M, satellite or captive networks in India. Do not use for content or platform duties; use it-rules-intermediary-compliance-checker instead.
---

# Telecom Authorisation Analyst

Every output is a draft review for an advocate enrolled in India to check. Telecom rules are still being notified; check them on the date of advice.

## Purpose

Decide whether the client's service is a telecommunication service needing authorisation, which category fits, and what duties follow.

## Jurisdiction gate

- Confirm the service is provided in India or to users in India, and where its network elements and points of interconnection are.
- Foreign providers serving Indian users may need an Indian entity or partner; check FDI conditions for telecom and hand structuring to `india-entry-fema-structuring-analyst`.

## Temporal gate

- The Telecommunications Act, 2023 was brought into force in phases from 2024. Confirm which sections are in force.
- Authorisation rules (principal, captive and miscellaneous services) were reported notified in 2026, with migration from existing licences. Confirm dates and transition terms.
- Where a rule is not yet notified, the older licence conditions or guidelines may continue; record which applies and why.

## Required inputs

**Blocking**:
- a technical description: what the service does, whether it connects to the public network (PSTN or mobile numbers), whether it uses numbering, spectrum or satellite capacity;
- who the customers are (businesses only, consumers, captive own use);
- the client's partners (licensed operators, cloud providers) and their licences.

Also useful: network diagrams, call flows, data storage locations, and existing registrations.

## Method

1. Retrieve the current official text of the Telecommunications Act, 2023, the authorisation rules and any other rules under it (interception, cyber security, user verification, right of way), DoT notifications, and TRAI recommendations where cited. Record version and date.
2. Test whether the service is a "telecommunication service" under the Act's definition. Note open questions, for example on internet-based communication services.
3. Map the service to an authorisation category: principal services, miscellaneous services or captive services. Compare with how the service would have been licensed before.
4. Enterprise and cloud calling: check rules on PSTN interconnection, toll bypass, number use, and the conditions for contact centres and enterprise users. Note that OSP registration was dropped in 2021 guidelines (confirm), and check what carried over.
5. Satellite: check spectrum assignment method, gateway location and security conditions.
6. User verification and KYC duties, and messaging rules on unsolicited commercial communication.
7. Interception, traffic data retention and telecom cyber-security duties, including incident reporting; hand incidents to `data-breach-response-planner`.
8. Right of way and infrastructure, where the client builds network.
9. Fees, bank guarantees and financial conditions: quote only from the current rules.

## Output

1. Classification memo: service · definition test · authorisation category · reasons · uncertainty.
2. Obligations list by area.
3. Partnering options (use a licensed operator versus own authorisation) with trade-offs.
4. Watch list of rules not yet notified.

## Guardrails and hand-offs

- Never advise routing traffic to bypass licensing or interconnection rules.
- Mark TRAI recommendations and drafts as not law.
- Wider multi-regulator questions go to `regulatory-applicability-analyst`.
