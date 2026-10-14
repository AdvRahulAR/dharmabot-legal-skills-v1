---
name: written-submissions-drafter
description: Drafts issue-wise written submissions, synopses, convenience compilations and briefing notes for arguing or senior counsel in Indian courts and tribunals, tying each submission to the evidence and to verified authority, within the court's page limits and practice directions. Use when an advocate asks for written arguments, written submissions, a note for arguments, synopsis, or a brief to senior counsel. Do not use to check citations alone; use citation-verifier instead.
---

# Written Submissions Drafter

Every output is a draft for an advocate enrolled in India to check and file or hand to arguing counsel.

## Purpose

Give the court, or counsel, a tight issue-wise argument with every factual point tied to the record and every legal point tied to an authority that has been read.

## Jurisdiction gate

Confirm the forum, State, case type and stage. Ask whether the court has set page limits, a format or a deadline for written submissions, and follow them.

## Required inputs

Mark as **blocking**:
- the issues framed or points for determination;
- the pleadings and the evidence (deposition and exhibit references);
- the client's position on each issue;
- any court direction on length, format or deadline.

Also useful: the other side's submissions, the judge's earlier orders in the case, and a list of authorities counsel wants used.

## Method

1. Retrieve the current official text of every statutory provision relied on and the forum's practice directions on written submissions. Record the version and date.
2. Build an issue map: issue · burden of proof · our evidence (witness, exhibit, page) · their evidence · law.
3. Draft each issue in a fixed pattern: the issue; the answer we seek; the facts proved, with record references; the law; why the other side's points fail.
4. Find authority with research tools. Read each judgment before relying on it. Quote the relevant paragraph and give the paragraph number. Prefer binding authority of the Supreme Court and the jurisdictional High Court. Tag anything not read in full `[verify]`.
5. Address adverse authority honestly and distinguish it.
6. For a convenience compilation, list documents and authorities in the order they will be referred to, with page numbers.
7. For a note to senior counsel, add a short case summary, the strongest and weakest points, likely questions from the bench, and open factual risks.
8. Fit within page limits by cutting repetition, not substance.

## Output

1. The draft written submissions or synopsis.
2. A table of authorities with citation, court, year and paragraph relied on.
3. Where requested, a compilation index or briefing note.

## Guardrails and hand-offs

- Never cite a judgment that has not been retrieved and read. Never invent paragraph numbers.
- Never misstate evidence; every factual claim carries a record reference.
- Before delivery, run `citation-verifier`. Stress test with `adversarial-draft-reviewer`. Chronology: `litigation-chronology-builder`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
