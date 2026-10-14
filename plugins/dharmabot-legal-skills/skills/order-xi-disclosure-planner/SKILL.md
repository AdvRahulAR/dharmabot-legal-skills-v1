---
name: order-xi-disclosure-planner
description: Plans disclosure in Indian commercial suits under Order XI of the Code of Civil Procedure as amended by the Commercial Courts Act, 2015, covering the documents list and declaration, inspection, admission and denial of documents with reasons, discovery applications, costs for unreasonable denial, and privilege under the Bharatiya Sakshya Adhiniyam, with High Court original-side rules. Use when a lawyer says "plan our admission-denial affidavit", "what inspection should we seek" or "Order XI disclosure". Do not use to check initial filing readiness; use commercial-suit-filing-checker instead.
---

# Order XI Disclosure Planner

Every output is a draft plan for an advocate enrolled in India to check.

## Purpose

Run disclosure in a commercial suit on time and with reasons, so no document is deemed admitted by default and the other side's gaps are exposed.

## Jurisdiction gate

Confirm the suit is a commercial suit before a Commercial Court, Commercial Division or the original side of a High Court, and note the State or UT. Record the applicable High Court rules (for example the Delhi High Court original-side rules) and any practice directions on admission-denial.

## Required inputs

Mark as **blocking**:
- the pleadings with their documents lists and declarations;
- the other side's documents, paginated;
- the court and the dates of filing and service, so time limits can be computed;
- which party the advocate acts for.

Also useful: the client's own document inventory, privilege concerns, and any orders on inspection or timelines.

## Method

1. Retrieve the current official text of Order XI as applicable to commercial suits, the Commercial Courts Act, 2015, the relevant High Court rules and practice directions, and the Bharatiya Sakshya Adhiniyam provisions on privileged communications (believed to be sections 132 to 134; confirm). Record version and date.
2. Compute each time limit for inspection and for the statement of admission and denial with `limitation-calculator`, noting any condonation limits in the rules. Flag any limit already near or past.
3. Check the client's own disclosure: are all documents in power, possession, control or custody listed, including those adverse to the client? Is the declaration on oath complete?
4. For each of the other side's documents, propose a position: admit, deny, or admit existence but not contents or correctness. Give a reason for every denial, as the rules require. Separate correctness of contents, existence, execution, issuance and receipt.
5. Identify documents the other side should have disclosed but did not. Draft targeted inspection requests and, if refused, grounds for a discovery application.
6. Check privilege claims on both sides: legal advice, communications with counsel, and settlement communications. Plan redactions with `redaction-reviewer`.
7. Flag documents whose unreasonable denial may attract costs.

## Output

1. Draft statement of admission and denial: document · page · position · reason.
2. Inspection request list and discovery application outline.
3. Privilege log.
4. Timeline with every deadline and the rule it comes from.

## Guardrails and hand-offs

- Never recommend denying a document the client knows to be genuine.
- Never invent time limits; compute them from the retrieved rules.
- Initial filing readiness goes to `commercial-suit-filing-checker`; interrogatories and other applications to `civil-interlocutory-application-drafter`; before filing, `pre-filing-verification-checker`.
