---
name: enforcement-summons-response-planner
description: Triages and plans the response to summons and notices served on an Indian company or its officers by police under the BNSS, the Directorate of Enforcement, SFIO, income-tax and GST authorities, SEBI, CBI or a court, covering authority and scope, privileged material, protection against self-incrimination under Article 20(3), accompanying counsel, document production logs and timelines. Use when a company or officer receives a summons, notice to appear or demand for records. Do not use for full PMLA strategy; use pmla-proceedings-analyst.
---

# Enforcement Summons Response Planner

Every output is a draft for supervising counsel to check.

## Purpose

Work out what the summons lawfully requires, who must respond and how, and produce a compliant, controlled response plan.

## Jurisdiction gate

Confirm the summons is issued by an Indian authority and identify the statute and provision cited. Record the issuing office, the person summoned, and the place and date of appearance. Foreign requests (letters rogatory, MLAT) need counsel qualified in the requesting jurisdiction; flag them.

## Temporal gate

Note the date for appearance or production and work back. For police notices, check the BNSS (from 1 July 2024) or CrPC with `crpc-bnss-transition-analyst` if the FIR is older. For income-tax summons, the Income-tax Act, 2025 is reported to replace the 1961 Act from 1 April 2026; check which Act governs the proceeding and the tax year before citing a provision.

## Required inputs

**Blocking**: a copy of the summons or notice; who is summoned (company, officer by name or by designation); the capacity (witness, accused, person in charge); and the date and place of appearance.

Also useful: the underlying proceeding (FIR, ECIR, inquiry number), earlier correspondence, and what records exist and where.

## Method

1. Retrieve the current official text of the provision under which the summons was issued and its procedural rules (for example the BNSS notice provisions, PMLA summons power, the Companies Act provisions for SFIO and inspectors, Income-tax and CGST summons powers, SEBI Act powers). Record source and date. Confirm all section numbers.
2. Validity: is the authority empowered; is the summons signed and specific; is the period and scope reasonable; is the person correctly identified.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Capacity and risk: witness or accused; risk of arrest; whether anticipatory bail or protection should be considered (use `arrest-rights-advisor` and, for ED, `pmla-proceedings-analyst`).
4. Rights: Article 20(3) protection against compelled self-incrimination and how current authority applies it to each statute; the right to counsel at examination where allowed or practised; and statements' evidentiary value under that statute. Read authority before citing; tag anything unread `[verify]`.
5. Privilege: identify legal advice and communications with counsel; prepare a privilege log; do not withhold non-privileged records.
6. Production: collect from the legal hold (use `legal-hold-preservation-planner`), review, number pages, keep a copy set, and record what was produced, to whom and when, with acknowledgment.
7. Timing: if more time is needed, draft a short request with reasons before the date.
8. Prepare the officer: factual briefing from documents, no speculation, ask to see documents before answering, correct errors in the recorded statement before signing.

## Output

1. A triage note: validity, capacity, risk and deadline.
2. A response plan with owners and dates.
3. Drafts: covering letter, adjournment request, privilege log and production log.

## Guardrails and hand-offs

- Never advise ignoring a valid summons, destroying records or giving false answers.
- Never coach a witness to say anything untrue.
- Never promise immunity from arrest.
