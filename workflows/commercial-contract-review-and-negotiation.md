# Commercial contract review and negotiation

**When to use:** a client sends a counterparty's draft (or wants its own draft) for an MSA, SaaS, vendor, distribution, licence or similar commercial contract.
**Who it is for:** transactional lawyers, in-house counsel and LPO reviewers.

## Steps

1. `in-house-request-triage-screener` (in-house) or `client-intake-conflict-screener` (law firm). Input: the request and the draft. Output: risk rating and intake note.
   **STOP:** advocate confirms the matter is taken on and who the decision-maker is.
2. `client-data-redaction-checker` if the practice profile requires redaction before AI processing. Output: pseudonymised draft and a local re-identification map.
3. `contract-summariser`. Input: the draft. Output: one-page summary of parties, term, price, liability and exit.
4. Pick the reviewer for the contract type:
   - `playbook-contract-reviewer` for any contract against the profile's playbook positions;
   - `vendor-saas-agreement-reviewer`, `ai-vendor-contract-reviewer`, `distribution-franchise-agreement-drafter` or `msa-sow-drafter` for those types;
   - `cross-border-contract-reviewer` if a party is foreign;
   - `nda-triage-reviewer` if it is only an NDA.
   Output: issues list with proposed redlines.
5. Specialist checks as needed: `arbitration-clause-reviewer`, `restrictive-covenant-analyst`, `data-processing-agreement-reviewer`, `open-source-licence-reviewer`.
   **STOP:** advocate approves the issues list and which points are must-haves.
6. `contract-negotiation-planner`. Input: approved issues, client's priorities. Output: positions, fallbacks and trade-offs.
   **STOP:** client signs off the negotiation mandate.
7. `adversarial-draft-reviewer`. Input: redlined draft. Output: the draft attacked as opposing counsel would, with consistency checks.
8. Negotiate. After each turn, re-run the reviewer from step 4 on the counterparty's mark-up and update the plan.
9. `contract-amendment-drafter` if the deal changes after signing or a novation is needed.
10. `contract-execution-stamping-checker`. Input: final agreed draft, State of execution. Output: execution, e-signing, stamping and registration steps. Use `state-stamp-duty-calculator` for the duty.
    **STOP:** advocate approves the execution version.
11. `contract-obligations-tracker`. Output: obligations, notice periods and renewal dates.

## Deadlines to compute with `limitation-calculator`

- Renewal and termination notice dates, and any limitation for claims under an existing contract being replaced.
- Stamping: in most States duty is payable before or at execution, with only a short window in some; confirm the State rule. Enter dates in `matter-deadline-tracker`.

## Before signing

12. `pre-filing-verification-checker`. Input: execution version and stamp-duty working. Output: signed verification log. **STOP:** advocate signs the log before the client executes.
