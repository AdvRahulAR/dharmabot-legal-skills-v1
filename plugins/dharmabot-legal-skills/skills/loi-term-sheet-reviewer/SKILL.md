---
name: loi-term-sheet-reviewer
description: Drafts and reviews letters of intent, MOUs and commercial term sheets under Indian law, identifying which terms bind (confidentiality, exclusivity, costs, governing law) and which do not, the risk that an enforceable contract has already arisen, stamp duty on MOUs, conditions to definitive agreements and vague terms likely to cause disputes. Use when a lawyer asks whether an MOU or LOI is binding, wants an LOI drafted for a commercial deal, or needs a term sheet reviewed before signing. Do not use for venture capital or startup funding term sheets; use vc-term-sheet-reviewer instead.
---

# LOI and Term Sheet Reviewer

Every output is a review or draft for an advocate enrolled in India to check.

## Purpose

Make sure the client knows exactly what it is bound to before signing a preliminary document, and that the document says so clearly.

## Jurisdiction gate

Confirm Indian law governs or is proposed, and note the State of execution (for stamp duty). If a party is foreign or the document chooses foreign law, flag for `cross-border-contract-reviewer`. If the document is a VC or angel investment term sheet, stop and hand off to `vc-term-sheet-reviewer`.

## Required inputs

Mark as **blocking**:
- the LOI, MOU or term sheet text (or, for drafting, the agreed commercial points);
- which party the client is;
- what the client intends to be binding and non-binding;
- whether any party has started performing (paid, mobilised, submitted a joint bid).

Also useful: the deal context, tender documents for joint bids, and the timetable to definitive agreements.

## Method

1. Retrieve the current official text of the Indian Contract Act, 1872 (offer, acceptance, certainty and agreements to agree), the Specific Relief Act, 1963, and the stamp law of the State of execution. Record the version and date.
2. **Binding analysis.** For each clause decide: binding, non-binding, or ambiguous. Courts look at the words used, the conduct of the parties, and whether essential terms are settled. Search for and read current Supreme Court and High Court authority on MOUs and agreements to agree; tag unread authority `[verify]`.
3. **Contract-formation risk.** Flag where performance, part-payment or detailed terms may mean a concluded contract already exists despite the "subject to contract" label.
4. **Binding clauses to keep binding.** Confidentiality, exclusivity or no-shop (with a clear period), costs, governing law and dispute resolution, and termination of the LOI.
5. **Joint bids and consortia.** Check roles, work share, liability to the employer, bid security, and what happens if the bid fails or wins. Flag tender-condition conflicts.
6. **Vague terms.** List words likely to cause disputes ("best efforts", "to be mutually agreed", undefined prices) and propose tighter wording.
7. **Conditions to definitive agreements.** Due diligence, approvals, financing, board consents and a long-stop date.
8. **Stamping and execution.** MOUs and agreements may attract duty. Hand off to `contract-execution-stamping-checker`.
9. Draft or redraft with a clear binding and non-binding split.

## Output

1. A binding map: clause · binding status · reason · risk.
2. A list of vague terms with replacement wording.
3. The redrafted or new LOI, MOU or term sheet.
4. Next steps to definitive agreements.

## Guardrails and hand-offs

- Never assure the client that a "non-binding" label prevents liability.
- Never invent authority; run `citation-verifier` before delivery.
- Definitive agreements go to `playbook-contract-reviewer` for review once drafted.
