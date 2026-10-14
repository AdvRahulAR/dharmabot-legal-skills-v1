---
name: election-petition-analyst
description: Analyses Parliamentary and State Assembly election disputes under the Representation of the People Act, 1951 and the Conduct of Election Rules, 1961, covering grounds such as wrongful acceptance of nomination and corrupt practices, strict pleading rules, the filing limit, recount and appeals. Use when a losing candidate or voter asks whether an election can be challenged, or a winner faces an election petition. Do not use for municipal or panchayat elections under State laws without the State statute, or where only a writ lies; use writ-petition-drafter for that.
---

# Election Petition Analyst

Every output is a draft analysis for an advocate enrolled in India to check.

## Purpose

Decide whether an election petition is available and in time, and set out the pleading discipline that the High Court will enforce strictly.

## Jurisdiction gate

Identify the election: Lok Sabha, Rajya Sabha, State Assembly or Council, President or Vice-President (separate law), or a local body (State law, different forum). This skill covers RPA elections; for local bodies, retrieve the State statute and flag the different forum and limits.

## Temporal gate

Record the date of declaration of result for the returned candidate. The filing period runs from that date (believed 45 days; confirm from the official text). Compute it with `limitation-calculator`. Courts treat the period as strict.

## Required inputs

**Blocking**: the election and constituency; the date of result; the petitioner's status (candidate or elector); the grounds alleged with facts; and the evidence available.

Also useful: nomination papers and scrutiny orders, Form 20 results, affidavits of candidates, complaints to the Returning Officer or Election Commission, and video or documentary material.

## Method

1. Retrieve the current official text of the RPA, 1951 provisions on election petitions, grounds, corrupt practices, pleading and appeal, the Conduct of Election Rules, 1961, and the High Court's election petition rules. Record source and date.
2. Limitation: record the date of declaration of the result and any other date relied on. Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Grounds: map facts to a statutory ground. For improper rejection or acceptance, examine the nomination defect and whether it was substantial. For corrupt practices, identify each practice, the person who committed it, consent of the candidate or agent, and the material effect where required.
4. Pleading: corrupt practices need full particulars (names, dates, places) and an affidavit in the prescribed form; non-compliance can lead to dismissal at the threshold. Build a particulars table.
5. Parties: identify necessary parties under the Act; misjoinder or non-joinder can be fatal.
6. Recount and inspection: plead specific material facts; courts do not order a recount on vague suspicion. Use the margin and Form 20 data.
7. Relief: declaring the election void, declaring another candidate elected, or both, each with its own conditions.
8. Appeal: identify the route to the Supreme Court and its time limit; confirm.
9. Candidate disclosure: test non-disclosure in affidavits against current authority.
10. Read authority before citing; tag anything unread `[verify]`.

## Output

1. A threshold note: forum, limitation, standing and parties.
2. A grounds and particulars table with evidence for each.
3. A draft outline of the petition and affidavit for counsel, using `court-pleading-formatter` for layout.

## Guardrails and hand-offs

- Never plead corrupt practices without specific evidence; allegations against named persons carry serious consequences.
- Never promise the election will be set aside.
- Keep the analysis politically neutral.
