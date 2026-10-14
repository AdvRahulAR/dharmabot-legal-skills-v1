---
name: foreign-law-research-memo-drafter
description: Researches a question of US (federal or State), UK (England and Wales), EU, UAE (onshore, DIFC, ADGM) or Singapore law from official primary sources and drafts a research memo with citations in the jurisdiction's style (Bluebook, OSCOLA and others) for review by counsel qualified there. Use when an Indian lawyer supporting a foreign firm, or advising an Indian client on a foreign issue, needs a sourced research note. Do not use to give final advice on foreign law; the memo is research for qualified counsel.
---

# Foreign Law Research Memo Drafter

Every output is a research draft for review by a lawyer qualified in that jurisdiction.

## Purpose

Produce an accurate, fully sourced research memo on a foreign-law question. Every authority comes from a source that was actually read, and the limits of the research are stated.

## Jurisdiction gate

Identify the jurisdiction precisely: the US State or federal law, England and Wales or Scotland, the EU instrument and member State, UAE onshore or DIFC or ADGM. If the user's question mixes jurisdictions, split it. Say who will review the memo, and mark it "Research memo – not legal advice – for review by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the question, stated narrowly;
- the jurisdiction;
- the relevant facts;
- the date the law is needed as of.

Also useful: the instructing lawyer's preferred format and citation style, and known starting authorities.

## Method

1. Read `references/foreign-jurisdictions.md` for official sources in each jurisdiction.
2. Plan the research: the statutes, regulations, cases and secondary sources to check, with search terms.
3. Retrieve primary sources from official sites (for example eCFR, GovInfo, Congress.gov, State legislatures, CourtListener; legislation.gov.uk, Find Case Law; EUR-Lex, CURIA; UAE Legislation, DIFC and ADGM Courts; Singapore Statutes Online, eLitigation). Note the version and as-of date of each statute.
4. For each authority, record the citation in the jurisdiction's style, a pinpoint, a short quotation (checked with `citation-verifier`), and its weight (binding, persuasive, which court). Check for later treatment where a citator is available; otherwise say treatment was not checked.
5. In the UAE onshore, note that the primary language of legislation and courts is Arabic and that English versions may be unofficial translations.
6. Write the memo: question presented, short answer, facts assumed, analysis by issue, open questions, and authorities consulted.

## Output

1. The memo, in the format and citation style requested.
2. A table of authorities, with source URLs and the date checked.
3. A list of research gaps and items to confirm.

## Guardrails

- Never cite an authority not actually read in this session. Never invent citations.
- Do not express foreign-law conclusions as advice; frame them as research findings.
- Hand off to `citation-verifier` before delivery.
