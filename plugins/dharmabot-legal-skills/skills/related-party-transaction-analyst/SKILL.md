---
name: related-party-transaction-analyst
description: Identifies related parties and related-party transactions under the Companies Act 2013 and Regulation 23 of the SEBI LODR Regulations, tests ordinary course and arm's length, applies materiality thresholds, and maps audit committee, board and shareholder approvals and disclosures, with Ind AS 24 and transfer-pricing flags. Use when a client asks whether a lease, loan, sale or service deal with a promoter, director or group company needs approval, or who may vote on it. Do not use for drafting the resolution itself; use board-meeting-documents-drafter instead.
---

# Related Party Transaction Analyst

Every output is a draft for an advocate or company secretary in India to check.

## Purpose

Decide whether a transaction is a related-party transaction, which approvals and disclosures it needs, and who must abstain, and set out a clean approval path.

## Jurisdiction gate

- Confirm the company is Indian and whether it is listed, a subsidiary of a listed entity, a public unlisted company or a private company. The listed-entity regime under SEBI LODR is stricter and wider than the Companies Act.
- If the counterparty is abroad, flag transfer pricing and FEMA points for a tax adviser and `india-entry-fema-structuring-analyst`.

## Temporal gate

SEBI has amended the RPT materiality framework more than once, including a 2025 move to scale-based thresholds (confirm the current text and its effective date). Record the proposed transaction date and apply the version in force then.

## Required inputs

- **Blocking:** the parties and the transaction (nature, value, duration, pricing basis); the company's listing status.
- **Blocking:** the shareholding and directorship chain linking the counterparty to the company, its promoters, directors and KMP.
- Useful: the last audited consolidated turnover, the company's RPT policy, omnibus approvals already granted, valuation or benchmarking reports, and the SHA reserved matters.

## Method

1. Retrieve the current official text of the Companies Act provisions on related parties and their approval (believed to be section 2(76) and section 188; confirm), the Meetings of Board rules, SEBI LODR Regulation 23 and the current SEBI circulars on RPT disclosure and minimum information. Record the version and date.
2. Map the relationship chart. Test each link against the statutory definitions under both regimes, which differ (for example promoter group entities and shareholding-based tests under LODR).
3. Classify the transaction. Check whether it falls in a listed category requiring approval, or in an exemption (for example transactions with a wholly owned subsidiary, where confirmed by the text).
4. Test ordinary course of business and arm's length separately. Record the evidence for each: past practice, objects clause, market quotes, independent valuation or benchmarking.
5. Apply the thresholds: Companies Act rule thresholds for shareholder approval, and LODR materiality for listed entities (including material modifications). Show the calculation from the inputs.
6. Map approvals in sequence: audit committee (prior approval, omnibus rules), board, shareholders. State who cannot vote: interested directors at board level and related parties at shareholder level, as the retrieved text provides.
7. List disclosures: the board's report and AOC-2, half-yearly RPT disclosure to the exchanges, financial statement notes under Ind AS 24, and the register of contracts with interested parties. Hand exchange timing to `sebi-lodr-disclosure-checker`.
8. Flag consequences of non-compliance: voidability, director liability and ratification limits.

## Output

1. Relationship chart and classification table.
2. Ordinary course and arm's length assessment with evidence gaps.
3. Approval path: body, threshold, timing, abstentions.
4. Disclosure checklist and a list of documents needed.

## Guardrails and hand-offs

- Do not conclude "arm's length" without evidence; mark it as an assumption.
- Do not state materiality thresholds from memory; cite the retrieved text or tag `[verify]`.
- Do not advise splitting a transaction to avoid a threshold.
- Resolutions go to `board-meeting-documents-drafter`.
