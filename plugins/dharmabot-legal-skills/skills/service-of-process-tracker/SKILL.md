---
name: service-of-process-tracker
description: Tracks service of summons and notices in Indian civil and criminal courts under Order V of the Code of Civil Procedure and the Bharatiya Nagarik Suraksha Sanhita, 2023, covering process fee, court, postal, courier, email and electronic service, defects in returned service reports, deemed service, and substituted service applications with paper publication. Use when summons came back unserved, door locked or refused, or an advocate needs a service status table. Do not use for service abroad; use cross-border-service-evidence-planner.
---

# Service of Process Tracker

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Keep a clear record of service on every party, spot defective service reports early, and move to substituted service only when the law allows it.

## Jurisdiction gate

Confirm the case is before an Indian court and record the State and court. Note any High Court rules on process and electronic service, and whether the matter is a commercial suit with its own service rules. If any party is outside India, hand that party to `cross-border-service-evidence-planner`.

## Temporal gate

For criminal cases, check whether the BNSS or the Code of Criminal Procedure, 1973 governs. If the case began before 1 July 2024, run `crpc-bnss-transition-analyst` first.

## Required inputs

Mark as **blocking**:
- the court, case number and the list of parties to be served with addresses;
- the orders directing issue of summons or notice, with dates;
- the returned service reports or postal tracking, for each attempt.

Also useful: email addresses and phone numbers given in the pleadings, the client's knowledge of where the party lives or works, and earlier addresses.

## Method

1. Retrieve the current official text of Order V CPC (including the rules on court service, courier and electronic modes, refusal, affixture and substituted service), the BNSS chapter on processes to compel appearance (believed to run from section 63 to 71; confirm), and the High Court's process rules. Record the source and date.
2. Build a service table: party · address · mode · date issued · date returned · endorsement · status.
3. Review each report for defects: no witness to affixture, no attempt at the right time, vague "not found", no statement of inquiries made, wrong address.
4. Note where deemed service may apply (for example refusal, or postal service with correct address), and confirm the current rule and case law before relying on it. Tag unread authority `[verify]`.
5. If ordinary service has genuinely failed, draft an application for substituted service with an affidavit of the attempts made and why the party is avoiding service. Propose the mode (paper publication in a named local newspaper, affixture, email, messaging service) that the court may accept.
6. Track process fee, steps and deadlines set by the court. Hand dates to `matter-deadline-tracker`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.

## Output

1. The service status table.
2. A defect note on each returned report.
3. Draft substituted service application and affidavit, with a draft publication text.
4. A list of steps due and their dates.

## Guardrails and hand-offs

- Never treat a party as served without a report or order that shows it.
- Never invent attempts, endorsements or addresses.
- Do not use a party's contact details beyond what the court permits.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
