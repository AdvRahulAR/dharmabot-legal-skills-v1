---
name: superdari-property-release-drafter
description: Drafts applications for interim custody (superdari) and release of seized vehicles, cash, jewellery, phones and documents under the Bharatiya Nagarik Suraksha Sanhita, 2023, with ownership proof, photographs, panchnama, indemnity bond and undertaking to produce, and flags special-law bars under NDPS, excise, forest and PMLA laws. Use when police have seized a client's vehicle, phone, cash or gold and the client wants it back pending trial. Do not use for PMLA provisional attachment; use pmla-proceedings-analyst.
---

# Superdari and Property Release Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Get seized property back to its owner on terms that protect the evidence, before it rots in a police yard, and identify early when a special law bars release.

## Jurisdiction gate

Confirm the seizure was made in India in a criminal case. Record the State, police station, case number and the court with jurisdiction. Identify whether the seizure was under a special law (NDPS, State excise, forest, wildlife, customs, PMLA, mining). Many special laws have their own confiscation procedure that may bar the Magistrate's power; retrieve those provisions before drafting.

## Temporal gate

Record the date of seizure and of the FIR. If either falls before 1 July 2024, run `crpc-bnss-transition-analyst` to decide whether the CrPC or BNSS provisions apply.

## Required inputs

Mark as **blocking**:
- the FIR or complaint particulars and the offences alleged;
- the seizure memo or panchnama, with the date and description of the property;
- proof that the applicant owns or is entitled to the property (RC, invoice, bank record, purchase bill);
- whether any confiscation proceeding has started before another authority.

Also useful: photographs, insurance, hypothecation and financier details, and the investigation status.

## Method

1. Retrieve the current official text of the BNSS provisions on custody and disposal of property pending trial and on property seized by police (believed to be sections 497 and 503; confirm from the official text), any State rules, and the special law that applies. Record the source and date.
2. Check for a bar. If a confiscation proceeding is pending under a special law, note whether the Magistrate may still act and search for current authority.
3. Draft the application: case details, description of the property, the applicant's title, the date and circumstances of seizure, why custody with police serves no purpose, and the risk of deterioration.
4. Rely on settled guidance on early release of seized property, for example Sunderbhai Ambalal Desai v. State of Gujarat (Supreme Court, 2002); confirm current treatment and read later authority. Tag anything unread `[verify]`.
5. Propose conditions: photographs and video of the property, a detailed panchnama, an indemnity bond and surety, an undertaking to produce when required, and not to sell or alter it.
6. For phones and devices, address forensic imaging and data integrity before release.
7. For a third-party financier or joint owner, address their rights.

## Output

1. The superdari or release application with affidavit.
2. Draft indemnity bond and undertaking.
3. An annexure list (ownership proof, seizure memo, photographs).
4. A note on any special-law bar and the next forum if the Magistrate lacks power.

## Guardrails and hand-offs

- This skill does not handle bail.
- Never claim ownership facts not shown by documents.
- NDPS seizures go to `ndps-case-analyst`; PMLA attachment to `pmla-proceedings-analyst`; charge-sheet review to `chargesheet-review-analyst`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
