---
name: pre-filing-verification-checker
description: Runs the final pre-filing gate on any draft for an Indian court, tribunal or authority, confirming that every case, statute, quotation and pinpoint has been checked against an official or licensed source, that facts, dates and amounts match the record, and producing a verification log for the advocate to sign. Use when a lawyer says "run the pre-filing check", "verify before we file" or "give me the verification log", or when any drafting skill hands over a finished draft. Do not use to find new authorities or rewrite the draft; use legal-research-planner or adversarial-draft-reviewer instead.
---

# Pre-Filing Verification Checker

Every output is a review and a draft verification log for the advocate enrolled in India who files the document to check and sign.

## Purpose

Stop unverified material reaching a court. This is the mandatory last step for every drafting skill in this collection. It fails closed: anything not verified is listed as unverified, never passed silently.

Why it matters: in Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd. (2026 INSC 668, decided 2 July 2026) the Supreme Court set aside NCLT and NCLAT orders that relied on non-existent judgments, said that an advocate who cites AI-generated judgments without verifying them commits misconduct, and asked the Bar Council of India to frame norms (read the judgment before citing it). Responsibility stays with the advocate who signs, not with the tool.

## Jurisdiction gate

Confirm the forum (Supreme Court, High Court, district court, tribunal, arbitral tribunal or authority), the State or UT, and the filing date. The forum decides citation format, AI-disclosure duties and registry defect rules.

## Temporal gate

If the draft cites criminal, evidence or procedure law, check which code governed on the relevant dates (IPC, CrPC and Evidence Act, or BNS, BNSS and BSA, in force from 1 July 2024). Check the same for any recently replaced law.

## Required inputs

Mark as **blocking**:
- the final draft and its annexures;
- the record it relies on (pleadings, orders, documents, chronology);
- the source text, or access to an official or licensed source, for each authority.

Also useful: the citation-verifier report if already run, the forum's AI-use policy, and the registry checklist.

## Method

1. Retrieve the current official text of every statute, rule and notification cited (India Code, eGazette, the court's or regulator's website) and record the version and date retrieved.
2. List every authority: case, neutral or reporter citation, statutory provision, quotation and pinpoint paragraph or page.
3. For each case, confirm it exists from the court's website, the eCourts judgments portal or a licensed database. Record source, URL or database, and date. A citation found only in AI output or a secondary article is not verified.
4. For every quotation, hand off to `citation-verifier`, which runs its bundled script (scripts/check_quote.py in that skill) for exact-match checks. Record its result (EXACT, EXACT_AFTER_NORMALISING or NOT_FOUND) and the source hash it reports. Never repair a quotation that fails.
5. Check each proposition matches what the authority holds, and that it is not overruled, stayed or a dissent, where a citator is available. If not available, record "later treatment not checked".
6. Check statutory sections against the governing code, using `ipc-bns-concordance-mapper` for old and new criminal numbering.
7. Tie each factual assertion, date and amount to a page of the record. Check party names, cause title, case numbers and annexure references match the annexures filed.
8. Run `court-ai-policy-checker` for any AI-use disclosure or certificate the forum requires, and record it.
9. Hand registry-format defects to `efiling-bundle-defect-checker`.

## Output

1. **Verification log**, one row per item: item · type (case, statute, quote, pinpoint, fact, amount, annexure) · source checked (official or licensed, with URL or database) · date checked · method (read in full, script result and hash) · result (verified, corrected needed, not found, not checked) · checked by.
2. **Unverified items list**, most serious first, with what the advocate must do.
3. **AI-assistance note** as the forum requires.
4. **Signature block**: "I have reviewed this log and the items marked verified. Name, enrolment number, date." Left blank for the advocate.

## Guardrails and hand-offs

- Never mark an item verified unless its source text was actually read.
- Never invent a replacement authority. Point to `legal-research-planner` instead.
- Never sign or certify on the advocate's behalf. The log is unsigned until the advocate signs.
- Do not rewrite the draft. Send substantive weaknesses to `adversarial-draft-reviewer`.
- If any blocking item is unverified, say "NOT READY TO FILE" at the top.
