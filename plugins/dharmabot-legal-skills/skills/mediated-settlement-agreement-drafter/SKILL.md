---
name: mediated-settlement-agreement-drafter
description: Drafts enforceable settlement documents from mediation or conciliation in India, including mediated settlement agreements under the Mediation Act, 2023, conciliation settlements under the Arbitration and Conciliation Act, 1996, and compromise terms under Order XXIII Rule 3 CPC, with payment schedules, default clauses, withdrawal of cases and an enforcement note. Use when parties have settled in mediation or conciliation and a lawyer needs the agreement or compromise terms written up. Do not use for a Lok Adalat award; use lok-adalat-settlement-drafter instead.
---

# Mediated Settlement Agreement Drafter

Every output is a draft for an advocate enrolled in India to check before the parties sign.

## Purpose

Turn agreed terms into a document that can be performed without further argument and enforced if a party defaults.

## Jurisdiction gate

Identify the route that produced the settlement (Mediation Act, 2023; pre-institution mediation; court-referred mediation; conciliation under Part III of the Arbitration and Conciliation Act; or private negotiation in a pending case). Identify the State, the court or centre, and any pending cases. If a party or the performance is abroad, flag cross-border enforcement for counsel in that country.

## Temporal gate

Check which provisions of the Mediation Act, 2023 were in force on the date of settlement, including those on registration and enforcement as a decree. Record the date checked.

## Required inputs

Mark as **blocking**:
- the agreed terms (heads of terms, mediator's notes or the parties' summary);
- full legal names and signatory authority of every party;
- every pending case, notice or complaint between the parties, with forum and case number;
- the route of the settlement (as above).

Also useful: payment details, security offered (post-dated cheques, guarantees), tax treatment, and the State where it will be executed.

## Method

1. Retrieve the current official text of the governing law (the Mediation Act, 2023 and its notifications, Part III of the Arbitration and Conciliation Act, 1996, or Order XXIII CPC), the court's rules on compromise, and the stamp law of the State of execution. Record the version and date.
2. **Terms audit.** List every agreed term and every gap: who pays, how much, by when, how, and what happens on default. Ask the user to close gaps rather than inventing terms.
3. **Draft.** Recitals; the dispute and proceedings; settlement terms in numbered obligations; payment schedule with dates and account details left blank for the parties; default clause (acceleration, revival of claims, or decree for the full amount where lawful); withdrawal or disposal of each case with timing tied to payment; mutual releases, carved out for obligations under the agreement; confidentiality; costs; and signature and authentication blocks.
4. **Enforceability check.** Flag terms that may be unenforceable or unlawful: agreements to compound non-compoundable offences, waivers of statutory rights, restraints of trade, penalties, or terms affecting non-parties. Check that criminal cases can be closed only through the forum's lawful procedure.
5. **Route-specific steps.** For the Mediation Act, set out signing, authentication by the mediator, optional registration and enforcement as believed under the Act; confirm each from the text. For conciliation, note the believed status as an arbitral award on agreed terms; confirm. For court compromises, prepare the compromise application and joint memo.
6. **Stamping.** Check whether stamp duty applies to the agreement and any security; hand off computation to `state-stamp-duty-calculator`.

## Output

1. The settlement agreement or compromise terms.
2. The application or joint memo for each pending case.
3. An enforcement note: how the agreement is enforced, the forum, and default steps.
4. A signing checklist with authority, stamping and authentication.

## Guardrails and hand-offs

- Never add terms the parties did not agree; list open points instead.
- Never invent authority; tag unread authority `[verify]` and run `citation-verifier`.
- Enforcement after default goes to `execution-contempt-petition-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
