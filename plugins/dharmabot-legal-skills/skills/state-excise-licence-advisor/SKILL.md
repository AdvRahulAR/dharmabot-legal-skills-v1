---
name: state-excise-licence-advisor
description: Advises on State excise regimes for potable alcohol, such as the Kerala Abkari Act, the Karnataka Excise Act, 1965 and the Maharashtra Prohibition Act, 1949, covering licence categories, distance and zoning rules, prohibition States, renewals, transfers, fees, and replies to suspension or cancellation notices. Use when a client wants a bar, hotel, retail or wholesale liquor licence, a renewal or transfer, or has an excise suspension notice. Do not use for non-excise licences (use licence-application-drafter) or criminal excise prosecutions.
---

# State Excise Licence Advisor

Every output is a draft advice note for an advocate enrolled in India to check.

## Purpose

Tell the client which licence fits, whether the premises qualify, what it costs and takes, and how to answer an enforcement notice.

## Jurisdiction gate

Identify the State or UT and the district. Excise is a State subject, and rules differ sharply. Check first whether the State or area is under prohibition (for example Gujarat, Bihar, Nagaland, Mizoram and Lakshadweep have had prohibition regimes; confirm current status). Union Territories and Puducherry have their own laws.

## Temporal gate

Most States issue an annual or multi-year excise policy and fee schedule. Record the excise year in issue and confirm the policy, fee notification and any court stay in force on the relevant date.

## Required inputs

Mark as **blocking**: State and district; the activity (bar, hotel bar, club, retail shop, wholesale, brewery or microbrewery, event licence); the premises address and its distances to schools, places of worship and highways as the State rules measure them; and, for enforcement matters, the notice with its date.

Also useful: the hotel's star classification, building and fire approvals, trade licence, FSSAI licence, ownership or lease, and any earlier licences or violations.

## Method

1. Open `references/india-state-statutes.md` as a starting point, then retrieve the current official text of the State excise Act, rules, the excise policy and fee notifications from the State excise department website and State Gazette. Record versions and dates.
2. Map the licence category from the State's own list (names like FL-3, CL-7 or Form numbers differ by State). Confirm the category name from the rules.
3. Test eligibility: applicant type, hotel classification, minimum area and seating, distance rules, zoning, highway restrictions, and local body consent.
4. List approvals needed before and after the licence: fire, building, trade, FSSAI, police or district collector reports.
5. Set out fees, security deposit and duty structure from the current notification. Label any estimate.
6. Renewals and transfers: deadlines, transfer fees, change of partners or directors, and change of premises.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
7. **Suspension or cancellation notice.** Identify the alleged breach and rule, the reply deadline (use `limitation-calculator`), the hearing right, and the appeal or revision authority. Outline the reply grounds.
8. Search for and read current High Court authority on the State's rules; tag anything unread `[verify]`.

## Output

1. Advice note: recommended licence, eligibility findings, approvals, costs, timeline.
2. Document checklist for the application.
3. For notices: an issues table and a reply outline, with the appeal route.

## Guardrails and hand-offs

- Never state a fee, distance or duty figure from memory.
- Never advise ways to evade prohibition, duty or distance rules.
- Do not handle criminal excise prosecutions; recommend criminal counsel.
- For the reply, hand off to `regulator-notice-reply-drafter`; for an appeal, `regulatory-appeal-planner`; for the application form, `licence-application-drafter`.
- Run `citation-verifier` before delivery.
