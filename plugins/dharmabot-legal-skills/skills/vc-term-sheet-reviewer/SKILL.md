---
name: vc-term-sheet-reviewer
description: Reviews priced and convertible venture term sheets for Indian startups, covering valuation and the option pool shuffle, liquidation preference, anti-dilution, board seats and affirmative votes, ROFR, tag and drag, founder vesting, information rights, exclusivity and binding terms, and FEMA pricing for foreign investors, then drafts a negotiation response. Use when founders or investors ask to review a term sheet, compare it to Indian market practice, or prepare counter-proposals. Do not use to draft the definitive SSA and SHA; use shareholders-agreement-drafter instead.
---

# VC Term Sheet Reviewer

Every output is a review for an advocate enrolled in India to check before it goes to the client.

## Purpose

Explain what each term costs the client in economics and control, flag terms that cannot work under Indian law, and propose a negotiation position.

## Jurisdiction gate

- Confirm the issuer is an Indian company. If it is a foreign holding company (for example Delaware or Singapore) with an Indian subsidiary, mark foreign-law terms "to be confirmed by counsel qualified in [jurisdiction]".
- Identify any non-resident investor. FEMA pricing, instrument eligibility and reporting apply; flag for `india-entry-fema-structuring-analyst`.

## Required inputs

- **Blocking:** the term sheet; which side the client represents (founders, lead investor, existing investor).
- **Blocking for economics:** the current cap table and the round size.
- Useful: earlier SHAs and investor rights, the ESOP pool, the instrument proposed, and the client's priorities.

## Method

1. Retrieve the current official text of the Companies Act provisions on share issue and preference shares, the Share Capital and Debentures Rules, and the FEMA Non-Debt Instruments Rules and RBI master direction on foreign investment. Record the version and date.
2. Summarise the deal: instrument, pre and post money, round size, pool size and whether it sits in the pre-money (the pool shuffle), and effective price per share.
3. Review each term, with its effect and Indian-law points:
   - **Liquidation preference:** multiple, participating or non-participating, cap, seniority. Model outcomes with `cap-table-calculator`.
   - **Anti-dilution:** full ratchet versus broad-based weighted average; how it works through CCPS conversion ratio; FEMA pricing limits on conversion for foreign investors.
   - **Governance:** board seats, observer, quorum, affirmative vote list (flag operational items that would paralyse the company).
   - **Transfers:** ROFR, ROFO, tag, drag (threshold, price floor, warranties from founders), lock-in.
   - **Founders:** vesting reset, leaver terms, non-compete (post-exit believed largely void under s.27 of the Contract Act; confirm current authority [verify]), full-time commitment.
   - **Investor rights:** information, inspection, pre-emption, exit and put options (FEMA restricts assured returns to non-residents; confirm current rules).
   - **Binding terms:** exclusivity, confidentiality, costs, governing law.
4. Compare with Indian market practice. Describe norms qualitatively, not as figures, unless a cited source supports them.
5. Rank issues: deal-breakers, important, acceptable. Propose counters and fallbacks.

## Output

1. One-page deal summary.
2. Term-by-term table: term · what it says · effect on client · Indian-law issue · proposed counter.
3. Draft response email or redlined term sheet.
4. Items to carry into the definitive documents.

## Guardrails and hand-offs

- Do not value the company or opine on whether the price is fair.
- Do not describe a term as "market" without a basis.
- Convertible instruments go to `convertible-instrument-analyst`; definitive drafting to `shareholders-agreement-drafter`.
