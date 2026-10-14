---
name: education-institution-compliance-checker
description: Checks approvals and duties of schools, colleges and universities under the UGC Act, 1956 and UGC regulations, AICTE approval, NMC, nursing and NCTE norms, State fee regulation laws, CBSE and State board affiliation, and the reserved admissions duty under the Right of Children to Free and Compulsory Education Act, 2009. Use when a trust, society or company running an institution wants a compliance check, fee regulation advice or RTE admissions review. Do not use for trust registration or tax status (use nonprofit-fcra-compliance-advisor) or edtech consumer issues.
---

# Education Institution Compliance Checker

Every output is a draft compliance review for an advocate enrolled in India to check.

## Purpose

Give an institution a clear list of the approvals it must hold, the duties it must meet, and the gaps to close before inspection.

## Jurisdiction gate

Identify the State or UT and each institution's type: school (board), college (affiliating university), standalone institute, university (State, private, deemed), or foreign campus. Education is a concurrent subject, so State laws on fees, admissions and recognition vary. Foreign campus rules abroad are "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

UGC, AICTE, NMC, NCTE, the Indian Nursing Council and CBSE revise regulations and approval handbooks often, usually per academic year. Record the academic year in issue and retrieve the handbook or bye-laws for that year. State fee orders are often year-specific.

## Required inputs

Mark as **blocking**: the State; the operating entity and its legal form; each institution with its type, affiliation and approvals held; and the question in issue (fee regulation, RTE admissions, approval renewal, inspection).

Also useful: fee structure, admission data, land and building records, faculty data, last inspection report, and notices received.

## Method

1. Open `references/india-state-statutes.md` as a starting point, then retrieve the current official text of the relevant central Acts and regulations, the regulator's approval handbook, CBSE affiliation bye-laws, the State fee regulation law and orders, and the State RTE rules from official sites and the State Gazette. Record versions and dates.
2. Build an approvals register per institution: regulator, approval, validity, conditions, renewal date.
3. **Regulator norms.** Check land, building, faculty ratio, qualifications, intake, and disclosure on the website against the current handbook.
4. **Fees.** Identify the State fee committee or law, whether fees need approval, capitation bans, refund rules, and fee hike limits.
5. **RTE admissions.** For unaided non-minority schools, check the reserved seats at entry level, the State's lottery or portal process, reimbursement claims, and record-keeping. Check whether the school is a minority institution, as exemptions apply.
6. **Universities.** Check UGC rules on deemed or private university status, distance and online programmes, and degree nomenclature.
7. **Student protections.** Anti-ragging, grievance redressal, POSH, child protection, and disability access.
8. Search for and read current authority on fee regulation and RTE in the State; tag unread items `[verify]`.

## Output

1. Approvals register per institution.
2. Gap table: requirement · source · status · fix · deadline.
3. Short notes on fee regulation and RTE admissions.

## Guardrails and hand-offs

- Never state a fee cap, ratio or seat percentage as settled without the current source.
- Never advise capitation or concealing fees.
- For trust, society or FCRA matters, hand off to `nonprofit-fcra-compliance-advisor`; for approval applications, `licence-application-drafter`.
- Run `citation-verifier` before delivery.
