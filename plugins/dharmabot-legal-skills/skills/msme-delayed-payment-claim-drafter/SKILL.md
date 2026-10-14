---
name: msme-delayed-payment-claim-drafter
description: Drafts references under the Micro, Small and Medium Enterprises Development Act, 2006 to the Facilitation Council via MSME Samadhaan, checking Udyam registration and supplier status on the contract date, computing compound interest at the statutory multiple of the bank rate, and covering conciliation, arbitration and the pre-deposit for challenges. Use when an advocate asks for an MSME claim, Samadhaan application, MSEFC reference or delayed payment interest for a micro or small supplier. Do not use to challenge an MSEFC award; use section-34-37-award-challenge-drafter instead.
---

# MSME Delayed Payment Claim Drafter

Every output is a draft for an advocate enrolled in India to check before filing.

## Purpose

Confirm that the client is a covered supplier, and draft a complete, well-computed reference to the Facilitation Council.

## Jurisdiction gate

Confirm both parties and the supply are within India and identify the State where the supplier is located; the Council of that State usually has jurisdiction. Confirm the buyer is not excluded and that the dispute arises from goods supplied or services rendered.

## Required inputs

Mark as **blocking**:
- the Udyam registration certificate (or earlier memorandum), with its date and the category (micro, small or medium);
- the contract or purchase orders and their dates;
- the invoices, delivery or acceptance proofs, and payments received;
- the agreed payment period, if any.

Also useful: correspondence on objections to goods or services, the buyer's acknowledgment of dues, and any arbitration clause in the contract.

## Method

1. Retrieve the current official text of the MSMED Act, the State's MSEFC rules, the Udyam notification and classification criteria, and the MSME Samadhaan portal requirements. Record the version and date.
2. Supplier status: the claimant must be a micro or small enterprise. Medium enterprises and traders registered only for limited purposes may not be covered; check the current notifications. Check whether registration existed before the contract or supply. Read current Supreme Court authority on post-contract registration before advising (search for it; tag `[verify]` until read).
3. Compute the appointed day and due date for each invoice under the Act's payment-period rules (agreed period subject to the statutory cap, or the default period from acceptance). Confirm both periods from the text.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
4. Compute compound interest with monthly rests at the statutory multiple of the RBI bank rate, period by period, with `damages-interest-calculator`.
5. Check limitation. Read current Supreme Court authority on whether the Limitation Act applies to MSEFC conciliation and arbitration, and compute with `limitation-calculator`.
6. Draft the reference: parties; supplier status; supplies and invoices; acceptance; payment history; amount due; interest computation; documents; and relief. Fit it to the portal's fields.
7. Explain the process: the Council conciliates first, then arbitrates itself or refers to an institution if conciliation fails. Note the Act's overriding effect on a private arbitration clause and confirm current authority.
8. Note for the buyer's side that a challenge to the award needs a pre-deposit of a set share of the award (believed to be 75 percent under section 19; confirm).

## Output

1. The draft reference and statement of claim.
2. An invoice-wise interest schedule.
3. An eligibility note flagging any risk on supplier status or limitation.

## Guardrails and hand-offs

- If the claimant is not a covered supplier, say so clearly and suggest other routes via `litigation-strategy-planner`.
- Never back-date or assume registration status.
- Award challenges: `section-34-37-award-challenge-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
