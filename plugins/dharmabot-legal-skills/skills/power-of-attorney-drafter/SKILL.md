---
name: power-of-attorney-drafter
description: Drafts general and special powers of attorney under the Powers of Attorney Act, 1882 for property sales, litigation, banking and company matters in any Indian State or UT, with precise powers, limits, revocation and ratification, and plans execution in India or abroad with State stamp and registration rules. Use when a lawyer asks for a GPA or SPA, a POA for an NRI to sell a plot, a litigation POA, or a revocation of a POA. Do not use to legalise or apostille a document signed abroad; use document-legalisation-planner.
---

# Power of Attorney Drafter

Every output is a draft for an advocate enrolled in India to check before execution.

## Purpose

Give the agent exactly the powers the principal intends, no more, in a form the Sub-Registrar, bank or court will accept.

## Jurisdiction gate

Record where the POA will be executed (India or abroad) and the State or UT where it will be used. Stamp duty and registration rules for POAs differ sharply by State, and several States charge conveyance-level duty on a POA to sell given to a non-family member or for consideration. If executed abroad, note that it must be authenticated by a notary or Indian mission as required and stamped within the State's time limit after arrival.

## Required inputs

Mark as **blocking**:
- principal and agent details, their relationship, and the principal's residence country;
- the specific acts to be authorised and the property, case, account or company concerned;
- whether the POA is general or special, and any time limit;
- where it will be signed and where used.

Also useful: the title documents for property, case numbers for litigation, bank or registrar format requirements, and whether consideration has passed to the principal.

## Method

1. Retrieve the current official text of the Powers of Attorney Act, 1882, the relevant agency provisions of the Indian Contract Act, 1872, the Registration Act, 1908, the State stamp law and any State rule requiring registration of POAs to sell. Open `references/india-state-statutes.md` as a starting point. Record the version and date.
2. Choose general or special. Prefer a special POA for a single sale or case.
3. List powers as specific, numbered acts: negotiate, sign the agreement and sale deed, receive consideration into a named account, appear before the Sub-Registrar, apply for mutation, sign vakalatnamas, compromise (only if intended).
4. Add limits: minimum price or approval, no power to mortgage or gift unless intended, no sub-delegation unless intended, duration, and accounting duties.
5. Add revocation and ratification clauses. Note that a POA ends on the principal's death or incapacity unless it is coupled with an interest. Flag any request to make it irrevocable and check whether an interest really exists.
6. Note that a POA is not a conveyance and a GPA-plus-agreement-plus-will does not transfer title (Suraj Lamp and Industries v. State of Haryana, Supreme Court, 2011; confirm current treatment).
7. Execution plan: in India, notarisation or registration as the State and the use require; abroad, hand off to `document-legalisation-planner`. Hand off stamp figures to `state-stamp-duty-calculator`.

## Output

1. The draft POA.
2. Execution, authentication, stamping and registration checklist for the place of signing and use.
3. A short draft revocation deed and notice, if asked.

## Guardrails

- Never draft a POA to disguise a sale or to avoid stamp duty.
- Never give powers wider than the instructions, and highlight any power to sell, mortgage, gift or compromise.
- Do not state stamp amounts or time limits from memory.
- Confirm the principal's capacity and free consent; the advocate or notary verifies identity.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
