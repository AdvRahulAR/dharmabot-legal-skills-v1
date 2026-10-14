---
name: takeover-code-trigger-analyst
description: Tests whether an acquisition of shares, voting rights or control in an Indian listed company triggers an open offer under the SEBI (Substantial Acquisition of Shares and Takeovers) Regulations 2011, covering initial and creeping thresholds, control, persons acting in concert, indirect acquisitions, Regulation 10 exemptions, offer price, timelines and disclosures. Use when a client will cross a shareholding threshold, acquire control, or buy a parent of a listed company. Do not use for CCI merger control; use cci-combination-filing-analyst instead.
---

# Takeover Code Trigger Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Decide whether an open offer is triggered, whether an exemption applies, and what disclosures and timeline follow.

## Jurisdiction gate

- Confirm the target's shares are listed on a recognised Indian stock exchange. An unlisted target is outside the SAST Regulations.
- For an indirect acquisition through a foreign parent, note that foreign law points need counsel qualified there, and FEMA points go to `india-entry-fema-structuring-analyst`.

## Temporal gate

Record the date of the agreement, the public announcement trigger and the acquisition. Apply the SAST text and SEBI circulars in force on each date.

## Required inputs

- **Blocking:** the acquirer and every possible person acting in concert; the current shareholding and voting rights of each, before and after the transaction; the transaction type (agreement, preferential allotment, market purchase, buy-back, indirect acquisition).
- **Blocking:** any rights the acquirer gets over board composition, management or policy (to test control).
- Useful: the SHA or investment agreement, the target's shareholding pattern, the price paid and recent trading data, and the target's group structure.

## Method

1. Retrieve the current official text of the SAST Regulations, SEBI's current FAQs and relevant circulars from sebi.gov.in. Record the version and date.
2. Identify persons acting in concert from the definition and the deemed categories. Aggregate holdings.
3. Test the triggers from the text:
   - initial acquisition threshold (widely understood to be 25% of voting rights; confirm);
   - creeping acquisition limit for holders already above that level, within a financial year, up to the maximum permissible non-public shareholding (confirm figures);
   - acquisition of control, irrespective of shareholding;
   - indirect acquisition, including whether it is "predominant" on the text's tests.
4. Check exemptions under Regulation 10 (believed to be the regulation; confirm against the official text), for example inter se transfers among promoters or qualifying parties, certain schemes, rights issues, buy-backs within limits. Note which are automatic with a report and which need a SEBI application under Regulation 11 (believed to be the regulation; confirm against the official text).
5. If triggered, outline: offer size, offer price parameters (negotiated price, volume-weighted averages, highest price paid), the public announcement, detailed public statement, draft letter of offer, escrow, and the timeline. Confirm every period from the text.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
6. List continual and event disclosures by the acquirer and the target, including encumbrance disclosures.
7. Flag interaction with ICDR (preferential allotment), LODR, PIT (trading in UPSI during the deal) and CCI approval.

## Output

1. PAC and shareholding table, before and after.
2. Trigger analysis by regulation, with the threshold source.
3. Exemption analysis and whether a SEBI application is needed.
4. Timeline and document list if an offer is required.

## Guardrails and hand-offs

- Do not treat the absence of a stated agreement as proof that persons are not acting in concert.
- Do not suggest structuring purely to stay just below a threshold without flagging the anti-avoidance risk.
- Never compute the offer price as final; a merchant banker does that.
- Issue mechanics go to `securities-issuance-compliance-checker`; merger control to `cci-combination-filing-analyst`.
