---
name: insolvency-claim-drafter
description: Prepares creditors' proofs of claim in CIRP, liquidation and personal insolvency under the Insolvency and Bankruptcy Code, 2016 and IBBI regulations, using the prescribed forms with interest workings and evidence, and helps IRPs, RPs and liquidators verify, classify and admit or reject claims. Use when a creditor needs to file a claim form, or an insolvency professional asks to verify claims, classify related-party or contingent claims, or draft rejection reasons. Do not use for the overall process timeline; use cirp-ppirp-timeline-checker.
---

# Insolvency Claim Drafter

Every output is a draft for an advocate or insolvency professional in India to check.

## Purpose

Prepare a complete, evidenced claim, or verify submitted claims consistently and record reasons.

## Jurisdiction gate

Confirm the process is under the IBC before an NCLT in India and note its type: CIRP, PPIRP, liquidation, voluntary liquidation, or personal guarantor or individual insolvency. Each has its own forms and timelines.

## Temporal gate

IBBI amended the claims rules in recent years, including treatment of late claims. The IBC (Amendment) Act, 2026 is reported to be partly in force from 26 May 2026; confirm whether it changes any claim step. Check which regulation version applies on the claim date and the public announcement date.

## Required inputs

Mark as **blocking**:
- the public announcement (date, last date for claims, forms prescribed);
- the creditor's category (financial, operational, workman, employee, other, home buyer, authorised representative class);
- the documents proving the debt: agreements, invoices, ledgers, decrees, security documents;
- for verification, the claims register and the corporate debtor's books.

Also useful: correspondence on disputes, interest terms, and related-party information.

## Method

1. Retrieve the current official text of the IBC, the relevant regulations and the prescribed claim forms, and IBBI circulars on claims. Record versions and dates.
2. Identify the correct form for the category. Do not rely on a remembered form letter.
3. Compute the claim to the insolvency commencement date. Show principal, contractual or statutory interest, and deductions such as advances and set-off. Hand off complex interest to `damages-interest-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
4. Identify security interest held and attach proof of creation and registration.
5. Build the annexure index and the affidavit or verification.
6. For verification: check each claim against books and documents; classify as financial, operational or other; flag related parties (who are excluded from CoC voting); mark contingent or disputed parts; and record admitted, rejected and pending amounts with reasons.
7. For late claims, check the current rules and NCLT and NCLAT authority on condonation. Search for and read it; tag unread authority `[verify]`.

## Output

1. The completed claim form with workings and annexure index.
2. Or a verification register: claimant, category, claimed, admitted, rejected, reason, evidence.
3. Draft communications of rejection or partial admission with reasons.

## Guardrails and hand-offs

- Never admit or inflate a claim without documents.
- Never classify a creditor to change voting share without a legal basis.
- Timeline questions go to `cirp-ppirp-timeline-checker`.
- Never invent case law. Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
