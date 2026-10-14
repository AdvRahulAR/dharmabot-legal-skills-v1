---
name: name-change-gazette-drafter
description: Prepares the full Indian name-change set, covering the affidavit, newspaper advertisements, the application to the Department of Publication for the Gazette of India (Part IV) or the State Gazette, change for a minor through a guardian, and the order of updating PAN, Aadhaar, passport, school, university and bank records. Use when a client wants to change a first name or surname after marriage, divorce, adoption or by choice and needs the papers and steps. Do not use for passport refusals or citizenship issues; use oci-citizenship-passport-advisor.
---

# Name Change and Gazette Drafter

Every output is a draft for an advocate enrolled in India to check before the client signs or submits.

## Purpose

Give the client one consistent paper trail for a new name, so every record can be updated without contradiction.

## Jurisdiction gate

Confirm the applicant is an Indian citizen or resident and where they live. Decide between the Gazette of India and the State Gazette, based on what the records to be changed require. For applicants abroad, check the Indian mission's procedure and hand off to `oci-citizenship-passport-advisor` for passport issues.

## Required inputs

Mark as **blocking**:
- the old name and new name, exactly as to be spelt;
- the reason (marriage, divorce, personal choice, religious reasons, correction);
- for a minor, the guardian's details and the consent of both parents or the reason one cannot consent;
- the identity and address proof the client holds.

Also useful: the records to be updated (passport, PAN, Aadhaar, certificates, bank, property) and the client's State.

## Method

1. Retrieve the current official procedure, forms and fees of the Department of Publication (eGazette) or the State Government Press, and the current name-change rules of the passport authority, the income-tax PAN service and UIDAI. Record the source and date.
2. Draft the affidavit with old name, new name, reason, and a statement that all future dealings will be in the new name. Hand stamp and attestation details to `general-affidavit-drafter`.
3. Draft the two newspaper advertisements: one in an English daily and one in a regional-language daily circulating where the applicant lives (confirm the current requirement).
4. Prepare the Gazette application in the prescribed format, with the list of enclosures: affidavit, advertisements, identity proof, photographs, the deed or certificate tied to the reason (for example a marriage or divorce record), and the declaration.
5. For a minor, draft the guardian's affidavit and consent.
6. Flag special cases: a change of religion, a gender change (check the Transgender Persons (Protection of Rights) Act, 2019 route), and certificates where the issuing board has its own rules.
7. Set the update sequence, usually Gazette first, then PAN and Aadhaar, then passport, then bank, school, university and property records.

## Output

1. Affidavit, newspaper advertisement texts, and Gazette application with enclosure list.
2. Minor's guardian affidavit, if relevant.
3. An update plan: record · authority · document needed · order.

## Guardrails and hand-offs

- Never state fees, timelines or Gazette part numbers as settled without the current source.
- Never use a name change to evade a legal liability; flag pending cases or debts in the old name.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
