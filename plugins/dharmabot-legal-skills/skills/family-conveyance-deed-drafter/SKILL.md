---
name: family-conveyance-deed-drafter
description: Drafts gift, settlement, release, relinquishment, partition and family settlement deeds and memoranda of family arrangement for property in any Indian State or UT under the Transfer of Property Act, 1882, personal law and the Registration Act, 1908, noting concessional family stamp duty. Use when a lawyer asks for a gift deed to a son, a release deed by sisters, a partition among brothers, or a family settlement recording an oral arrangement. Do not use for a sale to an outsider; use sale-deed-drafter.
---

# Family Conveyance Deed Drafter

Every output is a draft for an advocate enrolled in India to check before execution and registration.

## Purpose

Draft intra-family transfers that hold up later: correct instrument, correct parties, shares that match the law of succession, and the right stamp and registration route.

## Jurisdiction gate

Confirm the property is in India and record the State or UT. Many States charge concessional or fixed stamp duty for gifts, releases and partitions among defined family members, and the definition of family differs. Identify the personal law of each party (Hindu, Muslim, Christian, Parsi or other), since it governs inheritance shares and, for Muslims, whether an oral gift (hiba) is valid.

## Required inputs

Mark as **blocking**:
- the instrument wanted and its purpose;
- each party's name, age, relationship and personal law;
- how the transferor holds the property (self-acquired, inherited, joint family, co-owned) with the title documents;
- for releases and partitions, the full list of heirs or co-owners and the date of death of the person through whom they inherit;
- the property schedule in State format.

Also useful: existing mortgages, pending litigation, and whether any party is a minor or lives abroad.

## Method

1. Retrieve the current official text of the Transfer of Property Act, 1882 (gift provisions, believed to start at section 122; confirm), the Registration Act, 1908, the State stamp law and its family concession, and the applicable succession law. Open `references/india-state-statutes.md` as a starting point. Record the version and date.
2. Choose the instrument:
   - **Gift or settlement:** voluntary, without consideration, accepted in the donor's lifetime. Note the limited grounds for revocation and whether any condition (maintenance, life interest) is intended.
   - **Release or relinquishment:** only by a person who already holds a share, in favour of a co-owner.
   - **Partition:** division by metes and bounds among co-owners, each taking a defined portion.
   - **Family settlement or memorandum of family arrangement:** settles bona fide disputes among family members. A memorandum recording a past oral arrangement may not need registration, but one that itself creates rights does (for example Kale v. Deputy Director of Consolidation, Supreme Court, 1976; confirm current treatment).
3. Compute or confirm shares before drafting. Hand off to `intestate-succession-share-calculator`.
4. Draft: recitals of title and devolution, operative words, consideration or its absence, acceptance clause for gifts, schedule, possession, and covenants.
5. Flag risks: a heir left out; a minor's share released without court permission; a transfer that may defeat creditors (fraudulent transfer provisions of the TPA); coparcenary property gifted beyond the donor's share; and income-tax clubbing or gift-tax style provisions to confirm with a tax adviser.
6. Hand off stamp and fee computation to `state-stamp-duty-calculator` and the title check to `property-title-diligence-analyst`.

## Output

1. The draft deed or deeds, with schedules.
2. A family tree and share table used for the draft.
3. Execution and registration checklist, including mutation afterwards.
4. Risk notes for counsel.

## Guardrails

- Never record a sale as a gift or a gift as a release to save stamp duty.
- Never omit a known heir or co-owner from the recitals.
- Do not state a stamp rate or concession from memory.
- The advocate attends execution; this skill does not.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
