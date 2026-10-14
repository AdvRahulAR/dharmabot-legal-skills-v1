---
name: section-34-37-award-challenge-drafter
description: Assesses and drafts a challenge to a domestic arbitral award under section 34 of the Arbitration and Conciliation Act, 1996, or an appeal under section 37, or a reply resisting one, mapping each finding against the statutory grounds including public policy and patent illegality, the strict limitation period and stay of enforcement. Use when a client lost an arbitration and asks whether to challenge, or the award-holder needs to oppose a set-aside petition or appeal. Do not use to enforce a foreign award; use foreign-judgment-award-enforcement-analyst instead.
---

# Section 34 and 37 Award Challenge Drafter

Every output is a draft for an advocate enrolled in India to check, sign and file.

## Purpose

Tell the client honestly whether a challenge has a real ground, and draft the petition, appeal or reply within time.

## Jurisdiction gate

Confirm the award was made in an arbitration seated in India. Identify the court with jurisdiction under the Act and the Commercial Courts Act, 2015 (High Court original side or Commercial Court). Foreign awards go to `foreign-judgment-award-enforcement-analyst`. Note whether the arbitration is an international commercial arbitration, because the patent-illegality ground is believed to be unavailable then.

## Temporal gate

Record the date the signed award was received by the party (not merely issued), and the date of any section 33 correction or interpretation request. Limitation runs from these dates. If the award was received more than three months ago, flag the condonation limit at the top.

## Required inputs

Mark as **blocking**:
- the award, the date of receipt and how it was received;
- the pleadings and key procedural orders;
- who the client is (award-debtor or award-holder) and the stage (section 34, section 37, or reply);
- any section 33 application and its outcome.

Also useful: hearing transcripts, evidence relied on, and whether enforcement or execution has begun.

## Method

1. Retrieve the current official text of sections 34, 36 and 37 of the Arbitration and Conciliation Act, 1996, the Commercial Courts Act, 2015, and the court's rules. Record the version and date. Confirm every section, rule and article number used in this skill against that official text before relying on it.
2. **Limitation.** The period is believed to be three months from receipt, extendable by up to thirty days on sufficient cause and no further. Confirm from the text and compute with `limitation-calculator`. Section 37 appeals carry their own period; confirm from the Commercial Courts Act and current authority.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
3. **Map the award.** Build a table of every finding: issue · finding · evidence relied on · paragraph.
4. **Test grounds narrowly.** Incapacity; invalid agreement; lack of notice or inability to present the case; matters beyond the reference; improper composition or procedure; non-arbitrability; conflict with public policy (fraud or corruption, fundamental policy of Indian law, basic notions of morality or justice); and, for domestic awards only, patent illegality on the face of the award. Explain that courts do not re-appreciate evidence or reinterpret the contract where a view is possible.
5. Search for and read current Supreme Court authority on each ground in play, and on the court's power to modify or sever an award. Tag anything not read in full `[verify]`.
6. **Stay.** Filing does not stay enforcement automatically. Draft a separate stay application with a deposit or security offer and the conditions courts usually impose.
7. **Draft.** Petition or appeal: synopsis, list of dates, grounds tied to award paragraphs, prayer, stay application, affidavit and annexures. For a reply, rebut each ground with record references and the limits on interference.

## Output

1. A merits note: ground · award paragraph · assessment (strong, arguable, weak) · reason.
2. The draft petition, appeal or reply, and the stay application where needed.
3. A limitation and filing note with the last safe filing date.

## Guardrails and hand-offs

- Never present re-arguing the merits as a ground.
- Never guarantee a set-aside or a stay.
- Never invent authority; run `citation-verifier` before delivery.
- After the challenge fails or time expires, enforcement goes to `execution-contempt-petition-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
