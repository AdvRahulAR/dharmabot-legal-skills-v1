---
name: bsa-electronic-evidence-certificate-drafter
description: Prepares the certificate for admitting an electronic record (WhatsApp chats, emails, CCTV footage, call records, screenshots, documents on a computer or phone) under the Bharatiya Sakshya Adhiniyam, 2023, with a device and hash schedule, and checks it against the statutory requirements. Use when an advocate or party must produce electronic evidence in an Indian court or asks for a "section 63 certificate" or "65B certificate". Do not use for analysing what the evidence proves.
---

# BSA Electronic Evidence Certificate Drafter

Every output is a draft for an advocate enrolled in India to check. The certificate is signed by the person who can truthfully certify it, not by the AI.

## Purpose

Draft a certificate that meets the statutory requirements for secondary evidence of an electronic record, describe the record precisely, and record hash values so its integrity can be checked.

## Jurisdiction gate

Confirm the proceeding is before an Indian court or tribunal and note whether it is civil or criminal.

## Temporal gate

The BSA came into force on 1 July 2024. If evidence is being produced in a proceeding that may still be governed by the Indian Evidence Act (believed to be section 65B; confirm against the official text), run `crpc-bnss-transition-analyst` or ask the advocate which statute the court applies, and draft under that statute.

## Required inputs

Mark as **blocking**: a description of each electronic record (type, file name, date and time range, source application); the device or system it was produced from (make, model, owner, who controlled it and how it was used in the ordinary course); who will sign and in what capacity (the person in charge of the device, and an expert where the statute requires one); and how the copy was made (export, screenshot, download, forensic image).

Also useful: hash values already computed, chain-of-custody notes, and the court's format.

## Method

1. Retrieve the official text of the BSA provision on admissibility of electronic records (believed to be section 63) and the certificate format in its Schedule, including whether the format has separate parts for the party and for an expert. Confirm from the source. Also search for, read and apply current Supreme Court and High Court authority on the certificate: on hash values, and on who is competent to sign the expert part. Cite it, or mark it `[verify]` if not read in full.
2. Check each statutory condition against the facts supplied: the device was regularly used; information was regularly fed in during the ordinary course; the device was operating properly, or any defect did not affect the record; and the copy reproduces the information. List any condition the facts do not support.
3. Draft the certificate in the statutory format, filled in only with facts supplied. Use placeholders such as `[DEVICE SERIAL NUMBER]` for anything missing; never invent it.
4. Prepare a schedule of records: item number · description · file name · size · hash algorithm · hash value · date and time · source device.
5. If hash values are not supplied, explain how to compute them (for example SHA-256 with a standard tool) and leave the column for the signer to complete. Do not make up hash values.
6. Add a short chain-of-custody note: who copied what, when, onto which medium, and where it has been kept.

## Output

1. Draft certificate(s) in the statutory format.
2. The schedule of records.
3. A checklist of conditions met and not yet met.
4. Notes on who must sign and what they must personally verify before signing.

## Guardrails

- The signer must have personal knowledge. Say so prominently.
- Never fill in device details, dates, hash values or the signer's capacity from assumption.
- Do not claim that the evidence is admissible; admissibility is for the court.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
- Mark every section, article, rule number and period as believed and to be confirmed against the official text, in tables, headings and drafted letters as well as in notes, and tag [verify] anything not checked against a primary source. A closing disclaimer alone is not enough. This covers s.65B and its sub-clauses of the Indian Evidence Act and s.63 BSA and its sub-sections, in the checklist and in the certificate text.
- If the user asserts a statute or section for the certificate, do not adopt it; say which provision you believe applies, mark it to be confirmed against the official text, and ask which statute the court applies.
