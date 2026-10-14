---
name: board-meeting-documents-drafter
description: Drafts board, committee and shareholder resolutions, notices of board and general meetings with explanatory statements, and minutes under the Companies Act 2013 and Secretarial Standards SS-1 and SS-2, and lists the ROC forms to file. Use when someone asks for a board resolution, circular resolution, EGM or AGM notice, explanatory statement, postal ballot notice or minutes. Do not use to check whether annual filings are overdue; use roc-secretarial-compliance-checker instead.
---

# Board Meeting Documents Drafter

Every output is a draft for an advocate or company secretary in India to check before circulation.

## Purpose

Produce resolutions, notices and minutes that match the company's articles, the Companies Act 2013 and the Secretarial Standards, and that record only what actually happened.

## Jurisdiction gate

- Confirm the company is incorporated in India under the Companies Act 2013 or an earlier Companies Act.
- Identify the class: private, public unlisted, listed, OPC, small company, Section 8, government company or subsidiary of a foreign company. Exemptions and notice periods differ by class.
- For listed companies, SEBI LODR adds requirements; hand off disclosure timing to `sebi-lodr-disclosure-checker`.

## Required inputs

- **Blocking:** company name, CIN and class; the business to be transacted; the meeting type (board, committee, general meeting, circulation, postal ballot).
- **Blocking for minutes:** the actual attendance, quorum, chair, interests declared, discussion summary and votes. Do not draft minutes without them.
- Useful: the AOA, previous minutes, the shareholding pattern, and any shareholders' agreement with reserved matters.

## Method

1. Retrieve the current official text of the relevant Companies Act provisions and rules, SS-1 and SS-2 from the ICSI website, and the current e-forms on the MCA portal. Record the version and date.
2. Classify each item of business:
   - matters only the board may decide at a meeting (not by circulation);
   - matters needing an ordinary or special resolution;
   - matters reserved for investors under the SHA and AOA.
3. Check the board mechanics: notice period and mode, quorum (including interested directors who cannot count), video-conferencing rules, and the chair's role.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. For general meetings, draft the notice with the explanatory statement (believed to be section 102; confirm). Disclose each director's and KMP's interest and the material facts. For a preferential allotment, include the disclosures required by the private placement and preferential issue rules.
5. Draft resolutions in operative form ("RESOLVED THAT ... RESOLVED FURTHER THAT ..."), with authority to named officers to file forms and sign documents.
6. Draft minutes from the inputs only. Follow SS-1 or SS-2 on contents, signing and the time for entry. Mark any gap `[input needed]`.
7. List the forms to be filed after the meeting (for example MGT-14 for certain resolutions, PAS-3 after allotment, DIR-12 for director changes). Confirm each form and its deadline from the MCA portal. Hand deadlines to `limitation-calculator` if a date-count is needed.

## Output

1. Notice (with agenda and explanatory statement) or circular resolution.
2. Resolutions, each with its type (board, ordinary, special).
3. Draft minutes, or a minutes template if the meeting has not happened.
4. A post-meeting filing table: form, trigger, deadline (verified), attachments.

## Guardrails and hand-offs

- Never invent attendance, votes, dissent or interest disclosures.
- Never backdate notices, minutes or resolutions.
- Flag when an interested director cannot vote or count for quorum.
- Securities issue steps go to `securities-issuance-compliance-checker`; recurring compliance to `roc-secretarial-compliance-checker`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
