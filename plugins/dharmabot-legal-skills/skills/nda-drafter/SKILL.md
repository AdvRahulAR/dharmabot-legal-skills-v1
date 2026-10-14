---
name: nda-drafter
description: Drafts mutual or one-way non-disclosure agreements and confidentiality clauses under Indian law, covering the definition and exclusions, permitted use, term and survival, return or destruction, residuals, injunctive relief, handling of personal data under the DPDP Act, 2023, and governing law and dispute resolution. Use when a lawyer asks for an NDA, a confidentiality agreement, or a confidentiality clause for a deal, vendor evaluation or partnership. Do not use to triage an NDA received from the other side; use nda-triage-reviewer instead.
---

# NDA Drafter

Every output is a draft for an advocate enrolled in India to check before it is sent.

## Purpose

Produce a balanced, enforceable NDA that fits the deal and protects the client's information without overreaching.

## Jurisdiction gate

Confirm that Indian law will govern, or is proposed to govern. Note each party's country and Indian State. If a party is foreign, keep Indian governing law as the default only if the client wants it, and flag the choice of law, forum and enforcement for `cross-border-contract-reviewer`.

## Temporal gate

The DPDP Act, 2023 and the DPDP Rules, 2025 commence in phases. If personal data will be shared, check which obligations are in force on the signing date and from when. Record the date checked.

## Required inputs

Mark as **blocking**:
- mutual or one-way, and which party discloses;
- the purpose of disclosure (the deal or evaluation);
- the parties' legal names, entity types and addresses;
- whether personal data, source code, trade secrets or price-sensitive information will be shared.

Also useful: the client's template or playbook, the desired term, the counterparty's likely objections, and the preferred dispute forum.

## Method

1. Retrieve the current official text of the Indian Contract Act, 1872 (especially section 27 on restraint of trade), the Specific Relief Act, 1963 on injunctions, the DPDP Act, 2023 and Rules, and SEBI insider-trading rules if a listed company is involved. Record the version and date.
2. **Definition.** Cover information in any form, disclosed before or after signing, marked or reasonably understood as confidential. Avoid "all information" definitions that courts may find too vague.
3. **Exclusions.** Public domain, prior possession, independent development, lawful receipt from a third party, and compelled disclosure with notice where lawful.
4. **Use and disclosure.** Limit use to the purpose. Permit disclosure to representatives on a need-to-know basis, with the recipient liable for them.
5. **Term and survival.** Set a disclosure period and a confidentiality period. Keep trade secrets protected for as long as they remain secret.
6. **Return or destruction.** Allow retention of backup copies and copies required by law, still kept confidential.
7. **Residuals.** Omit by default for the discloser; if the client is the recipient and wants one, draft it narrowly and flag the risk.
8. **Personal data.** If shared, require processing only for the purpose, reasonable security safeguards, breach notice, and deletion. Hand off a full data processing agreement to `data-processing-agreement-reviewer` if needed.
9. **Restraints.** Keep non-solicit and non-compete out of the NDA. If the client insists, flag that restraints beyond confidentiality may be void under section 27 and refer to `restrictive-covenant-analyst`.
10. **Remedies and disputes.** Injunctive relief without proof of special damage (as an agreed acknowledgement, not a binding bar), governing law, and courts or arbitration. Check that any arbitration clause names a seat.
11. **Boilerplate.** No licence or obligation to proceed, no warranty, notices, entire agreement, counterparts and electronic signature.

## Output

1. The draft NDA, clean, with numbered clauses.
2. A cover note: key choices made, options for the counterparty's likely pushback, and execution and stamping points for `contract-execution-stamping-checker`.

## Guardrails and hand-offs

- This skill drafts; it does not negotiate. Counter-proposals go to `contract-negotiation-planner`.
- Never include penalties presented as liquidated damages without a genuine pre-estimate.
- Do not state a stamp duty figure; hand off to `state-stamp-duty-calculator`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
