---
name: registry-letter-drafter
description: Drafts letters and applications to Indian court registries, covering listing and early-hearing requests, tagging and de-tagging, cause-list corrections, inspection of records, return of originals, and ordinary or urgent certified-copy applications, logging the dates needed for exclusion under section 12 of the Limitation Act, 1963. Use when an advocate asks for a registry letter, an urgent certified copy for an appeal, or a request to tag connected matters. Do not use for mentioning memos before the bench; use urgent-mentioning-memo-drafter.
---

# Registry Letter and Certified Copy Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce short, correct registry correspondence, and keep an exact record of certified-copy dates so the time can later be excluded when limitation is computed.

## Jurisdiction gate

Confirm the court is in India and identify it (Supreme Court, High Court and bench, district or subordinate court, tribunal). Registry practice and copy-application forms differ by court. Use the court's own form and procedure where one exists.

## Required inputs

Mark as **blocking**:
- the court, case number and parties;
- what is requested (listing, tagging, correction, inspection, return of documents, certified copy);
- for certified copies, the document wanted (judgment, decree, order, deposition) and its date, and whether urgent.

Also useful: the connected case numbers and the order directing tagging; the purpose of the copy (appeal, revision, execution).

## Method

1. Retrieve the court's current official rules on registry correspondence and certified copies, the copying or e-copy procedure, and the text of section 12 of the Limitation Act, 1963. Record the source and date.
2. Check the request is one the registry can grant. Where it needs a judicial order (for example early hearing in some courts), say so and suggest the right application.
3. Draft a short letter or application: reference line with case number, the request, the reason, the documents enclosed, and the advocate's details.
4. For certified copies, use the court's form or online copying portal. Note the decree as a separate document where an appeal needs it.
5. Create a copy log with the date of application, the date the cost or folio charges were notified, the date of deposit, the date the copy was ready, and the date of delivery. Leave blanks where facts are unknown.
6. Draft a polite follow-up letter if the copy is delayed, quoting the application number.
7. Hand the copy log to `limitation-calculator` to compute time, and to `matter-deadline-tracker` to diarise it. Do not compute limitation here.

## Output

1. The letter or application.
2. The certified-copy log (if relevant).
3. A follow-up letter template.
4. A note of next steps and hand-offs.

## Guardrails and hand-offs

- Do not compute the limitation period; use `limitation-calculator`.
- Mentioning memos go to `urgent-mentioning-memo-drafter`.
- Bundle or defect issues go to `efiling-bundle-defect-checker`.
- Never invent application numbers, dates or charges.
- Keep tone formal and brief. Do not seek a favour from registry staff.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
