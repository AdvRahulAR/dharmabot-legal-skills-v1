---
name: cyber-crime-complaint-drafter
description: Drafts cyber crime complaints for the National Cyber Crime Reporting Portal, helpline 1930, police, banks and platforms in India for online financial fraud, hacking, identity theft, sextortion, non-consensual images, cyberstalking and defamation, under the IT Act, 2000 and the Bharatiya Nyaya Sanhita, 2023, with fund-freeze and preservation requests. Use when a client was scammed online, lost money to a fake app, had an account hacked or found intimate images posted. Do not use where police refuse to register an FIR and a Magistrate complaint is needed; use criminal-complaint-drafter.
---

# Cyber Crime Complaint Drafter

Every output is a draft for an advocate enrolled in India or the victim to check before filing. Urgent steps come first.

## Purpose

Get funds frozen and evidence preserved quickly, and give police a clear, complete complaint they can act on.

## Jurisdiction gate

- Confirm the victim, the money trail or the offender has an Indian connection, and note the victim's State, district and nearest police station.
- A complaint can be filed where the victim is; a zero FIR is available under the BNSS. Check the State police cyber cell's current process.
- If the platform or funds are abroad, flag mutual legal assistance and hand to `extradition-mutual-legal-assistance-analyst`.

## Temporal gate

If any offence was committed before 1 July 2024, the IPC defines the offence, not the BNS. Map it with `ipc-bns-concordance-mapper`. Procedure for a complaint or FIR registered on or after 1 July 2024 is generally under the BNSS, while proceedings already pending continue under the CrPC; confirm current authority on the BNSS savings clause with `crpc-bnss-transition-analyst`.

## Required inputs

**Blocking**:
- date and time of each event and of discovery;
- what happened, in the victim's words;
- for fraud, each transaction (date, time, amount, UTR or reference, from and to account or UPI ID, bank);
- for image abuse or harassment, the platform, profile links and URLs, without the images themselves.

Also useful: chats, emails with headers, call logs, app names and download links, and any complaint number already generated.

## Method

1. Retrieve the current official text of the IT Act offences and the BNS provisions in play, the portal's current complaint categories and limits (cybercrime.gov.in), and the RBI rules on customer liability for unauthorised electronic transactions. Record version and date.
2. Urgent steps for financial fraud: call 1930 or file on the portal at once, then write to the victim's bank asking it to block the instrument, raise a dispute, and request freezing of beneficiary accounts. Note the RBI reporting window that limits customer liability (believed to be three working days for zero liability; confirm).
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Build a chronology and a transaction table from the documents only.
4. Map facts to offences, for example identity theft, cheating by personation, privacy violation, obscene or sexually explicit material, cheating, extortion, stalking and defamation. State each section as "believed to be"; confirm from the text.
5. Draft the portal complaint text within the portal's limits, and a fuller police complaint with annexures.
6. Draft a bank letter (block, dispute, freeze, preserve KYC and transaction logs) and platform requests (takedown, account suspension, data preservation). For intimate images, cite the short takedown period in the IT Rules (reported as 2 hours after the 2026 amendment; confirm).
7. Evidence list: screenshots with visible URLs, dates and times; exported chats; email headers; bank statements; device details. Ask that original devices be kept unaltered. Hand the certificate to `bsa-electronic-evidence-certificate-drafter`.
8. If police do not register an FIR, set out escalation to senior officers and the Magistrate route, and hand to `criminal-complaint-drafter`.
9. Protect the victim: ask for identity protection where the law provides it, and suggest safety steps (passwords, two-factor, SIM checks).

## Output

1. Urgent action list with timings.
2. Portal complaint text and police complaint.
3. Bank letter and platform requests.
4. Evidence checklist and annexure index.

## Guardrails and hand-offs

- Never include, describe in detail or attach intimate images. Refer to them by URL and date only.
- Never promise recovery of money.
- Never advise the victim to contact, threaten or "hack back" the offender.
- A company-side data breach goes to `data-breach-response-planner`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
