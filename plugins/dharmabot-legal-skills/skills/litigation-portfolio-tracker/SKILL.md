---
name: litigation-portfolio-tracker
description: Builds and maintains an organisation-wide litigation and claims register for an Indian company, covering forum, stage, counsel, amount at stake, probability for contingent-liability and provision decisions under Ind AS 37, legal spend against budget, next dates and trends, with board or audit committee summaries and listed-company disclosure flags under SEBI LODR. Use when a legal head asks to "consolidate our cases", "litigation report for the audit committee" or "contingent liability schedule". Do not use for a single matter's day-to-day diary; use matter-deadline-tracker instead.
---

# Litigation Portfolio Tracker

Every output is a draft register and report for the general counsel or supervising advocate to review.

## Purpose

Give management one accurate, current view of all disputes, their exposure and their cost, in a form finance and the board can use.

## Jurisdiction gate

Confirm the organisation is Indian or has Indian litigation. Record the States and UTs and fora involved (consumer commissions, labour courts, tax authorities, tribunals, High Courts, the Supreme Court, arbitrations). Foreign matters are listed but marked "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the case list or source data (counsel reports, case diaries, invoices), with forum, case number and parties;
- the reporting date and audience (management, audit committee, board, auditors);
- whether the company is listed.

Also useful: last period's register, materiality thresholds set by the board, legal budget, and finance's provisioning policy.

## Method

1. Retrieve the current official text of Ind AS 37 (provisions and contingent liabilities), the SEBI LODR Regulations and the company's materiality policy if listed (litigation disclosure is believed to fall under Regulation 30; confirm), and any sector rules on reporting claims. Record version and date.
2. Normalise each matter into one row: ID, forum, State, case number, parties, nature, the company's role, counsel, filing date, stage, last and next date, amount claimed, interest, and insurance or indemnity cover.
3. Verify next dates from the court's cause list or eCourts status where possible; flag rows not verified.
4. Record counsel's assessment as probable, possible or remote, with the date and basis. Do not assign a probability yourself; mark missing assessments.
5. Map each matter to provision, disclosure as contingent liability, or neither, using the Ind AS 37 tests. Flag for finance and auditors to decide.
6. Track legal spend: billed, accrued and budgeted per matter and per counsel.
7. For listed companies, flag matters that may need disclosure under the materiality policy, and changes since the last disclosure.
8. Analyse trends: new matters by type and forum, ageing, repeat claimants, and outcomes.

## Output

1. The register as XLSX, one row per matter, with a data dictionary sheet.
2. Contingent-liability and provision schedule for finance.
3. Board or audit committee summary: totals, top exposures, movements, disclosure flags and spend against budget.
4. Exceptions: missing assessments, stale dates, data conflicts.

## Guardrails and hand-offs

- Never state a probability or amount counsel has not given. Mark it missing.
- The final provisioning and disclosure decision belongs to management, the auditors and the board.
- Keep privilege in mind: label counsel assessments privileged and confidential.
- Day-to-day diaries go to `matter-deadline-tracker`; single-matter budgets to `matter-plan-builder`; disclosure drafting to `sebi-lodr-disclosure-checker`.
