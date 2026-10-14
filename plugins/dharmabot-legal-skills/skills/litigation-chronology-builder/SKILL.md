---
name: litigation-chronology-builder
description: Builds a source-linked chronology or list of dates and events from pleadings, documents and correspondence for Indian courts and tribunals, including the Supreme Court list of dates, with each entry tied to its source page and gaps and conflicting dates flagged. Use when an advocate asks for a list of dates, synopsis of events, timeline, chronology or dates and events. Do not use to draft the submissions or petition built on it; use written-submissions-drafter or special-leave-petition-drafter instead.
---

# Litigation Chronology Builder

Every output is a draft for the supervising advocate to check against the record.

## Purpose

Produce an accurate, sourced chronology that counsel can rely on, and a court-ready list of dates drawn from it.

## Jurisdiction gate

Note the forum the chronology is for and any format rule (for example the Supreme Court's list of dates in an SLP, or a High Court's synopsis rules). The skill itself is not jurisdiction-specific, but the court-ready version must follow that forum's format.

## Required inputs

Mark as **blocking**:
- the documents, with page numbers or a paginated compilation;
- the purpose (working file, SLP, appeal, written submissions);
- the time window and parties of interest.

Also useful: a short case theory, so material events can be marked.

## Method

1. Retrieve the forum's current official rules or practice directions on lists of dates or synopsis, and record the version and date. If none apply, record that.
2. Read every document in order. Extract each dated event with: date; event; actor; source document and page; quotation of the key words where the wording matters.
3. Normalise dates to one format. Where a document gives only a month or year, record exactly that. Do not fill in a day.
4. Flag conflicts: the same event given different dates in different sources. Show both with sources.
5. Flag gaps: periods where an event must have happened but no document shows it. List what to ask the client for.
6. Mark limitation-relevant events (cause of action, acknowledgments, receipt of orders, certified copy applications) and send them to `limitation-calculator`.
7. Mark events that are material to the case theory.
8. Produce the court-ready list of dates: concise, neutral, each entry supported by the record, in the forum's format.

## Output

1. A working chronology table: date · event · actor · source and page · note (conflict, gap, material, limitation).
2. A court-ready list of dates.
3. A list of gaps and conflicts with suggested documents to obtain.

## Guardrails and hand-offs

- Never fill a gap by assumption or "likely" dates.
- Every entry must cite its source page.
- Keep the court-ready version factual; argument belongs elsewhere.
- Next: `written-submissions-drafter`, `special-leave-petition-drafter`.
