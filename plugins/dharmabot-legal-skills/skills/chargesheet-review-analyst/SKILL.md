---
name: chargesheet-review-analyst
description: Reviews a police report or chargesheet under the Bharatiya Nagarik Suraksha Sanhita, 2023 with its witness statements, seizure memos, forensic and medical reports, mapping evidence to each offence ingredient and flagging investigation lapses, missing sanction, delay, electronic evidence certificate defects under the Bharatiya Sakshya Adhiniyam and contradictions. Use when an advocate asks to go through a chargesheet, list gaps in the prosecution case, or prepare a victim-side note on a weak investigation. Do not use to draft the discharge application itself; use discharge-application-drafter.
---

# Chargesheet Review Analyst

Every output is a review for an advocate enrolled in India to check.

## Purpose

Produce a page-referenced gap note on a police report for the defence, or for the victim where the investigation is weak.

## Jurisdiction gate

Confirm the police report was filed before an Indian court. Record the State, court and police station. Note any special statute (NDPS, POCSO, SC/ST Act, UAPA, PMLA) with its own procedure or presumptions, and use `ndps-case-analyst` or `pocso-case-analyst` alongside where relevant.

## Temporal gate

Record the dates of offence, FIR, investigation steps and filing. Before 1 July 2024 the CrPC and Indian Evidence Act may govern parts of the investigation; check with `crpc-bnss-transition-analyst`.

## Required inputs

**Blocking**: the full police report with all annexed documents and the list of documents relied on; the offences; whom the user acts for.

Also useful: the FIR, case diary extracts supplied, earlier bail orders and the client's account (kept separate from the record).

## Method

1. Retrieve the current official text of the offences, the BNSS provisions on the police report, statements, search, seizure, medical examination and audio-video recording of searches, and the BSA provisions on electronic records (certificate believed to be under s.63 BSA; confirm). Record source and date.
2. Index the record: every document with page range, date and author.
3. Build an ingredient matrix: each offence, each ingredient, the evidence for it, and its page.
4. Build a witness table: each witness, what they saw, when their statement was recorded, and contradictions with others and with documents.
5. Check investigation steps: delay in FIR or statements; independent witnesses at seizure; mandatory videography where required; sealing and forwarding to the laboratory; chain of custody; test identification; site plan; arrest compliance.
6. Check legal preconditions: sanction for prosecution, special-statute approvals, and limitation for taking cognizance where applicable.
7. Check electronic evidence: what device, who extracted it, hash and certificate status. Hand off certificate issues to `bsa-electronic-evidence-certificate-drafter`.
8. Check missing documents the accused is entitled to, and plan an application for them.
9. Search for authority on each lapse only as needed. Read it; tag anything unread `[verify]`.

## Output

1. Record index.
2. Ingredient matrix and witness table, with page references.
3. Gap note in order of importance: fatal, serious, minor.
4. Action list: discharge, documents to call for, expert evidence, and trial preparation.

## Guardrails and hand-offs

- Stay within the record. Do not grade witness credibility beyond contradictions visible on paper.
- Never invent a page, statement or report finding.
- Mark the client's own account separately from the record.
- Next steps go to `discharge-application-drafter` or `criminal-trial-readiness-checker`.
