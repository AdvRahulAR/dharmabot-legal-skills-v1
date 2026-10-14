---
name: sarfaesi-enforcement-planner
description: Plans enforcement under the SARFAESI Act, 2002 and the Security Interest (Enforcement) Rules, 2002 for secured lenders, or the defence for borrowers and guarantors, from NPA classification and the demand notice through possession, DM or CMM assistance, valuation and auction to a challenge before the DRT. Use when a client has received a SARFAESI demand or possession notice, a lender wants a recovery plan, or an auction is announced. Do not use to draft the DRT application itself; use drt-application-drafter.
---

# SARFAESI Enforcement Planner

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Map where the matter stands in the SARFAESI process, what each side may lawfully do next, and the dates that control it.

## Jurisdiction gate

Confirm the lender is a secured creditor that may use SARFAESI (bank, notified financial institution, eligible NBFC, or asset reconstruction company) and that the security is enforceable under the Act. Flag exclusions early: agricultural land, small loans below the notified minimum, pledges of movables, and other carve-outs in the Act. Confirm each from the current text. Note the State for DM or CMM jurisdiction and local practice.

## Required inputs

Mark as **blocking**:
- the client's role (lender, borrower, guarantor, tenant, third-party purchaser);
- every notice received or issued, with dates and mode of service;
- the loan and security documents, and the NPA date as stated by the lender;
- whether an auction date has been fixed.

Also useful: account statements, valuation reports, any reply already sent, pending litigation or IBC proceedings, and any OTS offer.

## Method

1. Retrieve the current official text of the SARFAESI Act, the Security Interest (Enforcement) Rules, the RBI prudential norms on NPA classification, and any notification on eligible lenders or minimum amounts. Record versions and dates. Section numbers below are for orientation; confirm each.
2. Check the NPA classification against RBI norms and the account history. A wrong classification is a common defence.
3. Test the demand notice (believed to be section 13(2)): amount, details of secured assets, service on all borrowers and guarantors, and the notice period.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. If the borrower replied, check whether the lender gave reasons for rejecting the objections within the time the Act requires (believed to be section 13(3A)).
5. Test the possession notice and its publication, and any DM or CMM order (believed to be section 14) for jurisdiction, affidavit content and application of mind.
6. Test valuation and the sale notice: the rule on the gap between notice and auction, reserve price, publication, and the borrower's right to redeem before sale. Confirm the current redemption position from recent Supreme Court authority.
7. Check any moratorium under the IBC that would stop enforcement.
8. Build options for the client. Borrower: reply, payment, OTS, restructuring, a DRT application (believed to be section 17) with stay, or a writ only in exceptional cases. Lender: cure defects, re-issue notices, proceed to auction, or file before the DRT.
9. Compute every deadline with `limitation-calculator`. Search for and read current authority on each contested point; tag unread authority `[verify]`.

## Output

1. A stage map: step, document, date, compliance status, defect found.
2. An options table: option, legal basis, cost, timing, risk.
3. A dated action plan with the next three steps and who does them.

## Guardrails and hand-offs

- Never advise on concealing, transferring or damaging secured assets, or on obstructing lawful possession.
- Never promise that an auction will be stayed.
- DRT drafting goes to `drt-application-drafter`; settlement proposals go to `one-time-settlement-proposal-drafter`.
- Never invent case law. Run `citation-verifier` before delivery.
