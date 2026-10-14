---
name: lok-adalat-settlement-drafter
description: Prepares a matter for a Lok Adalat in India. It checks whether it can be referred (pending case or pre-litigation), drafts the referral application, a settlement-terms sheet, and the compromise or settlement record for the award, and explains the effect of the award. Use when parties want to settle before a Lok Adalat or National Lok Adalat, a legal services body needs referral papers, or an advocate asks "can this case go to Lok Adalat". Do not use for Permanent Lok Adalat public-utility disputes or court-annexed mediation.
---

# Lok Adalat Settlement Drafter

Every output is a draft for an advocate, legal services authority or the parties to check.

## Purpose

Get a dispute into a Lok Adalat on the right footing and record a clear, enforceable settlement.

## Jurisdiction gate

Confirm the dispute is in India and identify the State, district and the court where it is pending (if any). Check that the dispute is one a Lok Adalat may decide. Offences that are not compoundable by law cannot be settled there; flag such matters and stop.

## Required inputs

Mark as **blocking**: whether the case is pending (court, case number, stage) or pre-litigation; the parties; the dispute in brief; and the terms both sides are willing to consider.

Also useful: amounts claimed and offered, payment schedule, property details, earlier orders, and any upcoming Lok Adalat sitting.

## Method

1. Retrieve the current text of the provisions of the Legal Services Authorities Act, 1987 on Lok Adalats (believed to be sections 19 to 21), the relevant State regulations and the current Lok Adalat schedule from the State or district legal services authority. Record the date.
2. Check eligibility for reference: for a pending case, the grounds on which the court may refer it (believed to include both parties agreeing, one party applying where the court sees a chance of settlement, and the court finding the matter suitable on its own; confirm the current wording of section 20); for a pre-litigation matter, the application route to the authority.
3. Draft the referral application or joint memo for reference.
4. Prepare a terms sheet: each obligation, who performs it, amount, date, and what happens on default. Remove vague terms ("as agreed", "reasonable time").
5. Draft the compromise or settlement record that the Lok Adalat will use to make its award, with the parties' signatures and identification.
6. Explain the effect of an award in plain terms, citing the provisions retrieved: that it is treated as a court decree, is final and binding, and that refund of court fee may be available where a pending case is settled (confirm the current rule for that State and court).

## Output

1. Eligibility note.
2. Draft referral application.
3. Terms sheet and draft settlement record.
4. Plain-language explanation of the award's effect (offer a version in the person's language via `regional-language-legal-drafter`).
5. Checklist of documents and identity proofs to bring.

## Guardrails

- Never pressure a party to settle or describe a settlement as their only option.
- Make sure both parties' consent is recorded in their own understanding; flag any sign one party does not understand the terms.
- Do not use for criminal matters that cannot be compounded.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
