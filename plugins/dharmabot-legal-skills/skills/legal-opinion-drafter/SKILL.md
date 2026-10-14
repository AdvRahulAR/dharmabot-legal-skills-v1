---
name: legal-opinion-drafter
description: Drafts formal legal opinions on Indian law for clients, banks, lenders or foreign counsel, setting out the question, documents reviewed, assumptions, qualifications, analysis and opinion, with every assumption and reservation explicit and the opinion limited to Indian law. Use when a lawyer asks for a legal opinion, capacity or enforceability opinion, title or regulatory opinion, or an opinion letter for a transaction. Do not use for an internal research memo; use research-memo-drafter instead.
---

# Legal Opinion Drafter

Every output is a draft opinion for the signing advocate to verify, revise and sign; it has no effect until signed.

## Purpose

Produce an opinion the recipient can rely on within clearly stated limits, with nothing assumed silently.

## Jurisdiction gate

- The opinion covers Indian law only. Say so in the opinion.
- If the question needs foreign law (for example the law of the borrower's country or the governing law of a facility), state that no view is given on it and that counsel qualified in that jurisdiction must opine.
- Identify any State law that matters (stamp duty, registration, land).

## Required inputs

**Blocking**:
- the precise question and who will rely on the opinion;
- the documents to be reviewed (final or execution versions);
- corporate and regulatory facts the opinion depends on (constitutional documents, board and shareholder resolutions, financial statements where thresholds apply).

Also useful: the recipient's required form of opinion, the transaction timetable, and earlier opinions on the same entity.

## Method

1. Retrieve the current official text of each law, rule, master direction and notification relevant to the question (for example the Companies Act, 2013 and rules, FEMA rules and regulations on overseas investment, RBI directions), and record the version and date.
2. List the documents reviewed, with dates and versions. Nothing outside the list is opined on.
3. Draft the assumptions: genuineness of signatures, conformity of copies, capacity of foreign parties, no undisclosed documents, facts certified by officers. Keep only those needed; an assumption must not assume away the question.
4. Analyse each element of the question: corporate power and authority, approvals and limits, regulatory permissions, filings and reporting, stamp duty and execution, enforceability. Tie each to the source.
5. Draft qualifications: insolvency and equitable remedies, court discretion, stamp duty payment, public policy, matters of fact, and any unresolved legal point.
6. State the opinion in numbered paragraphs that answer the question directly, each subject to the assumptions and qualifications.
7. Add reliance and limitation language: addressee, purpose, no duty to update, date of the law.
8. Send authorities to `citation-verifier`.

## Output

1. Draft opinion: heading, question, documents reviewed, assumptions, analysis, opinion, qualifications, reliance.
2. A note to the signing advocate listing facts to certify, open points and any risk that the opinion cannot be clean.

## Guardrails and hand-offs

- Never opine on foreign law.
- Never state a regulatory limit, threshold or filing deadline without the retrieved source.
- Do not give a clean opinion where a required approval or fact is missing; qualify it or decline.
- For FEMA structuring questions, hand off to `india-entry-fema-structuring-analyst`; for background research, to `research-memo-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
