---
name: regional-language-legal-drafter
description: Drafts legal documents in any Indian scheduled language (Hindi, Bengali, Marathi, Telugu, Tamil, Gujarati, Urdu, Kannada, Odia, Malayalam, Punjabi, Assamese and others), or turns an English legal draft into one, with an aligned English parallel. Covers legal notices, client letters, affidavits, subordinate-court petitions, legal-aid applications and plain-language explanations. Use when an advocate or legal-aid worker needs a document in an Indian language, or wants a client to understand a document. Do not use to check someone else's translation; use legal-translation-verifier.
---

# Regional Language Legal Drafter

Every output is a draft for an advocate enrolled in India who reads the language to check before it is signed or sent.

## Purpose

Produce clear, correct legal text in the reader's language that a court will accept and a client can understand. Pair it with a line-by-line English parallel so nothing is lost or added.

## Jurisdiction gate

Identify the State, the forum or reader, and the language. Check `references/india-state-statutes.md` for the State's official languages, then confirm whether the forum accepts that language for this document. Subordinate courts usually work in the State's language, while most High Courts and the Supreme Court require English filings. Where English is required, produce the regional-language text only as a translation for the client, or as an accompanying translation if the court's rules allow it.

## Required inputs

Mark as **blocking**:
- the language and script (for example Hindi in Devanagari, Urdu in Nastaliq, Punjabi in Gurmukhi);
- the document type and purpose;
- the content (an English draft, or the facts and instructions);
- the reader (court, opposite party, client);
- the register (formal court language or plain language).

Also useful: a glossary or earlier document the advocate prefers, and names and places spelled as in official records.

## Method

1. If there is no English text, draft in English first and have the user confirm it, so the substance is fixed before translation.
2. Write in the correct Unicode script. Use standard legal terms already used in that State's courts, and the official legal glossaries where known (for example those published by the Legislative Department and State official-language bodies). Keep statute names, section numbers and case citations in the form courts use, usually the English title with an explanation on first use.
3. Keep names, addresses, dates, amounts, survey and plot numbers, and case numbers exactly as in the source. Write amounts in figures and words, using Indian digit grouping, and check that the two match.
4. For plain-language versions, use short sentences, explain each legal term once in brackets, and prefer common words to English loan words where a common word exists.
5. Lay out the result as a two-column table or alternating paragraphs, language and English, numbered identically.
6. List every term where you chose between translations, so the advocate can confirm the choice.
7. Run `legal-translation-verifier` on the result, or tell the user to.

## Output

1. The document in the chosen language.
2. The aligned English parallel.
3. A terminology list.
4. Items to verify (names, numbers, terms).

## Guardrails

- Never change meaning to make the text read better. If a sentence cannot be translated cleanly, flag it.
- Mark the document as an AI-assisted draft until a fluent advocate has checked it.
- AI output in Indian languages can contain spelling, script and grammar errors, especially in lower-resource languages. Say so, and ask for fluent review of anything to be filed.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
