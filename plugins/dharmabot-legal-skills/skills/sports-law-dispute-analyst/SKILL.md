---
name: sports-law-dispute-analyst
description: Analyses Indian sports disputes involving athletes, clubs and federations, including governance and recognition under the National Sports Governance Act 2025 and the Sports Code, selection disputes and writs against federations, anti-doping under the National Anti-Doping Act 2022 and the WADA Code, player transfer and contract disputes, and CAS or federation arbitration. Use when an athlete is dropped from selection, charged with a doping violation, or in a contract dispute with a club. Do not use to draft the writ itself; use writ-petition-drafter.
---

# Sports Law Dispute Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Identify the athlete's or body's remedies, the right forum, and the deadlines that could close them.

## Jurisdiction gate

Identify the sport, the federation (national, State or international), the event and where the decision was made. Indian courts, the statutory bodies under the 2025 Act, the anti-doping panels and international bodies (the international federation, CAS) may each have a role. Contracts with foreign clubs may be governed by foreign law; flag them for counsel there.

## Temporal gate

The National Sports Governance Act 2025 is being brought into force in stages, and the National Anti-Doping Act 2022 was amended in 2025. Check which provisions have commenced and whether the National Sports Tribunal is functioning. The WADA Code and international standards are revised periodically. Record the dates of the decision, the sample collection and any notice.

## Required inputs

Mark as **blocking**:
- the decision or charge being challenged, with its date and the body that made it;
- the athlete's level (State, national, international) and federation membership;
- for doping: the notice of charge, the substance, and whether a provisional suspension applies.

Also useful: selection criteria published in advance, trial results, federation constitution, player contract, and correspondence.

## Method

1. Retrieve the current official text of the National Sports Governance Act and notifications, the National Sports Development Code where still relevant, the National Anti-Doping Act and its rules, the WADA Code and the federation's constitution and selection policy. Record versions and dates.
2. **Selection disputes.** Were criteria published before trials? Were they followed? Was the athlete heard? Note the internal appeal, any statutory grievance or tribunal route, and the High Court writ route against bodies performing public functions. Search for and read current authority on writs against federations.
3. **Anti-doping.** Map the charge, the B-sample right, the hearing panel and appeal body, the burden on the athlete, and routes to reduce sanction (no fault, no significant fault, therapeutic use exemption, contaminated product). Check strict deadlines for B-sample requests and appeals. Compute with `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
4. **Governance.** Recognition, elections, eligibility and conflicts within the federation under the 2025 Act.
5. **Contract and transfer disputes.** Identify the dispute clause: federation dispute resolution chamber, CAS, Indian arbitration or courts. Hand off clause analysis to `arbitration-clause-reviewer`.
6. Note interim relief options and the effect of a provisional suspension on selection.
7. Tag anything not read in full `[verify]`.

## Output

1. A remedies map: issue · forum · deadline (to confirm) · relief · prospects factors.
2. A list of documents to request from the federation or agency.
3. Recommended immediate steps.

## Guardrails and hand-offs

- Never advise an athlete to evade testing or delay sample collection.
- Never predict a sanction or selection outcome.
- For a writ, hand off to `writ-petition-drafter`.
- Before delivery, send citations to `citation-verifier`.
