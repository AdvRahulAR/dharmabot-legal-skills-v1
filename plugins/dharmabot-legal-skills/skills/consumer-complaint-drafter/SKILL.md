---
name: consumer-complaint-drafter
description: Checks whether a complaint lies under the Consumer Protection Act, 2019 (consumer status, deficiency in service, defect, unfair trade practice, limitation, pecuniary limits by consideration paid and territory) and drafts the complaint for online filing in the District, State or National Commission, or the opposite party's written version. Use when an advocate asks to file a consumer case, consumer complaint, complaint against a dealer, bank, builder, insurer or hospital, or a reply to one. Do not use for appeals against commission orders; use consumer-appeal-drafter instead.
---

# Consumer Complaint Drafter

Every output is a draft for an advocate enrolled in India, or the complainant, to check before filing.

## Purpose

Decide whether a consumer complaint lies and where, then draft a complaint (or written version) that the Commission can admit and decide on the documents.

## Jurisdiction gate

Confirm the transaction is with a seller or service provider in India, and note the State and district. Check for a sector forum that may be more suitable or exclusive (for example RERA for real estate, the Banking or Insurance Ombudsman, TRAI and telecom, or a statutory arbitration). Note that an arbitration clause does not by itself bar a consumer complaint; confirm current authority.

## Temporal gate

The Consumer Protection Act, 2019 replaced the 1986 Act from 20 July 2020 (confirm). Check which Act governs if the cause of action or filing is older. Check the current pecuniary limits notified under the 2019 Act and the current e-filing portal (e-Jagriti has replaced e-Daakhil; confirm the current portal and its rules).

## Required inputs

Mark as **blocking**:
- the complainant's details and whether the goods or service were bought for personal use or for a commercial purpose;
- the bill, invoice, policy, agreement or receipt showing consideration paid;
- the defect or deficiency, with dates and evidence (job cards, emails, expert or test reports);
- the date the cause of action arose;
- for a written version, the complaint and the date of service of notice.

## Method

1. Retrieve the current official text of the Consumer Protection Act, 2019, the Consumer Protection (Jurisdiction of the District Commission, the State Commission and the National Commission) Rules as amended, the Consumer Commission procedure regulations, and the mediation regulations. Record the version and date.
2. Consumer status: test the commercial-purpose exclusion and the self-employment exception on the facts.
3. Cause: classify each grievance as defect, deficiency, unfair trade practice, restrictive trade practice, excess price, hazardous goods or product liability. Hand off product liability heads to `product-liability-analyst`.
4. Forum: pecuniary limit by consideration paid, not by compensation claimed; territorial options include the complainant's residence or place of work. Confirm both from the current text.
5. Limitation: two years from the cause of action, with condonation for sufficient cause (confirm). Use `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
6. Draft the complaint: parties; facts; defect or deficiency; legal basis; notice and reply; jurisdiction; limitation; reliefs (replacement, refund, repair, compensation, punitive damages where warranted, costs); verification and affidavit; document index.
7. State whether the complainant consents to mediation, and consider early settlement.
8. Opposite party's written version: preliminary objections, para-wise reply, defences, and documents. Calendar the strict time to file it; see New India Assurance Co Ltd v Hilli Multipurpose Cold Storage Pvt Ltd (Supreme Court, Constitution Bench, 2020) and confirm current treatment.
9. Check fees and filing requirements on the portal. Tag unread authority `[verify]`.

## Output

1. An eligibility and forum note.
2. The draft complaint with affidavit and index, or the written version.
3. A filing checklist and a list of missing evidence.

## Guardrails and hand-offs

- Never inflate compensation or invent losses.
- Never advise filing where the purchase was clearly commercial without flagging the risk.
- Legal aid screening: `legal-aid-eligibility-screener`. Appeals: `consumer-appeal-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
