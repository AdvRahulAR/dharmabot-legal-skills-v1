---
name: oppression-mismanagement-petition-drafter
description: Drafts petitions before the National Company Law Tribunal for oppression and mismanagement under the Companies Act, 2013, with the eligibility check and waiver application, interim relief applications, and the respondent's reply and maintainability objections under the NCLT Rules, 2016, mapping each act to board records and the articles. Use when a minority shareholder has been removed as director, diluted, or excluded from management, or a company must answer such a petition. Do not use for IBC petitions; use ibc-application-drafter.
---

# Oppression and Mismanagement Petition Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Draft a petition (or reply) that proves a course of oppressive or prejudicial conduct with documents, meets the eligibility threshold or justifies waiver, and seeks relief the NCLT can grant.

## Jurisdiction gate

Confirm the company is incorporated in India and identify the NCLT bench with jurisdiction over its registered office. Check whether an arbitration clause, a pending suit or an IBC proceeding affects maintainability. Foreign holding structures may need a separate analysis of the shareholders' agreement.

## Required inputs

Mark as **blocking**:
- the company's name, type (private, public, Section 8) and registered office;
- the petitioner's shareholding and how many members join the petition;
- the acts complained of, with dates;
- the documents available: articles, shareholders' agreement, board and general meeting minutes, MCA filings.

## Method

1. Retrieve the current official text of the Companies Act provisions on oppression and mismanagement (believed to be sections 241 to 246), the eligibility provision and waiver (believed to be section 244), the NCLT Rules, 2016 and forms, and the bench's practice directions. Record the source and date.
2. Test eligibility against the statutory thresholds by number of members or share capital. If not met, draft a waiver application showing why the case deserves it.
3. Build a chronology from the records. Pull MCA filings (for example allotment and director-change forms) to check notices, quorum and resolutions.
4. Map each act to a head: removal as director, dilution by allotment, exclusion from information, siphoning, breach of articles or the shareholders' agreement. Note whether it forms a continuing course of conduct.
5. Draft reliefs the tribunal may grant (setting aside allotments, restoring directorship, regulating affairs, buy-out, investigation). Keep them specific.
6. Draft an interim application: status quo on shareholding, restraint on further allotment or asset sale, and inspection.
7. Check limitation and delay. Whether the Limitation Act applies and how is a live point; search for current authority and tag unread cases `[verify]`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
8. For a respondent, draft the reply and maintainability objections: threshold, delay, arbitration, legitimate business decisions, and the petitioner's own conduct.

## Output

1. Company petition in the NCLT form, with synopsis, facts, grounds and reliefs.
2. Waiver application, if needed.
3. Interim application.
4. An exhibit map: act · date · document · relief linked.

## Guardrails and hand-offs

- Never invent shareholding figures, meeting dates or minutes.
- NCLAT appeals and IAs in existing proceedings go to `nclt-nclat-appeal-drafter`.
- Governance documents go to `board-meeting-documents-drafter`; SHA drafting to `shareholders-agreement-drafter`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
