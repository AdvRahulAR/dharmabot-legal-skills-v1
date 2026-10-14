---
name: engagement-letter-drafter
description: Drafts engagement and retainer letters for Indian clients of advocates and law firms, covering scope and exclusions, staffing, fixed, hourly, stage-wise or retainer fees, GST on legal services under reverse charge, expenses, confidentiality and termination, checked against the Bar Council of India Rules including the bar on contingency fees. Use when you need an engagement letter, retainer agreement, fee letter or scope letter for a domestic client. Do not use for foreign clients; use foreign-client-engagement-checker instead.
---

# Engagement Letter Drafter

Every output is a draft for an advocate enrolled in India to check, adapt and sign.

## Purpose

Record clearly what the firm will do, what it will not do, how it will be paid and how the relationship ends, in terms that comply with the BCI Rules and current GST law.

## Jurisdiction gate

- Confirm the client is in India and the engagement is governed by Indian law.
- If the client is foreign, or fees come from abroad, stop and hand off to `foreign-client-engagement-checker`.
- Note the State of the client and the firm, since GST place of supply and stamp duty on any formal agreement may depend on it.

## Required inputs

**Blocking**:
- the client's legal name and type (individual, firm, company, LLP, government body);
- the scope of work agreed, in the client's own terms;
- the fee model and amounts;
- confirmation that the conflict check is cleared (from `client-intake-conflict-screener` or the firm's register).

Also useful: staffing, billing frequency, advance or retainer amount, expected local counsel or experts, and the client's billing guidelines.

## Method

1. Retrieve the current official text of the BCI Rules on fees and professional conduct, and the current GST notifications on legal services (rate and reverse-charge entries) from the CBIC website. Record the versions and dates. Do not state the GST rate or turnover threshold from memory.
2. Write the scope as a list of included tasks and a list of exclusions (appeals, related proceedings, tax advice, foreign law, travel).
3. Name the responsible advocate and the team. State who can give instructions on the client's side.
4. Set the fee model.
   - Fixed fee: tie it to defined deliverables and stages.
   - Hourly: rates by seniority and the time-recording unit.
   - Stage-wise for litigation: filing, pleadings, evidence, arguments, each as a separate fee.
   - Retainer: monthly amount, hours covered and overage rate.
5. Check fee terms against the BCI Rules. Remove any term that makes the fee depend on the result of litigation or gives the advocate a share in the claim. A success-linked bonus in litigation must not be drafted; flag it for the advocate.
6. GST: identify whether the recipient is a business entity and whether reverse charge applies under the current notification. Write the GST clause from the retrieved text, and leave the rate as a bracketed field.
7. Expenses: court fees, stamp duty, clerkage, travel, local counsel and expert fees, with a cap or approval threshold.
8. Add confidentiality, data handling (including use of AI tools, if the firm uses them), conflicts disclosure, document retention, communication channels and the client's duty to give true and complete information.
9. Termination: either side may end it; fees for work done; return of papers; the advocate's duty not to withdraw at a stage that harms the client without reasonable notice.

## Output

1. The draft engagement letter with a scope schedule and a fee schedule.
2. A short cover note listing assumptions and bracketed fields to fill.
3. A compliance check table: term · rule checked · result.

## Guardrails and hand-offs

- No contingency or result-based fee in litigation; no promise of outcome.
- No GST rate, threshold or section number stated without the retrieved source.
- For the work plan and budget, hand off to `matter-plan-builder`.
- For invoices under this letter, hand off to `time-billing-narrative-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
