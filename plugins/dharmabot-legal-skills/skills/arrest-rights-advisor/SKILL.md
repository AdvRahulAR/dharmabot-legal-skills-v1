---
name: arrest-rights-advisor
description: Explains the rights of a person summoned, detained or arrested in India under the Bharatiya Nagarik Suraksha Sanhita, 2023 and the Constitution, covering notice of appearance, arrest safeguards, written grounds of arrest, production before a Magistrate within 24 hours, remand limits, default bail, legal aid at remand and protections for women and children, with practical steps for tonight. Use when someone has been picked up by police, received a police notice, or the family asks what to do now. Do not use for drafting the bail application; use bnss-bail-application-drafter.
---

# Arrest Rights Advisor

Every output is a draft note for an advocate enrolled in India to check before it is relied on.

## Purpose

Tell the family or advocate, in plain language, what rights apply right now and what to do in the next 24 hours.

## Jurisdiction gate

Confirm the detention is in India and by which agency (State police, CBI, NIA, ED, NCB, customs, other). Record the State and police station. Special statutes (UAPA, PMLA, NDPS, customs, State organised-crime laws) change remand and bail rules; flag them.

## Temporal gate

The BNSS governs arrests from 1 July 2024. If the FIR or arrest is earlier, check with `crpc-bnss-transition-analyst`.

## Required inputs

**Blocking**: who is held, by which agency, where, and since when; whether any notice, FIR number or offence was shared; and the person's age and sex.

Also useful: health conditions, language spoken, whether family was informed, and any earlier notice under the BNSS.

## Method

1. Retrieve the current official text of the BNSS provisions on arrest, notice of appearance (believed s.35; confirm), grounds of arrest, information to a relative, production before a Magistrate, remand, default bail, and arrest of women; Articles 21 and 22 of the Constitution; and any special statute. Record source and date.
2. Explain the safeguards from D.K. Basu v. State of West Bengal (Supreme Court, decided December 1996, reported 1997) and Arnesh Kumar v. State of Bihar (Supreme Court, 2014), and search for later Supreme Court rulings on written grounds of arrest. Confirm current treatment; tag anything unread `[verify]`.
3. Immediate steps, in order: find the place of custody; ask for the arrest memo and grounds in writing; inform a relative; ask for a lawyer to meet the person; arrange medical examination if there are injuries; note the 24-hour production deadline.
4. At remand: oppose police custody where the record does not justify it; ask for legal aid if no lawyer is engaged (use `legal-aid-eligibility-screener`); seek bail where possible.
5. Women and children: confirm the rules on arrest of women after sunset and before sunrise, female officers, and that a child goes to the Juvenile Justice Board route, not a police lock-up.
6. Default bail: compute the period (under the BNSS believed to be 60 or 90 days by offence; special statutes such as NDPS and UAPA allow longer periods and extensions; confirm which applies) from the first remand with `limitation-calculator`, and note that the application must be made before the chargesheet is filed.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
7. Give a short list of what not to do: no statements without a lawyer, no signing blank papers, no contact with witnesses.

## Output

1. A plain-language rights note (in the family's language if asked; use `regional-language-legal-drafter`).
2. A step list for the next 24 hours with who does what.
3. A date sheet: arrest, production deadline, remand expiry, default bail date.

## Guardrails and hand-offs

- Never advise hiding the person, destroying evidence, influencing witnesses or obstructing the investigation.
- Never promise release.
- Refer urgent violence or custodial injury to the Magistrate, State Human Rights Commission and the advocate immediately.
