---
name: research-memo-drafter
description: Drafts objective internal research memos on Indian law in question, short answer, facts, analysis and conclusion form, weighing contrary authority and research gaps, and drafts policy notes and submissions to public consultations by ministries and regulators. Every proposition is tied to a source supplied or marked for verification. Use when a lawyer asks for a research memo, legal memo, policy note or consultation response. Do not use for a signed opinion to a client or lender; use legal-opinion-drafter instead.
---

# Research Memo Drafter

Every output is a draft memo for supervising counsel to check before anyone relies on it.

## Purpose

Give the reader a balanced, sourced answer to a defined question, with the weaknesses and gaps visible.

## Jurisdiction gate

- Confirm the question is under Indian law and record the State or UT and forum.
- Identify which courts' decisions bind the forum.
- Foreign-law points go to `foreign-law-research-memo-drafter` and are marked to be confirmed by counsel qualified there.

## Temporal gate

Record the dates of the relevant events. If the law changed around them (new criminal codes, Labour Codes, Income-tax Act 2025, Mediation Act 2023, DPDP Rules phasing, new State tenancy laws), say which version applies and why, and check whether the new law is in force and from when.

## Required inputs

**Blocking**:
- the question and the facts;
- the sources gathered so far, or permission to research from official sources;
- the purpose (internal advice, litigation, policy submission) and the reader.

Also useful: a research plan from `legal-research-planner`, word limit, deadline, and the house style.

## Method

1. Retrieve the current official text of each statute, rule and notification relied on (India Code, eGazette, regulator sites) and record the version and date.
2. Restate the question precisely. Split it into issues.
3. For each issue, read the primary sources. Read judgments in full before citing; record the paragraph relied on. Anything not read in full is tagged `[verify]`.
4. Analyse each issue: the rule, how courts have applied it, how it applies to these facts, the strongest contrary argument and authority, and the answer on that issue.
5. Note gaps: facts needed, unresolved questions, conflicting High Courts, pending references to larger benches.
6. Write the short answer last, in three to five sentences, with the level of confidence.
7. For policy notes and consultation submissions: summarise the proposal, identify the legal basis and constitutional limits, compare with existing law, and give numbered recommendations with drafting suggestions. Respect the consultation's format and deadline.
8. Send the citation list to `citation-verifier` before delivery.

## Output

1. Memo: question · short answer · facts and assumptions · analysis by issue · conclusion · gaps and next steps.
2. Table of authorities with a read-in-full column.
3. For consultations: submission with numbered comments, each tied to a clause of the draft.

## Guardrails and hand-offs

- Never fabricate a citation, quotation, paragraph number or section number.
- Present contrary authority fairly; do not bury it.
- Do not convert the memo into advice to a client without the advocate's review.
- Hand off to `adversarial-draft-reviewer` for a stress test, and to `legal-opinion-drafter` if a formal opinion is needed.
