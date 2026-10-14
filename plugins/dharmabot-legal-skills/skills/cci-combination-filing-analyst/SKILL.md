---
name: cci-combination-filing-analyst
description: Applies the Competition Act 2002 as amended in 2023 and the CCI Combination Regulations 2024 to test whether a deal needs Competition Commission of India approval, covering asset and turnover thresholds, the deal value threshold with substantial business operations in India, de minimis and Schedule I exemptions, control and material influence, green channel, Form I or II, gun-jumping and timelines. Use when a client asks whether a deal or minority investment must be notified to the CCI. Do not use for cartel or abuse of dominance matters; use anti-competitive-conduct-analyst instead.
---

# CCI Combination Filing Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Decide whether a transaction is a notifiable combination, whether an exemption applies, and if a filing is needed, which form, when and with what content.

## Jurisdiction gate

- The Competition Act reaches combinations outside India that have, or are likely to have, an appreciable adverse effect on competition in India. Map every party's Indian assets, turnover and business operations.
- Foreign merger control filings in parallel need counsel qualified in each jurisdiction; list them only as "to be confirmed".

## Temporal gate

The 2023 amendments (including the deal value threshold and shorter review periods) and the Combination Regulations 2024 were reported to take effect from 10 September 2024; confirm. Thresholds are revised by notification from time to time. Apply the thresholds in force on the date of the trigger event.

## Required inputs

- **Blocking:** the parties and their groups; the transaction structure (shares, voting rights, assets, merger); the stake and rights acquired (board seats, vetoes, information rights).
- **Blocking:** the value of the transaction, and the latest audited assets and turnover in India and worldwide for the target and acquirer group.
- Useful: the trigger document (board approval or binding agreement), business overlaps and vertical links, and the target's Indian users, GMV or turnover for the business operations test.

## Method

1. Retrieve the current official text of the Competition Act 2002 provisions on combinations, the current threshold and de minimis notifications, the Combination Regulations 2024 (including Schedule I), and the CCI's current FAQs and guidance from cci.gov.in. Record the version and date.
2. Identify the trigger event and the filing deadline (if any) under the current text.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Test the target-level de minimis exemption against the notified figures.
4. Test the asset and turnover thresholds at party and group level, in India and worldwide. Show the arithmetic.
5. Test the deal value threshold: the value of the transaction (including deferred, non-compete and interconnected consideration as the regulations define) and whether the target has substantial business operations in India under the regulations' tests.
6. Test control and material influence. Assess the rights acquired, including affirmative votes, board seats and access to commercially sensitive information.
7. Check Schedule I exemptions (for example certain minority acquisitions solely as an investment, intra-group restructurings), reading the conditions and carve-outs closely, especially for overlaps.
8. If notifiable: choose Form I or Form II, test green channel eligibility (no horizontal, vertical or complementary overlaps), outline overlaps and relevant markets, and list the information needed. Flag that market analysis may need an economist.
9. Set the standstill and review timeline from the current text, and explain gun-jumping risk, including for interconnected steps.

## Output

1. Notifiability analysis: thresholds, deal value test, exemptions, control.
2. Filing recommendation: form, green channel, timing and standstill.
3. Information and document request list.
4. Risk note on gun-jumping and overlaps.

## Guardrails and hand-offs

- Do not state threshold figures without citing the current notification; tag `[verify]` otherwise.
- Never advise closing or exercising rights before approval where a filing is needed.
- SPA conditions go to `share-purchase-agreement-reviewer`; listed targets to `takeover-code-trigger-analyst`.
