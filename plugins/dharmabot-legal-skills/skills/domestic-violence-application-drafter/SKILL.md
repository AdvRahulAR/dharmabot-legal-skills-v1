---
name: domestic-violence-application-drafter
description: Advises a person facing domestic violence and drafts applications under the Protection of Women from Domestic Violence Act, 2005 before a Magistrate for protection, residence in the shared household, monetary relief, custody and compensation orders and interim ex parte relief, with links to criminal remedies under the Bharatiya Nyaya Sanhita, 2023. Use when a lawyer asks for a DV Act application, a residence order after a woman is thrown out of the matrimonial home, or urgent protection orders. Do not use for a criminal complaint alone; use criminal-complaint-drafter.
---

# Domestic Violence Application Drafter

Every output is a draft for an advocate enrolled in India to check and file.

## Purpose

Secure the aggrieved person's safety first, then draft a DV Act application with the right reliefs and interim orders.

## Jurisdiction gate

Confirm the matter is in India and the aggrieved person is a woman in a domestic relationship with the respondent (marriage, relationship in the nature of marriage, family). Identify the Magistrate with jurisdiction: where she resides or works, where the respondent resides, or where the cause arose (confirm the provision). Record the State for the Protection Officer and service provider network.

## Temporal gate

The BNS replaced the IPC from 1 July 2024. For acts before that date, criminal remedies are under the IPC; check with `crpc-bnss-transition-analyst` where dates straddle it.

## Required inputs

Mark as **blocking**:
- immediate safety status (is she safe now, and where can she stay);
- the relationship and the shared household details;
- incidents of violence (physical, sexual, verbal, emotional, economic) with dates;
- the reliefs she wants;
- pending cases between the parties.

Also useful: medical records, photographs, messages, police complaints, the Domestic Incident Report if made, children's details, and the respondent's income.

## Method

If the client is in immediate danger, give safety steps before any drafting.

1. Retrieve the current official text of the DV Act, 2005 and its Rules (including the prescribed forms), and relevant BNS provisions. Record the version and date.
2. Safety plan: emergency helplines, police, the Protection Officer, shelter homes, and a safe place to stay. Do not record her current location in any draft unless the court needs it, and then seek confidentiality.
3. Domestic Incident Report: through the Protection Officer or service provider; the court can take cognisance on the application even without one (confirm current authority).
4. Draft the application in the prescribed form, with:
   - protection orders against specified acts and contact;
   - residence orders: right to reside in the shared household, which need not be owned by the husband (Satish Chander Ahuja v. Sneha Ahuja, Supreme Court, 2020; confirm current treatment);
   - monetary relief: maintenance, medical costs, loss of earnings, and household expenses (hand off quantum to `maintenance-petition-drafter`);
   - temporary custody of children;
   - compensation for injuries and mental torture.
5. Interim and ex parte relief: plead urgency and prima facie case with an affidavit.
6. Link criminal remedies under the BNS (cruelty by husband or relatives, and others the facts support); hand off to `criminal-complaint-drafter`.
7. If she cannot afford a lawyer, screen for free legal aid with `legal-aid-eligibility-screener`.

## Output

1. Safety steps checklist.
2. Draft DV Act application with interim relief affidavit.
3. Evidence list and next-steps note.

## Guardrails

- Keep the survivor's location and contact details confidential.
- Never add incidents not described by the client.
- Never advise contacting or confronting the respondent.
- Never promise an order or a timeline.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
