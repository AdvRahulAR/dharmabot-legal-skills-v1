---
name: regulatory-appeal-planner
description: Plans appeals against Indian regulators and specialised tribunals, including the Securities Appellate Tribunal, TDSAT, APTEL, NGT, NCLAT, CESTAT, the Appellate Tribunal under PMLA and SAFEMA, consumer and RERA appellate bodies, and statutory appeals to the High Court or Supreme Court, with forum, limitation, pre-deposit and stay strategy. Use when a regulator's order has gone against a client and they want to appeal, seek a stay, or know the deadline. Do not use to reply to a show cause notice before an order; use regulator-notice-reply-drafter.
---

# Regulatory Appeal Planner

Every output is a draft plan for an advocate enrolled in India to check.

## Purpose

Identify the correct appellate forum, the deadline, any pre-deposit, and the stay strategy, and outline the grounds.

## Jurisdiction gate

Identify the regulator, the statute under which it acted, and the officer who passed the order. The statute fixes the appellate forum; confirm it. Note the bench with territorial jurisdiction where the tribunal sits in benches.

## Temporal gate

Record the date of the order and of its receipt. Appeal periods and condonation limits differ by statute. Some tribunals have changed through the Tribunals Reforms Act, 2021 and later amendments; confirm the current forum for the order's date.

## Required inputs

**Blocking**: the impugned order; the date of receipt; the statute and provision under which it was passed; and the penalty, direction or debarment imposed.

Also useful: the show cause notice and reply, hearing record, documents relied on by the regulator, and the client's ability to make any pre-deposit.

## Method

1. Retrieve the current official text of the appeal provision in the governing statute, the tribunal's procedure rules and forms, fee rules, and any pre-deposit provision. Record source and date. Confirm each section number.
2. Forum: appeal to a tribunal, then a further appeal (often to the Supreme Court on a question of law). Check whether any intermediate appeal must be used first.
3. Limitation: compute the period and the maximum condonable delay with `limitation-calculator`. Flag where the statute caps condonation.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
4. Pre-deposit: check whether a deposit is mandatory, the percentage, and whether it can be waived.
5. Stay: the forum's power to stay, the factors applied, and the urgency. Consider whether to comply under protest pending appeal.
6. Grounds: breach of natural justice (no hearing, documents withheld, no cross-examination where required), wrong law, findings without evidence, disproportionate penalty, parity with others, and limitation for initiating proceedings.
7. Writ maintainability: where a statutory appeal lies, the High Court will usually decline a writ unless an exception applies. Flag this before considering `writ-petition-drafter`.
8. Further appeal to the Supreme Court: identify the route, including statutory appeals and special leave petitions (use `special-leave-petition-drafter`).
9. Read authority before citing; tag anything unread `[verify]`.

## Output

1. A forum, deadline and pre-deposit table.
2. A stay strategy note.
3. A grounds outline linked to the record.
4. A filing checklist (forms, fee, affidavit, vakalatnama, copies).

## Guardrails and hand-offs

- Never promise a stay or reversal.
- Never advise non-compliance with an order that has not been stayed.
- Never invent deadlines or deposit percentages.
