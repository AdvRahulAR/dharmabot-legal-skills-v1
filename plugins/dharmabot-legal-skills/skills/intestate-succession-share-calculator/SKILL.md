---
name: intestate-succession-share-calculator
description: Identifies legal heirs and computes intestate shares with workings in India under the Hindu Succession Act, 1956 (including daughters as coparceners), the Indian Succession Act, 1925 for Christians, Parsis and others, Muslim personal law and any State uniform civil code, including coparcenary notional partition, and drafts legal heir or family membership certificate applications. Use when a lawyer asks who inherits from a person who died without a will, or for a legal heir certificate application. Do not use when there is a will; use will-drafter or probate-succession-certificate-drafter.
---

# Intestate Succession Share Calculator

Every output is a draft calculation for an advocate enrolled in India to check.

## Purpose

Produce a family tree, the governing rule, and each heir's fractional share with the arithmetic shown.

## Jurisdiction gate

Ask, never assume: the deceased's religion, sex, domicile and date of death, and where the property is. Check whether a State uniform civil code governs (Uttarakhand in force; Gujarat's code reportedly received the President's assent in September 2026 and comes into force on a date the State notifies; Assam's bill was reportedly passed by the Assembly in May 2026, with assent not confirmed; check assent, commencement and coverage, including any Scheduled Tribe exclusion [verify]); Goa has its own succession law; Scheduled Tribes may follow custom. Some States amended the Hindu Succession Act before 2005; check State amendments.

## Temporal gate

The date of death decides the law. For Hindus, the Hindu Succession (Amendment) Act, 2005 made daughters coparceners by birth; the Supreme Court held this applies whether or not the father was alive on the amendment date (Vineeta Sharma v. Rakesh Sharma, 2020; confirm current treatment). Deaths before 1956 follow the older Hindu law.

## Required inputs

Mark as **blocking**:
- religion, sex and date of death of the deceased;
- a full list of relatives, living and predeceased, with dates of death;
- whether there is any will;
- property type: self-acquired, inherited ancestral, coparcenary, agricultural land.

Also useful: earlier partitions, releases, and whether any heir converted or remarried.

## Method

1. Retrieve the current official text of the applicable Act (and any State amendment or State code), the schedules or classes of heirs, and relevant State agricultural tenure rules. Record the version and date.
2. Build the family tree.
3. Apply the rules:
   - **Hindu male:** Class I heirs take together; then Class II, agnates, cognates. For a coparcenary interest, perform the notional partition first to find the deceased's share, then distribute it.
   - **Hindu female:** the separate scheme for her property, which depends on the source of the property.
   - **Christians and others under the 1925 Act:** spouse and lineal descendants, then kindred.
   - **Parsis:** the separate Parsi chapter of the 1925 Act.
   - **Muslims:** sharers, residuaries and distant kindred under the applicable school (Hanafi or Shia); confirm the school.
4. Show the arithmetic as fractions with a common denominator and check the shares add to one.
5. Note excluded or disqualified heirs (for example a murderer) and the effect of conversion or remarriage only as the current law provides.
6. Legal heir or family membership certificate: identify the issuing authority in the State (Tahsildar or equivalent), the documents and the format; draft the application.

## Output

1. Family tree.
2. Share table with workings and the rule for each step.
3. Draft legal heir certificate application and document list.
4. Next steps: release or partition deeds (`family-conveyance-deed-drafter`), mutation (`land-records-mutation-advisor`), or succession certificate (`probate-succession-certificate-drafter`).

## Guardrails

- Never compute before religion, date of death and the heir list are known.
- Never omit a predeceased heir's branch without checking whether it takes by representation.
- A legal heir certificate is not proof of title; say so.
