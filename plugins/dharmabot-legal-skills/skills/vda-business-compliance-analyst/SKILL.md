---
name: vda-business-compliance-analyst
description: Maps the Indian regime for virtual digital asset businesses, covering the flat tax and TDS on VDA transfers under the Income-tax Acts of 1961 and 2025, GST on platform services, ASCI rules on VDA ads, FEMA questions for offshore platforms, FIU-IND action on unregistered exchanges, and the open status of any VDA statute. Use when a crypto exchange, wallet, NFT or Web3 business wants to launch in India or onboard Indian users. Do not use for the PMLA and KYC check (use aml-sanctions-compliance-checker) or for investment advice.
---

# VDA Business Compliance Analyst

Every output is a draft analysis for an advocate enrolled in India to check.

## Purpose

Produce a launch-readiness map for a VDA business: each regime, what it requires, and what remains legally uncertain.

## Jurisdiction gate

Identify where the business is incorporated, where its servers and team are, and whether it serves users in India. Offshore platforms serving Indian users are in scope. Foreign licensing (for example in Dubai or Singapore) is "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

- The Income-tax Act, 2025 is reported to apply from 1 April 2026, replacing the 1961 Act. For transactions before that date, use the 1961 Act; for later ones, use the 2025 Act. Map provisions with `income-tax-act-2025-concordance-mapper`.
- RBI, SEBI and the government have issued statements and consultation papers on crypto at different times. Record the date of each and check for any later policy or bill.
- Check the current list of offshore entities FIU-IND has acted against.

## Required inputs

Mark as **blocking**: the business model (exchange, broker, custodian, wallet, NFT marketplace, staking, payments); the assets offered; whether Indian users are served and how they pay in (INR rails, P2P, card); and the entity structure.

Also useful: user terms, marketing material, current KYC flow, banking partners, and any regulator correspondence.

## Method

1. Retrieve the current official text of the VDA provisions in the Income-tax Acts, the CBDT circulars and notifications on VDA TDS, GST notifications, the PMLA notification bringing VDA service providers in scope, ASCI's VDA guidelines, and RBI and SEBI statements. Record versions and dates.
2. **Characterise** each asset and activity: VDA as defined, NFT exclusions, stablecoins, tokenised securities (possible SEBI issues).
3. **Direct tax.** Flat rate on transfer income, no set-off of losses, TDS on transfer consideration and who deducts it on an exchange. Confirm rates and thresholds from current text.
4. **GST.** Platform fees and place of supply for offshore platforms (OIDAR questions). Mark for the GST adviser.
5. **PMLA.** Note reporting-entity status and FIU-IND registration; hand off the detailed check to `aml-sanctions-compliance-checker`.
6. **FEMA.** Indian users remitting to offshore platforms, LRS questions, and Indian entities holding VDAs abroad. Mark unsettled points.
7. **Advertising.** Apply ASCI VDA disclaimer and risk-warning rules and influencer disclosure; hand off claims review to `advertising-claims-reviewer`.
8. **Consumer and data.** Terms fairness under the Consumer Protection Act and DPDP duties.
9. **Open questions.** Record the absence of a dedicated VDA statute and policy risk.

## Output

1. Regime map: area · requirement · source · status (settled, unsettled) · action.
2. Pre-launch checklist.
3. A short risk note on regulatory uncertainty.

## Guardrails and hand-offs

- Never state a tax rate or TDS threshold from memory.
- Never advise on structuring to avoid TDS, PMLA or FEMA.
- Never give investment advice or comment on asset value.
- Run `citation-verifier` before delivery.
