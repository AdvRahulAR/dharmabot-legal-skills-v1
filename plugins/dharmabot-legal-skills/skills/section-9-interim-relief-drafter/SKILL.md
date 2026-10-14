---
name: section-9-interim-relief-drafter
description: Drafts applications for interim measures in Indian-seated arbitration, either a court petition under section 9 of the Arbitration and Conciliation Act, 1996 or an application to the tribunal under section 17, covering prima facie case, balance of convenience, irreparable harm, securing the claim and bank guarantee encashment. Use when a lawyer wants to stop encashment of a bank guarantee, secure the amount in dispute, or get an urgent injunction pending arbitration. Do not use for a civil suit injunction; use interim-injunction-application-drafter instead.
---

# Section 9 Interim Relief Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Choose the right forum for interim relief in an arbitration and draft an application that meets the tests courts and tribunals actually apply.

## Jurisdiction gate

Confirm there is an arbitration agreement and the seat is in India. For a foreign-seated arbitration, check whether section 9 applies through the proviso to section 2(2) and hand off to `international-arbitration-planner`. Identify the court with jurisdiction: the seat court, and whether it is a High Court on its original side or a Commercial Court.

## Required inputs

Mark as **blocking**:
- the arbitration clause and the contract;
- the stage: before invocation, notice sent, tribunal constituted, or award made;
- the relief needed and the threatened act with its date (for example a demand to encash a guarantee);
- the instrument or asset at stake (bank guarantee text, property, account).

Also useful: correspondence, the claim amount, evidence of the respondent's financial condition or asset dissipation, and any earlier orders.

## Method

1. Retrieve the current official text of sections 9 and 17 of the Arbitration and Conciliation Act, 1996, the Commercial Courts Act, 2015 where it applies, the rules and practice directions of the court, and CPC provisions on injunctions and attachment. Record the version and date. Confirm every section, rule and article number used in this skill against that official text before relying on it.
2. **Forum.** If the tribunal is constituted, test the bar in section 9(3): the court should not entertain the petition unless the section 17 remedy is not efficacious. Explain why the court is still needed, or draft for the tribunal instead.
3. **Timing.** If relief is sought before arbitration, record the believed requirement that proceedings start within 90 days of the order (section 9(2)); confirm from the text and diarise it. Hand off the follow-on notice to `arbitration-invocation-notice-drafter`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
4. **Grounds.** Build each from the record: prima facie case on the contract; balance of convenience; irreparable harm not compensable in money; and urgency.
5. **Bank guarantees.** Read the guarantee. An unconditional guarantee is usually treated as independent of the contract. Courts restrain encashment only in narrow cases such as egregious fraud or special equities causing irretrievable injustice. Search for and read current Supreme Court and jurisdictional High Court authority; do not overstate the exception.
6. **Securing the amount.** For deposit or attachment-type relief, plead specific facts showing intent to defeat an award, mirroring the standards of Order XXXVIII CPC as courts apply them. Check current authority.
7. **Post-award.** If an award exists, consider whether section 9 relief or enforcement under section 36 is the better path.
8. Draft the petition: cause title, jurisdiction and seat, facts, arbitration agreement, grounds, urgency, prayer (interim and ad interim), undertaking to commence arbitration, verification, affidavit and annexures. Add a caveat check and an advance-notice note where the court's rules require.

## Output

1. The draft petition or section 17 application with prayers.
2. A list of dates and annexures.
3. A short note: strongest and weakest grounds, the 90-day diary date if relevant, and risks of the order being refused or vacated.

## Guardrails and hand-offs

- Never promise an ad interim order.
- Do not allege fraud without documents that support it.
- Never invent authority; tag unread authority `[verify]` and run `citation-verifier`.
- Format to the court's rules with `court-pleading-formatter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
