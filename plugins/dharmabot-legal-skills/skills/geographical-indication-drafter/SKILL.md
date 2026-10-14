---
name: geographical-indication-drafter
description: Drafts geographical indication papers under the Geographical Indications of Goods (Registration and Protection) Act, 1999 and Rules, 2002, including the application and statement of case (origin link, producer body, inspection structure, map), authorised user applications, oppositions and renewals. Use when a producers' association, cooperative or State body wants to register a GI, add authorised users, oppose a GI or renew one. Do not use for infringement or passing off (use ip-infringement-analyst) or trademark oppositions (use trademark-opposition-drafter).
---

# Geographical Indication Drafter

Every output is a draft for an advocate enrolled in India or a registered GI agent to check.

## Purpose

Produce GI filings that prove the link between product and place, and that will survive examination and opposition.

## Jurisdiction gate

Confirm the goods originate in India and the filing is before the Geographical Indications Registry, Chennai. For protection abroad, mark the route "to be confirmed by counsel qualified in [jurisdiction]". Identify the State and districts that define the geographical area.

## Required inputs

Mark as **blocking**: the product and its proposed GI name; the applicant body and its legal form (association, cooperative, government body) with proof that it represents producers; the geographical area; and, for authorised users, the registered GI number and each producer's details.

Also useful: historical records, publications and archives proving reputation; production method; quality parameters and lab data; photographs; and existing trademarks using the name.

## Method

1. Retrieve the current official text of the GI Act, the GI Rules, the forms, the fee schedule and the Registry's manual and public notices from ipindia.gov.in. Record versions and dates.
2. Check the GI Journal and register: is the name already registered or applied for? If yes, switch to an authorised user application.
3. Test registrability: generic names, misleading names, and conflicts with prior trademarks.
4. **Statement of case.** Draft in sections:
   - name and description of goods;
   - geographical area with a map;
   - proof of origin and historical record;
   - method of production;
   - uniqueness and the link to the area (natural or human factors);
   - inspection body and quality control structure;
   - list of producers.
5. Prepare the consultative group documents and anticipate the examiner's questions.
6. **Authorised users.** Draft one application per producer in the prescribed form, with the producer's statement and the applicant body's consent. Make a batch tracker for large groups.
7. **Opposition.** Where needed, draft a notice of opposition or counter-statement with grounds and evidence; check the time limit with `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
8. **Renewal and labels.** Calendar renewal; advise on correct use of the GI name and logo on packaging.

## Output

1. Draft application and statement of case, with map annexure list.
2. Authorised user applications and a tracker.
3. Evidence checklist and an open-questions list.

## Guardrails and hand-offs

- Never invent historical references or lab data.
- Never state fees or deadlines from memory.
- For infringement or passing off, hand off to `ip-infringement-analyst`; for trademark conflicts, `trademark-opposition-drafter`.
- Run `citation-verifier` before delivery.
- Before anything is filed with the Registry, hand off to `pre-filing-verification-checker`.
