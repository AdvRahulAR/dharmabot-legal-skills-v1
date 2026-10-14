---
name: startup-legal-health-checker
description: Runs a legal health check of an Indian startup, covering incorporation and cap table records, founder IP assignment, employment and contractor papers, ESOPs, ROC filings, GST and tax registrations, DPDP Act compliance, key contracts, trademarks, and eligibility for DPIIT recognition and its benefits, then outputs a prioritised fix list. Use when founders ask for a legal health check, a pre-fundraise clean-up or whether they qualify for DPIIT recognition and the startup tax holiday. Do not use for a full buy-side diligence; use ma-due-diligence-analyst instead.
---

# Startup Legal Health Checker

Every output is a review for an advocate enrolled in India to check, with tax items for a chartered accountant.

## Purpose

Find the gaps an investor's diligence will find, rank them, and set out how to fix each before the startup goes to market.

## Jurisdiction gate

- Confirm the startup is an Indian company or LLP, and the States where it has offices, staff or warehouses (labour, Shops and Establishments and professional tax vary by State).
- A foreign holding company or foreign founders bring FEMA and foreign-law issues; mark them for `india-entry-fema-structuring-analyst` and counsel qualified abroad.

## Temporal gate

- DPDP Act 2023 and the DPDP Rules 2025 are being phased in; check which obligations are in force on the review date.
- The four Labour Codes and the Income-tax Act 2025 are recent; check whether and from when each applies.
- DPIIT eligibility criteria and benefits are set by notification; use the current one.

## Required inputs

- **Blocking:** CIN or LLPIN; date of incorporation; sector and business model; headcount and States of operation.
- **Blocking:** the documents to review (constitution, cap table, filings list, key contracts, employment templates). Without them, the output is a request list, not a health check.
- Useful: DPIIT certificate, trademarks filed, privacy policy, customer and vendor templates, and funding history.

## Method

1. Retrieve the current official text and notifications for each area: MCA records, the DPIIT startup notification and Startup India portal, the DPDP Act and Rules, the Labour Codes and State rules, GST registration rules, and the Trade Marks registry search. Record the version and date.
2. Check corporate records: AOA, allotments and filings, register of members, share certificates, board minutes, and cap table consistency.
3. Check founders: founders' agreement, vesting, and present IP assignment to the company.
4. Check people: offer letters, employment agreements with IP and confidentiality, contractor agreements (misclassification risk), POSH committee and policy, PF, ESI and gratuity registrations as headcount triggers apply.
5. Check ESOP scheme approvals and grant records.
6. Check tax and registrations: PAN, TAN, GST, professional tax, Shops and Establishments; flag filings for a CA.
7. Check data protection: notices, consent, processor contracts and breach readiness; hand detail to `dpdp-compliance-gap-analyst`.
8. Check key contracts (customers, vendors, cloud, licences) for assignment, liability and termination risks; check brand and IP filings.
9. Test DPIIT eligibility (age, turnover, entity type, innovation, not formed by reconstruction) and list available benefits (tax holiday with inter-ministerial board certification, self-certification under labour and environment laws, IPR fast-tracking), each from the current notification.
10. Rank findings: must fix before fundraising, fix soon, good practice.

## Output

1. Health-check table: area · finding · evidence · risk · fix · owner.
2. Prioritised fix list with rough effort.
3. DPIIT eligibility note and benefits list.
4. Items for a CA, and a document request list.

## Guardrails and hand-offs

- Mark anything not evidenced as "not seen", not as compliant.
- Do not promise DPIIT recognition or a tax benefit.
- Hand off: ROC gaps to `roc-secretarial-compliance-checker`; trademarks to `ip-portfolio-tracker`; labour gaps to `labour-codes-compliance-checker`.
