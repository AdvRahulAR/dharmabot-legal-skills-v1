---
name: legal-knowledge-bank-builder
description: Organises a law firm's or legal team's know-how into a precedent and template bank, a clause library with preferred and fallback positions, negotiation playbooks and short sourced practice notes, each tagged with a law-as-of date and an owner so stale material shows up. Use when a lawyer asks to build a clause library from past contracts, set up a precedent bank, write a practice note or refresh templates after a change in law. Do not use to review a single contract; use playbook-contract-reviewer instead.
---

# Legal Knowledge Bank Builder

Every output is a draft know-how entry for a supervising advocate to review and approve before it goes into the bank.

## Purpose

Turn scattered past work into reusable, current and anonymised material the whole team can trust, and show clearly when it was last checked.

## Jurisdiction gate

- Tag every entry with its governing law. Indian-law entries also need the State where stamp duty, registration or local law affects the clause.
- Entries on foreign law are tagged "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

**Blocking**:
- the source documents (past contracts, opinions, pleadings, notes);
- confirmation that the user is allowed to reuse them inside the firm or team;
- the owner who will approve and maintain the entries.

Also useful: the firm's existing taxonomy, negotiation outcomes on past deals, and the contract types to prioritise.

## Method

1. Retrieve the current official text of every statute, rule or notification an entry relies on (India Code, eGazette, regulator sites), and record the version and date as the entry's law-as-of date.
2. Anonymise first. Remove client names, counterparties, prices, dates, project names and anything that would identify a client. Replace with neutral placeholders.
3. For a clause library, group clauses by type (definitions, payment, liability cap, indemnity, IP, confidentiality, data protection, termination, dispute resolution, governing law, stamp duty and execution).
4. For each clause type, record:
   - the preferred position and its text;
   - one or two fallback positions and when each is acceptable;
   - the walk-away point;
   - the legal basis and risks under Indian law, with sources;
   - how often each version was accepted in past deals, if the data exists.
5. For practice notes: question answered, short answer, sources read, law-as-of date, owner and next review date. Keep each note to one or two pages.
6. For templates: mark every drafting choice that depends on facts with a bracketed note.
7. Set a review cycle. Flag entries that rely on laws that changed recently or are being phased in (for example the new criminal codes, the Labour Codes, the DPDP Rules, the Income-tax Act 2025).
8. Cite case law only after reading it; tag the rest `[verify]` and send to `citation-verifier`.

## Output

1. Clause library or precedent index: entry · type · governing law · law-as-of date · owner · status.
2. Each entry in full with preferred, fallback and walk-away positions.
3. Practice notes with sources.
4. A stale-content report listing entries past their review date.

## Guardrails and hand-offs

- Never put client-identifying or confidential terms into a shared bank.
- Never present an entry as current without a law-as-of date.
- Do not invent negotiation statistics.
- For applying the playbook to a live contract, hand off to `playbook-contract-reviewer` or `nda-triage-reviewer`.
