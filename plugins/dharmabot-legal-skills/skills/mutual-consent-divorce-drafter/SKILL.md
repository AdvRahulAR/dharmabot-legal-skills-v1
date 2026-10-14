---
name: mutual-consent-divorce-drafter
description: Drafts first and second motion petitions for divorce by mutual consent under the Hindu Marriage Act, 1955, Special Marriage Act, 1954 or Divorce Act, 1869, the settlement agreement on permanent alimony, stridhan, property, custody and withdrawal of other cases, and an application to waive the cooling-off period. Use when a lawyer asks for a mutual divorce petition, settlement terms between spouses, or a waiver of the six-month period. Do not use for a contested divorce; use matrimonial-petition-drafter.
---

# Mutual Consent Divorce Drafter

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Produce a joint petition and a settlement that will survive the second motion and later enforcement, without trading away a child's rights.

## Jurisdiction gate

Confirm the governing Act: the mutual consent provisions are believed to be section 13B of the Hindu Marriage Act, section 28 of the Special Marriage Act and section 10A of the Divorce Act; confirm from the official text. Check whether a State uniform civil code applies instead (Uttarakhand in force; Gujarat's code reportedly received the President's assent in September 2026 and comes into force on a date the State notifies; Assam's bill was reportedly passed by the Assembly in May 2026, with assent not confirmed; check assent, commencement and coverage, including any Scheduled Tribe exclusion [verify]). Identify the venue and the Family Court. If a spouse is abroad, check video appearance practice and hand off to `nri-matrimonial-dispute-analyst` if a foreign case exists.

## Required inputs

Mark as **blocking**:
- governing Act, marriage date and place, and the date of separation (the Acts require a minimum period of living separately; confirm);
- both parties' agreement on alimony, stridhan, property, custody and pending cases;
- children's ages and the agreed parenting arrangement;
- list of all pending cases between the parties and their courts.

## Method

1. Retrieve the current official text of the governing Act and State Family Court rules. Record the version and date.
2. First motion petition: marriage, separation, inability to live together, free consent, no collusion, settlement terms, and prayer.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Settlement agreement:
   - permanent alimony: amount, instalments tied to the first and second motions, mode of payment, and full and final wording;
   - stridhan and gifts: list and return;
   - property: transfers, with a note that immovable property transfers need separate stamped and registered deeds (hand off to `state-stamp-duty-calculator`);
   - custody and access: refer to `child-custody-planner`; child maintenance cannot be waived by a parent;
   - withdrawal or quashing of other cases, with timing linked to payments;
   - undertaking not to file further cases and default clauses.
4. Waiver application: the cooling-off period may be waived by the court in suitable cases (Amardeep Singh v. Harveen Kaur, Supreme Court, 2017; confirm current treatment). Plead the factors: separation period, failed mediation, settled issues, and hardship of waiting.
5. Second motion petition and joint affidavits confirming consent.
6. Note stamping of the settlement under the State stamp law.

## Output

1. First motion petition, settlement agreement, waiver application and second motion petition.
2. Payment and withdrawal schedule linked to each stage.
3. Checklist for each hearing.

## Guardrails

- Flag and refuse terms that waive a child's maintenance, bar a parent's contact without welfare reasons, or require withdrawal of a criminal case not compoundable without court leave.
- Either party may withdraw consent before the decree; tell the client.
- Never state that the court will waive the period.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
