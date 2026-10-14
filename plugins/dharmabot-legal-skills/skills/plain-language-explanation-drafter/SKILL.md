---
name: plain-language-explanation-drafter
description: Rewrites Indian judgments, statutes, rules, legal analysis and contract clauses into plain, accurate language for clients, citizens or business teams, in English or with a version prepared for translation into Hindi or another Indian language, adding a short what-this-means-for-you section and marking where simplification loses nuance. Use when a lawyer asks to explain a judgment, law or clause to a client in simple words. Do not use for a certified or court translation; use regional-language-legal-drafter or legal-translation-verifier instead.
---

# Plain Language Explanation Drafter

Every output is a draft explanation for the advocate to check for accuracy before it is shared.

## Purpose

Help a non-lawyer understand what a legal text says and how it may affect them, without changing its legal meaning.

## Jurisdiction gate

- Confirm the source is Indian law or an Indian judgment, and note the court and State.
- Note whether a judgment binds the reader's situation (Supreme Court, the reader's High Court) or is only persuasive.
- For foreign judgments or laws, explain only what the text says and mark application in India as uncertain.

## Required inputs

**Blocking**:
- the full source text (judgment, provision, clause or memo);
- the audience (for example a retired teacher, a shopkeeper, a company's sales team) and the language wanted.

Also useful: the client's situation, as the advocate describes it, and the questions the client has asked.

## Method

1. Retrieve the official text of the judgment from the court's website, or the provision from India Code, and record the version and date. Check whether the judgment has been appealed, stayed or overruled if that information is supplied or can be found; otherwise say it was not checked.
2. Identify the core points: who the parties were, what was decided, why, and what rule follows.
3. Rewrite in short sentences, common words and active voice. Explain unavoidable legal terms once, in brackets.
4. Use examples only where they are accurate. Keep amounts, dates and conditions exact.
5. Add "What this means for you" in three to five points, framed as general effects, not advice on facts not seen.
6. Mark every place where simplification loses nuance with "[simplified: ask your lawyer about ...]".
7. For a Hindi or other Indian-language version, prepare simple English designed for translation, and hand off the translation to `regional-language-legal-drafter`. Ask the advocate to have a fluent reader check it.
8. Read the result against the source line by line to confirm nothing changed in meaning.

## Output

1. Plain-language explanation (one page or less unless asked).
2. What this means for you.
3. A note to the advocate listing simplifications and points to confirm.

## Guardrails and hand-offs

- Do not add advice, predictions or reassurance that the source does not support.
- Do not drop conditions, exceptions or time limits.
- Do not present a translation as certified.
- For a hearing or matter update, hand off to `client-status-update-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
