# Employee termination and dispute

**When to use:** an employer wants to end an employee's employment (misconduct, performance, redundancy or closure), or an exit has turned into a dispute.
**Who it is for:** employment lawyers and in-house HR counsel acting for the employer. Employee-side counsel can use steps 3, 4, 8 and 11.

## Steps

1. `in-house-request-triage-screener` or `client-intake-conflict-screener`. Input: the request, employee's role and history. Output: risk rating and intake note.
   **STOP:** advocate confirms who instructs and accepts the matter.
2. `client-data-redaction-checker` if the profile requires redaction. Employee files contain personal data.
3. `gig-worker-classification-analyst`. Input: contract and working arrangement. Output: whether the person is an employee, workman, contractor or gig worker. This decides which law applies.
4. `termination-retrenchment-analyst`. Input: classification, contract, reason for exit, headcount. Output: lawful exit routes, notice and approval requirements, and risk.
   **STOP:** advocate and client approve the exit route before anything is communicated to the employee.
5. If misconduct: `disciplinary-inquiry-drafter`. Output: show-cause notice, charge-sheet and inquiry record. **STOP:** advocate approves each notice before issue.
6. If a sexual harassment complaint is involved: `posh-inquiry-report-drafter` through the Internal Committee, not the disciplinary route.
7. `restrictive-covenant-analyst`. Input: non-compete, non-solicit and confidentiality clauses. Output: what is enforceable after exit.
8. `employee-dues-calculator`. Input: salary, service, leave balance. Output: gratuity, notice pay, retrenchment compensation and full-and-final dues with working.
9. `employment-contract-drafter` for a separation agreement or release, if negotiated. **STOP:** advocate approves the release terms.
10. If the employee disputes the exit: `litigation-strategy-planner`. Output: settle, conciliate or defend.
11. `labour-dispute-claim-drafter`. Output: reply or pleading before the conciliation officer, Labour Court or Industrial Tribunal. Check whether the Labour Codes (reportedly in force from 21 November 2025; confirm) govern the dates in issue, and which forum then has jurisdiction.
    **STOP:** advocate approves the pleading.
12. If the employee goes to a civil court or High Court instead: `written-statement-drafter` or `writ-petition-drafter` as the case requires.
13. `matter-closure-retention-checker` when the matter ends. Output: retention and deletion of employee data.

## Deadlines to compute with `limitation-calculator`

- Notice period and payment of full-and-final dues and gratuity.
- Any prior notice to, or permission from, the appropriate government for retrenchment or closure.
- Limitation for the employee's dispute or claim, and time to reply. Enter them in `matter-deadline-tracker`.

## Before issue or filing

14. `pre-filing-verification-checker`. Input: termination letter, dues working or pleading. Output: signed verification log. **STOP:** advocate signs before anything is issued or filed.
