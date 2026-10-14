---
name: employment-contract-drafter
description: Drafts offer letters, employment agreements and consultant agreements under Indian law, covering wages as defined in the Code on Wages 2019, probation, notice, leave, confidentiality, IP assignment, data protection, restrictive covenants and termination, with State Shops and Establishments flags. Use when someone asks to draft an offer letter, an appointment letter, an employment agreement for a senior hire, or a consultancy agreement. Do not use for testing a non-compete; use restrictive-covenant-analyst instead.
---

# Employment Contract Drafter

Every output is a draft for an advocate enrolled in India to check before it is issued.

## Purpose

Produce a clear, enforceable offer letter, employment agreement or consultant agreement that fits the employee's statutory status and the State where they work.

## Jurisdiction gate

Confirm the employee works in India and record the State or UT and the city of the workplace. Leave, working hours, holidays and registration under the Shops and Establishments Act or factory law vary by State. For a remote employee, record where they actually work. For an expatriate or a foreign employer with no Indian entity, flag the permanent-establishment and payroll issue and hand off to `india-entry-fema-structuring-analyst`.

## Temporal gate

The four Labour Codes are reported to have come into force on 21 November 2025, replacing the earlier central labour laws. Central and State rules have followed in stages. Check whether the State's rules under each Code are notified, and from when, before relying on any threshold.

## Required inputs

Mark as **blocking**:
- the document type (offer letter, full agreement, consultant agreement);
- the role, duties and whether the person supervises or manages others;
- the employer entity and the State of work;
- the pay structure (each component of CTC), and any bonus, variable pay or ESOP grant;
- notice period, probation and any fixed term.

Also useful: the company's handbook, ESOP scheme, existing template, background-check policy and any client-imposed clauses.

## Method

1. Retrieve the current official text of the Code on Wages, the Industrial Relations Code, the Code on Social Security, the OSH Code, the relevant State Shops and Establishments Act and rules, and the DPDP Act and Rules. Record the version and date of each.
2. Classify the role. Decide whether the person is likely a "worker" or "employee" under the Codes (role, supervisory or managerial function, wage level). Workman-type staff get statutory protections that a contract cannot cut down. Flag the classification and its reasons.
3. For a consultant, test whether the arrangement is genuinely independent. If it looks like employment, hand off to `gig-worker-classification-analyst`.
4. Build the pay clause around the statutory definition of "wages" in the Code on Wages. Show which components are in and out of wages, and flag if exclusions exceed the reported 50 percent ceiling. Note the effect on PF, gratuity and bonus.
5. Draft the core terms: appointment, duties, place of work and transfer, probation, hours and leave (at least the State minimums), confidentiality, IP assignment of work product (with a moral-rights waiver to the extent permitted), personal data processing notice, conflicts and outside work, return of property, and termination.
6. Draft restrictive covenants in a defensible form: in-term exclusivity, confidentiality, non-solicitation of employees and clients. Avoid a broad post-term non-compete. Send any covenant the client insists on to `restrictive-covenant-analyst`.
7. Add ESOPs by reference to the scheme only. Do not restate vesting terms that may conflict with it.
8. Check stamp duty on the agreement under the State's stamp law with `state-stamp-duty-calculator`.

## Output

1. The draft offer letter or agreement, with clause headings.
2. A short drafting note: classification, wage-definition table, State-specific points, and clauses needing client decisions.
3. A list of annexures (job description, CTC breakup, IP schedule of prior inventions).

## Guardrails and hand-offs

- Never draft a clause waiving statutory dues, gratuity, PF or ESI.
- Do not label a worker a consultant to avoid statutory obligations.
- Do not state a threshold or wage ceiling as settled; mark it "confirm from the official text".
- For IP-heavy roles or a separate deed of assignment, hand off to `ip-assignment-licence-drafter`.
- For the establishment's statutory compliance, hand off to `labour-codes-compliance-checker`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
