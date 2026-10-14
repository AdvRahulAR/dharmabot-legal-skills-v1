---
name: general-affidavit-drafter
description: Drafts everyday non-litigation affidavits and declarations in India (identity, address, income, date of birth, gap year, single status, no-objection, undertaking) with numbered paragraphs, a verification separating knowledge from belief, State stamp paper or e-stamp needs, and the right attesting authority under the Oaths Act, 1969 and the Notaries Act, 1952. Use when a client needs an affidavit for a university, bank, passport office, employer or government department and asks where to get it attested. Do not use for pleading or evidence affidavits; use evidence-affidavit-drafter.
---

# General Affidavit Drafter

Every output is a draft for an advocate enrolled in India to check before the deponent signs.

## Purpose

Produce a short, accurate affidavit that the receiving authority will accept, and tell the client exactly how to execute and attest it.

## Jurisdiction gate

Confirm where the affidavit will be sworn (State or UT) and where it will be used (Indian authority or abroad). Stamp duty on affidavits, and any exemptions, vary by State. If the document will be used abroad, flag apostille or legalisation and hand off to `document-legalisation-planner`.

## Required inputs

Mark as **blocking**:
- the purpose and the receiving authority, with any format it prescribes;
- the deponent's full name, parent's or spouse's name, age, address and identity document type;
- the facts to be declared, with supporting documents;
- the State where it will be sworn.

Also useful: the language the authority wants, and whether self-declaration is accepted instead.

## Method

1. Retrieve the current official text of the Oaths Act, 1969, the Notaries Act, 1952 and Rules, the State stamp law and any State notification on affidavits or self-declarations, and the receiving authority's format. Record the source and date. Open `references/india-state-statutes.md` as a starting point for the State law.
2. Check whether the authority accepts a self-attested declaration. If so, tell the client; an affidavit may be unnecessary.
3. Use the prescribed format if one exists. Otherwise draft: title, deponent details, numbered paragraphs with one fact each, and a statement of purpose.
4. Write the verification. Separate facts from personal knowledge from those based on records or belief. Name the records.
5. Identify the stamp requirement (stamp paper, e-stamp or none) and confirm the value from the State source with `state-stamp-duty-calculator`. Never state amounts from memory.
6. Identify the attesting authority: notary, oath commissioner appointed by the court, Executive Magistrate, or another officer the rules allow. Note what the deponent must carry (identity proof, photographs).
7. Flag where an affidavit is the wrong instrument (for example a transfer of property needs a registered deed, and a name change needs Gazette publication).

## Output

1. The draft affidavit, ready to print on the right paper.
2. An execution note: stamp, attesting authority, documents to carry, and copies.
3. A list of facts the client must confirm before signing.

## Guardrails and hand-offs

- Never add facts the client has not confirmed. A false affidavit can be an offence; tell the client this plainly.
- Name changes go to `name-change-gazette-drafter`; translations to `regional-language-legal-drafter`.
- The notary or officer attests; this skill does not.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
