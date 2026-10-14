---
name: playbook-contract-reviewer
description: Reviews a commercial contract clause by clause against the organisation's playbook or Indian-law market positions, covering liability caps, indemnities, warranties, IP, payment, termination, data protection and dispute resolution, and enforceability under the Indian Contract Act and Specific Relief Act, producing a risk-ranked issues list, missing protections and replacement wording. Use when a lawyer asks to review, redline or mark up an MSA, customer agreement or other commercial contract. Do not use for a quick NDA triage; use nda-triage-reviewer instead.
---

# Playbook Contract Reviewer

Every output is a review for an advocate enrolled in India or in-house counsel to check before it goes to the counterparty.

## Purpose

Find every deviation from the client's position, rank it by risk, and give wording that fixes it.

## Jurisdiction gate

Identify the governing law, forum and each party's location. Apply Indian law where it governs. If foreign law governs, review commercial allocation only and hand off legal enforceability to `cross-border-contract-reviewer`.

## Required inputs

Mark as **blocking**:
- the full contract, including schedules and documents incorporated by reference;
- which party the client is;
- the playbook, or the client's confirmation to use Indian market defaults.

Also useful: the deal value, the relationship's importance, the client's risk appetite, earlier drafts and the counterparty's comments.

## Method

1. Retrieve the current official text of the Indian Contract Act, 1872 (including the provisions on damages, penalties, indemnity and restraint of trade), the Specific Relief Act, 1963 as amended in 2018, and any sector law the contract touches. Record the version and date.
2. Map the contract: parties, term, price, key obligations, and defined terms. Check that defined terms are used consistently.
3. Review each clause against the playbook. At least cover:
   - scope, deliverables and acceptance;
   - fees, invoicing, taxes (GST and withholding) and late payment;
   - warranties and disclaimers;
   - IP ownership, licences and background IP;
   - confidentiality and data protection (DPDP Act, 2023 and Rules, checking which provisions are in force);
   - indemnities: triggers, procedure, and whether they sit inside or outside the cap;
   - limitation of liability: cap amount, exclusions, consequential loss wording;
   - term, termination, cure and consequences;
   - assignment, change of control and subcontracting;
   - governing law, dispute resolution and seat;
   - force majeure.
4. **Enforceability.** Flag liquidated damages that look like penalties, restraints that may be void under section 27 (believed to be the section; confirm against the official text), waivers of statutory rights, and specific performance assumptions under the amended Specific Relief Act. Search for and read current authority where relied on; tag unread authority `[verify]`.
5. **Missing protections.** List clauses the playbook expects that are absent.
6. **Risk rank.** High (financial or legal exposure, must change), medium (should change), low (nice to have).
7. **Redlines.** For each issue give replacement wording and a fallback position.
8. Mark items needing business approval (commercial terms, caps, pricing).

## Output

1. An executive summary: overall risk and the top five issues.
2. An issues list: clause · issue · risk rank · proposed wording · fallback · approver.
3. Missing protections.
4. A redline in the format the user asks for (tracked text or clause-by-clause replacements).

## Guardrails and hand-offs

- Do not change commercial terms without flagging them for business approval.
- Never invent a playbook position or market standard; label defaults.
- Negotiation sequencing goes to `contract-negotiation-planner`; execution and stamping go to `contract-execution-stamping-checker`.
