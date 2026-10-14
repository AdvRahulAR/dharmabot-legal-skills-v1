---
name: foreign-matter-scoping-analyst
description: Scopes a matter with a foreign element for an Indian lawyer. Identifies the governing law, forum and every jurisdiction involved (India, US, UK, UAE including DIFC and ADGM, EU, Singapore and others), which parts the Indian lawyer can handle, which need locally qualified counsel, and which cross-border skills to use next. Use at the start of any cross-border instruction, when a foreign law firm sends work, or when someone asks "can I advise on this" or "which law applies". Do not use for purely domestic Indian matters.
---

# Foreign Matter Scoping Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Before any substantive work starts, map the jurisdictions, laws and forums involved, decide what an Indian lawyer can properly do, and plan the rest of the work.

## Jurisdiction gate

This skill exists to find the jurisdictions involved, so it does not stop on a foreign element. It must not give substantive advice on foreign law as if from a lawyer qualified there. Mark every foreign-law point "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- who the client is and where they are (or the instructing foreign law firm, and its client);
- the parties and their places of incorporation or residence;
- what the client wants (transaction, dispute, compliance, opinion, document review);
- the key documents, or at least their governing-law and dispute-resolution clauses.

Also useful: where the assets, performance and evidence are; any proceedings already started anywhere; and deadlines.

## Method

1. Read `references/foreign-jurisdictions.md` for India's treaty position, court structures and sources.
2. List every connecting factor: parties' locations, place of contracting and performance, assets, governing-law and forum clauses, and where enforcement may be needed.
3. For each issue, identify the governing law (express choice, or what Indian conflict-of-laws rules and the likely foreign forum would apply) and the competent forum. In the UAE, distinguish onshore courts from DIFC and ADGM. In the US, identify the State. In the EU, identify the member State as well as EU law. In the UK, identify which of its legal systems applies.
4. Split the work:
   - **Indian law:** the Indian advocate can advise.
   - **Foreign law:** needs locally qualified counsel. The Indian lawyer may research, review documents or support under that counsel's supervision, as the relevant rules allow.
   - **International arbitration and treaty points:** check the specific rules.
5. Check professional limits:
   - the Advocates Act, 1961 and BCI rules for the Indian lawyer;
   - the BCI Rules on Foreign Lawyers and Foreign Law Firms if a foreign lawyer is working in India;
   - for US matters, the supervising US lawyer's duties under ABA Model Rules 5.1, 5.3 and 5.5 and Formal Opinion 08-451;
   - for UK matters, the SRA outsourcing position.

   Retrieve the current text of each.
6. Flag urgent points: limitation in each jurisdiction, interim relief, asset dissipation, sanctions exposure.
7. Recommend the next skills and the order to run them in, naming each by exact folder id in backticks in the response.

## Output

1. A jurisdiction map table: issue · governing law · forum · who can advise · source.
2. Work split: Indian lawyer, foreign counsel, joint.
3. Urgent points and deadlines.
4. A recommended plan, with the skills to run next, for example `foreign-client-engagement-checker`, `cross-border-contract-reviewer`, `foreign-judgment-award-enforcement-analyst`, `international-arbitration-planner`, `cross-border-data-transfer-analyst`, `document-legalisation-planner`, `cross-border-service-evidence-planner`, `foreign-law-research-memo-drafter`, `lpo-document-review-coder` and `india-entry-fema-structuring-analyst`.

## Guardrails

- Never present foreign-law conclusions as advice from a lawyer qualified there.
- Run a conflict check before substantive work: hand off to `foreign-client-engagement-checker`.
- Treat the treaty table as a starting point. Confirm each point from official sources.
