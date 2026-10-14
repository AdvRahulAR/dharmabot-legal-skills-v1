---
name: posh-inquiry-report-drafter
description: Supports an Internal Committee through a complaint under the POSH Act 2013 and Rules, drafting conciliation records, notices to the parties, an inquiry plan, hearing minutes, interim-relief recommendations and the inquiry report with findings and recommendations. Use when an Internal Committee or Local Committee has received a sexual harassment complaint and needs notices, a timeline or the inquiry report. Do not use for setting up POSH compliance; use posh-compliance-advisor instead.
---

# POSH Inquiry Report Drafter

Every output is a draft for the Internal Committee and its advising advocate to review. The Committee alone decides the findings.

## Purpose

Help the Committee run a fair, confidential, time-bound inquiry and record it in a report that withstands challenge.

## Jurisdiction gate

Confirm the complaint is under the POSH Act (an aggrieved woman, a workplace in India, conduct within the statutory definition). If the respondent is a government servant, a service-rules procedure may apply; ask which rules. If the complaint is against the employer itself, note the Local Committee route.

## Required inputs

Mark as **blocking**:
- the written complaint and its date of receipt;
- the Committee's composition and quorum;
- the dates of the alleged incidents (to test the limitation and extension provisions);
- whether the complainant has asked for conciliation;
- any police complaint or parallel proceeding.

Also useful: the respondent's reply, witness lists, documents and electronic evidence, and the employer's service rules or standing orders.

## Method

1. Retrieve the current official text of the POSH Act, the POSH Rules, the employer's policy and service rules. Record the version and date.
2. Check limitation for filing and whether the Committee recorded reasons for any extension.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
3. Offer conciliation only at the complainant's request and never on monetary settlement, as the Act is believed to provide; confirm the wording.
4. Build a timeline from receipt: copy to the respondent, reply, inquiry completion (believed to be 90 days) and report (believed to be within 10 days of completion). Confirm each period from the Act and Rules.
5. Draft notices: to the respondent with the complaint and documents; hearing notices to both parties; witness notices. Record that legal practitioners may not represent parties, if the Rules so provide; confirm.
6. Plan the inquiry: order of evidence, opportunity to cross-question through the Committee, handling of electronic evidence, and accommodation for the complainant.
7. Consider interim relief on the complainant's written request (transfer, leave, restraint on reporting) and record reasons.
8. Draft minutes of each hearing in neutral terms.
9. Draft the report: complaint summary, procedure followed, evidence, analysis on each allegation, findings recorded by the Committee, and recommendations within the Act. Address any malicious complaint or false evidence only on the Committee's own finding, noting that inability to prove a complaint is not itself malice.

## Output

1. Notices and the inquiry timeline.
2. Hearing minute templates.
3. The draft inquiry report in a format the Committee can complete and sign.
4. A natural-justice checklist.

## Guardrails and hand-offs

- Never decide guilt or write findings the Committee has not reached.
- Keep identities, statements and the report confidential; use initials in drafts.
- Never invent statements, evidence or dates.
- For a follow-on disciplinary process under service rules, hand off to `disciplinary-inquiry-drafter`.
- For gaps in the Committee's constitution or policy, hand off to `posh-compliance-advisor`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
