---
name: civil-interlocutory-application-drafter
description: Drafts routine interlocutory applications in Indian civil courts under the Code of Civil Procedure and the Limitation Act, including rejection of plaint, amendment of pleadings, impleadment and deletion of parties, condonation of delay, restoration, setting aside ex parte decrees, discovery and interrogatories, caveats and transfer petitions. Use when an advocate asks for an Order 7 Rule 11, Order 6 Rule 17, Order 1 Rule 10, section 5 delay condonation, caveat or transfer application. Do not use for injunctions or attachment; use interim-injunction-application-drafter instead.
---

# Civil Interlocutory Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Draft the right interlocutory application for the stage of the case, with the governing test stated and applied to the record.

## Jurisdiction gate

Confirm the proceeding is before an Indian civil court and note the court, State and case stage. Check whether the relief needs an application at all, or a separate suit, appeal or revision instead.

## Required inputs

Mark as **blocking**:
- the application type sought;
- the pleadings and orders relevant to it;
- the case stage (pre-trial, trial commenced, decree passed);
- for condonation or restoration, the exact dates and the reasons for delay or absence.

## Method

1. Retrieve the current official text of the governing provision, any High Court amendment, and the relevant rules. Record the version and date. Confirm every section, order and rule number used in this skill against that text.
2. Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
3. Identify the test and apply only the record. Typical tests:
   - **Rejection of plaint:** read the plaint and its documents only; no defence material. Bars include no cause of action, undervaluation, insufficient stamp and bar by law (including limitation on the plaint's own averments).
   - **Amendment:** necessary for the real controversy; after trial starts, show due diligence (believed to be the proviso to Order VI Rule 17; confirm). Check whether a time-barred claim is being introduced.
   - **Impleadment or deletion:** necessary or proper party.
   - **Condonation:** sufficient cause, explained day by day where possible; Limitation Act section 5 does not apply to suits.
   - **Setting aside ex parte decree:** non-service or sufficient cause, within time.
   - **Discovery and interrogatories:** relevance and necessity; in commercial suits, the amended Order XI.
   - **Caveat:** under section 148A CPC, with service on the likely applicant; note the period it remains in force.
   - **Transfer:** the correct court (District Court, High Court or Supreme Court) and grounds such as convenience or apprehension of bias.
4. Check limitation for the application itself with `limitation-calculator`.
5. Draft the application, the supporting affidavit, and a short proposed order.
6. Search for and read current authority on the test. Tag unread authority `[verify]`.
7. State in the note when a different remedy fits better (for example an appeal against a decree, not an application).

## Output

1. The draft application and affidavit.
2. A one-page note: test, how the facts meet it, weak points, and the alternative remedy if any.

## Guardrails and hand-offs

- Never invent dates or reasons for delay.
- Never use a Rule 11 application to argue disputed facts.
- Formatting: `court-pleading-formatter`. Supreme Court transfer or SLP: `special-leave-petition-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
