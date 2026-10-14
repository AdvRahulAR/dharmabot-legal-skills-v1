---
name: arbitration-invocation-notice-drafter
description: Drafts a notice invoking arbitration under section 21 of the Arbitration and Conciliation Act, 1996, or a request for arbitration under institutional rules such as MCIA, DIAC, ICA or IIAC, stating the claims, relief, arbitration agreement, proposed arbitrator and compliance with pre-arbitration steps. Use when a lawyer says invoke arbitration, send the section 21 notice, or file a request for arbitration with an institution. Do not use to appoint an arbitrator through the court; use section-11-appointment-petition-drafter instead.
---

# Arbitration Invocation Notice Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce a notice or request that validly commences arbitration, fixes the date of commencement for limitation, and sets up the next step if the other side does not cooperate.

## Jurisdiction gate

Confirm the arbitration is seated in India. If the clause names a foreign seat or foreign institution (for example SIAC or ICC with a seat abroad), hand off to `international-arbitration-planner`. Note the seat city and State.

## Required inputs

Mark as **blocking**:
- the arbitration clause and the contract it is in;
- the parties' correct legal names and addresses for notice under the contract;
- a summary of each claim with amounts and the date each cause of action arose;
- what pre-arbitration steps the clause requires and what has been done.

Also useful: correspondence, earlier notices, bank guarantees, invoices and the client's preferred arbitrator or panel.

## Method

1. Retrieve the current official text of the Arbitration and Conciliation Act, 1996 (section 21 on commencement, section 11 on appointment, section 43 on limitation), the Limitation Act, 1963, and any institutional rules named. Record the version and date. Confirm every section, rule and article number used in this skill against that official text before relying on it.
2. Read the clause. Identify the notice mechanics (address, mode, contract notice clause), the tribunal size and the appointment route. If the clause allows only one party to appoint, flag it and seek advice from `arbitration-clause-reviewer` before proposing a name.
3. Check pre-arbitration steps. If a negotiation or mediation tier is mandatory and not done, say so and suggest how to comply or why it is futile, with evidence.
4. Screen each claim against the clause scope and any exclusions (for example "excepted matters" in government contracts, or engineer's decisions declared final). List excluded claims separately.
5. Check limitation for each claim. Hand off computation to `limitation-calculator` and state that the notice date is believed to be the commencement date under section 21; confirm from the text and current authority.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
6. Draft the notice or request:
   - parties and capacity;
   - the contract and arbitration agreement quoted in full;
   - facts in short dated paragraphs;
   - each claim, its contractual basis, amount and interest claimed;
   - relief sought;
   - compliance with pre-arbitration steps;
   - the proposed arbitrator or panel, a request to concur within the agreed or statutory time, and a statement that the court will be approached otherwise;
   - reservation of the right to amend and add claims.
7. For an institutional request, follow the institution's form, filing fee and copy requirements. Ask the user to confirm current fees from the institution's website.
8. Prepare a dispatch plan: every contractual address, email if allowed, and proof of delivery to be kept.

## Output

1. The draft notice or request for arbitration.
2. A claims schedule: claim · clause · amount · interest · date of cause of action · limitation note.
3. A note on excluded or weak claims and missing documents.
4. A next-steps line with the date after which a section 11 petition may be considered.

## Guardrails and hand-offs

- Do not overstate amounts or invent figures; mark estimates as estimates.
- Never invent authority; tag anything not read in full `[verify]` and run `citation-verifier`.
- Do not threaten criminal action to pressure payment.
- If the respondent fails to appoint, hand off to `section-11-appointment-petition-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
