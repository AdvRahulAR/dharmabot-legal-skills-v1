---
name: ndps-case-analyst
description: Analyses cases under the Narcotic Drugs and Psychotropic Substances Act, 1985 for the defence or prosecution, covering small, intermediate and commercial quantity, search and seizure safeguards, sampling and inventory before a Magistrate, chain of custody, the twin conditions for bail and default bail. Use when an advocate asks to check an NDPS seizure for compliance with ss.42, 50 or 52A, assess bail in an NDPS case, or test the quantity classification. Do not use for drafting the bail application; use bnss-bail-application-drafter.
---

# NDPS Case Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Test an NDPS case step by step against the Act's mandatory safeguards and produce a checklist for bail, discharge or trial.

## Jurisdiction gate

Confirm the case is before an Indian Special Court under the NDPS Act. Record the State, the seizing agency (police, NCB, DRI, Customs, Excise) and the officer's rank and empowerment. State notifications and standing orders differ by agency.

## Temporal gate

Record the dates of seizure, sampling, arrest and chargesheet. Procedure before 1 July 2024 may follow the CrPC; check with `crpc-bnss-transition-analyst`. Confirm which version of the quantity notification and the drug-disposal rules applied on the seizure date.

## Required inputs

**Blocking**: the FIR or complaint; the seizure memo; the substance, gross and net weight; the place and manner of search (person, vehicle, building, public place); the arrest date; and whom the user acts for.

Also useful: the information recorded before the search, any report to a superior officer, the sampling and inventory record, the laboratory report, and the malkhana register.

## Method

1. Retrieve the current official text of the NDPS Act provisions on search with and without warrant, search of persons, arrest, sampling and disposal (believed ss.41 to 43, 50, 52, 52A and 55; confirm), the bail provision (believed s.37; confirm), the quantity notification and the current sampling rules or standing orders. Record source and date.
2. Quantity: classify small, intermediate or commercial from the notification. Note how current authority treats the neutral substance and mixtures; read before citing.
3. Search and seizure: is it a building, conveyance or public place; was the information recorded and sent to the superior officer where required; was the option of search before a Gazetted Officer or Magistrate given for a personal search; were independent witnesses joined; was search videographed where required.
4. Sampling and chain of custody: when and before whom samples were drawn; inventory certified by a Magistrate as required; sealing; dispatch and receipt at the laboratory; seal intact on receipt; malkhana entries.
5. Arrest: grounds of arrest given in writing; information to relatives; production.
6. Bail: apply the twin conditions where commercial quantity is involved. Assess delay in trial and long custody as current authority treats them. Check default bail time limits and any extension procedure; compute dates with `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
7. Search for and read current Supreme Court authority on each safeguard. Tag anything unread `[verify]`.

## Output

1. A safeguard checklist: each step, complied, not complied or unclear, with record reference.
2. A quantity and bail assessment.
3. Next steps: bail, default bail, discharge points, trial objections.

## Guardrails and hand-offs

- Never advise on concealing, transporting or evading detection of any substance.
- Never invent weights, times or record entries.
- Never promise bail.
- For a fuller record review, use `chargesheet-review-analyst`.
