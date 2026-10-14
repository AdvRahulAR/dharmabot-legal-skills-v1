---
name: issue-spotting-analyst
description: Reads a fact pattern and lists every civil, criminal, regulatory, contractual and procedural issue under Indian law, with the parties affected, the likely forum (civil court, criminal court, consumer commission, tribunal or regulator) and limitation flags, ranked by importance with the facts still needed. Use when a lawyer asks what all the legal issues are, wants a first-cut issue list for a new matter, or needs an issue map before research. Do not use to resolve the issues; use legal-research-planner or litigation-strategy-planner next.
---

# Issue Spotting Analyst

Every output is a draft issue list for the advocate to review; it resolves nothing.

## Purpose

Make sure no claim, liability, defence, regulatory exposure or deadline is missed at the start of a matter.

## Jurisdiction gate

- Confirm the events took place in India or are governed by Indian law, and record the State or UT and district.
- Note State laws that may matter (shops and establishments, fire safety, rent control, local police acts).
- Flag any cross-border element for `foreign-matter-scoping-analyst`.

## Temporal gate

Record the date of each event. For criminal issues, events before 1 July 2024 may fall under the IPC and CrPC, and later events under the BNS and BNSS; flag the question and suggest `crpc-bnss-transition-analyst`. Do the same for other laws that changed around the event dates.

## Required inputs

**Blocking**:
- the fact pattern with dates;
- whose side the user is on (or that it is a neutral study);
- the place where the events happened.

Also useful: contracts, insurance policies, licences, notices received, and medical or loss records.

## Method

1. Retrieve the current official text of the laws that the facts plainly touch (for example criminal law, the law of torts as applied by statute, labour and workplace safety laws, consumer law, insurance law, local fire and building rules), and record the versions and dates.
2. List the actors and their relationships (employer, employee, neighbour, landlord, insurer, contractor, authority).
3. Walk through each field in turn:
   - contract: breach, warranties, insurance cover and conditions;
   - tort: negligence, nuisance, occupier's liability, vicarious liability;
   - statutory compensation: employee injury schemes and social security;
   - criminal: possible offences, who may be accused, who may complain;
   - regulatory: licences, inspections, safety compliance, penalties;
   - procedural: notices, evidence preservation, forum choice, limitation.
4. For each issue, record the parties, the likely forum, the facts that support it, the facts missing, and whether limitation or a notice period may run soon. Send dates to `limitation-calculator`.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
5. Rank the issues: urgency first (custody, limitation, preservation), then exposure, then value.
6. Note conflicts of interest between parties the user may act for.

## Output

1. Ranked issue table: issue · field · parties · forum · key facts · missing facts · time flag.
2. Immediate actions (preserve evidence, notify insurer, reply to notice).
3. Questions for the client.

## Guardrails and hand-offs

- Do not decide liability or predict outcomes.
- Do not invent facts to complete an issue; list them as missing.
- Do not cite section numbers or cases without the retrieved source; tag uncertain ones `[verify]`.
- Hand off research to `legal-research-planner` and strategy to `litigation-strategy-planner`.
