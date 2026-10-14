---
name: nri-matrimonial-dispute-analyst
description: Analyses cross-border matrimonial disputes involving India, covering recognition of foreign divorce decrees under section 13 CPC, parallel proceedings and anti-suit relief, maintenance against NRI spouses, passport and look-out circular remedies, and child removal cases where India relies on welfare-based habeas corpus rather than the Hague Child Abduction Convention. Use when a lawyer asks about a UK or US divorce against an Indian wife, a demand to return a child abroad, or how to reach a husband who left India. Do not use for purely domestic custody; use child-custody-planner.
---

# NRI Matrimonial Dispute Analyst

Every output is a draft analysis for an advocate enrolled in India to check, with foreign-law points for counsel qualified abroad.

## Purpose

Map the parallel forums, tell the client what an Indian court will and will not recognise, and identify urgent protective steps.

## Jurisdiction gate

Record each spouse's citizenship, residence and domicile, the place and law of marriage, the child's habitual residence and current location, and every pending case in any country. Indian law governs the Indian proceedings and recognition in India. Read `references/foreign-jurisdictions.md` for orientation on the other country, and mark every foreign-law point "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the marriage particulars and the governing Indian Act;
- copies or details of the foreign proceedings (court, date, relief, next date, service on the client);
- the child's age, nationality, passports and where the child has lived and when;
- any orders already made in either country.

Also useful: visa and residence status, assets in each country, and evidence of abuse or abandonment.

## Method

1. Retrieve the current official text of section 13 and section 44A of the CPC, the governing marriage Act, the Guardians and Wards Act, 1890, the Passports Act, 1967 and current MEA and MHA guidance on look-out circulars and NRI marriages. Record the version and date. Confirm every section, rule and article number used in this skill against that official text before relying on it.
2. Foreign divorce: test recognition under section 13 CPC. A foreign matrimonial decree is generally recognised only if granted on a ground available under the law under which the parties married, by a forum where the respondent submitted or resided, and with the respondent's consent or participation (Y. Narasimha Rao v. Y. Venkata Lakshmi, Supreme Court, 1991; confirm current treatment).
3. Parallel proceedings: compare forums for the client; consider an Indian petition, a defence abroad, and anti-suit injunctions in India (narrow and exceptional; read current authority).
4. Maintenance against an NRI spouse: Indian remedies (see `maintenance-petition-drafter`), service abroad (hand off to `cross-border-service-evidence-planner`), and enforcing Indian orders abroad or foreign orders in India (hand off to `foreign-judgment-award-enforcement-analyst`).
5. Pressure points: passport impounding or revocation applications, look-out circulars where a criminal case justifies them, and attachment of Indian assets; note proportionality and current authority.
6. Child removal: India is not a party to the Hague Child Abduction Convention (confirm). Indian courts decide return or retention on the child's welfare, often through habeas corpus or Guardians and Wards Act proceedings, giving weight to but not mechanically following foreign orders. Read current Supreme Court authority on summary return versus elaborate inquiry; tag anything not read `[verify]`. Domestic custody planning goes to `child-custody-planner`.
7. Urgent steps: interim custody or no-removal orders, passport deposit, and protection under the DV Act where facts support it.

## Output

1. Forum map: country · proceeding · status · risk · next step.
2. Recognition and child-return analysis.
3. Urgent action list and questions for foreign counsel.

## Guardrails

- Never advise removing or concealing a child, or ignoring a foreign court's order without counsel there being consulted.
- Never state foreign law as settled.
- Never invent case citations; run `citation-verifier` before delivery.
