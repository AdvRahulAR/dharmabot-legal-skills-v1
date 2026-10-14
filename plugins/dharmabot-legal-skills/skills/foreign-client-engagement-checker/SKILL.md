---
name: foreign-client-engagement-checker
description: Checks and sets up an engagement between an Indian lawyer or firm and a foreign client or foreign law firm (US, UK, UAE, EU, Singapore and others). Covers conflicts, scope limited to what the Indian lawyer may do, supervision and outsourcing rules on the foreign side, confidentiality and data transfer, fee receipt under FEMA, GST on export of services, withholding tax and treaty documents, and a draft engagement letter. Use when a foreign client or law firm instructs an Indian lawyer, or for LPO and outsourcing arrangements. Do not use for engagements with Indian clients only.
---

# Foreign Client Engagement Checker

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Make sure a cross-border engagement is properly scoped, permitted on both sides, confidential, and paid in a compliant way, and produce the engagement letter.

## Jurisdiction gate

Identify the client's and any instructing firm's jurisdiction, and where the work will be used. If the work involves giving foreign-law advice directly to a foreign client, flag it. The Indian lawyer should normally work under a locally qualified lawyer's supervision for foreign law.

## Required inputs

Mark as **blocking**:
- client and instructing firm details;
- the scope of work;
- other parties to the matter, for conflicts;
- fee basis;
- where payment will come from.

Also useful: the foreign firm's standard outsourcing or vendor terms, data-protection requirements, and security questionnaires.

## Method

1. **Conflicts.** Check all parties and related entities against existing clients and matters. Record the check.
2. **Scope and permission.**
   - Confirm the work fits the Indian lawyer's permitted practice (Advocates Act, 1961 and BCI rules).
   - For US clients, check the supervising US lawyer's obligations under ABA Formal Opinion 08-451 and Model Rules 5.1, 5.3, 5.5 and 1.6, and any State rule that applies.
   - For UK clients, check the SRA Code for Firms on outsourcing.
   - See `references/foreign-jurisdictions.md` and retrieve the current texts.
3. **Confidentiality and data.**
   - Identify the personal data involved and the transfer route: GDPR or UK GDPR if the client is in the EU or UK; DPDP Act duties in India.
   - Hand off detailed transfer analysis to `cross-border-data-transfer-analyst`.
   - List the security measures the client will expect.
4. **Fees and payment.**
   - FEMA: receipt through an authorised dealer bank with an inward-remittance advice, and the right purpose code.
   - GST: whether the service qualifies as an export (recipient outside India, place of supply outside India, payment in convertible foreign exchange or as RBI permits, not merely a branch of the supplier). If so, it is zero-rated, so file a Letter of Undertaking.
   - Withholding tax: in the client's country, and whether the Indian lawyer needs a tax residency certificate or forms to claim treaty rates.

   Retrieve current rules for each; do not rely on these notes.
5. **Sanctions.** Screen the client and parties against current UN, US, UK and EU lists where the matter suggests any risk.
6. **Draft the engagement letter.** Cover parties, scope and exclusions (no foreign-law advice except under supervision), supervision, deliverables, fees, invoicing and taxes, confidentiality and data protection, conflicts, liability limits permitted by BCI rules, governing law and dispute resolution, and termination.

## Output

1. A compliance checklist with status: conflicts, permission, supervision, data, FEMA, GST, tax, sanctions.
2. The draft engagement letter.
3. Open items for the client or instructing firm.

## Guardrails

- Do not advertise or solicit, consistent with BCI Rule 36 (believed to be the rule; confirm against the official text).
- Do not agree to scope the Indian lawyer cannot lawfully perform.
- Mark every tax and FEMA point to be confirmed with a chartered accountant where material.
