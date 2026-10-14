# Cheque dishonour (section 138 NI Act)

**When to use:** a client holds a cheque returned unpaid and wants to prosecute the drawer, or a client has received a dishonour notice.
**Who it is for:** advocates for the payee (complainant); the defence branch is at step 10.

## Steps

1. `client-intake-conflict-screener`. Input: cheque, return memo, underlying transaction documents. Output: intake note and conflict result.
   **STOP:** advocate accepts the brief.
2. `limitation-calculator`. Input: cheque date, presentation date, and the date the payee received information of dishonour from the bank (the return memo date may differ). Output: last date for the demand notice, with working.
   Enter it in `matter-deadline-tracker`. This deadline is short; do this on day one.
3. `litigation-chronology-builder`. Output: dates of debt, cheque, presentation, return and any part payment.
4. `issue-spotting-analyst`. Input: chronology and documents. Output: legally enforceable debt, validity period of the cheque, reason for return, signatory and company-accused issues.
   **STOP:** advocate confirms the case is maintainable and who the accused will be.
5. `cheque-dishonour-case-drafter` (notice). Input: approved facts. Output: statutory demand notice.
   **STOP:** advocate approves the notice; send it by modes that create proof of dispatch and delivery.
6. `limitation-calculator`. Input: date the notice was served (or deemed served). Output: the date payment falls due and the window for filing the complaint, with working.
7. `cheque-dishonour-case-drafter` (complaint). Input: notice, proof of service, chronology. Output: complaint, pre-summoning evidence affidavit and list of documents; and the interim compensation application.
   **STOP:** advocate approves the complaint and the forum chosen (territorial jurisdiction).
8. `court-pleading-formatter` and `vakalatnama-appearance-drafter`. Output: formatted complaint and vakalatnama.
9. `criminal-compounding-application-drafter` or `lok-adalat-settlement-drafter` if the drawer offers to settle. Output: compounding application or settlement record.
10. If acting for the drawer instead: `legal-notice-drafter` for the reply notice, then `litigation-strategy-planner` to decide between settlement and defence on the debt.
11. `service-of-process-tracker`. Output: summons and service log after cognisance. Check whether the BNSS requires the Magistrate to hear the accused before taking cognisance of a complaint, and how courts apply this to cheque cases (confirm current authority).
12. `hearing-day-brief-builder` before each listing.

## Deadlines to compute with `limitation-calculator`

- Presentation within the cheque's validity.
- Demand notice from receipt of the return memo.
- Payment period after service of notice, then the complaint-filing window; and any condonation request if the complaint is late.

## Before filing

13. `pre-filing-verification-checker`. Input: notice, complaint, affidavit and annexures. Output: signed verification log. **STOP:** advocate signs, then files.
