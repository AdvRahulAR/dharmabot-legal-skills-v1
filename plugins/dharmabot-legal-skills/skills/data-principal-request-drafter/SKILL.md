---
name: data-principal-request-drafter
description: Handles requests from data principals under the Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 (access to a summary, correction, completion, erasure, nomination and grievance) and GDPR data subject requests where they apply, covering identity checks, scope, retention required by RBI, tax, PMLA and other laws, timelines and the response letter. Use when a customer or employee asks for their data, asks us to delete their data, or files a privacy grievance. Do not use for a programme-wide review; use dpdp-compliance-gap-analyst instead.
---

# Data Principal Request Drafter

Every output is a draft for an advocate enrolled in India or the client's privacy team to check before it is sent.

## Purpose

Give a lawful, complete and timely answer to one request, and record what was done, kept and deleted, and why.

## Jurisdiction gate

- Confirm the requester is a data principal whose data the client processes under the DPDP Act.
- If the requester is in the EU or UK, or the client is subject to GDPR, treat it also as a DSAR and mark GDPR points for EU or UK counsel.
- Check whether the client is a processor for this data. If so, pass the request to the fiduciary rather than answer it.

## Temporal gate

The DPDP rights provisions and the rights rules are believed to commence on 13 May 2027. Confirm from the Gazette. Before then, respond under the client's own privacy policy, the SPDI Rules, 2011 and contract, and say so in the internal note.

## Required inputs

**Blocking**:
- the request in full, with date received and channel;
- how the requester's identity has been or can be verified;
- the systems that hold the requester's data, and the products or accounts involved;
- any pending dispute, investigation, loan, claim or regulatory hold involving the requester.

Also useful: the client's retention schedule, privacy policy, and earlier correspondence.

## Method

1. Retrieve the current official text of the DPDP Act, the DPDP Rules (rights and grievance rules) and each retention law relied on, for example the RBI KYC Master Direction, PMLA record-keeping rules, Income-tax and GST record rules and the Companies Act. Record version and date.
2. Log the request and diarise the response period stated in the Rules or the client's published policy. The Rules are reported to set an outer limit for grievances; confirm it. For GDPR, the period is believed to be one month, extendable in some cases.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Verify identity proportionately. Do not ask for more data than needed to verify.
4. Classify each element of the request: access, correction, completion, updating, erasure, nomination, grievance, or withdrawal of consent.
5. Access: prepare a summary of the personal data and processing activities, and the identities of other fiduciaries and processors it was shared with, as the Act requires.
6. Correction and completion: fix data that is inaccurate or incomplete, or explain with reasons why not.
7. Erasure: erase unless retention is needed for the specified purpose or to comply with a law. For each item kept, cite the law and the period, and set a deletion date.
8. Flow the erasure or correction to processors, and keep confirmation.
9. Remove other people's personal data from any disclosure. Hand complex redaction to `redaction-reviewer`.
10. If a legal hold applies, keep the data and say so in the internal note, not necessarily in the letter.
11. Draft the response letter in plain language, with the grievance route and the right to complain to the Data Protection Board.

## Output

1. Response letter to the data principal.
2. Internal action note: deleted · retained (law and period) · corrected · sent to processors · deadline met.
3. Request log entry.

## Guardrails and hand-offs

- Never disclose third parties' personal data.
- Never refuse erasure by citing a retention law without checking that it covers that data item.
- Never mislead the requester about what is kept.
- Recurring or systemic issues go to `dpdp-compliance-gap-analyst`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
