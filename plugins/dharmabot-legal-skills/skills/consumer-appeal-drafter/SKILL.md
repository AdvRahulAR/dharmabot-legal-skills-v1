---
name: consumer-appeal-drafter
description: Drafts appeals under the Consumer Protection Act, 2019 to the State Commission, National Commission and Supreme Court, revision petitions and review applications, with the mandatory pre-deposit, limitation and condonation of delay, and applications to enforce Commission orders and seek penalties for non-compliance. Use when an advocate asks to appeal a District or State Commission order, file a consumer revision, review, execution or non-compliance application. Do not use to draft the original complaint; use consumer-complaint-drafter instead.
---

# Consumer Appeal Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Choose the correct appellate, revisional or enforcement remedy against a Consumer Commission order, and draft it with the pre-deposit and limitation handled.

## Jurisdiction gate

Confirm the order is from an Indian Consumer Commission and note which one, the State, and the date. Identify the next forum: District to State Commission, State to National Commission, and National Commission to the Supreme Court, as the Act provides for original and appellate orders. Confirm which orders are appealable and which are open only to revision.

## Temporal gate

Confirm whether the order was passed under the 2019 Act or the 1986 Act, and apply the remedy and pre-deposit rules of the governing Act. Check the current regulations and the e-filing portal.

## Required inputs

Mark as **blocking**:
- the impugned order and the date of receipt of the free or certified copy;
- the complaint, written version, evidence and arguments below;
- which party the client is, and the amount awarded;
- the client's ability to make the pre-deposit.

## Method

1. Retrieve the current official text of the Consumer Protection Act, 2019 provisions on appeals, revision, review and enforcement, and the procedure regulations of the State and National Commissions. Record the version and date.
2. Choose the remedy and state why it fits. Revision is usually limited to jurisdictional error or material irregularity. Review is limited to an error apparent on the record.
3. Compute limitation from the receipt of the order with `limitation-calculator`. If late, draft a condonation application with a dated explanation.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. Pre-deposit: an opposite party appealing against an award must deposit a statutory share of the amount ordered (believed to be 50 percent under the 2019 Act, without the monetary caps the 1986 Act had; confirm the current text for each forum). Show the computation.
5. Draft grounds tied to the order and the record. Flag any point not raised below; new facts usually need an application for additional evidence.
6. Draft a stay application with reasons and an offer of terms.
7. Enforcement: draft an application to execute the order as a decree and, for wilful non-compliance, an application for penalty under the Act's provisions on non-compliance (believed to be sections 71 and 72; confirm).
8. Search for and read current authority on the remedy and the grounds. Tag unread authority `[verify]`.

## Output

1. The draft appeal, revision, review or enforcement application with affidavit.
2. A pre-deposit and limitation note.
3. A list of points not raised below and evidence gaps.

## Guardrails and hand-offs

- Never misstate the order or the record.
- Never promise enhancement or reversal.
- Formatting: `court-pleading-formatter`. Deadlines: `limitation-calculator`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
