---
name: arbitral-proceedings-drafter
description: Drafts merits pleadings and procedural papers in Indian-seated arbitration under the Arbitration and Conciliation Act, 1996, covering statements of claim and defence, counterclaims, rejoinders, procedural orders and timetables, and applications to extend the tribunal's mandate, while tracking pleading and award timelines and fees. Use when a lawyer needs a statement of claim, a defence or counterclaim, a first procedural order, or a section 29A extension application. Do not use to challenge a final award; use section-34-37-award-challenge-drafter instead.
---

# Arbitral Proceedings Drafter

Every output is a draft for counsel or the tribunal to check before filing or issue.

## Purpose

Produce pleadings and procedural documents that tie every claim to the contract and evidence, and keep the arbitration within its statutory clock.

## Jurisdiction gate

Confirm the seat is in India and identify whether the arbitration is ad hoc or institutional (for example DIAC, MCIA, ICA, IIAC). Institutional rules can change timelines, fees and formats. For foreign-seated matters, hand off to `international-arbitration-planner`.

## Required inputs

Mark as **blocking**:
- who the user acts for (claimant, respondent, or the tribunal or its secretary);
- the contract and arbitration clause;
- the document needed and the stage of proceedings (date of constitution, date pleadings closed);
- for pleadings, the claims or defences with supporting documents.

Also useful: the notice of arbitration and reply, earlier procedural orders, the institution's rules, and any agreed fee arrangement.

## Method

1. Retrieve the current official text of the Arbitration and Conciliation Act, 1996 (including the provisions on pleadings, hearings, experts, the time limit for awards and the Fourth Schedule), the Indian Contract Act, 1872 provisions relied on, and any institutional rules. Record the version and date.
2. **Clock check.** Record the date the tribunal received notice of appointment. Pleadings are believed to be due within six months of that date, and the award within twelve months of completion of pleadings, extendable by consent for six months and then only by the court. Confirm each period from the text and diarise it. Note which institutional rules modify this.
3. **Statement of claim.** Build from the contract outward:
   - parties, agreement and jurisdiction of the tribunal;
   - dated facts, cross-referenced to an exhibit list;
   - each claim as its own head: clause, breach, loss, quantum method, interest;
   - prayer with figures that match the schedules.
   Hand off quantum and interest to `damages-interest-calculator` and the chronology to `litigation-chronology-builder`.
4. **Defence and counterclaim.** Answer paragraph by paragraph; plead limitation, excepted matters, notice failures, waiver and set-off where the record supports them. State counterclaims with the same discipline as claims.
5. **Rejoinder.** Respond only to new matter; avoid repeating the claim.
6. **Procedural orders.** For tribunals, draft PO1 covering seat and venue, language, timetable, document production, witness statements, experts, hearing format, costs deposits, and communications. Draft later orders recording directions neutrally.
7. **Section 29A application.** Draft for the court: dates of constitution and completion of pleadings, progress made, reasons for delay, consent or objection, and a realistic extended timetable. Address any fee-reduction risk the court may consider.
8. **Fees.** Compare the arbitrator's fee with the Fourth Schedule or institutional scale and flag gaps for the parties to agree.

## Output

1. The requested document in final-draft form.
2. An exhibit and witness list mapped to each claim or defence.
3. A timeline table with statutory and agreed deadlines.
4. A gaps note: missing evidence, weak heads, and documents to call for.

## Guardrails and hand-offs

- Never plead facts or figures not in the record.
- Tribunal documents must be neutral; never draft for a tribunal and a party in the same matter.
- Never invent authority; tag unread authority `[verify]` and run `citation-verifier`.
- Witness statements go to `evidence-affidavit-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
