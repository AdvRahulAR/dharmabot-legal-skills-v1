---
name: pre-institution-mediation-advisor
description: Advises whether pre-institution mediation under section 12A of the Commercial Courts Act, 2015 is mandatory before a commercial suit, tests whether urgent interim relief is genuinely contemplated, and prepares the application to the Legal Services Authority under the Pre-Institution Mediation and Settlement Rules, with notes on the Mediation Act, 2023. Use when a lawyer asks whether mediation is needed before filing a commercial suit, or how to start pre-institution mediation. Do not use for filing scrutiny of the plaint; use commercial-suit-filing-checker instead.
---

# Pre Institution Mediation Advisor

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Decide whether a commercial suit can be filed now or must go through pre-institution mediation first, and start that mediation correctly.

## Jurisdiction gate

Confirm the dispute is a "commercial dispute" of at least the "specified value" under the Commercial Courts Act, 2015. Identify the State and district, because the court, the Legal Services Authority and any State rules depend on it. If the claim is below the specified value or not commercial, say the Act does not apply and stop.

## Temporal gate

The Mediation Act, 2023 was notified in phases. Check which provisions are in force on the date of the advice, from when, and whether they amend section 12A or the PIMS Rules. Record the date checked.

## Required inputs

Mark as **blocking**:
- the nature of the dispute and the contract;
- the claim value with its computation;
- the place where the suit would be filed;
- whether urgent interim relief is needed, and the facts showing urgency.

Also useful: correspondence, limitation dates, and any contractual mediation or arbitration clause.

## Method

1. Retrieve the current official text of the Commercial Courts Act, 2015 (section 12A and the specified-value provision), the Commercial Courts (Pre-Institution Mediation and Settlement) Rules, 2018 as amended, the Mediation Act, 2023 with its commencement notifications, and the Limitation Act, 1963. Record the version and date. Confirm every section, rule and article number used in this skill against that official text before relying on it.
2. Check for an arbitration clause first. If one exists, the suit may be the wrong route; flag it.
3. **Mandatory or not.** For example, Patil Automation (Supreme Court, 2022) treated section 12A as mandatory; confirm current treatment, its prospective effect and later authority.
4. **Urgent relief test.** Courts look at whether the plaint genuinely contemplates urgent interim relief, judged from the plaintiff's standpoint, and reject attempts to dress up a money claim. Search for and read current authority. List the facts that do and do not support urgency. Do not invent urgency.
5. **Application.** Draft the application to the District Legal Services Authority (or High Court Legal Services Committee where the High Court has original commercial jurisdiction) in the form required by the Rules: parties, addresses, nature of dispute, claim, and relief sought.
6. **Timeline.** Record the believed period for completing the mediation and any extension by consent; confirm from the Rules. Note that the time spent is believed to be excluded from limitation; confirm and hand off computation to `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
7. **Outcomes.** If settled, the settlement is reduced to writing and signed; hand off to `mediated-settlement-agreement-drafter`. If not, obtain the failure report, which must be filed with the plaint.

## Output

1. An advice note: mandatory or exempt, with reasons and risk of rejection of the plaint.
2. The draft PIMS application and a covering letter.
3. A timeline with the mediation window and limitation position.
4. A preparation list for the mediation session.

## Guardrails and hand-offs

- Never advise skipping mediation by pleading urgency that does not exist.
- Never invent authority; tag unread authority `[verify]` and run `citation-verifier`.
- Mediation preparation goes to `mediation-brief-drafter`; plaint scrutiny goes to `commercial-suit-filing-checker`.
