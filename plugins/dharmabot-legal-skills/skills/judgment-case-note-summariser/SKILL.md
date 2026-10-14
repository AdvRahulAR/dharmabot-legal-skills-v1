---
name: judgment-case-note-summariser
description: Produces a case note from an Indian judgment covering bench, citation, facts, issues, holdings, ratio decidendi, obiter, statutes considered and later treatment where supplied, and maps a set of authorities on one point into a table showing court, bench strength, holding, whether followed, distinguished or overruled, High Court conflicts and binding or persuasive value. Use when a lawyer asks for a case note, judgment summary, headnote or precedent map. Do not use to check whether citations exist; use citation-verifier instead.
---

# Judgment Case Note Summariser

Every output is a draft case note for the advocate to check against the judgment.

## Purpose

Capture what a judgment actually decided, and how it fits with other authority, so the advocate can rely on it accurately.

## Jurisdiction gate

- Confirm the court (Supreme Court, a High Court, tribunal or foreign court) and the bench strength.
- For binding value, record the forum where it will be used. A High Court judgment binds courts subordinate to it; elsewhere it is persuasive.
- Foreign judgments are persuasive only; mark them so.

## Temporal gate

Note the date of the judgment and the version of the law it applied. If the provisions have since been replaced or renumbered (for example IPC to BNS, CrPC to BNSS, Evidence Act to BSA), add the likely corresponding provision as "to be confirmed with `ipc-bns-concordance-mapper`".

## Required inputs

**Blocking**: the full text of the judgment (or each judgment for a precedent map). A headnote or news report is not enough; ask for the full text.

Also useful: the point the advocate cares about, later judgments that cite it, and the forum where it will be used.

## Method

1. Retrieve the official copy of the judgment from the court's website or a reliable reporter, and record the citation, neutral citation if any, and date accessed.
2. Record: case name, court, bench and judges, date, citation, counsel if relevant, and the provisions considered.
3. Summarise the facts briefly and the procedural history.
4. State the issues as the court framed them.
5. Give the holding on each issue with paragraph numbers.
6. Separate ratio from obiter. Explain why each statement is one or the other. Note concurring and dissenting opinions.
7. Later treatment: record only what the user supplies or what you have read. Never infer that a judgment was followed or overruled. If not checked, say "later treatment not checked".
8. For a precedent map: one row per authority, sorted by court and bench strength, with holding, relation to others, and conflicts between High Courts. Mark which binds the user's forum.
9. Send the citation list to `citation-verifier`.

## Output

1. Case note with paragraph references.
2. Precedent map table, if asked: case · court · bench · date · holding · treatment · binding or persuasive.
3. Points of uncertainty, tagged `[verify]`.

## Guardrails and hand-offs

- Never invent subsequent history, paragraph numbers or quotations.
- Quote the judgment only from the text supplied or retrieved.
- Hand off to `research-memo-drafter` if the advocate needs analysis built on the note.
