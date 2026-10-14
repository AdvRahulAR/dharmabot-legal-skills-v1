---
name: infrastructure-energy-contract-reviewer
description: Reviews Indian energy and infrastructure contracts, including power purchase agreements and open access under the Electricity Act 2003 and CERC and SERC regulations, PPP concessions on model concession agreements (BOT, HAM, TOT), and EPC or FIDIC-style construction contracts, and analyses delay, extension of time, liquidated damages, variation and defect claims. Use when a lawyer asks to review a PPA, concession or EPC contract or assess a delay claim. Do not use for bid eligibility or tender challenges; use tender-procurement-compliance-checker.
---

# Infrastructure and Energy Contract Reviewer

Every output is a review for an advocate enrolled in India to check.

## Purpose

Identify the client's risks in an energy or infrastructure contract, and set out the strength of any delay, defect or payment claim with the right dispute route.

## Jurisdiction gate

Confirm the governing law is Indian and identify the State, the counterparty (DISCOM, NHAI, a State authority, a private EPC contractor) and the regulator with jurisdiction (CERC for inter-State generation and transmission, the SERC otherwise). If the contract names a foreign law or seat, flag it for `cross-border-contract-reviewer`.

## Required inputs

Mark as **blocking**:
- the contract or contracts, with schedules and amendments;
- which party the client is;
- the question: pre-signing review, or a live claim or dispute.

For claims, also **blocking**: the programme, notices sent and received, and correspondence on the delay or defect. Also useful: bid documents, tariff order, letters of award, and payment history.

## Method

1. Retrieve the current official text of the Electricity Act, the relevant CERC or SERC regulations, the Electricity (Late Payment Surcharge and Related Matters) Rules, the Electricity (Promoting Renewable Energy Through Green Energy Open Access) Rules, change-in-law rules, and any model concession agreement the contract follows. Record versions and dates.
2. Map the deal: parties, term, tariff or annuity, conditions precedent, security, and step-in rights.
3. **PPA review.** Check tariff adoption or determination, scheduling and curtailment, deemed generation, payment security (letter of credit, State guarantee, payment security mechanism), late payment surcharge, change in law and its compensation formula, force majeure, termination payments and the regulator's role in disputes.
4. **Concession review.** Compare against the model concession agreement: concession period, revenue risk, land handover, change of scope, termination payments, lender substitution and the independent engineer's role.
5. **EPC review.** Check scope and interfaces, time for completion, extension of time triggers and notice bars, liquidated damages and caps, variations, performance guarantees, defects liability, insurance and limitation of liability.
6. **Delay or defect claim.** Build a chronology from the record only. Identify the causes and who bears each risk. Test notice compliance and concurrent delay. Ask whether liquidated damages are a genuine pre-estimate or need proof of loss under Indian contract law, and search for current Supreme Court authority. Tag anything not read in full `[verify]`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
7. **Dispute route.** Identify the forum: regulatory commission adjudication (and APTEL appeal), arbitration under the contract, conciliation boards, or courts. Note any statutory bar.

## Output

1. A risk table: clause · issue · risk level · suggested position or redline.
2. For claims, a claim analysis: event · contract basis · notice compliance · evidence · strength.
3. The dispute route and next steps.

## Guardrails and hand-offs

- Never compute a claim figure without the inputs; hand off quantum and interest to `damages-interest-calculator`.
- Never state that a regulator will allow a tariff or change-in-law claim.
- For arbitration filings, hand off to `arbitral-proceedings-drafter`.
- For tender and bid issues, hand off to `tender-procurement-compliance-checker`.
- Before delivery, send citations to `citation-verifier`.
