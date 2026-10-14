---
name: time-billing-narrative-drafter
description: Converts diary notes, emails and calendar records into accurate time entries and draft invoices that match the engagement terms, and reviews invoices from outside or local counsel against agreed rates, billing guidelines and scope, flagging block billing, vague entries and duplication. Use when a lawyer asks to write time entries, prepare a client bill, clean up narratives, or check a counsel invoice before payment. Do not use to set fee terms; use engagement-letter-drafter for that.
---

# Time and Billing Narrative Drafter

Every output is a draft for the responsible advocate or the reviewing in-house counsel to check before it is sent or paid.

## Purpose

Produce bills that are specific, accurate and consistent with what the client agreed, and give in-house teams a fair, evidence-based review of counsel invoices.

## Jurisdiction gate

This skill applies to any engagement. Confirm the engagement terms (rates, caps, billing guidelines) and the currency. For tax lines on Indian invoices, use only the GST treatment confirmed by the firm's accountant or from the retrieved notification; do not compute tax from memory.

## Required inputs

**Blocking**:
- the engagement letter or agreed rate card and billing guidelines;
- the work records for the period (diary notes, emails, calendar, time sheets) or, for review, the invoice and its supporting entries.

Also useful: the budget or estimate, earlier invoices, and the matter plan.

## Method

1. Retrieve the current engagement terms and the client's billing guidelines, and record their version and date. If the bill includes GST, retrieve the current official notification or rely on the firm's tax adviser, and record which.
2. For drafting time entries:
   - one task per entry; start with a verb; name the document, hearing or person involved;
   - record actual time in the agreed unit; no rounding up beyond it;
   - separate non-billable work (internal training, conflict checks, billing itself) unless the terms say otherwise.
3. Check each entry against scope. Mark out-of-scope work for the advocate to decide whether to bill or seek approval.
4. Compare totals with the budget and flag variance with a reason.
5. For reviewing an incoming invoice, test:
   - rates against the agreed rate card, by timekeeper;
   - block billing (several tasks under one time figure);
   - vague entries ("work on file", "research", "attendance");
   - duplication (two people attending the same hearing, repeated drafting of the same document);
   - staffing above the agreed level, travel and expense limits, and unapproved disbursements;
   - arithmetic and tax lines.
6. Grade each issue: query, reduce, or reject, with the reason and the guideline it breaches.

## Output

1. Draft time entries table: date · timekeeper · narrative · time · rate · amount.
2. Draft invoice summary with fee, expense and tax lines (tax as bracketed fields until confirmed).
3. For reviews: issue table (entry · issue · guideline · proposed action · amount at stake) and a short note to the counsel.

## Guardrails and hand-offs

- Never inflate time, invent work, or back-fill entries without a record.
- Never alter entries to hide out-of-scope work; flag it.
- Keep narratives free of privileged strategy where invoices may be shared with auditors.
- For changing fee terms, hand off to `engagement-letter-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
