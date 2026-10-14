---
name: termination-retrenchment-analyst
description: Reviews a proposed termination, layoff, retrenchment or closure under the Industrial Relations Code 2020 and State law for risk, covering worker status, notice and retrenchment compensation, prior-permission thresholds, last-in-first-out, misconduct dismissals, executive exits and separation agreements with releases. Use when a client wants to let people go, run a reduction in force, close a unit or settle an executive exit. Do not use for running a misconduct inquiry; use disciplinary-inquiry-drafter instead.
---

# Termination Retrenchment Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Identify the lawful route for an exit, the process and payments it requires, and the risk of challenge, and prepare the documents.

## Jurisdiction gate

Confirm the employees work in India and record the State or UT of each establishment. Note the appropriate government for the establishment. State amendments and rules on layoff, retrenchment and closure may differ.

## Temporal gate

The IR Code is reported to be in force from 21 November 2025, replacing the Industrial Disputes Act. Apply the IR Code to terminations effected on or after commencement. If notice was given, or the exit started, before that date, map which law applies and check the savings provisions.

## Required inputs

Mark as **blocking**:
- the number of people affected, their roles, wages and dates of joining;
- the establishment's type and total headcount for the preceding twelve months;
- the reason (misconduct, performance, redundancy, closure, end of fixed term);
- the employment contracts, standing orders and any settlement with a union.

Also useful: seniority lists, prior layoffs, any pending disputes, and the business case for redundancy.

## Method

1. Retrieve the current official text of the IR Code chapters on layoff, retrenchment and closure, the central and State rules, and the State Shops and Establishments law. Record the version and date.
2. Classify each person as worker or non-worker under the IR Code, using actual duties and wage level, not job title.
3. For workers, check retrenchment conditions: notice or pay in lieu, retrenchment compensation, notice to the appropriate government, the reskilling fund contribution, and last-in-first-out unless reasons are recorded. Confirm every number.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
4. Check whether the establishment crosses the prior-permission threshold for layoff, retrenchment or closure under the IR Code (reported as raised to 300; confirm, including any State change).
5. For misconduct, check that the standing orders and a fair domestic inquiry support dismissal. Hand off to `disciplinary-inquiry-drafter` if no inquiry has been held.
6. For non-workers and executives, apply the contract, State Shops and Establishments notice rules and any severance policy.
7. Screen for discriminatory or retaliatory dismissal (pregnancy or maternity, disability, POSH complainants, whistleblowers, union activity, protected workers) and flag it at the top.
8. Draft separation or settlement agreements: dues paid, release of claims, confidentiality, non-disparagement, return of property, and a carve-out for non-waivable statutory rights.

## Output

1. An exit plan per group: route · process · notices · payments · timeline · risk.
2. Draft termination letters, notices to the government where required, and separation agreements.
3. A risk note, including likely Labour Court exposure (reinstatement, back wages).

## Guardrails and hand-offs

- Never describe a release as waiving statutory dues that cannot lawfully be waived.
- Never advise disguising retrenchment as resignation or performance exit.
- Hand off dues computation to `employee-dues-calculator`.
- If a dispute is raised, hand off to `labour-dispute-claim-drafter`.
