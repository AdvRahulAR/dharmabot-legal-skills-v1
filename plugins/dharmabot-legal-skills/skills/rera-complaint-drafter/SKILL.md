---
name: rera-complaint-drafter
description: Drafts allottee complaints under the Real Estate (Regulation and Development) Act, 2016 before a State RERA Authority or its Adjudicating Officer, for refund with interest, delay interest, possession, defect rectification or compensation, in the State portal's format, and compares the consumer forum route. Use when a lawyer asks for a RERA complaint against a builder for delayed possession, refund of booking money, or structural defects after handover. Do not use to review an agreement before signing; use builder-buyer-agreement-reviewer.
---

# RERA Complaint Drafter

Every output is a draft for an advocate enrolled in India to check and file.

## Purpose

Prepare a complaint the State RERA portal will accept, choosing the right relief and forum, with a clean payment and delay chronology.

## Jurisdiction gate

Record the State or UT where the project is, and its RERA registration number. Each State has its own rules, forms, fees and portal, and some send compensation claims to the Adjudicating Officer while others let the Authority decide them; check the current State position and any Supreme Court ruling on the split. Check whether the project is registered or should have been, and whether it falls within an exemption (for example a project completed before RERA commenced).

## Required inputs

Mark as **blocking**:
- the allotment letter, agreement for sale or builder-buyer agreement;
- the payment record (receipts, bank statements, loan disbursements);
- the promised possession date and any extension or force majeure claimed;
- the relief the client wants (stay and take delay interest, or withdraw and take a refund);
- the project's RERA registration details.

Also useful: correspondence, demand letters, the occupancy certificate status, defect photos, and any earlier consumer, civil or insolvency proceeding.

## Method

1. Retrieve the current official text of the Real Estate (Regulation and Development) Act, 2016, the State rules and regulations, and the State Authority's complaint form and fee. Open `references/india-state-statutes.md` as a starting point. Record the version and date.
2. Choose the relief. Refund with interest or delay interest for every month of delay are believed to be under section 18; compensation is believed to be adjudged under section 71; complaints are believed to be filed under section 31. Confirm each number from the source.
3. Compute interest only on the formula in the State rules (typically linked to a bank lending rate plus a margin; confirm) and show the arithmetic per payment. Hand off date checks to `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
4. Compare forums. An allottee may also approach a consumer commission (Imperia Structures Ltd v. Anil Patni, Supreme Court, 2020; confirm current treatment). Note the risk of parallel proceedings and of insolvency proceedings against the promoter. For the consumer route, hand off to `consumer-complaint-drafter`.
5. Draft: parties, project details, facts with dated chronology, violations, relief, interim relief (for example restraint on cancellation or third-party sale), list of documents and verification, in the portal's structure.
6. Search for and cite current RERA Appellate Tribunal and Supreme Court authority only after reading it; tag the rest `[verify]`.

## Output

1. Draft complaint in the State format.
2. Interest computation table.
3. Forum comparison note and filing checklist.

## Guardrails

- Never promise a refund or a date of payment.
- Never invent payment amounts or dates; mark gaps.
- Do not state interest rates or fees from memory.
- Filing and appearance are done by the advocate or the allottee.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
