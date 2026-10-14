---
name: cross-border-contract-reviewer
description: Reviews a contract between an Indian party and a foreign party (US, UK, UAE, EU, Singapore and others) for the cross-border risks an Indian lawyer must catch. Covers governing law and forum, whether a judgment or award would be enforceable in India and abroad, Indian mandatory law (Contract Act limits, FEMA, stamp duty on foreign-executed documents, withholding tax), data transfer, sanctions and export control, currency and payment terms, and redlines. Use for MSAs, SaaS, distribution, licensing, services, JV and supply agreements with a foreign counterparty. Do not use for purely domestic contracts.
---

# Cross-Border Contract Reviewer

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Find the clauses that fail or bite differently because the deal crosses borders, explain the risk to the Indian or foreign client, and propose wording.

## Jurisdiction gate

Identify every party's jurisdiction and the governing law clause. Indian-law points can be advised on. Points that turn on the foreign governing law are marked "to be confirmed by counsel qualified in [jurisdiction]". If no Indian party, asset or performance is involved, say so; this skill adds little.

## Required inputs

Mark as **blocking**:
- the contract and schedules;
- which party the client is;
- the client's commercial priorities;
- where each party has assets and performs.

Also useful: the client's playbook or fallback positions, and deal size.

## Method

1. Read `references/foreign-jurisdictions.md`.
2. **Governing law and forum.** Is the choice valid and sensible? Is the dispute route court or arbitration, and if arbitration, what are the seat, institution, rules and language? Hand off arbitration clause design to `international-arbitration-planner`.
3. **Enforceability test.** For each likely outcome, ask where it would need enforcing and whether that works:
   - a foreign court judgment in India: is the country a reciprocating territory under s.44A CPC (believed to be the section; confirm against the official text)? (The US is believed not to be; the UK, UAE and Singapore are believed to be. Confirm from the current Gazette notifications [verify].)
   - a foreign award in India: is the seat in a country notified under the New York Convention? (The UAE was not notified at the last check.)
   - an Indian judgment or award abroad.

   Flag clauses that leave the client with an unenforceable win.
4. **Indian mandatory and public-policy limits.** Check restraints of trade and non-competes (Indian Contract Act, 1872, s.27), clauses restricting legal proceedings (s.28), stated damages and penalty clauses (under s.74, a court awards reasonable compensation up to the stated sum, rather than drawing the English penalty distinction), specific performance, and consumer or employment protections where relevant. Retrieve current text and authority, and confirm each section number against the official text.
5. **FEMA.** Check pricing and payment terms, guarantees, deferred payments, advance payments, foreign-currency accounts, and any equity or debt features. Hand off structuring to `india-entry-fema-structuring-analyst`.
6. **Tax.** Check withholding on payments to non-residents under the Indian income-tax law now in force, the treaty position, grossing-up clauses, GST (import of services and reverse charge, export of services), and permanent-establishment risk. Mark these for chartered-accountant confirmation.
7. **Stamp duty.** Instruments executed abroad and later brought into India may be dutiable within a time limit after receipt. Use `state-stamp-duty-calculator`.
8. **Data and IP.** Check personal data flows (hand off to `cross-border-data-transfer-analyst`), IP ownership and assignment formalities, and licences.
9. **Sanctions, export control and anti-bribery.** Check for US, UK, EU and UN sanctions and export-control clauses, and anti-corruption clauses such as the FCPA and UK Bribery Act.
10. **Boilerplate that crosses borders.** Check language, notices and service of process agent, currency and exchange-rate risk, force majeure, and the time-zone of deadlines.
11. Rank the issues, and propose replacement wording for the top issues.

## Output

1. A risk table: clause · issue · governing law (India or foreign) · risk (high, medium, low) · recommendation.
2. Redline wording for high and medium issues.
3. Points for foreign counsel and for the chartered accountant.
4. An enforcement map: what enforcement looks like in each place the client may need to enforce.

## Guardrails

- Mark foreign-law conclusions as needing local counsel confirmation.
- Never state a tax rate or treaty rate without the current source.
- Keep commercial choices for the client; explain trade-offs rather than deciding.
