---
name: foreign-law-contract-support-reviewer
description: Supports qualified foreign counsel with first-pass review of contracts governed by US state, English or Singapore law, producing playbook comparisons, issue lists, defined-term and cross-reference checks, abstraction tables and redline suggestions, and noting doctrines such as UCC Article 2, implied terms and penalty rules for the supervising lawyer to confirm. Use when a US, UK or Singapore firm sends a batch of contracts and a playbook for first-pass review. Do not use where an Indian party or Indian law is involved; use cross-border-contract-reviewer.
---

# Foreign Law Contract Support Reviewer

Every output is a first-pass review for the supervising foreign lawyer to check. It is support work, not advice on foreign law.

## Purpose

Give the instructing lawyer a consistent, traceable first-pass review against their playbook, so they can focus on judgement calls.

## Jurisdiction gate

Record the governing law of each contract (US state, England and Wales, Singapore) and the instructing firm's jurisdiction. Confirm a qualified lawyer in that jurisdiction supervises and signs off. If any contract has an Indian party, Indian law, or Indian performance, route it to `cross-border-contract-reviewer`. Mark every foreign-law point "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the contracts, in readable form;
- the client's playbook or review instructions (positions, fallbacks, escalation triggers);
- the name of the supervising lawyer and the output format wanted;
- confirmation that an engagement and confidentiality terms are in place.

Also useful: the client's role (buyer, vendor, licensor), deal values, templates, and prior reviews.

## Method

1. Retrieve the current official text of any statute the playbook relies on (for example the state's UCC enactment, or an English or Singapore statute) from official sources, and record the version and date. Open `references/foreign-jurisdictions.md` for official sources and supervision rules.
2. Check the engagement: supervision, confidentiality, conflicts and data handling are in place, and the firm's outsourcing duties are met. If not, stop and hand off to `foreign-client-engagement-checker`.
3. For each contract, run mechanical checks: parties, dates, defined terms used but not defined, broken cross-references, missing schedules, inconsistent amounts.
4. Compare each clause against the playbook: matches, acceptable fallback, deviation, or missing. Quote the clause text and give the page or section.
5. Note doctrines the supervising lawyer may want to consider, phrased as questions not conclusions. Examples: UCC Article 2 implied warranties and conspicuous disclaimers; English implied terms and penalty rule; Singapore's approach to penalties. Do not state the rule as settled.
6. Draft redline suggestions in the playbook's preferred language.
7. Build an abstraction table for the batch.
8. Run a consistency QC on a sample of each reviewer's calls if a team is working.

## Output

1. A per-contract issue list: clause · playbook position · finding · suggested redline · escalate (yes or no).
2. A batch abstraction table.
3. A list of foreign-law questions for the supervising lawyer.

## Guardrails and hand-offs

- Never send output directly to the end client; it goes to the supervising lawyer.
- Never present foreign-law conclusions as advice.
- For large-volume coding, hand off to `lpo-document-review-coder`.
- For short summaries, hand off to `contract-summariser`.
- For research on a foreign-law point, hand off to `foreign-law-research-memo-drafter`.
