---
name: criminal-trial-readiness-checker
description: Checks whether the defence is ready for a criminal trial in India under the Bharatiya Nagarik Suraksha Sanhita and Bharatiya Sakshya Adhiniyam, 2023, covering defence theory, prosecution witness order, admissibility objections, electronic evidence certificates, documents to summon, defence witnesses, the accused's examination and fallbacks. Use when trial starts soon, an advocate asks if the defence is ready, or wants a trial checklist with owners. Do not use for planning the questions for a particular witness; use cross-examination-planner.
---

# Criminal Trial Readiness Checker

Every output is a draft checklist for an advocate enrolled in India to check.

## Purpose

Find what is missing before trial and assign each item to a person and a date, while keeping the defence lawful and evidence-led.

## Jurisdiction gate

Confirm the trial is before an Indian court. Record the court, State, trial type and any special statute (for example NDPS, POCSO, PMLA) with reverse burdens or presumptions. Note the court's practice on day-to-day trials and video-conference evidence.

## Temporal gate

Record the dates of offence, chargesheet and charge. If any is before 1 July 2024, check with `crpc-bnss-transition-analyst` whether the CrPC and Indian Evidence Act or the new codes govern each step.

## Required inputs

**Blocking**: the charge as framed; the police report and its documents; the prosecution witness list; the trial date and stage; and the defence theory as the advocate sees it.

Also useful: bail conditions, earlier orders, the client's account, and any defence documents or experts.

## Method

1. Retrieve the current official text of the BNSS trial provisions for the trial type, the examination of the accused (believed to be s.351 BNSS; confirm), defence evidence, and the BSA provisions on admissibility, burden, presumptions and electronic records. Record source and date.
2. State the defence theory in two or three sentences. Test it against every prosecution witness and document. Flag any part that depends on facts the defence cannot prove lawfully.
3. Witness plan: for each prosecution witness, what they will prove, prior statements available for contradiction, and whether cross-examination is planned. Hand off question design to `cross-examination-planner`.
4. Objections: list documents and exhibits to object to (mode of proof, primary versus secondary evidence, electronic certificate defects, hearsay, confessions to police). Record each objection for the order sheet.
5. Documents and witnesses to summon: applications for production, expert evidence and official records, with time to serve.
6. Accused's examination: list incriminating circumstances likely to be put, and prepare truthful explanations from the record.
7. Defence evidence: decide whether to lead any, with witness availability and risks.
8. Fallbacks: lesser offence, compounding or plea bargaining where lawful, and sentencing material via `sentencing-mitigation-analyst`.
9. Search for authority only where an objection depends on it. Read it; tag anything unread `[verify]`.

## Output

1. A readiness checklist: item, status (ready, partial, missing), owner and due date.
2. A witness-by-witness table.
3. A list of objections and applications to file before or at trial.
4. A short risk note for the client meeting.

## Guardrails and hand-offs

- Never suggest coaching witnesses, fabricating documents or delaying for its own sake.
- Never invent record contents.
- Never predict the verdict.
- For record gaps, use `chargesheet-review-analyst`.
