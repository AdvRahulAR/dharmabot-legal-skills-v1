---
name: sebi-lodr-disclosure-checker
description: Checks event-based and periodic obligations of listed entities under the SEBI (Listing Obligations and Disclosure Requirements) Regulations 2015, covering materiality of events under Regulation 30 and its timelines, market rumour verification, board and committee composition, financial results and corporate governance reports, and drafts the exchange disclosure. Use when a listed client asks what must be disclosed to BSE or NSE and by when, or whether its board meets LODR. Do not use for insider trading or trading window questions; use insider-trading-pit-checker instead.
---

# SEBI LODR Disclosure Checker

Every output is a draft for an advocate or the company secretary and compliance officer of a listed entity to check.

## Purpose

Decide whether an event must be disclosed, by when and in what form, and draft the disclosure. Also check standing governance obligations when asked.

## Jurisdiction gate

- Confirm the entity has specified securities, debt securities or other instruments listed on a recognised Indian stock exchange. Obligations differ by what is listed (equity, NCDs, SME platform).
- If the entity is also listed abroad, note that foreign rules need counsel qualified there.

## Temporal gate

SEBI amends LODR and its master circular often. Record the event date and time, and apply the regulations and circulars in force then. Check for amendments of the last twelve months.

## Required inputs

- **Blocking:** the listing status and exchanges; the event, with the date and time the company became aware of it, and the time the board decided (if a board decision).
- **Blocking for materiality:** the company's board-approved materiality policy and the figures needed for the quantitative test (for example turnover, net worth, profit after tax, as the current text requires).
- Useful: the board meeting outcome, contracts or orders received, the tax demand or regulatory order, and any media report or rumour.

## Method

1. Retrieve the current official text of SEBI LODR, the current LODR master circular and any later circulars on disclosure of material events, from sebi.gov.in. Record the version and date.
2. Classify the event:
   - deemed material (listed in Part A of Schedule III; disclose without a materiality test);
   - material if it crosses the materiality test (Part B) or the company's policy;
   - not material, but consider voluntary disclosure.
3. Apply the quantitative and qualitative tests from the retrieved text. Show the arithmetic. Where the company's policy is missing, say so and stop short of a final view.
4. Fix the deadline. Timelines are short and depend on the trigger (board decision, event within the company, event from outside). Confirm each from the current text; compute from the time of awareness.
5. Draft the disclosure with the details the master circular prescribes for that event type. Use a fact-only tone, no promotional language.
6. For a media report or market rumour, check whether the top listed entities' verification requirement applies to this company, and draft the confirmation, denial or clarification.
7. For governance checks, test board composition, independent director proportion, committee constitution, meeting frequency, the corporate governance report and the results timeline against the retrieved text.
8. Note follow-up updates the company must make (for example on outcome of litigation or completion of an acquisition).

## Output

1. Event classification and reasoning, with deadline and its basis.
2. Draft exchange disclosure for each event.
3. For governance reviews, a gap table: requirement · status · fix.
4. Open points for the compliance officer.

## Guardrails and hand-offs

- Do not decide materiality without the company's policy; flag it as provisional.
- Do not suggest delaying a disclosure; if the deadline has passed, say so and draft a delayed-disclosure explanation.
- Treat the event information as UPSI; hand trading window and leak issues to `insider-trading-pit-checker`.
- Related-party events go to `related-party-transaction-analyst`.
