---
name: lost-document-reissue-planner
description: Plans and drafts the steps to replace lost originals in India, covering the police lost-document report, public notice, indemnity bond and affidavit, certified copies of registered deeds from the Sub-Registrar under the Registration Act, 1908, duplicate share certificates under the Companies (Share Capital and Debentures) Rules, 2014 and the RTA process, duplicate marksheets, degrees and vehicle RCs. Use when a client has lost a sale deed, share certificate, marksheet or RC in a flood, fire or theft. Do not use for a title opinion; use property-title-diligence-analyst.
---

# Lost Document Reissue Planner

Every output is a draft for an advocate enrolled in India to check before the client acts on it.

## Purpose

Give the client a sequenced plan and the draft papers to replace each lost original, and explain the legal effect of the loss.

## Jurisdiction gate

Confirm where each document was issued (State, Sub-Registrar office, company and RTA, board or university, RTO). Procedures differ by State and issuer. If an issuer is abroad, flag that its own law applies.

## Required inputs

Mark as **blocking**:
- a list of each lost document with its type, date, issuer and any number known;
- how and when it was lost (theft, fire, flood, misplacement);
- whether the property or shares are mortgaged or pledged, and to whom.

Also useful: photocopies or scans, the encumbrance certificate, folio numbers, and any court case involving the asset.

## Method

1. Retrieve the current official procedure for each issuer: the State police lost-report portal, the Registration Act, 1908 and State rules on certified copies, the Companies (Share Capital and Debentures) Rules, 2014 and current SEBI circulars on duplicate securities, the board or university rules, and the Motor Vehicles rules on duplicate RCs. Record the source and date.
2. Lodge the loss report first. Most authorities ask for it. Draft the narrative from the client's account only.
3. For title deeds:
   - obtain a certified copy from the Sub-Registrar; it is admissible secondary evidence, but explain that the original's loss can affect sale and loan;
   - draft a public notice for newspapers inviting claims;
   - draft an indemnity and affidavit, if a bank or buyer needs them;
   - check the encumbrance certificate with `encumbrance-certificate-analyst`.
4. For shares in unlisted companies, draft the request, indemnity and affidavit, and note the board's approval and time limits under the rules. For listed shares, follow the RTA and current SEBI process (for example issue in demat form). Flag if shares were moved to the IEPF; that needs a separate claim.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
5. For marksheets and degrees, draft the application to the board or university with the loss report and affidavit.
6. For vehicle RCs, prepare the duplicate application with the loss report and, if hypothecated, the financier's consent.
7. Sequence the steps and flag dependencies.

## Output

1. A replacement plan table: document · issuer · steps · papers · fee source · order.
2. Drafts: loss report narrative, public notice, indemnity bond, affidavits and request letters.
3. A risk note on title or ownership effects.

## Guardrails and hand-offs

- Do not give a title opinion; use `property-title-diligence-analyst`.
- Affidavit formalities go to `general-affidavit-drafter`.
- Never invent document numbers, dates or fees.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
