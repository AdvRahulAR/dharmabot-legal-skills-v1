---
name: fema-regularisation-drafter
description: Decides whether a FEMA reporting lapse can be cured by a Late Submission Fee filing through FIRMS or the AD bank, or needs compounding under the Foreign Exchange (Compounding Proceedings) Rules, 2024, estimates the amount, and drafts the compounding application, chronology and covering letter. Use when a company missed an FC-GPR, FC-TRS or ODI filing, or wants to compound a FEMA contravention. Do not use to structure a new investment (use india-entry-fema-structuring-analyst) or defend ED adjudication (use regulator-notice-reply-drafter).
---

# FEMA Regularisation Drafter

Every output is a draft for an advocate enrolled in India, working with the company's chartered accountant and AD bank, to check.

## Purpose

Pick the cheapest lawful route to regularise a FEMA lapse, and produce a filing-ready draft with a clean chronology.

## Jurisdiction gate

Confirm the lapse is under the Foreign Exchange Management Act, 1999 and its rules or regulations (NDI Rules, ODI Rules and Regulations, borrowing, or other). Identify the RBI Regional Office or Foreign Exchange Department office with jurisdiction. Check who compounds: RBI for most contraventions, the Directorate of Enforcement for others. Under the 2024 Rules (confirm the current text), compounding is reportedly not available once an adjudicating authority has passed a penalty order, and section 3(a) contraventions are excluded; it may still be possible while adjudication is pending, before the order. If the Directorate has issued a notice or started investigation or adjudication, flag it, check these bars from the Rules, and route the defence to `regulator-notice-reply-drafter`.

## Temporal gate

- The Foreign Exchange (Compounding Proceedings) Rules, 2024 replaced the 2000 Rules, and RBI issued revised compounding directions. Confirm their dates and any later amendment from the Gazette and rbi.org.in.
- Record the date of each transaction, the due date of each filing, and the actual filing date. Old lapses may fall under older LSF or compounding regimes; check the transitional provisions.
- Check the current LSF formula and any cap or cut-off after which LSF is not available.

## Required inputs

Mark as **blocking**: the transaction documents (board resolutions, allotment or transfer records, remittance certificates, KYC); the filing that was due and the date it was due; whether it has since been filed and when; any communication from the AD bank, RBI or ED; and earlier compounding by the same entity.

Also useful: the company's FIRMS entity master status, FCRS/FIRMS screenshots, valuation reports and the CA's working papers.

## Method

1. Retrieve the current official text of FEMA, the Compounding Proceedings Rules 2024, the relevant Master Direction on reporting or compounding, and the LSF provisions from the Gazette and rbi.org.in. Record versions and dates.
2. List every lapse separately: transaction, regulation, due date, actual date, delay.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
3. Classify each lapse:
   - reporting delay only, where LSF is available and the filing can still be made;
   - delay beyond the LSF window, or a substantive contravention (pricing, sectoral cap, approval route, wrong instrument), which needs compounding.
4. Check bars and conditions from the Rules: an adjudication order already passed, an amount that cannot be quantified, section 3(a) contraventions (believed to be s.3(a) FEMA; confirm against the official text), a similar contravention compounded within the cooling-off period, and whether the contravention is technical or serious.
5. Estimate LSF or compounding amount using the current formula or guidance table only. Show the working and label it an estimate.
6. Draft the compounding application in the prescribed form, with the chronology, statement of contravention, reasons for delay, rectification steps, and undertakings.
7. Draft the covering letter to the AD bank or RBI office, and the annexure index.
8. List what the AD bank or RBI is likely to ask for, so the client can pre-empt it.

## Output

1. Route memo: lapse-by-lapse table with route, reasons and estimated amount.
2. Draft compounding application, chronology, undertakings and covering letter.
3. Annexure checklist and an open-questions list.

## Guardrails and hand-offs

- Never present an amount as final. RBI or the AD bank determines it.
- Never backdate, reconstruct or alter documents to cure a lapse.
- Do not admit facts beyond the record; keep admissions precise.
- Use `limitation-calculator` for any time-bound response.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`.
- For a new investment structure, hand off to `india-entry-fema-structuring-analyst`.
