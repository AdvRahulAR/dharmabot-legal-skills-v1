---
name: regulator-notice-reply-drafter
description: Analyses and drafts replies to show-cause notices, inspection reports, examination findings and information requests from Indian regulators such as SEBI, RBI, IRDAI, FSSAI, pollution control boards and labour authorities, covering jurisdiction, limitation and delay, natural justice, merits, mitigation, settlement or compounding options and hearing notes. Use when a client has received a show-cause notice, inspection observations or a regulator's letter and asks for a reply and hearing plan. Do not use for an appeal against a final order; use regulatory-appeal-planner instead.
---

# Regulator Notice Reply Drafter

Every output is a draft for an advocate enrolled in India to check and settle before filing.

## Purpose

Protect the client's position in the reply and the hearing, without admissions it does not need to make, and keep settlement options open.

## Jurisdiction gate

- Confirm the regulator, the statute and the officer issuing the notice, and that the notice is under Indian law.
- Check whether the officer has power under the provision cited, and whether proceedings in parallel (criminal, tax, another regulator) exist.

## Required inputs

**Blocking**:
- the notice with all annexures and its date of service;
- the deadline for reply and any hearing date;
- the client's documents on each allegation;
- whether any related criminal complaint, investigation or other proceeding exists.

Also useful: past correspondence with the regulator, earlier inspection reports, and internal reviews.

## Method

1. Retrieve the current official text of the statute, regulations and circulars cited in the notice, and the regulator's procedure regulations (for example SEBI adjudication and settlement regulations, RBI compounding guidance). Record version and date.
2. Diarise the reply deadline. If time is short, draft a request for inspection of documents and extension at once.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. List each allegation, the provision invoked, the evidence relied on, and documents not supplied.
4. Preliminary objections: jurisdiction and power, limitation or unexplained delay, vagueness, non-supply of relied-upon documents, and prejudgment. Search for and read current authority before relying on any; tag anything not read in full `[verify]`.
5. Merits: reply para by para with facts and documents. Admit only what is undisputed and necessary.
6. Mitigation: first lapse, corrective action, no investor or consumer loss, systems improved, cooperation.
7. Settlement or compounding: explain the route, timing and consequences (for example SEBI settlement applications have time windows; confirm). Flag that settlement terms may require admissions or disclosures.
8. Criminal exposure: flag any statement that could be used in a prosecution, and route the wording to senior counsel.
9. Hearing notes: key points, documents to carry, likely questions, and who attends.
10. Hand document preservation to `legal-hold-preservation-planner`. Before delivery, run citations through `citation-verifier`.

## Output

1. Draft reply with preliminary objections, para-wise reply, mitigation and prayer.
2. Letter seeking inspection of documents or extension, where needed.
3. Risk note: allegations ranked by exposure, admissions flagged, settlement option.
4. Hearing notes.

## Guardrails and hand-offs

- Never add facts or documents not supplied, and never backdate records.
- Never guarantee that the notice will be dropped.
- Never advise ignoring a statutory deadline.
- Appeals go to `regulatory-appeal-planner`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
