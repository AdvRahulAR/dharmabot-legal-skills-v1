---
name: privacy-notice-consent-drafter
description: Drafts notices and consent requests under the Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025, consent withdrawal and grievance text, website and app privacy policies and cookie notices for Indian businesses, built only on data flows the client has confirmed, with SPDI Rules carry-over where still relevant. Use when a client asks for a privacy policy, DPDP notice, consent screen copy, cookie banner or a privacy policy update. Do not use for a full readiness assessment; run dpdp-compliance-gap-analyst first when the data flows are not mapped.
---

# Privacy Notice and Consent Drafter

Every output is a draft for an advocate enrolled in India to check before publication.

## Purpose

Produce notice, consent and policy text that matches what the client actually does with personal data, in language a data principal can understand.

## Jurisdiction gate

- Confirm the service is offered to people in India, or the processing happens in India.
- If the service targets EU or UK users, flag GDPR and ePrivacy requirements for cookies and mark them "to be confirmed by counsel qualified in the EU or UK".
- Check sector rules with their own consent requirements, for example RBI directions on digital lending, telecom commercial communication rules, or health data rules. Retrieve them before drafting.

## Temporal gate

- The DPDP Rules on notice content are believed to commence 18 months after notification (13 May 2027). Confirm from the Gazette and check for any amendment.
- Until then, the SPDI Rules, 2011 privacy-policy duty may still apply. Draft text that satisfies both, and say which parts become mandatory when.

## Required inputs

**Blocking**:
- a data-flow table for each purpose: data items, source, purpose, ground, recipients and processors, storage location, retention;
- the channel and screen where the notice and consent appear (sign-up, KYC, checkout, cookie banner);
- whether children or persons with disability may use the service;
- grievance officer or DPO contact details.

Also useful: the existing policy, terms of use, brand voice, and the languages the client serves.

## Method

1. Retrieve the current official text of the DPDP Act, the DPDP Rules (especially the notice rule), the SPDI Rules, and any sector direction in play. Record version and date.
2. Read the data-flow table back to the client as a list. Draft nothing about processing they have not confirmed.
3. Keep the notice separate from terms of use. The consent request must be clear, itemised and limited to data needed for the stated purpose.
4. Draft the notice: an itemised list of personal data with the specific purpose and the goods or services each enables; how to withdraw consent; how to exercise rights; how to raise a grievance; and how to complain to the Data Protection Board.
5. Draft consent controls: no pre-ticked boxes, no bundling of unrelated purposes, separate toggles for optional purposes such as marketing, and a withdrawal route as easy as the grant.
6. Children: add an age gate and a verifiable parental consent flow. Remove tracking and targeted advertising aimed at children unless an exemption in the Rules clearly applies.
7. Privacy policy: who the client is, data categories, purposes, grounds, recipients and processor categories, transfers abroad, retention, security, rights, grievance contact, updates and effective date.
8. Cookie notice: classify each cookie or SDK (strictly necessary, functional, analytics, advertising). Ask for consent before non-essential ones that process personal data.
9. Plain language: short sentences, layered text for mobile, no "including but not limited to" padding.
10. Consistency check: the notice, policy, consent screens and terms must say the same thing. List every mismatch.
11. Languages: hand Eighth Schedule versions to `regional-language-legal-drafter`.

## Output

1. Standalone DPDP notice and consent text, screen by screen.
2. Withdrawal, rights and grievance text.
3. Privacy policy and cookie notice.
4. A table mapping each sentence to the data-flow row it relies on.
5. Open questions and items the client must confirm.

## Guardrails and hand-offs

- Never describe processing, safeguards or certifications the client has not confirmed.
- Never draft dark patterns: confirm-shaming, hidden decline options or forced consent.
- Do not promise rights timelines tighter or looser than the Rules without client sign-off.
- Platform terms go to `ecommerce-platform-terms-checker`; readiness gaps to `dpdp-compliance-gap-analyst`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
