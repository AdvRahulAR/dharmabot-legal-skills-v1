---
name: court-pleading-formatter
description: Formats a pleading, petition, application, affidavit or appeal for filing before any Indian court or tribunal, from district courts to any of the 25 High Courts and the Supreme Court. Covers cause title, case-type naming, party array, synopsis and list of dates where required, index, verification, annexure numbering and a filing and e-filing checklist. Use when an advocate has the substance of a draft and needs it in the right court format. Do not use to decide what to plead.
---

# Court Pleading Formatter

Every output is a draft for an advocate enrolled in India to check before filing.

## Purpose

Put a draft into the form the chosen court expects, and list everything needed to file it, without changing its substance.

## Jurisdiction gate

Identify the court or tribunal, its State, and whether filing is physical or electronic. High Courts with benches may differ in practice between seats; confirm which seat or bench. For a forum outside India, stop. Foreign filings need local counsel.

## Required inputs

Mark as **blocking**:
- the draft text;
- the court, bench and case type, as that court names it (for example O.S., C.S., Civil Suit, Crl.M.C., CRM-M, W.P.(C), CWP, SLP(C), Bail Appln.);
- the parties with full descriptions;
- whether it is a fresh filing or in a pending case (with the case number).

Also useful: a recently filed document from the same court that the advocate considers correct. Follow it in preference to any general pattern.

## Method

1. Identify the rules that govern form and filing:
   - **Subordinate courts:** the State's civil and criminal rules of practice, or the High Court's general rules and orders for subordinate courts. See `references/india-state-statutes.md` for likely names.
   - **High Court:** the High Court's own rules, practice directions and e-filing instructions.
   - **Supreme Court:** the Supreme Court Rules, 2013, and current circulars.
   - **Tribunals:** their own procedure rules.

   Retrieve the current versions from the court's website and record them.
2. If the advocate supplied a model document, follow its layout, headings and standard wording. Note any point where it seems to differ from current rules.
3. Build the cause title: court, bench, case type and number (blank for a fresh filing), and parties with descriptions, numbers and status. Keep the party array identical across every document in the set.
4. Add the parts the forum requires for that case type. Typical examples are a synopsis and list of dates, index, memo of parties, urgency application, verification or affidavit, vakalatnama or memo of appearance, certificate of compliance, and translations of vernacular documents.
5. Number annexures in the forum's style (for example P-1, A-1, Annexure 1). Check that every annexure cited in the text is in the list, and every listed annexure is cited.
6. Check page and paper rules the court prescribes (paper size, margins, font, line spacing, bookmarking, OCR for e-filing).
7. Produce a filing checklist: copies, court fee (from `state-court-fee-calculator`), process fee, e-filing steps, and service of advance copies.
8. If asked, produce a `.docx` using the advocate's template; otherwise produce clean Markdown.

## Output

1. The formatted document.
2. A list of changes made (formatting only).
3. The filing checklist.
4. Points to verify against current court practice.

## Guardrails

- Never change facts, prayers or grounds while formatting. If something looks wrong, flag it.
- Where a requirement could not be confirmed from a current source, mark it `[verify]`.
