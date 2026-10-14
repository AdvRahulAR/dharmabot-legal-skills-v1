---
name: legal-translation-verifier
description: Checks a translation of a legal document between English and any Indian language, or a foreign language such as Arabic, French or German, for errors that change legal meaning, such as wrong or missing names, dates, amounts, survey and case numbers, negations, conditions, obligations, parties and legal terms. Use when an advocate receives a translated judgment, deed, FIR, contract, foreign court document or notice, or before filing or sending a translation, or asks "is this translation accurate". Do not use to produce the translation; use regional-language-legal-drafter.
---

# Legal Translation Verifier

Every output is a review for a person who reads both languages to confirm.

## Purpose

Find every place where a translation differs from its source in a way that could change legal meaning, and rank the findings by seriousness.

## Jurisdiction gate

Language-neutral. Note the document type and its use (filing in India, filing abroad, evidence, client understanding), because that sets the standard of accuracy needed. Courts in India and abroad often require certified or sworn translations; for example, onshore UAE courts generally work in Arabic and require legal translation. Say when a certified translation is likely to be needed.

## Required inputs

Mark as **blocking**: the source text and the translation, both complete. If only the translation is supplied, ask for the original; a translation cannot be checked without it.

Also useful: which language is the source, a glossary the advocate prefers, and the purpose.

## Method

1. Align source and translation paragraph by paragraph (sentence by sentence for short documents). List any paragraph present in one and missing from the other.
2. **Mechanical checks.** Do these exhaustively: compare every name, date (watch for Hijri, Saka or other calendars, and day–month order), amount (figures and words, digit grouping, currency), percentage, survey, document, case and section number, and address. Flag any mismatch, including a transliteration that could point to a different person or place.
3. **Meaning checks.** Look for:
   - dropped or added negations;
   - changed modals ("shall" vs "may");
   - changed conditions ("if", "unless", "provided that");
   - changed time limits;
   - swapped parties;
   - changed tense where it affects whether something happened.
4. **Terminology.** Check that legal terms are translated consistently and in the correct legal sense. Watch for false friends between legal systems, for example common-law terms rendered with civil-law concepts.
5. Rate each finding: **critical** (changes rights or obligations), **major** (could mislead) or **minor** (style or spelling).
6. For each critical and major finding, suggest a corrected rendering in the translation's language, with a back-translation into English.

## Output

1. A summary: findings by severity, and whether the translation is fit for its stated purpose.
2. A findings table: location · source · translation · issue · severity · suggested correction.
3. A mechanical-check table of all numbers and names compared.

## Guardrails

- Quote both texts exactly.
- Do not "improve" style unless asked; focus on meaning.
- AI review does not replace a certified or sworn translation where a court or law requires one.
