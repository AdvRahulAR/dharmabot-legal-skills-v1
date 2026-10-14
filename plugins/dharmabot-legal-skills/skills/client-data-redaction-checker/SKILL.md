---
name: client-data-redaction-checker
description: Pseudonymises client material before it goes to any AI tool, replacing names, Aadhaar, PAN, account, phone and case numbers, addresses and health data with consistent placeholders, and keeps a re-identification map only on the user's machine, in line with advocates' confidentiality duties and the DPDP Act, 2023. Use when a lawyer says "strip the client identifiers", "anonymise this file before AI" or "mask names and keep a key". Do not use to review redactions for production or court filing; use redaction-reviewer instead.
---

# Client Data Redaction Checker

Every output is a draft pseudonymised file and a review of residual risk for the advocate to check before any AI use.

## Purpose

Let a lawyer use AI on a matter without sending client identities to the AI provider. Replace identifiers with stable placeholders, keep the key locally, and flag what still identifies the client.

## Jurisdiction gate

Confirm the matter is handled by an Indian advocate, firm, legal department or legal-aid body, and whether any foreign data law also applies (for example GDPR for EU clients). Note whether the matter involves children, sexual offences or health, where identity protection is stricter.

## Temporal gate

The DPDP Act, 2023 and the DPDP Rules, 2025 are being brought into force in phases. Check which provisions are in force on today's date and record the notification relied on.

## Required inputs

Mark as **blocking**:
- the material to be pseudonymised;
- a local folder where the re-identification map can be saved;
- confirmation that this skill is running locally (for example a local Claude Code or Codex session on the user's machine), or that the user accepts the raw text is already with this tool.

Also useful: the AI tool and purpose, and identifiers the user wants kept (for example a public company's name).

## Method

1. Retrieve the current official text of the DPDP Act and Rules (India Code, eGazette, MeitY), the Aadhaar Act provisions on storing and displaying Aadhaar numbers, and the protections on victim and child identity (believed to be section 72 of the BNS; also POCSO and the Juvenile Justice Act). Record version and date.
2. Detect identifiers: personal names and aliases; Aadhaar, PAN, passport, voter ID and driving licence numbers; bank account, card, UPI and loan numbers; phone numbers and email addresses; addresses, survey numbers and PIN codes; vehicle numbers; case, FIR and crime numbers; dates of birth; employer and school names.
3. Flag special categories: health and medical records, children, sexual offence victims, caste, religion, sexual orientation, financial distress and biometric data. Default to removing them unless the task needs them.
4. Replace each identifier with a consistent typed placeholder (PERSON_1, ACCOUNT_2, ADDRESS_3). The same person keeps the same placeholder across all files. Keep relationships readable ("PERSON_1's wife PERSON_2").
5. Write the re-identification map to a local file in the user's chosen folder. Never print the map, or any original value, in the AI conversation or output.
6. Re-scan the output for leaks: initials, nicknames, unique job titles, rare places, signatures, metadata, file names and image text. Check scanned pages for text the scan missed.
7. Assess residual risk: can the client still be identified from context? Suggest generalising (a city instead of a street, a year instead of a date).

## Output

1. The pseudonymised text or files.
2. Path to the local re-identification map (contents never shown).
3. Residual-risk note: high, medium or low, with items left in and why.
4. A short DPDP note: the lawyer as data fiduciary, purpose limitation, reasonable security safeguards, and the need for processor terms with the AI provider.

## Guardrails and hand-offs

- Pseudonymised data is still personal data if it can be re-identified. Say so.
- Never upload the map or put it in prompts, memory or shared drives without the user's instruction.
- Never claim the redaction is complete. The advocate checks it.
- Ethics questions on client consent go to `professional-conduct-advisor`.
- Redaction for production or court filing goes to `redaction-reviewer`.
- Whether the AI tool is acceptable at all goes to `legal-ai-vendor-screener`.
