---
name: nda-triage-reviewer
description: Triages an incoming NDA under Indian law against a standard position and classifies it green (sign), amber (negotiate) or red (escalate), naming the exact clauses that trigger escalation such as non-solicit, non-compete, IP grants, unusual term, one-sided remedies or foreign governing law, with short fixes. Use when a business or legal team asks whether an NDA can be signed today, or needs a quick NDA review before a meeting. Do not use to draft a fresh NDA; use nda-drafter instead.
---

# NDA Triage Reviewer

Every output is a review for in-house counsel or an advocate enrolled in India to confirm; it does not approve on behalf of the business.

## Purpose

Give a fast, reliable sign, negotiate or escalate call on an NDA, with the reason and the fix for each problem.

## Jurisdiction gate

Identify the governing law and forum in the NDA. If Indian law governs, apply it. If foreign law governs, classify at least amber, and flag the clause for `cross-border-contract-reviewer`; do not assess foreign-law enforceability.

## Required inputs

Mark as **blocking**:
- the full NDA text;
- which side the client is (discloser, recipient or both);
- the purpose of the discussions.

Also useful: the organisation's NDA playbook or standard positions, the counterparty's identity and sector, and whether personal data or source code will be exchanged. If no playbook is supplied, say so and use the default positions below.

## Method

1. Retrieve the current official text of the Indian Contract Act, 1872 (including section 27), the Specific Relief Act, 1963, and the DPDP Act, 2023 and Rules if personal data is in scope. Record the version and date. Load the client's playbook if supplied.
2. Read the whole NDA, including schedules and anything incorporated by reference.
3. Check each item against the standard position:
   - mutuality matches the deal;
   - definition is reasonable and has the usual exclusions;
   - use is limited to the purpose;
   - disclosure to representatives and affiliates is allowed;
   - term and survival are within the playbook;
   - return or destruction allows legal and backup retention;
   - no residuals clause against the client;
   - no licence or IP assignment;
   - no non-solicit, non-compete, exclusivity or standstill;
   - remedies are mutual; no uncapped indemnity or liquidated damages;
   - governing law and forum are acceptable;
   - no obligation to proceed or to buy.
4. Classify:
   - **Green:** no deviations, or only cosmetic ones.
   - **Amber:** deviations with a known fix the counterparty usually accepts.
   - **Red:** restraints, IP grants, indemnities, foreign law with foreign courts, or anything outside the playbook.
5. For each amber or red item, quote the clause, explain the risk in one line, and give replacement wording.
6. Note execution points (signatory authority, e-signature, stamping) for `contract-execution-stamping-checker`.

## Output

1. A verdict line: GREEN, AMBER or RED, and who must approve.
2. An issues table: clause · text · risk · fix · must-have or nice-to-have.
3. A short redline or replacement clauses.

## Guardrails and hand-offs

- Never say "approved"; say "within playbook" or "needs approval from ...".
- If the NDA is part of a larger agreement, stop and hand off to `playbook-contract-reviewer`.
- Never invent a playbook position; mark defaults as defaults.
- For a fresh counter-draft, hand off to `nda-drafter`.
