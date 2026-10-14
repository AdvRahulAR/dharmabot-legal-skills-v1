---
name: foreign-judgment-award-enforcement-analyst
description: Analyses how to enforce a foreign court judgment or arbitral award in India, or an Indian judgment or award abroad (US, UK, UAE including DIFC and ADGM, EU, Singapore and others). Covers the reciprocating-territory route under s.44A CPC, the s.13 CPC conclusiveness tests, a fresh suit on a judgment, Part II of the Arbitration and Conciliation Act for New York Convention awards, defences, limitation and the court with jurisdiction. Use when a client holds a foreign decree or award against an Indian party, or an Indian decree or award against someone abroad. Do not use for domestic Indian decrees or awards.
---

# Foreign Judgment and Award Enforcement Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Choose the correct enforcement route, test the defences the other side will raise, and set out the steps, forum and deadlines.

## Jurisdiction gate

Identify the country and court (or arbitral seat) where the judgment or award was made, and where enforcement is sought. For enforcement in India, this skill applies Indian law. For enforcement abroad, it gives a structured overview only and marks every point for confirmation by local counsel.

## Required inputs

Mark as **blocking**:
- the judgment or award, with the date, court or tribunal, and seat;
- the parties;
- where the debtor's assets are;
- whether the judgment or award is final, and any appeals or set-aside proceedings anywhere.

Also useful: the underlying contract, proof of service in the original proceedings, whether the debtor appeared, and amounts and interest.

## Method

1. Read `references/foreign-jurisdictions.md`, then retrieve the current official text of the provisions used below and the current Gazette notifications. Every section number in this skill is believed to be correct but must be confirmed against the official text.
2. **Classify the instrument, then use one track only.** Decide whether the client holds a foreign court judgment (track A) or a foreign arbitral award (track B). If the client holds both (for example an award and a seat-court judgment on it), analyse each in its own track and keep the conclusions separate. The s.44A CPC reciprocating-territory list and the s.44 Arbitration Act New York Convention notification list are different. Never use one to answer a question about the other. Within a track, do not discuss the other track's list or routes unless the client also holds that other kind of instrument.

### A. Foreign court judgments (CPC s.44A / s.13)

3. **Reciprocating-territory check (s.44A CPC list only).** Retrieve the current s.44A notifications and check that the specific court that gave the judgment is covered, not just the country.
   - UAE courts, believed to include the DIFC Courts and ADGM Courts, were notified as a reciprocating territory under s.44A (believed January 2020) [verify]. Whether the UAE is a notified seat under s.44 of the Arbitration Act is irrelevant to a UAE court judgment.
   - s.44A covers money decrees only, not sums payable for taxes, fines or penalties [verify] (always tag this [verify] in the response). Check that the judgment is for a sum of money of the kind covered.
4. **Route.**
   - **Reciprocating territory** (for example the UK, Singapore, the UAE): execution as if an Indian decree under s.44A CPC, by filing a certified copy in a District Court, subject to the exceptions in s.13 CPC (sections believed to be as stated; confirm against the official text).
   - **Not a reciprocating territory** (for example the US and EU member States): file a suit on the judgment, or on the original cause of action. The judgment is conclusive only if none of the s.13 exceptions applies.
5. **Section 13 CPC tests.** Test each exception separately against the record, and look for presumptions under s.14 (both believed to be the sections; confirm against the official text):
   - competent jurisdiction;
   - decision on the merits (watch default judgments);
   - incorrect view of international law or refusal to recognise Indian law;
   - natural justice;
   - fraud;
   - breach of Indian law.

   Search for and read current Supreme Court authority on each test that is in play. Tag anything not read in full `[verify]`.
6. **Limitation for track A.** Do not choose the limitation article yourself. Hand the period to `limitation-calculator` (naming it in the response), and give only the dates computed with `scripts/date_calc.py` and the options for the advocate to confirm.

### B. Foreign arbitral awards (Arbitration and Conciliation Act Part II, s.44 notified countries)

7. **Notified-seat check (s.44 New York Convention list only).** Retrieve the current notifications under s.44 of the Arbitration and Conciliation Act, 1996 and check whether the seat of the arbitration is in a notified country. The s.44A CPC list says nothing about this.
   - The UAE was not a notified s.44 seat at the last check [verify]. Retrieve the current notifications before relying on this.
8. **Route.**
   - **Notified seat:** apply under Part II, in the High Court with jurisdiction, and test the s.48 grounds for refusal narrowly (sections believed to be as stated; confirm against the official text).
   - **Seat not notified:** the award cannot be enforced under Part II. Explain the alternatives, chiefly a suit on the award [verify]. Explanation 2 to s.44A CPC is believed to exclude an arbitration award from "decree" even where the award is enforceable as a decree [verify]. Always write this as believed and tag it [verify] wherever it appears in the response, so whether a seat-court judgment that confirms or incorporates the award can be executed under s.44A is doubtful [verify]. Present that only as a contested option, with the risk stated, and analyse any such judgment separately under track A.
9. **Limitation for track B.** Do not choose the limitation article yourself. Hand the period to `limitation-calculator` (naming it in the response), and give only the dates computed with `scripts/date_calc.py` and the options for the advocate to confirm.

### Common steps

10. **Dates.** Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead. Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
11. **Indian judgment or award abroad.** Outline the likely route in the target country, mark every point for local counsel, and list the documents to prepare. These usually include certified and legalised copies (hand off to `document-legalisation-planner`), translations (hand off to `legal-translation-verifier`), proof of service, and proof of finality.
12. **Interim protection.** Consider attachment before judgment, or s.9 relief for foreign-seated international commercial arbitrations under the proviso to s.2(2) (believed to be the provisions; confirm against the official text), unless the parties excluded it. Check current authority where both parties are Indian [verify].

## Output

1. Which track applies (A, B or both, kept separate), and the recommended route, with reasons and alternatives.
2. A defence table: ground · facts · assessment · evidence needed.
3. Forum, documents, steps and timeline.
4. Points for local counsel abroad.

## Guardrails

- If a blocking input is missing, ask for each one by name (the judgment or award, court or seat, country, finality and where the debtor's assets are) before giving a substantive answer.
- Confirm the reciprocating-territory and New York Convention lists from the Gazette before relying on them.
- Mark every section number and period as believed and to be confirmed against the official text, in tables and headings as well as notes.
- Never use the s.44A CPC reciprocating-territory list to answer a question about an arbitral award, or the s.44 Arbitration Act notification list to answer a question about a court judgment.
- Never cite a judgment you have not read; tag uncertain authority `[verify]`.
- Do not advise on foreign law as if qualified there.
