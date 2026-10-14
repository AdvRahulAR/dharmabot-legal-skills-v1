---
name: digital-lending-compliance-reviewer
description: Reviews a digital lending product, LSP agreement and app flow against the RBI (Digital Lending) Directions, 2025 and connected Master Directions, covering fund flows, KFS and APR, cooling-off, default loss guarantee, multi-lender display, data limits and grievance redressal. Use when an NBFC, bank or fintech asks to audit a lending app, LSP contract, KFS or loan journey screenshots against RBI digital lending rules. Do not use to decide whether a licence is needed (use financial-services-licensing-analyst) or to draft DPDP notices (use privacy-notice-consent-drafter).
---

# Digital Lending Compliance Reviewer

Every output is a review for an advocate enrolled in India or the regulated entity's compliance officer to check.

## Purpose

Produce a clause-level and screen-level gap list for a digital lending arrangement, tied to the current RBI text, with practical fixes.

## Jurisdiction gate

Confirm the lender is an RBI-regulated entity (commercial bank, co-operative bank, NBFC, or All India Financial Institution) lending to borrowers in India. If the lender is unregulated, or the product is a pure BNPL or wallet credit line of uncertain character, stop and hand off to `financial-services-licensing-analyst`. Note any State money-lending law the facts raise, but do not analyse it here.

## Temporal gate

- The Digital Lending Directions were reissued in 2025 (believed to be dated 8 May 2025). Several parts reportedly had later start dates, including multi-lender LSP display (reported as 1 November 2025) and reporting of digital lending apps to RBI. Confirm each date from rbi.org.in.
- In November 2025 RBI consolidated thousands of circulars into entity-wise Master Directions. Check whether the digital lending provisions now sit inside the consolidated direction for the lender's entity type, and cite that text.
- DPDP Rules, 2025 apply in phases from 13 November 2025 (Consent Manager provisions reported from 13 November 2026; most fiduciary duties reported from 13 May 2027). Record the review date and say which phase applies.

## Required inputs

Mark as **blocking**: the lender's entity type and RBI registration category; the LSP or partnership agreement; the loan journey (screenshots or a screen-by-screen flow); the KFS template; and the fund-flow diagram (disbursement and repayment accounts).

Also useful: the DLG agreement, grievance redressal policy, privacy notice, app permission list, the list of digital lending apps reported to RBI, and recovery agent arrangements.

## Method

1. Retrieve the current official text of the Digital Lending Directions and the consolidated Master Direction for the lender's entity type from rbi.org.in, with any FAQs. Record the version and date. Use `rbi-master-direction-mapper` if the documents cite repealed circulars.
2. Map the parties: regulated entity, each LSP, each digital lending app, any DLG provider, any co-lender.
3. **Fund flows.** Check that disbursal goes to the borrower's own account and repayment to the regulated entity's account, with no pass-through or pool account controlled by the LSP. Check that LSP fees are paid by the lender, not charged to the borrower.
4. **Disclosure.** Test the KFS against the prescribed format: APR computation, all fees, penal charges, cooling-off terms, and recovery mechanism. Check that the KFS is shown before execution and sent after it.
5. **Cooling-off and prepayment.** Confirm exit terms match the Directions.
6. **Multi-lender LSPs.** Check that all matching offers are shown neutrally, with lender names, APR and KFS links, and no default ranking or nudging.
7. **Dark patterns.** Test each screen against the CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023 and the June 2025 self-audit advisory (for example false urgency, basket sneaking, forced action).
8. **Data.** Check need-based collection, no access to contacts, media or call logs, consent and revocation, storage in India and deletion. Flag DPDP points for `privacy-notice-consent-drafter`.
9. **DLG.** Check the guarantor's eligibility, the cap, form of cover, invocation period and disclosure. Confirm the cap figure from the current text.
10. **Grievance and reporting.** Check grievance officers named on the app and website, escalation to the RBI Ombudsman, and reporting of each app to RBI's portal.
11. **Contract.** Review LSP agreement clauses on audit rights, outsourcing, data handling and termination. Hand off general vendor terms to `vendor-saas-agreement-reviewer`.

## Output

1. Gap table: requirement · source paragraph · document or screen · finding · severity · fix.
2. Redline notes for the LSP agreement and KFS.
3. A short note listing open questions and the dates applied.

## Guardrails and hand-offs

- Never state a cap, percentage or period from memory; quote the current paragraph.
- Never certify that a product is "RBI compliant". Findings are a review, not an assurance.
- Never suggest structuring around the Directions.
- Tag any authority or RBI FAQ not read in full `[verify]`; run `citation-verifier` before delivery.
- For a regulator query or show-cause notice, hand off to `regulator-notice-reply-drafter`.
