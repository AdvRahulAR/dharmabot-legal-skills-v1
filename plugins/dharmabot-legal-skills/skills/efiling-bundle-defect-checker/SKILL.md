---
name: efiling-bundle-defect-checker
description: Checks and compiles an e-filing paper book against the technical specifications of the Supreme Court, the High Courts and the eCourts eFiling portal, and maps each registry objection or defect memo to a precise fix and refiling deadline. Use when a registry has returned a petition with objections, when an advocate asks for a defect list or fix list, or before uploading a bundle (OCR, bookmarks, pagination, DSC). Do not use to format the cause title or party array; use court-pleading-formatter.
---

# E-Filing Bundle and Defect Checker

Every output is a review for an advocate enrolled in India to check before refiling.

## Purpose

Get a filing through scrutiny at the first or second attempt. Turn the registry's objection sheet into a numbered fix list, and check the whole bundle against the forum's current technical rules.

## Jurisdiction gate

Identify the forum (Supreme Court, which High Court and bench, or which district court on the eCourts eFiling portal) and the case type. Technical rules differ by court and change often. If the forum is a tribunal with its own portal, say so and use that tribunal's rules.

## Required inputs

Mark as **blocking**:
- the forum and case type;
- the objection sheet or defect memo, with its date (for a returned filing);
- the bundle itself, or a page-wise index if the PDF is not shared.

Also useful: the diary or filing number, the date of first filing, the court-fee receipt, and the advocate's DSC or e-sign details.

## Method

1. Retrieve the forum's current official e-filing guidelines, practice directions and registry rules from its website. Record the version and date. Take every specification from them, not from memory.
2. Build the check list from that source. Typical items: OCR-searchable text, page size and margins, font and line spacing, resolution and colour, maximum file size and splitting, bookmarks for each document, continuous pagination matching the index, annexure marking (for example P-1, R-1), legible true typed copies of dim or vernacular pages, translations, and DSC or e-sign on the right pages.
3. Read each registry objection. Classify it: technical (fixable here), substantive (the advocate must decide), fee, or limitation and delay.
4. Map each objection to the exact fix, the page affected and who does it. Do not alter the text of the pleading.
5. Find the refiling deadline in the court's rules for curing defects, and flag if a delay in refiling needs a condonation application. Confirm the period from the rules; do not assume it.
6. Hand court-fee objections to `state-court-fee-calculator` and cause-title or layout objections to `court-pleading-formatter`.
7. Run a final pass on the corrected bundle: index against pagination, bookmarks open the right page, every annexure is referred to in the pleading, and affidavits are attested and dated.

## Output

1. A fix table: objection · category · page · exact fix · owner · status.
2. A pre-upload checklist for the forum, with the source and date of each specification.
3. The refiling deadline and any delay note.
4. A covering letter for refiling, if wanted, through `registry-letter-drafter`.

## Guardrails and hand-offs

- Do not change the substance of a pleading to clear an objection. Flag substantive objections for the advocate.
- Never state a technical limit or refiling period as settled without the current source.
- Do not apply a DSC, e-sign or upload. The advocate or advocate-on-record does this.
- Keep client documents confidential and do not upload them to unapproved tools.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
