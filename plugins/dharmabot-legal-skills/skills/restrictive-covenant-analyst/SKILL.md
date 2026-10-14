---
name: restrictive-covenant-analyst
description: Analyses non-compete, non-solicitation, garden-leave and confidentiality clauses in employment, consultancy and business-sale contracts under section 27 of the Indian Contract Act 1872, separating in-term from post-term restraints, and suggests enforceable alternatives. Use when a lawyer asks whether a departing employee can be stopped from joining a competitor, whether a non-compete is valid, or how to protect clients and confidential information. Do not use for drafting the full contract; use employment-contract-drafter instead.
---

# Restrictive Covenant Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Give a reasoned view on whether a restraint is likely to be enforced in India, what relief is realistic, and what the client can do instead.

## Jurisdiction gate

Confirm the contract's governing law and where the employee works and would compete. If a foreign governing-law or foreign-court clause is present, note that Indian courts are likely to apply section 27 as a matter of Indian public policy for enforcement in India, and confirm current authority. Flag foreign-law points for counsel qualified there.

## Required inputs

Mark as **blocking**:
- the full text of the restrictive clauses and the definitions they use;
- the type of contract (employment, consultancy, shareholder, business sale);
- whether the restraint operates during the term or after it ends;
- the employee's role, access to confidential information, and the new role or business.

Also useful: the exit date and manner of exit, any garden-leave pay, evidence of data taken or clients approached, and the new employer's details.

## Method

1. Retrieve the current official text of section 27 of the Indian Contract Act and its exception for the sale of goodwill. Record the version and date.
2. Sort each clause into: in-term exclusivity, post-term non-compete, non-solicitation of clients, non-solicitation of employees, confidentiality, garden leave, and business-sale restraint.
3. Apply the settled lines, after reading current authority:
   - in-term restraints are generally enforceable if reasonable (for example Niranjan Shankar Golikari v. Century Spinning, Supreme Court, 1967; confirm current treatment);
   - post-term non-competes in employment are generally void, whatever their reasonableness (for example Superintendence Co. of India v. Krishan Murgai, Supreme Court, 1980; confirm current treatment);
   - confidentiality obligations survive and can be enforced through injunction;
   - non-solicitation is treated inconsistently across High Courts; read the jurisdictional High Court's recent decisions;
   - restraints tied to the sale of goodwill or shares may fall within the exception if reasonable in time and area.
4. Test garden leave: is the employee still employed and paid in full, and is the period proportionate?
5. Look at the evidence of actual misuse. A confidentiality or trade-secret case on real facts is usually stronger than a bare non-compete.
6. Search for and read current Supreme Court and High Court decisions. Tag anything not read in full `[verify]`.
7. Suggest enforceable alternatives: longer notice with garden leave, deferred or clawback-linked variable pay, tighter confidentiality, specific client non-dealing tied to confidential information, and invention assignment.

## Output

1. A clause-by-clause table: clause · type · likely enforceability · reasons · authority.
2. Realistic remedies (injunction on confidentiality, damages, clawback) and their evidential needs.
3. Recommended redraft language or alternatives.

## Guardrails and hand-offs

- Never promise an injunction or a particular outcome.
- Never invent a case, citation or paragraph number.
- Do not advise on steps that pressure an employee unlawfully, such as withholding statutory dues.
- To seek urgent relief, hand off to `interim-injunction-application-drafter`.
- To redraft the contract, hand off to `employment-contract-drafter`.
