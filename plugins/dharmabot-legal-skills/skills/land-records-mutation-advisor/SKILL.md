---
name: land-records-mutation-advisor
description: Advises on State land revenue procedures across Indian States and UTs, covering mutation after sale, inheritance or partition, record names such as khata, patta, 7/12, jamabandi and khatauni, correction of entries, land-use conversion, agricultural land purchase restrictions and ceiling laws, and appeals in the revenue hierarchy. Use when a lawyer asks how to mutate inherited land, correct a wrong name in the RTC, convert farmland to non-agricultural use, or appeal a Tahsildar's mutation order. Do not use for a full chain-of-title opinion; use property-title-diligence-analyst.
---

# Land Records and Mutation Advisor

Every output is a draft advice note for an advocate enrolled in India to check.

## Purpose

Explain which revenue record must change, who decides, what to file, and how to challenge a refusal, in the specific State.

## Jurisdiction gate

Record the State or UT, district, taluk or tehsil and village or urban local body. Revenue law is State law, and procedures, officers, forms and record names differ widely. Urban property may be recorded by the municipality (property tax or khata) rather than the revenue department. If the State cannot be identified, stop.

## Required inputs

Mark as **blocking**:
- the State and location, and whether the land is agricultural, urban or converted;
- the event to be recorded (sale, gift, inheritance, partition, decree, acquisition) and its document;
- the current record extract (for example RTC/pahani, 7/12 and 8A, patta-chitta, jamabandi, khatauni, thandaper);
- for inheritance, the date of death, personal law and the list of heirs.

Also useful: earlier mutation orders, survey sketches, conversion orders, and any objection or pending case.

## Method

1. Retrieve the current official text of the State land revenue code or Act, the mutation and record-of-rights rules, any land-use conversion law, and the State's land-reform, ceiling and agricultural land purchase restrictions. Open `references/india-state-statutes.md` as a starting point and confirm on the State revenue department's official portal. Record the version and date.
2. Identify the record and the officer: village officer, revenue inspector, Tahsildar or Mamlatdar, and the online mutation system if the State has one.
3. Mutation: list the documents (registered deed, death certificate, legal heir or family membership certificate, succession certificate where needed, affidavits, no-objections from other heirs), notice to interested persons, objection period and order. Hand off share computation to `intestate-succession-share-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
4. Correction of entries: clerical correction versus disputed entries; the forum and evidence each needs.
5. Conversion and land use: the competent authority, master-plan or zoning compatibility, conversion charges, and conditions. Check whether the State has replaced prior permission with deemed or online conversion.
6. Purchase restrictions: who may buy agricultural land in this State (some limit purchase to agriculturists or residents, or set income or area caps), ceiling limits, assigned or granted land bars, and Scheduled Area or tribal land transfer bans.
7. Remedies: appeal and revision hierarchy (Sub-Divisional Officer, Collector, Revenue Tribunal or Board of Revenue, as the State provides) and limitation; hand off dates to `limitation-calculator`.
8. Remind the client that revenue entries are for fiscal purposes and do not confer title; title disputes go to the civil court.

## Output

1. Advice note: applicable law, officer, steps, documents, fees to confirm, timeline, remedies.
2. Document checklist and draft application or objection, if asked.
3. Points to check live on the State portal.

## Guardrails

- Never state conversion charges, ceiling limits or eligibility rules from memory.
- Never suggest a benami purchase or a route around agricultural purchase bans.
- Hand off title questions to `property-title-diligence-analyst`.
