---
name: state-stamp-duty-calculator
description: Classifies an instrument (sale, gift, settlement, release, partition, lease, mortgage, agreement, power of attorney, affidavit, share transfer and others) and computes the stamp duty and registration fee payable in any Indian State or Union Territory, under that State's stamp law or the Indian Stamp Act, 1899 as it applies there. Shows the Schedule article, the value used and the arithmetic. Use when someone asks "how much stamp duty for this deed" or must check stamping before execution or registration, including documents executed abroad. Do not use for court fees; use state-court-fee-calculator.
---

# State Stamp Duty Calculator

Every output is a draft for an advocate enrolled in India to check before execution or registration.

## Purpose

Identify the correct Schedule article for an instrument, the value on which duty is charged, and the stamp duty and registration fee payable in the right State.

## Jurisdiction gate

Identify which State's stamp law applies: where the instrument is executed, where the property is, and whether the instrument is brought into another State or into India from abroad. If more than one State is involved, consider whether duty is payable in each, and whether any credit for duty already paid is available. Some instruments carry uniform rates set by the central government under the Indian Stamp Act, 1899 (for example certain securities instruments); check this before applying a State rate.

## Required inputs

Mark as **blocking**:
- the instrument, or a full description of its operative terms;
- the parties and their relationship (some States give concessions within a family, or to women purchasers);
- the property description, extent and location;
- the consideration or market value stated;
- the place and date of execution.

Also useful: the guideline, ready-reckoner or fair value notified for the property, and whether the document will be registered.

## Method

1. Open `references/india-state-statutes.md` for the likely stamp statute in that State. Treat it as a starting point only.
2. Retrieve the current official text of the stamp statute and its Schedule, every rate notification, the State's valuation rules (guideline value, ready reckoner or fair value), and the current registration fee table. Record versions and dates. Never use remembered rates.
3. Classify the instrument by its operative words, not its title. If it covers several distinct matters, consider whether each attracts separate duty.
4. Determine the chargeable value: the higher of consideration and market or guideline value where the statute requires it, otherwise as the article specifies.
5. Apply the rate and show the arithmetic. Apply a concession only if every condition is met, and say which fact meets each condition.
6. Compute the registration fee and any surcharge, cess or metro levy the State charges.
7. For an instrument executed outside the State or outside India, retrieve the time limit for stamping after it is received in the State, and any authentication needed before registration. Hand off foreign execution formalities to `document-legalisation-planner`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
8. State the consequences of under-stamping (impounding, penalty) in general terms, citing the provisions retrieved.

## Output

1. Classification: the article, with one sentence on why.
2. A table: item · value used · rate · amount (stamp duty, registration fee, other charges).
3. The total payable, with arithmetic.
4. Open questions and risks.
5. Sources and dates.

## Guardrails

- If a rate could not be retrieved, leave it blank and mark the result `[unverified]`.
- Never suggest structuring a transaction to evade duty.
- Describe payment and e-stamping steps only from current official sources.
