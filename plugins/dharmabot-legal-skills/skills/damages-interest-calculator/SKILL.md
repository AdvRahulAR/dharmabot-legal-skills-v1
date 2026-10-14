---
name: damages-interest-calculator
description: Quantifies civil claims head by head with the arithmetic shown, covering damages and liquidated damages under the Indian Contract Act, contractual interest, interest under section 34 of the Code of Civil Procedure and the Interest Act, 1978, compound interest under the MSMED Act, mesne profits and compensation for loss of use. Use when an advocate asks to compute damages, interest, pre-suit and pendente lite interest, mesne profits or the claim amount for a plaint. Do not use for limitation periods; use limitation-calculator instead.
---

# Damages Interest Calculator

Every output is a draft computation for an advocate enrolled in India to check.

## Purpose

Produce a transparent claim computation that a court or tribunal can follow line by line, with the legal basis and evidence for each head.

## Jurisdiction gate

Confirm Indian law governs the claim and note the forum (civil court, commercial court, arbitral tribunal, MSME Council, consumer commission). The forum affects which interest powers apply. If a foreign law governs the contract, stop and hand off to `foreign-matter-scoping-analyst`.

## Required inputs

Mark as **blocking**:
- the contract terms on price, interest, liquidated damages and payment dates;
- the invoices or loss documents, with amounts and due dates;
- payments received and their dates and appropriation;
- the date up to which the computation is to run.

Also useful: market rate evidence, rental values for mesne profits, and mitigation steps taken.

## Method

1. Retrieve the current official text of the Indian Contract Act provisions on compensation for breach and on stipulated sums, section 34 CPC, the Interest Act, 1978, the MSMED Act interest provisions and the RBI bank rate history where needed. Record the version and date.
2. List each head separately: principal; contractual interest; liquidated damages; general damages; consequential loss; mesne profits; costs.
3. For each head, state the legal basis and test it. Damages need a causal link, foreseeability and proof of loss; a stipulated sum is a ceiling, and actual loss or a genuine pre-estimate still matters (confirm current Supreme Court treatment). Show mitigation.
4. Interest: use the contractual rate if there is one. Otherwise state which power the forum has to award interest and that the rate is discretionary; compute alternative scenarios at rates the advocate selects, never one asserted as the legal rate. For MSMED claims, compute compound interest with monthly rests at the multiple of the bank rate the Act sets, using the bank rate for each period, after confirming both from the official text.
5. Separate pre-suit, pendente lite and future interest periods, and simple from compound.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
6. Show every calculation: amount × rate × days ÷ 365 (or the contract's convention), and running totals. Use a script or spreadsheet for long series and show the input table.
7. Apply part-payments in the order the contract or law requires, and say which rule was used.
8. List the evidence needed to prove each head.

## Output

1. A summary table: head · basis · amount · evidence.
2. A detailed working for each head, including interest schedules.
3. Assumptions and alternatives the advocate must choose between.

## Guardrails and hand-offs

- Never inflate a figure or include a head without a factual and legal basis.
- Never present a discretionary interest rate as fixed by law.
- Never invent the bank rate or any market figure; source it or ask.
- Pleading: `plaint-drafter`. Deadlines: `limitation-calculator`.
