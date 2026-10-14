---
name: uae-difc-adgm-law-mapper
description: Maps which UAE regime applies to an India-UAE matter (federal onshore law and courts, DIFC and ADGM common-law courts and their laws, DIAC arbitration) for contracts, company set-up, employment, data protection and debt recovery, and links it back to India through the UAE's reciprocating-territory status under s.44A CPC, the India-UAE CEPA and BIT, and attestation chains. Use when a Dubai or Abu Dhabi party owes an Indian client money, or a client is setting up or contracting in the UAE. Do not use for the enforcement analysis in India; use foreign-judgment-award-enforcement-analyst.
---

# UAE, DIFC and ADGM Law Mapper

Every output is a draft for an advocate enrolled in India to check. UAE-law points are for UAE-qualified counsel to confirm.

## Purpose

Work out which UAE legal system and forum govern each issue, and what that means for recovery and enforcement in India.

## Jurisdiction gate

For each issue, identify:
- where the counterparty is incorporated (mainland, a free zone, DIFC, ADGM);
- the governing-law clause and dispute clause (courts, which courts, arbitration seat and institution);
- where the assets are (UAE, India, elsewhere).
Onshore courts work in Arabic under civil law; DIFC and ADGM courts are common-law courts in English. Mark every UAE-law conclusion "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the contract, with the governing-law and dispute clauses;
- the counterparty's legal name and licence details (mainland, free zone, DIFC or ADGM);
- the claim amount and supporting documents;
- where the counterparty has assets.

Also useful: correspondence, cheques or guarantees, and any proceedings already started.

## Method

1. Retrieve the current official text of the relevant UAE laws (UAE Legislation portal), DIFC and ADGM laws and court rules, DIAC rules, and India's s.44A notification for the UAE. Record versions and dates. Open `references/foreign-jurisdictions.md` for the India-UAE position, attestation and sources.
2. Identify the competent court. A DIFC-law choice alone may not give the DIFC Courts jurisdiction over a mainland party; check the opt-in rules and current authority. If arbitration applies, check the institution after the 2021 changes to Dubai arbitration centres.
3. Map recovery options: onshore payment order or claim, DIFC or ADGM small claims or full claim, arbitration, and cheque-related remedies. Note language and translation costs onshore.
4. Map other issues if raised: company set-up (mainland or free zone), employment (federal labour law or DIFC or ADGM employment law), and data protection (UAE PDPL, DIFC and ADGM data laws; check the current regulator).
5. Link back to India:
   - UAE court judgments: the UAE is a reciprocating territory, with the notified courts listed in the Gazette; execute under s.44A CPC, subject to s.13.
   - UAE-seated arbitral awards: the UAE was not notified as a New York Convention territory under section 44 of the Arbitration and Conciliation Act at the last check (reported as of 2025). Check the Gazette now; if still not notified, plan alternatives (for example suing on the award or the underlying claim, or a seat change in future contracts).
   - Investment claims: check the India-UAE BIT and CEPA provisions.
6. Plan documents: attestation chain (the UAE is not believed to be an Apostille Convention party; confirm on the HCCH status table), translations into Arabic, and powers of attorney. Hand off to `document-legalisation-planner`.

## Output

1. A regime map: issue · governing law · forum · reasons · points for UAE counsel.
2. A recovery and enforcement route chart, UAE to India.
3. A document and attestation checklist.

## Guardrails and hand-offs

- Never present UAE law as settled; UAE counsel confirms.
- Confirm the s.44A CPC and section 44 Arbitration Act notifications from the Gazette before relying on them.
- For arbitration strategy, hand off to `international-arbitration-planner`.
- For enforcement in India, hand off to `foreign-judgment-award-enforcement-analyst`.
