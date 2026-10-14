---
name: compliance-calendar-builder
description: Builds a compliance calendar for an Indian entity covering periodic and event-driven filings, returns, renewals and registers under company law, income tax and GST, the Labour Codes, sector regulators such as RBI, SEBI and IRDAI, environment laws and State licences, with due dates, forms, owners and evidence, plus an audit-readiness view. Use when a client asks for a compliance calendar, statutory due-date tracker, annual compliance checklist or filing schedule for its offices in one or more States. Do not use for one matter's court deadlines; use matter-deadline-tracker instead.
---

# Compliance Calendar Builder

Every output is a draft for an advocate enrolled in India, the company secretary or the compliance head to check.

## Purpose

List every recurring and triggered obligation the entity actually has, with a date, form, owner and proof, so nothing is missed and an auditor can follow it.

## Jurisdiction gate

- Confirm the entity type (company, LLP, firm, trust, branch of a foreign company) and its regulators.
- List every State and UT where it has an office, warehouse, factory or employees. State laws on shops and establishments, professional tax, labour welfare funds, and trade licences differ. Open `references/india-state-statutes.md` as a starting point.

## Temporal gate

- The four Labour Codes were reported brought into force on 21 November 2025, with Central and State rules following. Check which State rules are notified, and whether older labour returns still apply in transition.
- The Income-tax Act, 2025 was reported to apply from 1 April 2026. Use its forms and due dates for periods it governs and the 1961 Act for earlier ones; confirm.
- Due dates are often extended by circular. Mark each date "statutory" or "as extended by [circular, date]".

## Required inputs

**Blocking**:
- entity type, CIN or registration status, financial year, and whether listed;
- business activities and every licence or registration held;
- States and UTs of operation, and headcount in each;
- the calendar period required.

Also useful: last year's filings, auditor's observations, and the owner for each function.

## Method

1. Retrieve the current official text and portal guidance for each regime: MCA (Companies Act and rules), Income-tax and GST portals, EPFO and ESIC, Labour Code rules (Central and State), the sector regulator's returns list, and State portals. Record version and date.
2. Build the obligation universe by domain: corporate and secretarial; direct tax; GST; labour and payroll; sector regulator; environment and pollution consents; State licences and renewals; data protection and cyber; contracts and insurance renewals.
3. Keep only obligations confirmed for this entity's activities, size and States. Note why each applies.
4. For each, record: trigger, frequency, due-date rule, form, portal, owner, approver, evidence of compliance, and penalty exposure (to confirm from the text).
5. Add event-driven items: change of directors or address, allotments, related party transactions, charge creation, new State, new licence.
6. Mark dates that depend on notifications, extensions or yet-to-be-notified rules.
7. Adjust for holidays and portal practice; set internal deadlines before statutory ones.
8. Build the audit-readiness view: obligation, status, filing reference, and document location.
9. Hand secretarial detail to `roc-secretarial-compliance-checker` and labour items to `labour-codes-compliance-checker` for checking.

## Output

1. Calendar table: month · obligation · law · form · due date · internal date · owner · evidence · status.
2. Event-driven obligations list.
3. Assumptions and open questions.
4. A CSV-ready version for import into a tracker.

## Guardrails and hand-offs

- Never invent a due date or form; leave "to confirm" where unclear.
- Never present the calendar as complete for activities or States not disclosed.
- Filing is done by the client or its professionals, not by this skill.
