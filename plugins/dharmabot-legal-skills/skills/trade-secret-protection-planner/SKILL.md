---
name: trade-secret-protection-planner
description: Plans trade secret protection in India, which has no dedicated statute, covering classification of confidential information, access controls, confidentiality and invention clauses, onboarding and exit protocols, forensic preservation on a suspected leak, and the elements of a breach of confidence injunction. Use when a company wants a trade secret programme or a key employee left for a competitor with code or customer lists. Do not use to draft the NDA (use nda-drafter), test a non-compete (use restrictive-covenant-analyst) or draft the injunction (use interim-injunction-application-drafter).
---

# Trade Secret Protection Planner

Every output is a draft plan for an advocate enrolled in India to check.

## Purpose

Help a business protect what it cannot patent, and act fast and lawfully when a leak is suspected.

## Jurisdiction gate

Confirm the business and the people involved are in India, and note the city for the competent court (commercial court or High Court on its original side). For employees, servers or recipients abroad, mark foreign remedies (for example the US Defend Trade Secrets Act) "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**: what information is at stake and why it is secret and valuable; how it is stored and who can access it; the employment or contractor agreements that apply; and, for a suspected leak, what is known (dates, devices, downloads, the new employer).

Also useful: IT access logs, HR exit records, NDAs with vendors, and any earlier incidents.

## Method

1. Retrieve the current official text of the Indian Contract Act provisions on restraint of trade, the IT Act provisions on unauthorised access, relevant BNS offences, and the Commercial Courts Act on urgent interim relief. Record versions and dates. Note that a trade secrets bill has been proposed in the past; check its status.
2. **Inventory.** List categories of confidential information (source code, formulas, pricing, customer data, processes). Rank by value and risk.
3. **Controls.** Access by role, marking, logging, data loss prevention, clean desk and device rules, and vendor access.
4. **Contracts.** Check confidentiality, invention assignment, non-solicit and return-of-material clauses in employment and vendor agreements. Hand off gaps to `nda-drafter` and non-compete questions to `restrictive-covenant-analyst`.
5. **Onboarding and exit.** Onboarding declarations that no third-party secrets are brought in; exit interviews, device return, access revocation and a written reminder of continuing duties.
6. **Suspected leak.**
   - Preserve first: image devices and mailboxes through a qualified forensic examiner with a chain of custody; issue a legal hold through `legal-hold-preservation-planner`.
   - Do not access the employee's personal accounts or devices without lawful basis.
   - Plan a cease-and-desist letter to the employee and, if appropriate, the new employer.
   - Assess urgent relief: the information, its confidentiality, the circumstances of confidence, actual or threatened misuse, and harm.
7. Search for and read current High Court authority on breach of confidence and on post-employment restraints; tag unread items `[verify]`.

## Output

1. Protection programme: inventory, controls, contracts and protocols.
2. For a leak: a 72-hour action plan and an evidence log template.
3. A pleading outline of the breach of confidence elements for the injunction drafter.

## Guardrails and hand-offs

- Never advise covert surveillance or access to personal devices or accounts without lawful basis.
- Never assert that a non-compete is enforceable after employment ends.
- Do not overstate secrecy; generic skill and knowledge are not trade secrets.
- For the injunction, hand off to `interim-injunction-application-drafter`.
- Before any letter is sent, hand off to `pre-filing-verification-checker`.
