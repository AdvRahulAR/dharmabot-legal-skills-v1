---
name: environmental-clearance-analyst
description: Maps the environmental, forest, wildlife and coastal clearances an Indian project needs under the Environment (Protection) Act 1986, the EIA Notification 2006, the Van (Sanrakshan Evam Samvardhan) Adhiniyam 1980, the Wild Life (Protection) Act 1972 and the CRZ Notification 2019, with sequence and document list. Use when a lawyer asks which clearances a project needs, whether it is category A or B, or whether a public hearing or forest diversion applies. Do not use for consent to operate or waste-rule compliance; use pollution-consent-compliance-checker.
---

# Environmental Clearance Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Tell the client which clearances the project needs, from which authority, in what order, and what can stall it.

## Jurisdiction gate

Confirm the project site is in India and identify the State or UT and district. Clearance authorities, State Expert Appraisal Committees, forest procedures and coastal zone plans vary by State. Ask whether any part of the site is offshore, in a Scheduled Area or near an inter-State or international boundary.

## Temporal gate

EIA schedules, exemptions and forest rules are amended often. The 2023 forest law amendment changed which land is covered. The Supreme Court's 2025 rulings on ex post facto clearances were followed by a recall, so the law on regularisation is unsettled. Record today's date and the date of any work already begun on site.

## Required inputs

Mark as **blocking**:
- project type, capacity or size (MW, tonnes per annum, built-up area, hectares);
- exact location (survey numbers or coordinates) and total land area;
- land status: private, revenue, forest (recorded or deemed), or mixed;
- whether any construction or operation has already started.

Also useful: distance to protected areas, eco-sensitive zones, coast, rivers and inter-State boundaries; water source; tree count; and any earlier approval or show-cause notice.

## Method

1. Retrieve the current official text of the EIA Notification 2006 and its Schedule, the CRZ Notification 2019, the forest Act and its current rules, the Wild Life Act and any office memoranda the PARIVESH portal applies. Record each version and date. Open `references/india-state-statutes.md` for the State's courts and starting points.
2. Screen the project against the EIA Schedule. Decide whether it is listed, and if so category A (central) or B (State), and B1 or B2. Note any general condition that lifts a B project to A. Mark every exemption you rely on "to be checked live".
3. For listed projects, set out the stages: screening, scoping and terms of reference, baseline study, public consultation, appraisal and decision. Note when a public hearing can be exempted, from the current text only.
4. Check forest land. Recorded forest, deemed forest under the Supreme Court's orders and land the amended Act now excludes need separate treatment. Map the stage I and stage II process, compensatory afforestation, net present value and Forest Rights Act compliance with gram sabha consent.
5. Check wildlife. Distance to a national park, sanctuary or eco-sensitive zone may need a State and National Board for Wildlife recommendation.
6. Check the coast. Classify the site under the approved Coastal Zone Management Plan and identify the State authority.
7. Add linked approvals: consent to establish from the State board, groundwater, tree felling, and wetland rules.
8. If work has started, flag violation proceedings, penalty or environmental compensation, and the current law on ex post facto clearance. Search for the latest Supreme Court and NGT authority and read it before relying on it. Tag anything not read in full `[verify]`.

## Output

1. A clearance map: approval · law · authority · trigger · status · typical documents.
2. A sequence chart with dependencies (what must precede what).
3. A document list for the first filing.
4. A risk note: deemed-forest exposure, public hearing risk, litigation history at the site, and work already done.

## Guardrails and hand-offs

- Never state a project is exempt unless the current official text says so; quote the entry relied on.
- Never give timelines as assured; approval times vary.
- Do not advise starting work before clearance.
- For consent to establish and operate and waste rules, hand off to `pollution-consent-compliance-checker`.
- For a challenge to a clearance, hand off to `ngt-application-drafter`.
- Before delivery, send citations to `citation-verifier`.
