---
name: section-11-appointment-petition-drafter
description: Drafts petitions under section 11 of the Arbitration and Conciliation Act, 1996 to a High Court (domestic) or the Supreme Court (international commercial arbitration) for appointment of an arbitrator after the agreed procedure fails, keeping to the limited prima facie existence inquiry and addressing limitation, unilateral-appointment clauses and arbitrator disclosures. Use when the other side ignored the arbitration notice, refused to appoint, or appointed someone ineligible. Do not use to review or repair the clause itself; use arbitration-clause-reviewer instead.
---

# Section 11 Appointment Petition Drafter

Every output is a draft for an advocate enrolled in India to check, sign and file.

## Purpose

Get an arbitrator appointed by the court quickly, without inviting a mini-trial on merits.

## Jurisdiction gate

Confirm the seat is in India. Decide the forum: for a domestic arbitration, the High Court with jurisdiction over the seat; for an international commercial arbitration, the Supreme Court. Check whether the clause names an arbitral institution and whether any designated institution scheme has been notified that changes the route. Confirm current position from the official text.

## Required inputs

Mark as **blocking**:
- the arbitration clause and the contract;
- the invocation notice, its date and proof of delivery;
- the respondent's reply or silence, and the time elapsed;
- the seat, and whether any party is foreign.

Also useful: the proposed arbitrator's details and disclosure, any earlier section 9 or section 11 orders, and the claim summary.

## Method

1. Retrieve the current official text of section 11 and the Fifth, Sixth and Seventh Schedules of the Arbitration and Conciliation Act, 1996, the High Court's or Supreme Court's arbitration rules and scheme, and the Limitation Act, 1963. Record the version and date.
2. **Failure of procedure.** Show exactly how the agreed procedure failed: no appointment within the agreed time or the statutory period, or a disagreement. Confirm the period from the text.
3. **Limitation.** Current Supreme Court authority is believed to apply a three-year period to the filing of the petition, running from failure to appoint after a valid notice. Confirm the article and authority, and hand off computation to `limitation-calculator`. Separately note that the underlying claims must not be ex facie dead.
4. **Scope of inquiry.** Draft on the basis that the court examines only the prima facie existence of an arbitration agreement. Search for and read recent Supreme Court authority on this (including the effect on stamping objections and "accord and satisfaction" pleas). Tag anything not read in full `[verify]`.
5. **Unilateral or ineligible appointment.** If the respondent appointed alone, or the clause gives one party control, plead ineligibility under section 12(5) and the Seventh Schedule where it applies, and the equality concerns addressed by the Supreme Court (for example Perkins Eastman, 2019, and the CORE Constitution Bench, 2024). Confirm current treatment and the effective date of those rulings.
6. **Institution.** If the clause names an institution that should appoint, flag it. The court may refer the matter there instead.
7. Draft the petition: cause title, parties, the agreement, chronology, failure of procedure, limitation, prayer for appointment (sole or presiding), suggested qualifications, fee note referring to the Fourth Schedule or the institution's rules, verification and affidavit.
8. Prepare a short disclosure checklist for the proposed arbitrator under the Sixth Schedule.

## Output

1. The draft section 11 petition with prayer.
2. Index of annexures and a list of dates.
3. A filing note: forum, court fee check, limitation status, and weak points to prepare for at the first hearing.

## Guardrails and hand-offs

- Do not argue merits beyond what is needed to show an arbitrable dispute.
- Never invent case names, citations or dates; run `citation-verifier`.
- Do not predict which arbitrator the court will appoint.
- If the clause itself is defective, return to `arbitration-clause-reviewer`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
