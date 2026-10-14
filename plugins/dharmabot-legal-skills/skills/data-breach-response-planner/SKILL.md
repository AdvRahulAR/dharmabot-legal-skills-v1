---
name: data-breach-response-planner
description: Use when a client reports ransomware, a hack or leaked customer data, asks what must we report and by when, or asks whether a CERT-In or regulator report was made within time (deadlines counted in hours). Plans the legal response to a personal data breach or cyber incident in India, covering CERT-In reporting under the April 2022 Directions, Data Protection Board and data principal intimation under the DPDP Rules, 2025, RBI, SEBI, IRDAI and other sector reporting, evidence preservation, police complaints, contractual notices and communications, and cyber-security programme duties. Do not use for drafting the police or portal complaint itself; use cyber-crime-complaint-drafter.
---

# Data Breach Response Planner

Every output is a draft for an advocate enrolled in India and the client's incident lead to check. Time-critical steps are listed first.

## Purpose

Give the client a clock-by-clock list of who must be told what, by when and how, and protect evidence and legal position while the technical team contains the incident.

## Jurisdiction gate

- Confirm the affected entity, systems and data principals in India, and whether any are abroad.
- Identify every regulator with reporting rules for this client: CERT-In (all service providers, intermediaries, data centres, body corporates and government bodies covered by the Directions), the Data Protection Board, RBI, SEBI, IRDAI, PFRDA, DoT, NCIIPC for critical information infrastructure.
- For foreign regulators (for example a GDPR authority), mark duties "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

- The DPDP breach intimation rule is believed to commence on 13 May 2027. Confirm from the Gazette. If the incident is earlier, apply CERT-In, IT Act and sector rules, and note what changes after commencement.
- Record the time the incident was detected or reported to the client ("noticed"), not only when it began. CERT-In timelines run from noticing.

## Required inputs

**Blocking**:
- what happened, and the time and date it was noticed;
- systems affected and whether the incident is ongoing;
- categories of data involved (for example KYC, financial, health, children's) and an estimate of people affected;
- the client's sector and any licence or registration it holds.

Also useful: forensic firm details, cyber insurance policy, key customer and vendor contracts, and whether the attacker made demands.

## Method

1. Retrieve the current official text of the CERT-In Directions of 28 April 2022 and FAQs, the DPDP Act and Rules, and each sector direction in play (for example RBI IT governance and cyber-security directions, SEBI CSCRF, IRDAI information and cyber-security guidelines). Record version and date.
2. Build a reporting clock table. CERT-In: report listed incident types within six hours of noticing, in the prescribed format (confirm). DPDP (once in force): intimate the Board without delay and give a detailed report within the period in the Rules (reported as 72 hours; confirm); inform each affected principal without delay. Sector regulators: retrieve each timeline; several are counted in hours.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates. Run the script even for a period in hours: do not add hours by hand. For a period in hours, give `--start` with a time, for example `--start 2026-10-15T14:30 --period 6h`.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. Containment and preservation: ask the incident lead to keep system images, logs and attacker communications. CERT-In requires logs to be kept in India for a set period (believed to be 180 days; confirm). Hand legal hold to `legal-hold-preservation-planner`.
4. Privilege: engage the forensic firm through counsel with a defined legal-advice purpose. Do not assume Indian law will protect the forensic report; keep factual and advisory documents apart.
5. Police and portal complaint: hand to `cyber-crime-complaint-drafter`, with the evidence list.
6. Contracts: notice duties to customers, processors, lenders, insurers and payment networks. Check insurer notice conditions before any ransom discussion.
7. Listed company: check disclosure of material events. Hand to `sebi-lodr-disclosure-checker`.
8. Data abroad or foreign principals: hand to `cross-border-data-transfer-analyst` and mark foreign notifications for local counsel.
9. Communications: notices to individuals with what happened, likely impact, steps taken and steps they should take. No speculation on cause or attribution.
10. Ransom demands: flag sanctions, PMLA and regulator exposure; the decision goes to senior counsel and the board.
11. Post-incident review: map gaps against the CERT-In Directions, sector frameworks and ISO/IEC 27001 controls where the client uses it.

## Output

1. Reporting clock table: recipient · trigger · deadline · form or channel · content · owner · status.
2. Draft notices to regulators and individuals.
3. Evidence and preservation checklist.
4. Privilege protocol note.
5. Post-incident remediation list.

## Guardrails and hand-offs

- Never advise delaying a mandatory report to manage reputation.
- Never state the cause, scope or attacker identity beyond what the forensic facts support.
- Never advise paying or facilitating a ransom; flag it for senior counsel.
- Do not fill in numbers of affected people or data items; mark them "to be confirmed".
