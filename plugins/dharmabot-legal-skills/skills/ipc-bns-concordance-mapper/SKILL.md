---
name: ipc-bns-concordance-mapper
description: Maps provisions of the repealed Indian Penal Code, Code of Criminal Procedure and Indian Evidence Act to their counterparts in the Bharatiya Nyaya Sanhita, Bharatiya Nagarik Suraksha Sanhita and Bharatiya Sakshya Adhiniyam (and back), with a note on what changed. Use when an advocate asks "what is the BNS section for IPC 420", needs a table of old-to-new sections for a pleading, or must check whether an offence was changed or dropped. Do not use to decide which code governs a case; use crpc-bnss-transition-analyst for that.
---

# IPC–BNS Concordance Mapper

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Give an accurate, sourced mapping between the old and new criminal statutes, and flag every difference in wording, ingredients, punishment or classification that could matter in the matter at hand.

## Jurisdiction gate

This skill covers Indian central criminal law only. Ask whether a State amendment or a special statute (for example NDPS, POCSO, the IT Act, a State police Act) is involved. If so, map the central code provisions and say that the special or State law must be checked separately.

## Required inputs

- The section numbers or offence descriptions to map, and the direction (old to new, or new to old). **Blocking.**
- Why the mapping is needed (charge-sheet reading, drafting, bail, research). It decides how much detail on changes to give.

## Method

1. Retrieve the current official text of the relevant sections of both statutes from an official source (India Code, the Gazette of India, or the Ministry of Home Affairs publications). Do not rely on a remembered concordance; published unofficial tables contain errors.
2. For each provision, find the counterpart by comparing the operative words, not just the heading. One old section may now be split across several new sections, or several old sections merged into one.
3. Compare, side by side: definition and ingredients; punishment (minimum, maximum, fine, any new community-service option); whether cognizable, bailable and compoundable, and by which court triable (from the First Schedule of the CrPC and the BNSS); and any explanation, exception or illustration that was added, removed or reworded.
4. Mark a provision as **new** where the new statute creates an offence with no old counterpart, and as **omitted** where an old offence has no new counterpart. Say what the user should check next (for example, whether conduct is now covered by a special law).
5. Where the mapping is uncertain or the source text could not be retrieved, say so and mark the row `[verify]`.

## Output

A table with columns: old provision · new provision · subject · what changed · classification change (if any) · source checked. Follow it with a short note on any change that matters for the user's stated purpose. Give the source and the date you checked it.

## Verification

- Every row cites the official text consulted, or carries `[verify]`.
- Never cite a section number from memory without checking it.
- Do not paraphrase a changed ingredient as "same as before" unless the operative words match.

## Guardrails and hand-offs

- Do not advise which statute applies to a particular offence date. Hand off to `crpc-bnss-transition-analyst`.
- Do not analyse whether the facts satisfy an offence. Hand off to `fir-ingredients-analyst`.
- Do not present an unofficial concordance table as authoritative.
