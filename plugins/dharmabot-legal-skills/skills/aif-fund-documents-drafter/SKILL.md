---
name: aif-fund-documents-drafter
description: Drafts and reviews alternative investment fund documents under the SEBI (Alternative Investment Funds) Regulations, 2012 and the SEBI master circular, including the PPM in SEBI's template, contribution agreement, side letters and MFN terms, trust deed or LLP agreement, fees, carry and waterfall. Use when a fund manager asks to draft or review a PPM, contribution agreement, side letter or waterfall. Do not use to decide registration category or manager licensing (use financial-services-licensing-analyst) or for portfolio deal documents (use shareholders-agreement-drafter).
---

# AIF Fund Documents Drafter

Every output is a draft for an advocate enrolled in India and the fund's compliance officer to check.

## Purpose

Produce fund documents that are internally consistent, match SEBI's template and disclosures, and are ready for the merchant banker's due diligence.

## Jurisdiction gate

Confirm the fund is an AIF registered or to be registered with SEBI in India, and its category and sub-category. If the fund is in GIFT IFSC, stop: IFSCA fund management rules apply instead. For offshore feeders or foreign investors, mark foreign-law points "to be confirmed by counsel qualified in [jurisdiction]" and flag FEMA downstream-investment questions.

## Temporal gate

SEBI amends the AIF Regulations and master circular often (for example on PPM templates, accredited investors, angel funds, pro-rata rights, dematerialisation and certification of key personnel). Retrieve the master circular and every circular issued after it, and record the cut-off date used.

## Required inputs

Mark as **blocking**: fund category and sub-category; legal form (trust, LLP or company) and jurisdiction of the vehicle; target corpus and sponsor and manager commitment; term and extension; investment strategy; and the commercial terms (management fee, hurdle, carry, catch-up, distribution waterfall).

Also useful: investor profile (domestic, foreign, accredited), key personnel, conflict situations, co-investment plans, existing side letter requests.

## Method

1. Retrieve the current official text of the AIF Regulations, the SEBI master circular for AIFs, the PPM template, and later circulars from sebi.gov.in. Record versions and dates.
2. Build a term sheet that every document will follow. Flag gaps before drafting.
3. **PPM.** Follow SEBI's template structure: Part A (mandatory disclosures) and Part B (supplementary). Draft fee, expense, waterfall, conflicts, risk factors, valuation, key person, and winding-up sections. Check investment conditions and concentration limits against the category.
4. **Waterfall.** Write it in steps and add a worked example with illustrative numbers clearly marked as illustrative. Test clawback and giveback.
5. **Contribution agreement.** Commitment, drawdown notices, default remedies, transfer restrictions, representations, KYC, tax, and indemnity. Keep it consistent with the PPM.
6. **Side letters and MFN.** Check SEBI limits on differential rights and disclosure duties. List MFN carve-outs.
7. **Constitution document.** Trust deed or LLP agreement: roles of trustee, sponsor, manager, investment committee.
8. **Investor eligibility.** Minimum investment, accredited investor treatment and any large value fund terms; confirm thresholds from current text.
9. **Process.** List the PPM audit, merchant banker due diligence and SEBI filing steps, and who signs what.

## Output

1. Draft PPM sections, contribution agreement and side letter template.
2. Waterfall schedule with a worked example.
3. Consistency table: term · PPM · contribution agreement · side letter.
4. Open-issues list for the manager.

## Guardrails and hand-offs

- Never state a minimum investment, fee cap or threshold from memory.
- Never promise returns or draft marketing that implies them.
- Do not give tax opinions on pass-through status; mark tax points for the fund's tax adviser.
- Run `citation-verifier` on regulatory references.
- Before anything is filed with SEBI or sent to investors, hand off to `pre-filing-verification-checker`.
- For CCPS or convertible terms in portfolio deals, hand off to `convertible-instrument-analyst`.
