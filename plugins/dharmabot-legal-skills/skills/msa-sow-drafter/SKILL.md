---
name: msa-sow-drafter
description: Drafts master services agreements, statements of work, consultancy and service agreements under Indian law with SLAs, change control, acceptance, fees and GST, IP ownership, DPDP Act data protection, liability, termination and dispute resolution, keeping the SOW as a reusable template. Use when a lawyer asks for an MSA, a services agreement, a consultancy agreement, an SOW or an SLA schedule. Do not use to review an MSA received from the other side; use playbook-contract-reviewer instead.
---

# MSA and SOW Drafter

Every output is a draft for an advocate enrolled in India to check before it is sent.

## Purpose

Produce a services framework that the client can reuse: one MSA with legal terms, and SOWs that carry the commercial detail.

## Jurisdiction gate

Confirm Indian law is to govern and note each party's State and country. If either party is foreign, flag tax, FEMA and governing-law points for `cross-border-contract-reviewer`. If the services are in a regulated sector (banking, insurance, health, telecom, government), flag that sector rules may override the template.

## Temporal gate

Check from when the following apply on the signing date: the DPDP Act, 2023 and Rules (phased), and the Income-tax Act, 2025 for withholding references. Use the provisions in force and record the date checked.

## Required inputs

Mark as **blocking**:
- which side the client is (supplier or customer);
- the services, delivery model and locations;
- fee model (fixed, time and materials, milestone, subscription);
- whether personal data or customer systems will be accessed.

Also useful: the client's template or playbook, service levels wanted, IP expectations, liability appetite, and the preferred dispute forum.

## Method

1. Retrieve the current official text of the Indian Contract Act, 1872, the Specific Relief Act, 1963, the CGST Act, 2017 and IGST rules on supply of services, the applicable income-tax law on withholding, the DPDP Act, 2023 and Rules, and the Copyright Act, 1957 on assignment of works. Record the version and date.
2. **Structure.** MSA (legal terms) plus Schedule 1 SOW template, Schedule 2 SLA, Schedule 3 change control, Schedule 4 data protection. State the order of precedence.
3. **Services and acceptance.** Deliverables, acceptance tests, deemed acceptance, and rework.
4. **SLA.** Metrics, measurement, reporting, service credits as a price adjustment, and a cap on credits. Avoid wording that makes credits look like a penalty.
5. **Fees.** Invoicing, due dates, GST added where applicable, withholding with certificates, disputed invoices, late-payment interest, and MSMED Act rights if the supplier is a registered MSE.
6. **IP.** Background IP stays with its owner. Foreground IP per the client's side, with an assignment that meets Copyright Act formalities. Hand off complex licensing to `ip-assignment-licence-drafter`.
7. **Data protection.** Roles (data fiduciary and processor), security, breach notice, sub-processors, deletion. Hand off a full DPA to `data-processing-agreement-reviewer`.
8. **Risk.** Warranties, indemnities (IP infringement, data breach, third-party claims), liability cap and exclusions, insurance.
9. **Term and exit.** Termination for convenience and breach, cure periods, transition assistance, and survival.
10. **Disputes.** Escalation, then arbitration with a stated seat and rules, or courts. Check that the clause works under `arbitration-clause-reviewer` standards.
11. **Boilerplate.** Non-solicit of staff (flag section 27 risk), assignment, subcontracting, force majeure, notices, counterparts and e-signature.

## Output

1. The draft MSA with schedules.
2. A blank SOW template and a completed first SOW if facts are given.
3. A drafting note: choices made, items for business sign-off, sector review flags, and execution points for `contract-execution-stamping-checker`.

## Guardrails and hand-offs

- Do not state GST or withholding rates; refer to the current law and the client's tax adviser.
- Do not present service credits as liquidated damages without analysis.
- Review against a playbook through `playbook-contract-reviewer`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
