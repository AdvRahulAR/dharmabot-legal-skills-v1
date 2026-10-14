---
name: builder-buyer-agreement-reviewer
description: Reviews agreements for sale, allotment letters and builder-buyer agreements for a homebuyer in any Indian State or UT against the Real Estate (Regulation and Development) Act, 2016 and the State model agreement, flagging one-sided cancellation and forfeiture, delay compensation, carpet area, specifications, common areas, maintenance and title, and unfair terms under the Consumer Protection Act, 2019. Use when a lawyer asks to vet a builder agreement before the buyer pays or mark up a developer's draft. Do not use to file a complaint after a default; use rera-complaint-drafter.
---

# Builder Buyer Agreement Reviewer

Every output is a draft review for an advocate enrolled in India to check.

## Purpose

Show the buyer, clause by clause, where the developer's draft departs from the law and the State model agreement, and what to ask for before paying.

## Jurisdiction gate

Record the State or UT and the project's RERA registration number. The State's model agreement for sale governs the minimum terms, and some States treat departures from it as void. If the project is not RERA-registered, flag this at the top and ask whether an exemption is claimed.

## Required inputs

Mark as **blocking**:
- the agreement, allotment letter or booking form, with annexures;
- the price breakdown and payment plan;
- the project's RERA registration number and the registration page details (possession date declared).

Also useful: the brochure, sanctioned plan, title documents, loan sanction, and the stage of construction.

## Method

1. Retrieve the current official text of the Real Estate (Regulation and Development) Act, 2016, the State rules and the State model agreement for sale, and the unfair contract and unfair trade practice provisions of the Consumer Protection Act, 2019. Open `references/india-state-statutes.md` as a starting point. Record the version and date.
2. Compare each clause with the model agreement and mark deviations.
3. Check the high-risk heads:
   - possession date matching the date declared on the RERA registration, and force majeure wording;
   - delay interest payable by the promoter versus interest charged to the buyer (they should be equal under the Act; confirm);
   - cancellation and forfeiture (amount, triggers, refund timeline);
   - carpet area, tolerance and price adjustment;
   - specifications, amenities and common areas, and changes to plans needing allottee consent;
   - maintenance, deposits, parking and club charges;
   - defect liability period;
   - title, mortgage on the project and the promoter's no-objection from the lender;
   - conveyance timeline and association formation;
   - dispute resolution and jurisdiction clauses.
4. Note clauses courts have treated as one-sided and unfair (search for and read current Supreme Court and National Commission authority; tag anything not read `[verify]`).
5. Check title and approvals only on documents supplied; hand off a full title check to `property-title-diligence-analyst`.

## Output

1. Review table: clause · issue · model agreement or statutory position · risk (high, medium, low) · proposed redraft.
2. Questions and document requests for the developer.
3. A one-page summary for the buyer in plain language.

## Guardrails

- Do not verify approvals not supplied, and say so.
- Never state interest rates or forfeiture limits from memory.
- Never advise the buyer to stop paying without counsel's advice on consequences.
- After a default, hand off to `rera-complaint-drafter`.
