---
name: judgment-alert-digest-builder
description: Builds a periodic digest of new judgments from the Supreme Court of India, High Courts and tribunals for chosen practice areas, with one or two lines per judgment, holding, bench, date, neutral citation where available and a link to the official court site or a licensed database, each verified to exist, and flags conflicts with earlier law. Use when a lawyer asks for a "weekly judgment digest", "new arbitration judgments this week" or "case law alert for our team". Do not use for a full case note on one judgment; use judgment-case-note-summariser instead.
---

# Judgment Alert Digest Builder

Every output is a draft digest for an advocate enrolled in India to review before circulation.

## Purpose

Give a team a short, reliable list of what changed in case law this period, with every entry traceable to an official source.

## Jurisdiction gate

Record the courts and tribunals covered (for example the Supreme Court, named High Courts, NCLAT, NCLT benches) and the practice areas. For a State-specific digest, note the State's High Court and its benches.

## Required inputs

Mark as **blocking**:
- the period (start and end dates);
- the courts and tribunals;
- the practice areas or topics.

Also useful: the audience (partners, clients, students), the house format, earlier digests to avoid repeats, and access to licensed databases.

## Method

1. Retrieve judgments from official sources first: the Supreme Court website, each High Court's judgments page, the eCourts judgments portal, and tribunal websites. Use licensed databases only where the user has access. Record the source and date of each search.
2. Filter by date of pronouncement or upload within the period, and by topic using statutes and keywords. Note whether reportable.
3. Read each candidate judgment. Discard those that only follow settled law, unless the team wants them.
4. For each kept judgment, record: case name as on the court site, court and bench, date, neutral citation if assigned, case number, official link, the holding in one or two lines, and the statutes involved.
5. Verify every entry through `citation-verifier`: the judgment exists at the link, the parties, date and citation match, and the holding is what the court decided, not a submission recorded.
6. Flag conflicts: a different view from an earlier Supreme Court or coordinate-bench decision, a reference to a larger bench, or a stay or appeal if known. Mark "later treatment not checked" where no citator is available.
7. Group entries by practice area, with the most significant first.

## Output

1. The digest: heading per practice area; each entry with case name, court, bench, date, citation, link, holding and why it matters.
2. A conflicts and watch list.
3. Sources searched and the date range covered.

## Guardrails and hand-offs

- Never include a judgment that has not been read and verified to exist at the official or licensed source.
- No invented citations or links. If no neutral citation is assigned, say so.
- Follow BCI Rule 36 (believed to be the rule; confirm against the official text) limits if the digest goes outside the firm; no promotion of results.
- Full case notes go to `judgment-case-note-summariser`; regulatory circulars to `regulatory-change-impact-analyst`.
