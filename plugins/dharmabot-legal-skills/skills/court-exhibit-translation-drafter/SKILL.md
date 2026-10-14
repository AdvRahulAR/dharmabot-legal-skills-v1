---
name: court-exhibit-translation-drafter
description: Prepares English translations of exhibits, records and orders written in Indian languages (Malayalam, Tamil, Hindi, Marathi, Bengali and others) for filing before the Supreme Court of India and High Courts, preserving names, numbers, survey and case numbers and layout, with the translator's certificate or affidavit the court's rules or registry require. Use when a lawyer says "translate these vernacular documents for the SLP", "English translation of the FIR and mahazar" or "true translation certificate". Do not use to check someone else's translation; use legal-translation-verifier instead.
---

# Court Exhibit Translation Drafter

Every output is a draft translation for an advocate enrolled in India and the translator to check before filing.

## Purpose

Produce faithful, filing-ready English translations of vernacular documents, in the form the target court's registry will accept.

## Jurisdiction gate

Identify the target court and its registry rules, the source language and script, and the State or UT the documents come from (which affects revenue and police terms). Note whether the court requires translation by an official translator or accepts a certified private translation.

## Required inputs

Mark as **blocking**:
- legible copies of each source document;
- the target court and case type;
- who will certify the translation (official translator, professional translator, or the advocate-on-record or advocate where permitted).

Also useful: an index of annexures with numbers, a glossary from earlier filings in the same matter, and the spellings of names already used in the pleadings.

## Method

1. Retrieve the current official text of the target court's rules and registry practice directions on translations (for the Supreme Court, the Supreme Court Rules, 2013 and registry circulars; for a High Court, its rules and e-filing directions). Record version and date. Confirm the certificate form from the source, not memory.
2. Open `references/india-state-statutes.md` to identify State revenue, police and land terms likely in the documents.
3. Translate in full, line by line. Do not summarise. Keep paragraph and page breaks, headings, tables and numbering.
4. Preserve exactly: names (transliterated consistently with the pleadings), dates, amounts in words and figures, survey, sub-division, crime, FIR and case numbers, and section references as written in the source.
5. Describe non-text matter in square brackets: [Seal], [Signature], [Thumb impression], [Stamp of the Village Officer], [Illegible], [Handwritten in margin].
6. For local legal and revenue terms (for example mahazar, thandaper, pattah), keep the term in italics with an English gloss in brackets on first use.
7. Mark any doubtful reading `[verify]` with the source page and line. Never guess a number.
8. Prepare the translator's certificate or affidavit in the form the court requires, with blanks for the translator's details and signature.
9. Send the draft to `legal-translation-verifier` for an independent check, then to `efiling-bundle-defect-checker` and `pre-filing-verification-checker`.

## Output

1. One English translation per document, headed with the annexure number, title and "True English translation of [document] in [language]".
2. A glossary of names and terms used, for consistency.
3. The certificate or affidavit, with blanks.
4. A list of `[verify]` points for the translator.

## Guardrails and hand-offs

- Translate; never correct, clarify or improve the source. Errors in the original stay, marked [sic].
- Never sign or certify as translator. The human translator or advocate does.
- Where the rules require an official translation, say so and do not present this draft as one.
- New documents in an Indian language go to `regional-language-legal-drafter`.
