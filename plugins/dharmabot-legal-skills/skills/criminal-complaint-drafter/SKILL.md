---
name: criminal-complaint-drafter
description: Drafts victim-side criminal complaints under the Bharatiya Nyaya Sanhita and Bharatiya Nagarik Suraksha Sanhita, 2023, including a written complaint to the police, a complaint to the Superintendent of Police, a Magistrate application to direct investigation, a private complaint, a protest petition and a victim compensation application. Use when police refuse to register an FIR, a client wants to file a private complaint, or a closure report must be opposed. Do not use to test whether facts make out an offence; use fir-ingredients-analyst for that.
---

# Criminal Complaint Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Turn a victim's account and documents into a complaint that pleads each ingredient of each offence, with dates and evidence, in the right sequence of remedies.

## Jurisdiction gate

Confirm the offence occurred, or its consequence ensued, in India. Record the State, district and police station with territorial jurisdiction. Ask whether a special statute applies (for example NI Act, POCSO, SC/ST (Prevention of Atrocities) Act, IT Act, GST). Special statutes may fix the forum, the complainant or a sanction requirement.

## Temporal gate

Record the date of each act. If any act is before 1 July 2024, the IPC and CrPC may govern the offence or the steps; run `crpc-bnss-transition-analyst` first. Use `ipc-bns-concordance-mapper` to map old and new provisions.

## Required inputs

**Blocking**: a dated narrative of what happened; who the accused are and what each did; the place; documents and witnesses for each fact; and what has been tried so far (police station visit, written complaint, SP complaint, any receipt or refusal).

Also useful: loss amounts with proof, any civil proceedings on the same facts, prior settlement talks, and the complainant's preferred language.

## Method

1. Retrieve the current official text of the BNS offences, the BNSS provisions on information to police, complaint to the Superintendent of Police, Magistrate-directed investigation and private complaints, any State amendment and the victim compensation scheme of the State. Believed provisions are BNSS s.173 (information and SP complaint), s.175(3) (Magistrate) and s.223 (private complaint); confirm each number and its current wording. Record the source and date.
2. Identify each offence that the facts support. For each, list its ingredients and map one fact and one item of evidence to each ingredient. Drop any offence whose ingredients are not supported.
3. Check whether the offence is cognizable. For non-cognizable offences the route differs; say so.
4. Check for a preliminary inquiry. The BNSS allows a preliminary inquiry for some offences by punishment range; confirm the range and note it in the complaint.
5. Sequence the remedies: written complaint to the station; then complaint to the Superintendent of Police; then the Magistrate application, supported by an affidavit and proof of the earlier steps. Search for and read current Supreme Court guidance on the affidavit and prior-approach requirements; tag anything unread `[verify]`.
6. For a private complaint, plan the pre-cognizance hearing of the accused if the BNSS proviso requires it, and the list of witnesses.
7. For a protest petition, address the closure report point by point from the case diary extracts and record.
8. For victim compensation, identify the State scheme, the authority (DLSA or SLSA) and documents needed.
9. Hand off citation checking to `citation-verifier` before delivery.

## Output

1. The complaint or application, with cause title, facts in numbered paragraphs, offence-ingredient table, prayer and verification or affidavit.
2. A list of annexures, marked to each paragraph.
3. A note to the advocate: offences dropped and why, gaps in proof, and the next step if this remedy fails.

## Guardrails and hand-offs

- Never add facts, offences, amounts or witnesses not in the instructions.
- Never frame a purely civil dispute as a criminal one; flag the risk of a quashing petition and costs.
- Do not threaten prosecution to extract payment.
- Protect the identity of victims of sexual offences and children.
- For a translation, hand off to `regional-language-legal-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
