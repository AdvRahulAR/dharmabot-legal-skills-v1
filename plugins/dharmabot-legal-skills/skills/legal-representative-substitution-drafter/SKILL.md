---
name: legal-representative-substitution-drafter
description: Drafts applications under Order XXII of the Code of Civil Procedure on the death, insolvency or marriage of a party, covering bringing legal representatives on record, intermeddlers, survival of the right to sue, setting aside abatement with condonation of delay, and the advocate's intimation under Rule 10A, in suits, appeals and execution. Use when a party has died during a case and the advocate needs substitution or set-aside-abatement papers. Do not use for impleadment or deletion under Order I Rule 10; use civil-interlocutory-application-drafter.
---

# Legal Representative Substitution Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Keep a proceeding alive after a party dies, or revive it after abatement, with the right application, the right respondents and a truthful explanation of any delay.

## Jurisdiction gate

Confirm the proceeding is before an Indian civil court, appellate court or executing court, and record the State. Note whether a special statute or the court's rules modify Order XXII. Check whether a State amendment to Order XXII applies.

## Required inputs

Mark as **blocking**:
- the case number, court, stage and the deceased party's position (plaintiff, defendant, appellant, respondent);
- the date of death and proof (death certificate);
- the date the applicant learnt of the death, and how;
- the proposed legal representatives with their relationship and addresses.

Also useful: any will, succession certificate or legal heirship certificate; whether the deceased's interest was joint or several; whether any representative is a minor.

## Method

1. Retrieve the current official text of Order XXII (Rules 1 to 12, including any State amendment), Order XXXII for minors, and the Limitation Act articles for substitution and for setting aside abatement (believed to be Articles 120 and 121; confirm). Record the source and date.
2. Decide whether the right to sue survives, and whether the suit abates wholly or only against the deceased. Check if the remaining parties can continue. Note that the abatement rules do not apply in the same way to execution proceedings (believed to be Rule 12; confirm), though substitution is still needed there.
3. Compute deadlines with `limitation-calculator`. If the substitution period has run, the suit has abated as to that party. Plan an application to set aside abatement and, if needed, to condone delay.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
4. Identify legal representatives as defined in the CPC, including intermeddlers. Where heirship is disputed, note that the court decides it only for the purpose of the suit. Hand heir identification to `intestate-succession-share-calculator`.
5. Draft the substitution application with a list of proposed legal representatives and an amended cause title.
6. Draft the set-aside-abatement and delay application. Explain each period of delay with dates. Address the rule that knowledge of death matters, and any Rule 10A intimation by counsel (believed to be Order XXII Rule 10A; confirm against the official text).
7. Check the exemption that may apply to non-contesting or ex parte defendants, and Rule 4A where no representative exists (confirm current wording).
8. Search for current Supreme Court and High Court authority on liberal construction in abatement cases. Read it; tag anything unread `[verify]`.

## Output

1. Substitution application with affidavit and amended memo of parties.
2. Application to set aside abatement and condone delay, if needed.
3. Rule 10A intimation memo, if counsel for the deceased is filing.
4. A note on deadlines, missing documents and heirship risks.

## Guardrails and hand-offs

- Never invent dates of death or knowledge. Delay must be explained with real facts.
- Impleadment or deletion on other grounds goes to `civil-interlocutory-application-drafter`.
- Never cite unread authority; hand citations to `citation-verifier`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
