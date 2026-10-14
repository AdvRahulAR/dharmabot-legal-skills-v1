---
name: employee-dues-calculator
description: Computes Indian terminal dues with the arithmetic shown, covering gratuity under the Code on Social Security 2020 (including fixed-term employees), retrenchment compensation under the Industrial Relations Code, notice pay, leave encashment, bonus and the full-and-final settlement, with income-tax exemption limits flagged. Use when someone asks to compute gratuity, leave encashment, notice pay or full and final dues for an exiting employee. Do not use for deciding whether an exit is lawful; use termination-retrenchment-analyst instead.
---

# Employee Dues Calculator

Every output is a draft computation for an advocate or payroll professional in India to review.

## Purpose

Produce a transparent full-and-final computation, with each formula, wage definition and assumption stated, so it can be checked line by line.

## Jurisdiction gate

Confirm the employee worked in India and the State of the establishment (for leave encashment, Shops and Establishments rules and any State gratuity practice). Note if the employer is a government or PSU body with its own gratuity rules.

## Temporal gate

The Code on Social Security and the IR Code are reported to be in force from 21 November 2025. For exits on or after that date, apply the Codes and their wage definition. For exits before it, apply the Payment of Gratuity Act, the Industrial Disputes Act and other repealed laws. For service spanning both, record the method used and flag it.

## Required inputs

Mark as **blocking**:
- dates of joining and exit, and the mode of exit (resignation, retrenchment, termination, retirement, death or disablement, end of fixed term);
- the last drawn pay, broken into each component;
- employment type (permanent or fixed-term) and worker status;
- leave balance and the leave policy;
- notice given or served.

Also useful: whether the employer is covered by gratuity insurance or a trust, any recoveries, bonus eligibility, and any more generous company scheme.

## Method

1. Retrieve the current official text of the gratuity, retrenchment, wage-definition and bonus provisions of the Codes, and the current Income-tax Act exemption provisions and notified limits. Record the version and date. Confirm whether the Income-tax Act, 2025 now governs the exit year.
2. Compute "wages" under the Code definition: list included components, excluded components, and the add-back if exclusions exceed the reported 50 percent ceiling.
3. **Gratuity:** check eligibility (continuous service rules, and the shorter period reported for fixed-term employees). Apply the statutory formula, show the rounding rule for part years, and apply the statutory ceiling. Confirm each figure from the text.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. **Retrenchment compensation and reskilling fund:** only for retrenchment of a worker. Show days per completed year and the basis.
5. **Notice pay:** under the contract or the law, whichever governs; show the per-day rate basis.
6. **Leave encashment:** under the State law or policy, with the per-day divisor used.
7. **Bonus:** pro rata eligibility and computation where covered.
8. Add pending salary and reimbursements; subtract lawful recoveries only.
9. Flag the tax treatment of each item, citing the exemption provision to be confirmed, and flag where the company scheme is more generous than the statute.

## Output

1. A computation table: item · formula · inputs · amount · source.
2. Assumptions and open points.
3. A short note on tax treatment and timelines for payment.

## Guardrails and hand-offs

- Never state a ceiling, divisor or exemption limit from memory; mark each "confirm from the official text".
- Never invent pay components or dates.
- Do not net off disputed recoveries without flagging them.
- For questions on the lawfulness of the exit, hand off to `termination-retrenchment-analyst`.
