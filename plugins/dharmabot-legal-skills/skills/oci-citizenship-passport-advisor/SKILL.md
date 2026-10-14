---
name: oci-citizenship-passport-advisor
description: Advises on Indian citizenship and travel documents under the Citizenship Act 1955 and Rules (registration, naturalisation, OCI cardholder registration and cancellation, renunciation and surrender certificates) and the Passports Act 1967 (issue, refusal, impounding, revocation, police verification, appeals and writs), and drafts representations and appeals. Use when an OCI card is cancelled or refused, a passport is impounded or refused, or a client needs to renounce or regain citizenship. Do not use to draft the writ petition itself; use writ-petition-drafter.
---

# OCI, Citizenship and Passport Advisor

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Explain the client's status and options, and draft the representation or appeal that fits the order made.

## Jurisdiction gate

Confirm the question is about Indian citizenship, OCI status or an Indian passport. Identify where the client lives and which authority acted (MHA, FRRO, an Indian mission abroad, a Regional Passport Office). Questions about the client's foreign nationality (for example whether the other country allows dual nationality) are foreign law: mark them "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

The Citizenship Act and Rules have been amended several times (including 2019 and the 2024 rules), and OCI rights are set by notifications that have changed. Record the dates of the order, of acquiring foreign citizenship, and of any travel on an Indian passport after that.

## Required inputs

Mark as **blocking**:
- the order or notice (cancellation, refusal, impounding, show-cause), with its date and issuing authority;
- the client's current nationality or nationalities and how and when each was acquired;
- for a minor, both parents' nationality and the child's place of birth.

Also useful: the OCI card or passport details (not to be stored), social media or other material relied on by the authority, earlier replies, and travel history.

## Method

1. Retrieve the current official text of the Citizenship Act and Rules, the OCI notifications, the Passports Act and Rules, and MHA and MEA guidance on the OCI and Passport Seva portals. Record versions and dates. Open `references/foreign-jurisdictions.md` for foreign official sources and legalisation needs.
2. Identify the provision used. OCI registration and cancellation are believed to be in sections 7A to 7D; impounding and revocation of passports in section 10 and appeals in section 11 of the Passports Act. Confirm each from the text.
3. Test the order: was a show-cause notice given, were reasons recorded, was the ground one the statute allows, and was the material disclosed? Note where reasons can be withheld in the public interest and how courts have treated that. Search for and read current authority, starting with Maneka Gandhi v Union of India (Supreme Court, 1978; confirm current treatment).
4. Check limits on review. Courts give weight to the executive in citizenship and security matters; explain this plainly.
5. Map remedies: a representation or review to the authority, a statutory appeal where one exists, and a writ petition in the High Court. Compute deadlines with `limitation-calculator`.
6. For renunciation or surrender certificates, list documents and the consequences of late surrender.
7. Draft the representation or appeal from the record only. Tag anything not read in full `[verify]`.

## Output

1. A status note: what the client is now, what the order does, and what follows.
2. Options with steps and deadlines.
3. The draft representation or appeal with an annexure list.

## Guardrails and hand-offs

- Never advise concealing a foreign nationality or misusing an Indian passport.
- Never predict the outcome of a security-based decision.
- For a writ, hand off to `writ-petition-drafter`.
- For documents executed abroad, hand off to `document-legalisation-planner`.
