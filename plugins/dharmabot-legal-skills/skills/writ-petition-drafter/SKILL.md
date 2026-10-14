---
name: writ-petition-drafter
description: Assesses and drafts writ petitions before a High Court under Article 226 or the Supreme Court under Article 32, covering maintainability, Article 12 status, alternative remedy, delay and laches, locus, and judicial review grounds such as illegality, irrationality, procedural impropriety, proportionality and natural justice, with interim relief. Use when a client wants to challenge government or authority action, an order passed without hearing, or seeks mandamus or habeas corpus. Do not use for a pure vires challenge to a statute; use constitutional-validity-analyst.
---

# Writ Petition Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Decide whether a writ lies, and draft a petition that shows the right, the wrong, the reason no other remedy is adequate, and the relief.

## Jurisdiction gate

Confirm the action is by an Indian authority. Identify the High Court with territorial jurisdiction (where the cause of action arose wholly or in part, or where the authority sits). Article 32 lies only for fundamental rights; note the Supreme Court's usual preference for Article 226 first. Record the High Court's writ rules and roster.

## Required inputs

**Blocking**: the impugned order, action or inaction; the date of it and of the petitioner's knowledge; the authority and its legal status; the right affected; and any statutory appeal, revision or other remedy available.

Also useful: representations made and replies, the governing statute and rules, notices issued, and similar cases decided.

## Method

1. Retrieve the current official text of the Constitution provisions, the statute and rules under which the authority acted, and the High Court's writ rules and forms. Record source and date.
2. Maintainability: is the respondent State or performing a public function; is there locus; is the dispute mainly about facts that need evidence (unsuitable for writ); is it a contractual dispute with no public law element.
3. Alternative remedy: identify it and test the exceptions recognised in Whirlpool Corporation v. Registrar of Trade Marks (Supreme Court, 1998), such as violation of natural justice, lack of jurisdiction or a challenge to vires. Confirm current treatment.
4. Delay: compute time from the cause of action; explain any delay with dates. Use `limitation-calculator` where a statutory appeal period is relevant by analogy.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
5. Choose the writ: certiorari, mandamus, prohibition, habeas corpus or quo warranto, and the precise order sought.
6. Grounds: illegality (no power, wrong law, irrelevant considerations), irrationality, procedural impropriety (no notice, no hearing, bias, no reasons), proportionality where rights are restricted, legitimate expectation, and discrimination under Article 14. Tie each ground to a document.
7. Interim relief: prima facie case, balance of convenience, irreparable harm, and urgency for listing.
8. Search for and read current Supreme Court and jurisdictional High Court authority. Tag anything unread `[verify]`. Hand off to `citation-verifier`.

## Output

1. A maintainability note with risks.
2. The writ petition: synopsis and list of dates, facts, questions of law, grounds, prayer, interim application and affidavit.
3. An annexure index and a list of necessary parties.

## Guardrails and hand-offs

- Never suppress a material fact or an alternative remedy; suppression can defeat the petition.
- Never promise interim or final relief.
- Use `court-pleading-formatter` for layout and `constitutional-validity-analyst` where a rule or statute is challenged.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
