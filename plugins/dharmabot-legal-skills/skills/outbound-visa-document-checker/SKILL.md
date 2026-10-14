---
name: outbound-visa-document-checker
description: Supports Indians applying for foreign visas, study or work permits and emigration by building document checklists from official guidance supplied, drafting affidavits (name, birth, relationship, sponsorship, no objection), planning police clearance through Passport Seva, apostille and attestation, and checking Emigration Act 1983 and eMigrate duties for ECR countries. Use when a client is applying for a UK, US, Canada, Australia, Gulf or EU visa and needs Indian documents. Do not use for foreign eligibility advice; use foreign-law-research-memo-drafter with counsel abroad.
---

# Outbound Visa Document Checker

Every output is a draft for an advocate enrolled in India to check. Foreign eligibility is for qualified advisers in that country.

## Purpose

Make sure the Indian documents an applicant submits are complete, consistent, properly executed and legalised, without straying into foreign immigration advice.

## Jurisdiction gate

Identify the destination country, the visa or permit category, and the applicant's State of residence in India. Indian law governs the affidavits, police clearance, apostille or attestation and emigration clearance. Destination rules are foreign law: use only the official guidance the client supplies or that is retrieved from the destination government's site, and mark eligibility points "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the destination country and exact visa or permit category;
- the destination's official document checklist or guidance (or permission to retrieve it);
- the applicant's identity documents and any mismatches in names or dates across them.

Also useful: education and employment records, sponsor details, marriage or birth certificates, earlier refusals and travel history.

## Method

1. Retrieve the current official text of the destination's document guidance, the Passport Seva police clearance process, MEA apostille and attestation rules, and the Emigration Act and eMigrate guidance. Record versions and dates. Open `references/foreign-jurisdictions.md` for apostille and attestation status by country.
2. Build a checklist: each required document · held · issues · action.
3. Find inconsistencies (name spellings, dates of birth, parents' names). Recommend the lawful fix: an affidavit, a gazette notification for name change, or correction at source. An affidavit does not cure every mismatch; say so.
4. Draft affidavits and declarations needed from India: one-and-the-same-person, birth, relationship, sponsorship and support, parental consent for minors, and employer no-objection letters. Use only facts the client confirms.
5. Plan police clearance and its validity window.
6. Plan legalisation: apostille for Apostille Convention countries; the attestation chain for others (for example the UAE). Hand off detail to `document-legalisation-planner`.
7. Check emigration: whether the destination is an ECR country and whether the passport is ECR or ECNR; registration on eMigrate for employment where required; and use of registered recruiting agents only.
8. Plan translations where the destination requires them, through `legal-translation-verifier`.

## Output

1. A document checklist with status and actions.
2. Draft affidavits and letters.
3. A legalisation and emigration plan with sequence.

## Guardrails and hand-offs

- Never draft false or backdated documents or affidavits; refuse and explain.
- Never advise on visa eligibility or prospects under foreign law.
- For foreign-law questions, hand off to `foreign-law-research-memo-drafter`.
