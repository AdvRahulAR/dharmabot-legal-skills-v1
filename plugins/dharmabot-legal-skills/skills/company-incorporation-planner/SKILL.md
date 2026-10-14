---
name: company-incorporation-planner
description: Compares a private limited company, OPC, LLP, Section 8 company and partnership firm under the Companies Act 2013, the LLP Act 2008 and the Indian Partnership Act 1932, then prepares the incorporation set and post-incorporation registration list. Use when a client asks which entity to form, wants SPICe+ inputs, an MOA and AOA, an LLP agreement or a partnership deed drafted, or asks what to register after incorporation. Do not use where any shareholder or partner is non-resident; use india-entry-fema-structuring-analyst instead.
---

# Company Incorporation Planner

Every output is a draft for an advocate enrolled in India, or a company secretary, to check before filing.

## Purpose

Recommend the right vehicle for the client's goals and prepare a complete, consistent incorporation set that a professional can file on the MCA portal or with the Registrar of Firms.

## Jurisdiction gate

- Confirm all founders, shareholders and partners are resident Indians. Any non-resident, foreign entity or OCI holder means FEMA applies: hand off to `india-entry-fema-structuring-analyst` before drafting.
- Record the State or UT of the registered office. Partnership registration, Shops and Establishments registration, professional tax and stamp duty on the MOA, AOA and deeds vary by State.
- Note any sectoral licence the business needs (for example NBFC, payments, insurance broking, FSSAI). Flag that it may dictate the entity type and minimum capital.

## Temporal gate

Check whether any Companies Act, LLP Act or rules amendment, or any change to the SPICe+ forms, has come into force recently. Record the form versions used and the date checked.

## Required inputs

- **Blocking:** number and residency of promoters; the business activity; the State or UT of the registered office.
- **Blocking for drafting:** proposed names (two or more), capital and shareholding or contribution ratio, and the first directors or designated partners.
- Useful: fundraising plans (equity investors expect a private company), profit-distribution intent, charitable objects, appetite for compliance cost, and existing brand or trademark.

## Method

1. Retrieve the current official text of the Companies Act 2013, the Companies (Incorporation) Rules, the LLP Act 2008 and LLP Rules, and the current SPICe+ and LLP incorporation forms from the MCA website. Record the version and date.
2. Build a comparison table on: liability; investor readiness (only a company can issue preference shares, convertibles and ESOPs); compliance load; audit trigger; tax on profits and distributions (flag for a CA); ease of exit and transfer; and member or partner limits.
3. Recommend one vehicle with reasons. Flag OPC conversion rules and Section 8 licensing conditions if those are under consideration.
4. Check name availability against MCA records and the trademark register. Flag names that may need a no-objection or that resemble existing marks.
5. Prepare the set for the chosen vehicle:
   - **Company:** SPICe+ data sheet (Part A and B inputs), MOA objects clause, AOA (Table F or tailored, with transfer restrictions and any founder terms), subscriber sheet, director consents and declarations, registered-office proof list.
   - **LLP:** incorporation inputs and an LLP agreement covering contribution, profit share, admission and cessation, designated partner duties and dispute resolution. Note the deadline to file the agreement (confirm from the rules).
   - **Partnership:** deed under the Indian Partnership Act 1932 and the State's registration steps.
6. Draft first-board items: auditor appointment, bank account, share certificates, statutory registers, commencement-of-business declaration. Hand the resolutions to `board-meeting-documents-drafter`.
7. List post-incorporation registrations with the authority for each: PAN and TAN, GST (if thresholds or inter-State supply apply), Shops and Establishments, professional tax, Udyam, EPF and ESI when headcount triggers apply, and DPIIT recognition if eligible.
8. Compute stamp duty on the MOA, AOA or deed with `state-stamp-duty-calculator`.

## Output

1. Entity comparison table and recommendation.
2. The incorporation set for the chosen vehicle, in draft.
3. A first-90-days checklist with authority, document and owner.
4. A list of open questions and assumptions.

## Guardrails and hand-offs

- Do not state fees, capital minimums or thresholds as settled; cite the retrieved source or tag `[verify]`.
- Do not file on the MCA portal or sign declarations; a professional does that.
- Never suggest nominee or benami holdings to hide a promoter.
- Founder equity, vesting and IP terms go to `founders-agreement-drafter`.
