---
name: court-ai-policy-checker
description: Checks the published AI-use policies, circulars and practice directions of the Supreme Court, High Courts, district courts, tribunals and arbitral institutions in India, and judicial warnings on AI-generated citations, then states what disclosure, certification or restriction applies to a filing, with the source and date checked. Use when a lawyer asks "do we need to disclose AI use", "is there an AI policy in this court" or "can we file AI-assisted submissions". Do not use for general ethics questions; use professional-conduct-advisor instead.
---

# Court AI Policy Checker

Every output is a review for the advocate filing the document to check.

## Purpose

Tell the advocate, for one forum and one filing, what the forum's own rules say about AI use: disclosure, certification, prohibited uses, and the consequences of unverified output.

## Jurisdiction gate

Identify the exact forum: court, bench or seat, the State or UT, and for district courts the High Court that supervises them. For arbitrations, identify the institution and seat. Policies differ by High Court, and a policy for judges may not bind advocates.

## Temporal gate

AI policies are new and change often. Record the date of each policy found and check for later circulars, amendments or withdrawals up to the filing date.

## Required inputs

Mark as **blocking**:
- the forum and case type;
- how AI was used (research, first draft, translation, summarising evidence, generating citations);
- the filing date.

Also useful: the AI tool used, and whether client data went into it.

## Method

1. Retrieve the current official text of any AI-use policy, circular, notification or practice direction from the forum's own website, and the rules of the supervising High Court. Record the URL, title, date and version.
2. Search the forum's notices and circulars pages, the High Court's notifications, and the arbitral institution's rules and guidance. For example, the Kerala High Court reportedly issued a 2025 policy on AI use for the district judiciary (confirm current text and whether it reaches advocates).
3. Search for judicial warnings or decisions on AI-generated or non-existent citations. For example, in Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd. (2026 INSC 668, decided 2 July 2026) the Supreme Court set aside tribunal orders resting on non-existent judgments, said that an advocate citing AI-generated judgments without verification commits misconduct, and asked the Bar Council of India to frame norms; check whether those norms have since issued. Read any authority before relying on it and tag the rest `[verify]`.
4. For each instrument found, record: who it binds (judges, staff, advocates, parties), what it requires, and whether it covers this use.
5. Map the result to the filing: disclosure needed or not; certificate or undertaking wording if prescribed; prohibited uses; verification duties.
6. If nothing is found, say "no published policy found as of [date] in [sources searched]". Do not treat silence as permission. Recommend the advocate's own verification regardless.

## Output

1. A one-line answer: disclosure required, recommended, or not found.
2. A table: instrument · issuing authority · date · binds whom · requirement · applies to this filing (yes, no, unclear) · source URL.
3. Draft disclosure or certificate wording, only where the forum prescribes or the advocate chooses to disclose.
4. Sources searched and date checked.

## Guardrails and hand-offs

- Never invent a policy, circular number or date. Quote only what was read.
- Do not answer general ethics or confidentiality questions. Hand off to `professional-conduct-advisor`.
- Record the result in the verification log through `pre-filing-verification-checker`.
