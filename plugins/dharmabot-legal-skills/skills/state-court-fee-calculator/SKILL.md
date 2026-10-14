---
name: state-court-fee-calculator
description: Values a suit, appeal, petition or application and computes the court fee payable before civil courts, High Courts and other fora in any Indian State or Union Territory, under that State's court-fees and suits-valuation law, showing the valuation provision, Schedule article and arithmetic. Use when an advocate asks "what court fee for this suit", needs a valuation paragraph for a plaint, or wants to check a fee before filing anywhere in India. Do not use for stamp duty on instruments; use state-stamp-duty-calculator.
---

# State Court Fee Calculator

Every output is a draft for an advocate enrolled in India to check before filing.

## Purpose

Work out how the proceeding must be valued, both for court fee and for pecuniary jurisdiction, and how much court fee is payable. Make every step traceable to the State's statute.

## Jurisdiction gate

Confirm the proceeding will be filed in India and identify the State or Union Territory and the forum (civil judge or munsiff, senior civil judge, district court, family court, rent court, commercial court, High Court, tribunal). Court fees are State law, and each State uses either its own Act or the Court-fees Act, 1870 as it amended it. If a special statute fixes its own fee (for example many tribunals and consumer commissions), retrieve that instead.

## Required inputs

Mark as **blocking**:
- the State or UT and the forum;
- the kind of proceeding and the relief claimed, word for word;
- the amounts or market value relied on (claim amount, property value, mesne profits, rent).

Also useful: the property description and location; whether the plaintiff is in possession; related reliefs (declaration with injunction, partition, possession); and any earlier valuation in the same matter.

## Method

1. Open `references/india-state-statutes.md` to find the likely statute for the State. Treat it as a starting point only.
2. Retrieve the current official text of that statute, its Schedules, and every amendment or rate notification (India Code, the State gazette, the State law department or the High Court website). Record the version and date. Never use remembered rates or slabs.
3. If the State applies the Court-fees Act, 1870 as amended, apply the State's amendment and Schedules, not the original central text. Identify the separate suits-valuation law if the State has one.
4. For each relief, find the valuation provision and decide whether the fee is ad valorem or fixed. Note where the Act links the value for court fee to the value for jurisdiction.
5. Find the value the provision requires (for example a claim amount, a multiple of rent, or a proportion of market value). Ask for facts not supplied; do not assume them.
6. Apply the Schedule rate to each relief and show the arithmetic step by step, including any rounding the Act prescribes.
7. Total the fee and state the jurisdictional value. If asked, state the court competent to try the suit under the State's civil courts law.
8. Draft the valuation paragraph for the plaint or memorandum.
9. Flag points open to objection, such as undervaluing a declaration with consequential relief, or a partition where possession is disputed.

## Output

1. A table: relief · valuation provision · value · Schedule article · rate · fee.
2. The total, with the arithmetic shown.
3. A draft valuation paragraph.
4. Risks and open questions.
5. The statute version used and its date. Note any place where `references/india-state-statutes.md` differed from the official text.

## Guardrails

- If the rate table could not be retrieved, give the structure of the calculation, leave the rate blank and mark the result `[unverified]`.
- Never round in the client's favour beyond what the Act allows.
- Where valuation is legally disputed, set out the competing views for the advocate; do not decide the dispute.
