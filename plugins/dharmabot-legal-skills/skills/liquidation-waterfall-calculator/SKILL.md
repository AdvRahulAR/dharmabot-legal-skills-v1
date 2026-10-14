---
name: liquidation-waterfall-calculator
description: Computes the distribution of liquidation proceeds under the priority order in the Insolvency and Bankruptcy Code, 2016, with arithmetic shown, covering costs, secured creditors who relinquish security, workmen and employees, unsecured financial creditors, government dues, secured shortfall and the rest, and lays out steps for compulsory and voluntary liquidation. Use when a liquidator, creditor or advocate asks how much each class gets, or how to run a liquidation. Do not use for checking a resolution plan's payouts; use resolution-plan-reviewer.
---

# Liquidation Waterfall Calculator

Every output is a draft computation for an insolvency professional or advocate in India to check.

## Purpose

Apply the statutory priority order to the actual proceeds and admitted claims, show every line of arithmetic, and flag priority points that are disputed.

## Jurisdiction gate

Confirm the liquidation is under the IBC before an NCLT in India, and whether it is compulsory or voluntary. Note any proceeds from assets outside India and mark foreign-law points for counsel qualified there.

## Temporal gate

Record the liquidation commencement date. The IBC (Amendment) Act, 2026 (provisions reported in force from 26 May 2026) is reported to change liquidation supervision and timelines. Confirm whether it alters the priority order or process for this liquidation.

## Required inputs

Mark as **blocking**:
- the amount available for distribution and its source;
- the list of admitted claims by class, with amounts;
- for each secured creditor, whether it relinquished security or realised it outside liquidation, and the realisation amount;
- insolvency resolution process costs and liquidation costs, with supporting figures.

Also useful: the liquidation commencement date, the workmen's dues period, pari passu and intercreditor agreements, and any NCLT orders on priority.

## Method

1. Retrieve the current official text of the IBC priority provision (believed to be section 53; confirm), the related provision on secured creditors who realise security, the Liquidation Regulations and the Voluntary Liquidation Regulations. Record versions and dates. Do not rely on a remembered order of priority.
2. List each tier in the statutory order, with the claims falling in it and the period limits that apply to workmen and employee dues.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Deduct costs first. Then distribute tier by tier. Within a tier, pay pro rata if funds are short. Show each step in a table.
4. For a secured creditor realising outside liquidation, apply the rules on paying the liquidator its share of costs and workmen's dues, and place any shortfall in its correct tier.
5. Flag disputed priority points, for example the ranking of government dues secured by statute, and the effect of intercreditor agreements. Search for and read current Supreme Court authority; tag unread authority `[verify]`.
6. Run a check: the total distributed plus balance equals the amount available.
7. For process steps, list the documents and filings: public announcement, claims, stakeholders' consultation, asset memorandum, sale, distribution, final report and dissolution application. Separate compulsory from voluntary liquidation steps.

## Output

1. A waterfall table: tier, claimant, admitted claim, amount paid, percentage recovered, balance.
2. A list of assumptions and disputed points.
3. A process checklist for the liquidation.

## Guardrails and hand-offs

- Never invent claim amounts or cost figures; ask for them.
- State that the computation changes if any NCLT order alters priority.
- Plan payouts go to `resolution-plan-reviewer`; claim verification to `insolvency-claim-drafter`.
- Run `citation-verifier` before delivery.
