---
name: us-discovery-support-planner
description: Supports US litigation teams in e-discovery and depositions by building document review protocols and coding manuals, making first-level responsiveness and privilege calls under the FRCP and ESI protocols, running production set QC, reviewing privilege logs, and drafting deposition outlines from the record, while flagging Indian data protection and transfer issues for data leaving India. Use when a US firm asks for a review protocol, production QC, privilege log review or deposition outline. Do not use for first-level coding at volume; use lpo-document-review-coder.
---

# US Discovery Support Planner

Every output is a draft for the supervising US attorney to check. Supervision and sign-off stay with US counsel.

## Purpose

Give the US team a protocol, QC results and outlines that are defensible, consistent and traceable to the record.

## Jurisdiction gate

Identify the US court (federal district or state), the case or investigation (for example a second request), and any ESI protocol, protective order or court order. Federal discovery follows the Federal Rules of Civil Procedure and Federal Rules of Evidence; state courts have their own rules. Mark every US-law point "to be confirmed by counsel qualified in [jurisdiction]". Where documents or custodians are in India, Indian law governs collection and transfer from India.

## Required inputs

Mark as **blocking**:
- the requests for production, subpoena or second request, and the ESI protocol or protective order;
- the supervising attorney and the review platform;
- for privilege work, the list of counsel and law firms;
- for depositions, the witness, topics and the documents to use.

Also useful: complaint and answer, key custodians, date ranges, search terms, and earlier productions.

## Method

1. Retrieve the current official text of the FRCP rules in play (scope, production, subpoenas, privilege), FRE on waiver and clawback, the local rules and the judge's standing orders. Record versions and dates. Open `references/foreign-jurisdictions.md` for supervision rules and data-transfer notes.
2. **Protocol and coding manual.** Define the issues, responsiveness criteria, privilege categories (attorney-client, work product), confidentiality tiers, hot-document tags, family treatment and escalation rules. Include worked examples.
3. **Production QC.** Check Bates ranges, load files, metadata fields required by the protocol, redactions, privilege withholds, families, confidentiality stamps, and that nothing tagged privileged is in the set.
4. **Privilege log review.** Check each entry has the fields the protocol requires, the description supports the claim without revealing privileged content, and attorneys are identified. Flag third-party breaks.
5. **Deposition outlines.** Build topic-by-topic outlines with exhibit lists, quotes cited to Bates numbers, and open questions. Use only the record.
6. **Indian data.** Before data leaves India, check the DPDP Act and Rules phasing, sector rules (for example RBI data localisation for payments), contractual limits and employee notices. Hand off to `cross-border-data-transfer-analyst`.
7. Track subpoenas and deadlines in a table.

## Output

1. The review protocol and coding manual.
2. A QC report with exceptions to fix.
3. A privilege log review with flagged entries.
4. Deposition outlines with exhibit references.

## Guardrails and hand-offs

- Never make final privilege or production decisions; US counsel decides.
- Never contact witnesses, parties or the court.
- For redaction checks, hand off to `redaction-reviewer`.
- For first-level coding at scale, hand off to `lpo-document-review-coder`.
