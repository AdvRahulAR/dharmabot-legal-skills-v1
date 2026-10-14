---
name: foreigners-registration-compliance-checker
description: Checks foreign nationals' compliance in India under the Immigration and Foreigners Act 2025 and the rules and orders under it, covering visa categories and conversions, employment visa conditions, e-FRRO registration, reporting duties of employers, hotels, hospitals and institutions, overstay penalties, exit permits and protected-area permits. Use when an expatriate's visa is expiring, a foreign employee missed FRRO registration, or an employer asks about its reporting duties. Do not use for structuring the employer's India entity; use india-entry-fema-structuring-analyst.
---

# Foreigners Registration Compliance Checker

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Find the foreign national's and the host's compliance gaps and set out the fastest lawful way to regularise them.

## Jurisdiction gate

Confirm the foreign national is in India or about to enter. Identify the nationality (some nationalities have special rules), the State and city of stay, and the FRRO or FRO with jurisdiction. Note any restricted or protected area involved.

## Temporal gate

The Immigration and Foreigners Act 2025 replaced the Foreigners Act 1946, the Registration of Foreigners Act 1939, the Passport (Entry into India) Act 1920 and the Immigration (Carriers' Liability) Act 2000. It and its Rules and Order are believed to have come into force on 1 September 2025; confirm. For acts or stays that began earlier, check the transition and savings provisions. Visa manual provisions change often.

## Required inputs

Mark as **blocking**:
- nationality, visa type, visa validity and entry date;
- the purpose of stay and the current activity (employment, business, study, medical, family);
- registration status on e-FRRO, and any overstay.

Also useful: employment contract, salary, the sponsoring entity, address proofs, earlier extensions or conversions, and any notice from the FRRO.

## Method

1. Retrieve the current official text of the Immigration and Foreigners Act 2025, its Rules and Order, any exemption orders, and the MHA visa manual and e-FRRO guidance. Record versions and dates.
2. Check the visa matches the activity. An employment visa usually needs a specific employer and salary conditions; business visas do not allow employment. Check whether conversion is allowed in India or needs exit.
3. Check registration: whether registration was required for this visa and stay, the deadline, and the method.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. Check host reporting: duties on employers, hotels and other accommodation providers, hospitals and educational institutions to report foreigners, with forms and timelines.
5. Overstay or default: the penalty or fee, regularisation procedure, and risk of exit permit refusal, blacklisting or prosecution. Do not state amounts; retrieve them.
6. Exit: exit permit requirements and timing before departure.
7. Labour and tax touchpoints: the employer's payroll, social security for international workers, and tax withholding. Refer to the right skill.
8. Search for and read current authority and MHA orders on disputed points. Tag anything not read in full `[verify]`.

## Output

1. A status table: requirement · source · status · deadline · action.
2. A regularisation plan with documents.
3. A host-entity compliance checklist.

## Guardrails and hand-offs

- Never advise working on the wrong visa or delaying disclosure of an overstay.
- Never state penalty amounts or processing times as fixed.
- For the employer's labour obligations, hand off to `labour-codes-compliance-checker`.
- For entity and FEMA questions, hand off to `india-entry-fema-structuring-analyst`.
