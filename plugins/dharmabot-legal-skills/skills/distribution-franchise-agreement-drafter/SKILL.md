---
name: distribution-franchise-agreement-drafter
description: Drafts and reviews distribution, agency, supply and franchise agreements under Indian law, covering territory and exclusivity, minimum purchase, pricing, trademark and know-how licence, quality control, royalties, GST and post-term restraints, with checks under the Competition Act, 2002, section 27 of the Indian Contract Act and FEMA for foreign franchisors. Use when a lawyer asks for a franchise agreement, a distributor, dealer or supply agreement, or a review of one. Do not use for a stand-alone trademark or IP licence; use ip-assignment-licence-drafter instead.
---

# Distribution and Franchise Agreement Drafter

Every output is a draft for an advocate enrolled in India to check before it is sent.

## Purpose

Build a channel agreement that protects the brand and revenue, survives competition-law scrutiny and works on exit.

## Jurisdiction gate

Confirm Indian law governs and identify every State where the network will operate, because stamp duty, shop and trade licences, and food or drug licences vary by State. If the franchisor, principal or supplier is foreign, flag FEMA and tax points for `india-entry-fema-structuring-analyst` and governing law for `cross-border-contract-reviewer`.

## Required inputs

Mark as **blocking**:
- the type of arrangement (distributor, agent, reseller, supply, contract manufacturing or franchise);
- which side the client is;
- territory, exclusivity and products or brand;
- the money flows (margins, fees, royalties, minimum purchases).

Also useful: the brand's trademark registrations, operations manual, existing network terms, and the sector (food, retail, pharma, automotive).

## Method

1. Retrieve the current official text of the Indian Contract Act, 1872 (agency, restraint of trade), the Sale of Goods Act, 1930, the Competition Act, 2002 as amended in 2023, the Trade Marks Act, 1999 on registered users and licensing, the CGST Act, 2017, FEMA current-account rules if a foreign party is paid, and sector licensing laws. Record the version and date.
2. **Characterise the relationship.** Distributor (buys and resells) versus agent (acts for principal). The label matters less than substance. Note tax and liability consequences.
3. **Commercial core.** Appointment, territory, exclusivity, products, minimum purchase or performance targets, ordering, pricing, payment, title and risk.
4. **Brand and know-how.** Trademark licence, quality control, manuals, training, audits, confidentiality and ownership of goodwill. Hand off detailed IP terms to `ip-assignment-licence-drafter`.
5. **Fees.** Franchise fee, royalties, marketing fund, GST on each, and withholding; leave rates to the client's tax adviser.
6. **Competition law.** Screen resale price maintenance, exclusive supply or distribution, tie-ins and refusal to deal under the Competition Act provisions on vertical agreements. Recommend "maximum" or "recommended" retail prices rather than fixed resale prices. Hand off real risk to `anti-competitive-conduct-analyst`.
7. **Restraints.** In-term non-compete is usually easier to defend than post-term restraints, which section 27 (believed to be the section; confirm against the official text) may make void. Draft post-term protection around confidentiality, de-branding and trademark use.
8. **Term and exit.** Renewal, termination for breach and convenience, buy-back of stock, de-identification, customer data, and transition.
9. **Liability and compliance.** Product liability, recalls, consumer complaints, labelling and licences, anti-bribery.
10. **Disputes.** Arbitration with a stated seat, or courts; injunction rights for brand misuse.

## Output

1. The draft agreement with schedules (territory, products, fees, standards).
2. A review note if reviewing: issues · risk · fix.
3. A compliance flag list: competition, FEMA, State licences, stamp duty.

## Guardrails and hand-offs

- Never fix resale prices in the draft without a competition-law warning.
- Do not state royalty remittance limits or tax rates; refer to current rules.
- Review against a playbook through `playbook-contract-reviewer`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
