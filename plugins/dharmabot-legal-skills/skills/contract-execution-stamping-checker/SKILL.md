---
name: contract-execution-stamping-checker
description: Checks how an Indian agreement must be executed before signing, covering signatory authority and board resolutions, e-signature validity and exclusions under the IT Act, 2000, stamp duty under the Indian Stamp Act and State stamp laws, e-stamping, under-stamping, notarisation and registration under the Registration Act, 1908, and produces a signing checklist. Use when a lawyer asks how to sign, e-sign, stamp or register an agreement, or whether an unstamped contract is valid. Do not use to compute the duty amount; use state-stamp-duty-calculator instead.
---

# Contract Execution Stamping Checker

Every output is a review for an advocate enrolled in India to check before the document is signed.

## Purpose

Prevent a valid deal from becoming hard to enforce because it was signed, stamped or registered the wrong way.

## Jurisdiction gate

Identify every State or UT where the document is signed, where the property is (if any), and where it will be acted on. Stamp law differs by State, and duty may be payable again when a document is brought into another State. If any party signs abroad, hand off to `document-legalisation-planner`.

## Required inputs

Mark as **blocking**:
- the document (or its type, parties and key terms);
- the place and date of each party's signature, and the signing method (wet ink, Aadhaar e-sign, digital signature certificate, platform signature);
- whether it concerns immovable property, a power of attorney, or a negotiable instrument.

Also useful: constitutional documents and board or partner authorisations, consideration and term, and whether the document is an amendment to a stamped original.

## Method

1. Retrieve the current official text of the Indian Stamp Act, 1899 and the stamp law of each relevant State, the IT Act, 2000 and its First Schedule, the Registration Act, 1908 and any State amendment, and the e-stamping procedure of each State. Record the version and date. Open `references/india-state-statutes.md` as a starting point for State laws.
2. **Authority.** Check who signs for each party: board resolution or power of attorney for companies, partner authority for firms and LLPs, and authorisation for government bodies. Flag related-party or shareholder approval needs.
3. **E-signature.** Confirm the method is an electronic signature recognised under the IT Act. Check that the document is not of a class excluded by the First Schedule (for example certain powers of attorney, trusts, wills and contracts for sale or conveyance of immovable property); confirm the current list.
4. **Stamping.** Decide where and when duty is payable: before or at execution, in the State of execution, and possibly again on receipt in another State. Check e-stamp availability and whether franking or adhesive stamps are allowed. Hand off computation to `state-stamp-duty-calculator`.
5. **Under-stamping effect.** Explain inadmissibility and impounding, and that the defect is believed to be curable by paying duty and penalty. For arbitration clauses, note the December 2023 seven-judge Constitution Bench decision; confirm current treatment. Do not advise signing unstamped to save duty.
6. **Registration.** Check whether registration is compulsory (for example certain leases and transfers of immovable property) or optional, the time limit, and the effect of non-registration. Confirm periods from the Act.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
7. **Attestation and notarisation.** Note where witnesses or notarisation are required or useful.
8. **Counterparts and dating.** Ensure each counterpart is stamped where needed and the execution date is consistent with the stamp date.

## Output

1. A signing checklist: step · who · document · law · status.
2. A State-wise stamp and registration table, with duty left to the calculator.
3. Red flags (excluded e-sign documents, missing authority, stamping after execution).

## Guardrails and hand-offs

- Never state a duty amount or rate from memory.
- Never suggest backdating, splitting documents or choosing a State only to evade duty.
- Registration, notarisation and stamping are done by the parties and professionals, not the AI.
