---
name: labour-codes-compliance-checker
description: Maps an establishment's obligations under the Code on Wages 2019, Industrial Relations Code 2020, Code on Social Security 2020 and OSH Code 2020, plus EPF, ESI, contract labour, standing orders, registers and returns, and State Shops and Establishments and factory licensing, with transition issues from the repealed laws. Use when a client asks what labour compliances apply to a factory, office or warehouse in a given State. Do not use for a single employee's exit dues; use employee-dues-calculator instead.
---

# Labour Codes Compliance Checker

Every output is a draft compliance map for an advocate enrolled in India to review.

## Purpose

Give the client a site-by-site list of labour registrations, contributions, registers, returns and inspections that apply, with the State rules that must be checked live.

## Jurisdiction gate

Identify each site by State or UT and district, and its type (factory, shop or commercial establishment, construction, plantation, mine, IT or ITES unit). Labour is a concurrent subject. State rules, exemptions and Shops and Establishments laws differ widely.

## Temporal gate

The four Codes are reported to have come into force on 21 November 2025, repealing 29 central labour laws. Central rules and State rules have been notified in stages through 2026, and some States lag. For each Code and State, record: the commencement notification, whether final State rules exist, and whether old rules continue under the transition provisions. For facts before commencement (unpaid dues, pending disputes, past inspections), apply the repealed law and the savings clauses.

## Required inputs

Mark as **blocking**:
- each site's State, type of establishment and activity;
- headcount at each site, split into employees, workers, contract labour, fixed-term, apprentices and gig or platform engagement;
- wage levels of the workforce (for coverage thresholds).

Also useful: existing registrations and licences, PF and ESI codes, standing orders, contractor list, and past inspection notices.

## Method

1. Retrieve the current official text of the four Codes, the central rules, each State's rules, and the commencement and transition notifications from eGazette and the Ministry of Labour and Employment. Record the version and date of each. Open `references/india-state-statutes.md` as a starting point for State laws.
2. Apply each Code's coverage thresholds to each site, confirming every number from the text.
3. **Code on Wages:** wage definition and the exclusions ceiling (reported as 50 percent; confirm), minimum and floor wages, timely payment, deductions, bonus, equal remuneration, registers.
4. **IR Code:** standing orders threshold, grievance redressal committee, works committee, trade union recognition, notice of change, layoff and retrenchment rules.
5. **Code on Social Security:** EPF and ESI coverage and contributions, gratuity (including fixed-term staff), maternity benefit, employees' compensation, building workers' cess, and aggregator contributions for gig and platform workers.
6. **OSH Code:** registration, factory licensing, contract labour licensing for contractors and principal employers, working hours, women's night work, safety committees, welfare facilities.
7. Add State laws: Shops and Establishments registration, labour welfare fund, professional tax, holidays and any State gig-worker law.
8. Flag transition issues: old registrations, licences and standing orders and how long they remain valid, and pending proceedings under repealed laws.

## Output

1. A site-by-site obligations table: obligation · source · threshold · status · action · frequency.
2. A list of State rules to check live, with the date last checked.
3. Transition issues and red flags.

## Guardrails and hand-offs

- Never state a threshold, contribution rate or due date as settled; mark each "confirm from the official text".
- Do not advise on splitting establishments to avoid thresholds.
- For a calendar of filings, hand off to `compliance-calendar-builder`.
- For worker classification questions, hand off to `gig-worker-classification-analyst`.
- For dues on exit, hand off to `employee-dues-calculator`.
