---
name: cap-table-calculator
description: Models cap table ownership and dilution with the arithmetic shown, covering priced rounds, pre-money and post-money ESOP pool top-ups, conversion of CCPS, CCDs, iSAFEs and convertible notes, anti-dilution adjustments and liquidation-preference waterfalls at different exit values, reconciled to the register of members under the Companies Act 2013. Use when founders or counsel ask to model a round, size an ESOP pool, convert notes or run an exit waterfall. Do not use to opine on valuation or on term sheet fairness; use vc-term-sheet-reviewer instead.
---

# Cap Table Calculator

Every output is a draft calculation for counsel and the company's finance team to review.

## Purpose

Show who owns what before and after each event, and who receives what at exit, with every step of arithmetic visible so it can be checked.

## Jurisdiction gate

- The arithmetic is jurisdiction-neutral. For an Indian company, reconcile to the register of members and the MCA shareholding records.
- Legal terms that drive the numbers (preference, anti-dilution, conversion) come from the actual documents. If the issuer is foreign, the legal reading of those documents needs counsel qualified there.

## Required inputs

- **Blocking:** the current cap table by holder and class, with fully diluted counts (issued shares, convertibles, granted and ungranted options).
- **Blocking for a round:** pre-money valuation, round size, and whether the pool top-up is counted pre-money or post-money.
- **Blocking for conversions and waterfalls:** the instrument terms (cap, discount, conversion ratio, preference multiple, participation, seniority, anti-dilution formula).
- Useful: the register of members and allotment filings, to reconcile.

## Method

1. Retrieve the official source for every input: the executed instrument terms, the AOA, and the register of members or MCA records. Record the document and date. Do not use term sheet figures where executed documents exist.
2. Reconcile the starting cap table to the register. List mismatches before calculating.
3. Define the share basis (issued, fully diluted, as-converted) and state which one each result uses.
4. Priced round: compute price per share = pre-money / pre-money fully diluted shares (adjusted for any pre-money pool top-up); new shares = investment / price. Show the solve for a post-money pool target.
5. Conversions: compute the conversion price under each test (cap price, discounted round price) and apply the lower or as the terms say. Show shares issued per instrument.
6. Anti-dilution: apply the exact formula in the documents (broad-based weighted average or full ratchet). Show the adjusted conversion ratio.
7. Waterfall: at each exit value, pay preferences in seniority, then participation or conversion choice for each class (each holder takes the better of preference or as-converted where the terms allow). Show the break-points.
8. Produce a summary and a check: totals equal 100% and proceeds equal the exit value.

## Output

1. Reconciled starting cap table and list of mismatches.
2. Post-event cap table (issued and fully diluted).
3. Step-by-step workings for each calculation.
4. Waterfall table at the requested exit values.
5. Assumptions list.

## Guardrails and hand-offs

- Show arithmetic; never present an unexplained figure.
- Do not round shares in a way that changes ownership; state the rounding rule from the documents.
- Do not opine on valuation, FEMA pricing or tax; flag them.
- Pool sizing feeds `esop-scheme-drafter`; term negotiation goes to `vc-term-sheet-reviewer`.
