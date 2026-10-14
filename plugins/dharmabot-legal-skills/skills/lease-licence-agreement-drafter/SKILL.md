---
name: lease-licence-agreement-drafter
description: Drafts and reviews residential and commercial leases, rent agreements and leave-and-licence agreements in any Indian State or UT under the Transfer of Property Act, 1882 and the applicable State rent control or tenancy law, covering rent and escalation, deposit, lock-in, fit-outs, subletting, termination, stamp duty and registration. Use when a lawyer asks for a rent agreement, a nine-year showroom lease, a leave and licence for Mumbai, or a review of a landlord's lease. Do not use for eviction or rent disputes; use tenancy-rent-control-analyst.
---

# Lease and Licence Agreement Drafter

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Choose between a lease and a licence, and draft or review the agreement so that it is enforceable, properly stamped and registered, and balanced for the client.

## Jurisdiction gate

Record the State or UT and city. Identify whether a State rent control law, a newer tenancy law based on the Model Tenancy Act, 2021, or only the Transfer of Property Act applies to these premises. Some laws exclude premises above a rent threshold, commercial premises or company tenants. Note any State-specific leave-and-licence rules (for example in Maharashtra).

## Temporal gate

Tenancy law is changing in several States. Check whether a new State tenancy law or its rules are in force on the agreement date, and from when, and whether the Rent Authority registration or filing it requires applies.

## Required inputs

Mark as **blocking**:
- the State and city, and whether the premises are residential or commercial;
- which party the client is;
- term, rent, deposit and escalation;
- the premises description and the lessor's title or authority to let.

Also useful: lock-in, fit-out period and rent-free period, permitted use, maintenance and utilities, signage, insurance, subletting and assignment wishes, and any draft received.

## Method

1. Retrieve the current official text of the Transfer of Property Act, 1882 (lease provisions), the Registration Act, 1908, the State stamp law, and the State rent control or tenancy law and rules. Open `references/india-state-statutes.md` as a starting point. Record the version and date.
2. Lease or licence: a lease transfers an interest in the property; a licence is a personal permission. Substance, not label, decides. Explain the practical difference for this State's rent law and eviction route.
3. Registration and stamp: leases above one year are generally compulsorily registrable; confirm the State rule, including any compulsory registration for leave-and-licence agreements. Hand off figures to `state-stamp-duty-calculator`.
4. Draft or review the core clauses: parties and authority; premises and use; term and renewal; rent, escalation and GST on commercial rent (confirm with a tax adviser); deposit and refund; lock-in; maintenance and repairs; fit-outs and reinstatement; subletting; access; insurance; indemnity; termination and notice; holding over; dispute resolution.
5. For a review, mark each clause: acceptable, negotiate, or reject, with a suggested redraft.
6. Flag conflicts with mandatory State law (for example deposit caps or notice periods under a new tenancy law).

## Output

1. The draft agreement, or a clause-by-clause review table with redlines.
2. Lease versus licence note, where relevant.
3. Execution, stamping, registration and any Rent Authority filing checklist.

## Guardrails

- Never quote a deposit cap, stamp rate or rent threshold from memory.
- Never draft a licence to disguise a lease in order to evade rent law.
- Disputes, eviction and rent fixation go to `tenancy-rent-control-analyst`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
