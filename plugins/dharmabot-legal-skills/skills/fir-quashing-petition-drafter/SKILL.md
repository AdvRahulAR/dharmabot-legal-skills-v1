---
name: fir-quashing-petition-drafter
description: Assesses and drafts High Court petitions to quash an FIR, chargesheet, complaint or summoning order under the inherent powers saved by the Bharatiya Nagarik Suraksha Sanhita, 2023 (formerly s.482 CrPC) or Article 226, on abuse of process, no offence disclosed, civil dispute or settlement. Use when a client wants an FIR quashed, needs a no-coercive-action prayer, or has settled with the complainant. Do not use when the case has reached the charge stage and discharge is the right remedy; use discharge-application-drafter.
---

# FIR Quashing Petition Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Decide whether quashing is the right remedy, and if so draft a petition that shows, from the prosecution's own case, why continuing would be an abuse of process.

## Jurisdiction gate

Confirm the FIR or complaint is pending in India and identify the High Court with jurisdiction over the police station or court. Record the High Court's rules on criminal petitions, index, synopsis and affidavit. If a special statute bars or limits the inherent power, flag it.

## Temporal gate

Record the FIR date and the date of filing. For FIRs or petitions from before 1 July 2024, check whether the CrPC or BNSS applies to the petition with `crpc-bnss-transition-analyst`.

## Required inputs

**Blocking**: the FIR or complaint; the stage (investigation, chargesheet filed, cognizance, charge framed); any earlier quashing or bail order; and the ground relied on.

For settlement: the compromise deed, affidavits of the complainant and the offences involved. For a civil-dispute plea: the contract, correspondence and any civil suit or arbitration.

## Method

1. Retrieve the current official text of the BNSS provision saving the High Court's inherent powers (believed to be s.528; confirm), Article 226, the offences alleged, and the High Court's rules. Record source and date.
2. Read the FIR as true on its face. For each offence, test whether its ingredients appear. Use `fir-ingredients-analyst` where the analysis is long.
3. Choose the grounds that fit, for example the categories in State of Haryana v. Bhajan Lal (Supreme Court, 1992) and, for settlement of non-compoundable offences, Gian Singh v. State of Punjab (Supreme Court, 2012). Confirm current treatment and read later authority before citing.
4. Test the civil-dispute argument against the record: was there dishonest intention at the start of the transaction, or only a later breach?
5. Check the stage. After charges are framed, the court may expect discharge or revision; after evidence begins, quashing is harder. Say which remedy fits better.
6. Flag heinous or serious offences, offences against society, and special statutes where settlement-based quashing is unlikely.
7. Draft interim prayers: stay of investigation or proceedings, or no coercive action, with grounds for urgency.
8. Search for and cite current Supreme Court and jurisdictional High Court authority, read in full. Tag the rest `[verify]`. Hand off to `citation-verifier`.

## Output

1. A remedy note: quashing, discharge or another route, with reasons.
2. The petition: synopsis and list of dates, facts, grounds, interim application, prayer and affidavit.
3. An annexure index and a note of weak points the State will raise.

## Guardrails and hand-offs

- Never contest disputed facts by defence evidence the court cannot consider at this stage; flag it instead.
- Never misstate the FIR's contents.
- Never promise a stay or quashing.
- Hand off layout to `court-pleading-formatter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
- Tag [verify] on every case cited that was not read in full, not only some; if no case was read, tag all of them, including Bhajan Lal and Gian Singh, and do not cite from memory without the tag.
- Mark every section, article, rule number and period as believed and to be confirmed against the official text, in tables, headings and drafted letters as well as in notes, and tag [verify] anything not checked against a primary source. A closing disclaimer alone is not enough.
