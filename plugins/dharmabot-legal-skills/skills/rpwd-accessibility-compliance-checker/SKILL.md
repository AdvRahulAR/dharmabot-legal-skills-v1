---
name: rpwd-accessibility-compliance-checker
description: Checks establishments, websites, apps and services against the Rights of Persons with Disabilities Act, 2016 and Rules, 2017 (reasonable accommodation, equal opportunity policy, building and ICT accessibility standards, the Supreme Court's 2024 Rajive Raturi directions), and drafts accommodation requests and complaints to the Chief or State Commissioner. Use when a person with a disability raises access barriers or an organisation wants an accessibility check. Do not use for writ petitions (use writ-petition-drafter) or general HR policies (use hr-policy-handbook-drafter).
---

# RPwD Accessibility Compliance Checker

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Find accessibility and accommodation gaps, propose fixes, and draft the request or complaint that moves the matter forward.

## Jurisdiction gate

Confirm the establishment is in India and classify it: government establishment, private establishment, or service provider. Duties differ by category. Identify the State or UT for the State Commissioner and any State RPwD rules. For employees of a government establishment, note service law routes and hand off to `service-law-matter-analyst`.

## Temporal gate

Accessibility standards are notified and revised by the Centre (for example harmonised building guidelines and ICT standards). In late 2024 the Supreme Court in Rajive Raturi v. Union of India reportedly directed the Centre to frame mandatory, non-negotiable accessibility rules. Check what rules or amendments have been notified since, and record the version applied.

## Required inputs

Mark as **blocking**: who is affected and the nature of the disability as they describe it (no medical records beyond what they choose to share); the establishment type; the barrier (building, website, app, document, process); and what has already been requested and refused.

Also useful: the equal opportunity policy, HR or service policies, accessibility audit reports, website URL, and correspondence.

## Method

1. Retrieve the current official text of the RPwD Act, the Central Rules and any State rules, notified accessibility standards (buildings, ICT, transport), and the Commissioners' procedure. Record versions and dates.
2. Identify duties by category:
   - employers: non-discrimination, reasonable accommodation, equal opportunity policy, grievance redressal officer;
   - service providers and public buildings: accessibility standards and timelines;
   - websites and apps: notified ICT standard and conformance level.
3. Test each barrier against the duty. For reasonable accommodation, consider whether the cost or burden is disproportionate, and record the reasoning.
4. Check the Raturi directions and later rules for any mandatory standard.
5. Propose fixes in order of effort: quick fixes, policy changes, building or code work.
6. **Accommodation request.** Draft a clear request from the person or their advocate: the need, the accommodation, and the timeline asked for.
7. **Complaint.** Where refused, draft a complaint to the Chief Commissioner or State Commissioner: parties, facts, duty breached, relief, and documents.
8. Search for and read current Supreme Court and High Court authority on reasonable accommodation; tag unread items `[verify]`.

## Output

1. Gap table: barrier · duty · source · gap · fix · priority.
2. Draft accommodation request and, where needed, Commissioner complaint.
3. A response plan for the establishment, if it is the client.

## Guardrails and hand-offs

- Respect the person's privacy; collect only what the claim needs.
- Never describe a disability in demeaning terms; use the Act's language.
- Do not state compliance deadlines from memory.
- For a writ, hand off to `writ-petition-drafter`; for policy drafting, `hr-policy-handbook-drafter`.
- Before any request or complaint is sent, hand off to `pre-filing-verification-checker`.
