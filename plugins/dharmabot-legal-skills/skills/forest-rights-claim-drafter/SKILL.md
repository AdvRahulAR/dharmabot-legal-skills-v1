---
name: forest-rights-claim-drafter
description: Drafts claims and appeals under the Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act, 2006 and Rules, 2008, including individual, community and community forest resource claims with evidence, Gram Sabha resolutions, petitions to the SDLC and DLC, and objections to diversion without FRA compliance. Use when a Gram Sabha, Forest Rights Committee or forest dweller wants to file a claim, appeal a rejection or object to diversion. Do not use to map project clearances (use environmental-clearance-analyst) or draft PILs (use pil-drafter).
---

# Forest Rights Claim Drafter

Every output is a draft for an advocate enrolled in India or the supporting legal aid team to check with the Gram Sabha.

## Purpose

Prepare complete, evidence-backed forest rights papers that the committees cannot reject on form, and keep appeal routes open.

## Jurisdiction gate

Confirm the land is forest land in India and identify the State, district, sub-division, tehsil and village. Note whether the area is a Scheduled Area (Fifth or Sixth Schedule), a protected area or a tiger reserve, as extra rules apply. State tribal welfare departments issue their own guidelines; retrieve them.

## Required inputs

Mark as **blocking**: the claimant (individual, family or community) and whether Scheduled Tribe or other traditional forest dweller; the village and Gram Sabha; the right claimed (land, community use, community forest resource); and, for appeals, the rejection order with date.

Also useful: evidence of occupation and use (voter IDs, ration cards, old receipts, encroacher fine slips, elders' statements, maps, satellite images), Forest Rights Committee composition, and Gram Sabha minutes.

## Method

1. Retrieve the current official text of the Forest Rights Act, the 2008 Rules as amended, the prescribed claim forms, Ministry of Tribal Affairs guidelines and circulars, and the State's orders. Record versions and dates.
2. Check eligibility: for other traditional forest dwellers, the residence period requirement; for all, the cut-off date for occupation. Confirm both from the Act.
3. Check the process: Gram Sabha convened with quorum, Forest Rights Committee formed, claim invited, field verification with forest and revenue officials.
4. **Individual claims.** Fill the prescribed form; attach at least two forms of evidence the Rules recognise; sketch map with boundaries.
5. **Community and CFR claims.** Describe customary boundaries, uses (grazing, minor forest produce, water bodies, sacred sites), and neighbouring villages' consent; attach map and resolution.
6. **Gram Sabha resolution.** Draft the resolution with attendance, quorum, and decision on each claim.
7. **Appeals.** Petition to the Sub-Divisional or District Level Committee against rejection or modification: grounds such as no reasons given, no field verification, evidence ignored, or no hearing. Check time limits with `limitation-calculator`.
8. **Diversion objections.** Where land is diverted without completed rights recognition or Gram Sabha consent, draft an objection to the authority and note the clearance angle for `environmental-clearance-analyst`.
9. Search for and read current Supreme Court and High Court authority on FRA rejections and evictions; tag unread items `[verify]`.

## Output

1. Draft claim forms and evidence index.
2. Draft Gram Sabha resolution.
3. Appeal or objection petition, with a chronology.
4. Next-steps note in plain language for the Gram Sabha, and a list of translations needed (hand off to `regional-language-legal-drafter`).

## Guardrails and hand-offs

- Never invent occupation evidence or statements.
- Never advise occupying new forest land.
- For land records, hand off to `land-records-mutation-advisor`; for a PIL, `pil-drafter`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`.
