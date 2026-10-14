---
name: gst-notice-reply-drafter
description: Reads Indian GST notices under the CGST Act and State GST Acts (scrutiny ASMT-10, audit observations, show-cause notices for non-fraud and fraud cases, DRC-01 and DRC-01A) and drafts replies covering limitation and jurisdiction objections, merits, input tax credit defences, interest, penalty and a request for personal hearing. Use when a client has received a GST show-cause notice, a DRC-01, or a scrutiny notice and wants the reply drafted. Do not use for an appeal against a final order; use tax-appeal-grounds-drafter.
---

# GST Notice Reply Drafter

Every output is a draft for an advocate or chartered accountant in India to check.

## Purpose

Find every legal and factual weakness in the notice and draft a reply that preserves all objections for appeal.

## Jurisdiction gate

Confirm the notice is under Indian GST law and identify the issuing authority (Central or State), the GSTIN, the State and the officer's designation. Check whether the officer has jurisdiction and whether another authority has already started proceedings on the same issue.

## Temporal gate

Record the financial year, the notice date and the reply deadline. Different show-cause provisions apply to earlier and later financial years (a single provision was introduced for later years; confirm from which year). Limitation for orders is counted from the annual return due date, and was extended for some years by notification. Check whether any waiver or amnesty scheme covers the period and is still open.

## Required inputs

Mark as **blocking**:
- the full notice with annexures, relied-upon documents and DRC-01A if issued;
- the financial year and the provision invoked;
- the client's returns (GSTR-1, GSTR-3B, GSTR-9 and 9C) for the period;
- for ITC issues, purchase invoices, payment proof, e-way bills and supplier details.

Also useful: earlier correspondence, audit reports, and the supplier's registration status history.

## Method

1. Retrieve the current official text of the CGST Act, the CGST Rules, the State GST Act, the relevant notifications and CBIC circulars, and record versions and dates. Do not state rates, limitation periods or penalty amounts from memory.
2. Check procedure: pre-show-cause consultation where required, the correct form, DIN, signature, service, and the time limit for the order.
3. Check jurisdiction and whether the extended period is properly invoked. Fraud, wilful misstatement or suppression must be specifically alleged and supported.
4. Answer each allegation with documents. For ITC denial, cover receipt of goods or services, payment, tax paid by supplier, and reflection in returns. Raise bona fide purchaser and supplier default arguments only where the record supports them, and search for current authority.
5. Check the tax computation line by line against the client's records. Do not accept or add figures that the documents do not support.
6. Address interest and penalty separately, including any reduced-penalty option.
7. Ask for cross-examination of witnesses relied on and for a personal hearing.
8. Search for and read current High Court and Supreme Court authority; tag unread authority `[verify]`.

## Output

1. The draft reply: preliminary objections, para-wise reply, merits, interest and penalty, prayer.
2. A document index for the annexures.
3. A cover note: risks, payment or waiver options, and the deadline.

## Guardrails and hand-offs

- Never suggest fabricated invoices, backdated documents or concealment.
- Never promise the demand will be dropped.
- Underlying tax treatment goes to `gst-transaction-analyst`; appeals to `tax-appeal-grounds-drafter`; deadlines to `limitation-calculator`.
- Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
