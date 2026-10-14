---
name: plaint-drafter
description: Drafts a plaint under Order VII of the Code of Civil Procedure for Indian civil courts and Commercial Courts, covering cause title, pecuniary, territorial and subject-matter jurisdiction, cause of action, limitation, valuation, court fee, reliefs and verification, with Commercial Courts Act additions. Use when an advocate asks to draft a plaint, suit for recovery, suit for declaration or injunction, or commercial suit. Do not use for summary suits under Order XXXVII; use summary-suit-order-xxxvii-drafter instead.
---

# Plaint Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Turn confirmed facts and documents into a plaint that satisfies Order VII CPC, survives an Order VII Rule 11 challenge, and lists everything needed for filing.

## Jurisdiction gate

Confirm Indian law governs and identify the State, district and court. Check for an arbitration clause or exclusive jurisdiction clause, and for any statute that bars civil court jurisdiction (for example RERA, DRT, consumer or tenancy laws). If the suit is a commercial dispute of specified value, apply the Commercial Courts Act and run `commercial-suit-filing-checker`.

## Required inputs

Mark as **blocking**:
- the parties' full names, descriptions and addresses;
- a confirmed statement of facts with dates;
- the key documents (contract, invoices, correspondence, notices);
- the reliefs sought and their amounts;
- the place where the cause of action arose and where defendants reside or work.

Also useful: the client's prior notice and reply, any interim relief needed, and the suit valuation the client prefers.

## Method

1. Retrieve the current official text of the CPC (Order VI, VII, and the jurisdiction sections), the Commercial Courts Act and its schedule amendments to the CPC, the State court fees and suits valuation law, and the High Court's civil rules. Record the version and date. Confirm every section, order and rule number used in this skill against that text.
2. Fix jurisdiction in three parts: pecuniary (value against the court's limit as currently notified), territorial (defendant's residence or cause of action), and subject-matter (no statutory bar).
3. Compute limitation from the right article with `limitation-calculator`. Plead acknowledgments or part-payments that extend time.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
4. Value the suit and compute court fee with `state-court-fee-calculator`. Quantify money claims and interest with `damages-interest-calculator`.
5. Draft: cause title; numbered paragraphs of material facts (not evidence or law); cause of action and when it arose; jurisdiction; limitation; valuation and court fee; a statement that no other suit is pending on the same cause, if true; reliefs, each specific; verification.
6. In a commercial suit, add the statement of truth, the documents disclosure affidavit and the s.12A mediation statement or the urgency case.
7. Prepare a list of documents with originals or copies, and the persons whose evidence is likely.
8. Search for and read current authority only where a legal point is pleaded. Tag anything not read in full `[verify]`.

## Output

1. The draft plaint with verification and, if commercial, the statement of truth.
2. A list of documents and an index.
3. A filing note: court fee, limitation, interim applications to file, and open factual gaps.

## Guardrails and hand-offs

- Never plead a fact the client has not confirmed. Put unconfirmed points in the filing note.
- Never invent citations, amounts or dates.
- Interim relief: `interim-injunction-application-drafter`.
- Formatting to court rules: `court-pleading-formatter`.
- Before filing a commercial suit, run `commercial-suit-filing-checker`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
