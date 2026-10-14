---
name: pleadings-matrix-builder
description: Builds a paragraph-level matrix of a civil suit's pleadings under the Code of Civil Procedure, setting each averment against the opponent's admission, specific denial, evasive denial or silence, with deemed admissions, proposed issues, burden of proof, the evidence needed for each issue and admissions usable for judgment. Use when a lawyer says "build a pleadings matrix", "suggest issues for framing" or "what has the defendant admitted". Do not use to draft the pleadings themselves or plan witness questions; use written-statement-drafter or cross-examination-planner instead.
---

# Pleadings Matrix Builder

Every output is a draft analysis for an advocate enrolled in India to check.

## Purpose

Show, paragraph by paragraph, what is admitted, what is truly in dispute, and what each side must prove, so issues can be framed and evidence planned.

## Jurisdiction gate

Confirm the suit is before an Indian civil or commercial court and note the State or UT, court and suit type. Commercial suits under the Commercial Courts Act, 2015 have stricter denial rules for written statements. Note any High Court original-side rules that change pleading practice.

## Required inputs

Mark as **blocking**:
- the plaint, written statement and any replication, rejoinder, counter-claim and written statement to counter-claim, with paragraph numbers;
- whether the suit is a commercial suit;
- which party the advocate acts for.

Also useful: documents filed with the pleadings, any amendment applications or orders, and issues already framed.

## Method

1. Retrieve the current official text of the Code of Civil Procedure provisions on pleadings, denials and deemed admissions (Order VIII, including the commercial-suit amendments), framing of issues (Order XIV), admissions (Order XII) and examination of parties (Order X), with the relevant High Court rules. Record version and date. Confirm every rule number from the source.
2. Number each averment in the plaint (and counter-claim) as a separate row. Split compound paragraphs into separate factual propositions.
3. Against each row, record the opponent's response with its paragraph: admitted, specifically denied, denied with a different version, evasive or general denial, not traversed, or "no knowledge".
4. Classify the legal effect: admitted, deemed admitted (state why and the rule relied on), or in issue. For commercial suits, test denials against the stricter requirement to give reasons and a positive version.
5. Note preliminary objections (limitation, jurisdiction, valuation and court fee, non-joinder, bar of suit) as separate issues of law or mixed issues.
6. Draft proposed issues in the conventional form ("Whether the plaintiff proves that ..."), each linked to the rows it arises from. Put issues of law triable first separately.
7. For each issue, record the burden of proof and the documents and witnesses needed, and the documents already on record.
8. List admissions usable for a judgment on admission or to narrow trial, with paragraph pinpoints.

## Output

1. The matrix: row · averment (para) · response (para) · classification · effect · linked issue · evidence needed.
2. Proposed issues, with burden and supporting rows.
3. Admissions list with pinpoints.
4. Gaps: averments the client's side has not supported with documents.

## Guardrails and hand-offs

- Quote pleadings accurately with paragraph numbers. Do not paraphrase an admission into something stronger.
- Never invent case law on deemed admission. Search, read and tag uncertain authority `[verify]`.
- Witness questioning goes to `cross-examination-planner`; evidence affidavits to `evidence-affidavit-drafter`; arguments to `written-submissions-drafter`.
