---
name: csr-esg-brsr-compliance-checker
description: Checks corporate social responsibility duties under the Companies Act, 2013 and the CSR Rules (applicability, committee, policy, Schedule VII activities, implementing agencies with CSR-1, unspent amounts and impact assessment) and ESG reporting under SEBI's Business Responsibility and Sustainability Report and BRSR Core, and maps greenwashing risk in sustainability claims. Use when a client asks whether CSR applies, how much to spend, how to treat unspent CSR, or whether it must file a BRSR. Do not use for setting up an NGO; use nonprofit-fcra-compliance-advisor instead.
---

# CSR, ESG and BRSR Compliance Checker

Every output is a draft review for an advocate enrolled in India, the company secretary and the auditors to check.

## Purpose

Tell the company whether CSR and BRSR duties apply, what they require this year, and where its sustainability claims could mislead.

## Jurisdiction gate

- CSR duties apply to Indian companies and to foreign companies with a branch or project office in India that meet the thresholds; confirm from the text.
- BRSR applies to listed entities by market-capitalisation rank as set by SEBI. Unlisted companies are not bound but may report voluntarily.

## Temporal gate

- CSR applicability depends on the immediately preceding financial year's figures. Record the year in which the threshold was crossed and the year the duty starts.
- SEBI has changed BRSR Core assurance and value-chain timelines more than once. Retrieve the circular in force for the reporting year.

## Required inputs

**Blocking**:
- financial statements for the last three financial years (net worth, turnover, net profit computed as the Act requires);
- whether the company is listed, and its market-capitalisation rank if so;
- current CSR policy, committee and projects, and any unspent amount.

Also useful: implementing agency details, impact assessment reports, and sustainability claims in reports, ads or product labels.

## Method

1. Retrieve the current official text of the Companies Act CSR provision (believed to be section 135), Schedule VII, the CSR Rules, MCA FAQs and circulars, and SEBI's BRSR and BRSR Core circulars. Record version and date.
2. Applicability: test net worth, turnover and net profit against the thresholds in the Act (confirm current figures). Explain which year's figures count.
3. Obligation: compute the prescribed spend from average net profits as the Rules define them. Show the working; do not round off silently.
4. Governance: CSR committee need (the Act exempts some companies below a spend level; confirm), CSR policy, annual action plan and board approvals. Hand board papers to `board-meeting-documents-drafter`.
5. Projects: check each against Schedule VII (believed to be the schedule; confirm against the official text) and excluded activities, implementing agency eligibility and CSR-1 registration, and administrative overhead limits.
6. Unspent amounts: ongoing project versus other, the transfer deadlines and destination, and penalties (confirm).
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
7. Impact assessment: whether required for this company and project size.
8. Reporting: annual report on CSR, and board report disclosures.
9. BRSR: check applicability, BRSR Core indicators, assurance or assessment requirements, and value-chain disclosures for the reporting year.
10. Greenwashing: test environmental claims against CCPA guidelines on misleading environmental claims and advertising law. Ask for evidence for each claim.

## Output

1. CSR applicability and spend computation with working.
2. CSR compliance checklist with status.
3. BRSR applicability note and gap list.
4. Claims risk table: claim · evidence · risk · fix.

## Guardrails and hand-offs

- Never treat spending on the company's own business or employees as CSR without testing the exclusions.
- Never compute figures from estimates; ask for audited numbers.
- Charity set-up questions go to `nonprofit-fcra-compliance-advisor`; ad claims to `advertising-claims-reviewer`.
