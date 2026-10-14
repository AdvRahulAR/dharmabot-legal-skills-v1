---
name: child-custody-planner
description: Plans custody, guardianship, access and relocation positions in India under the Guardians and Wards Act, 1890, the Hindu Minority and Guardianship Act, 1956 and personal law, centred on the child's welfare, and drafts the custody or visitation application and a parenting plan. Use when a lawyer asks to plan a custody case, seek interim custody or visitation, draft a parenting plan, or respond to a relocation by the other parent. Do not use where the child has been taken to or from another country; use nri-matrimonial-dispute-analyst.
---

# Child Custody Planner

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Build a custody position that a court will see as serving the child, and turn it into an application and a workable parenting plan.

## Jurisdiction gate

Confirm the child is in India and record where the child ordinarily resides; custody under the Guardians and Wards Act is generally sought where the minor ordinarily resides (confirm the provision). Identify the parents' personal law and whether a matrimonial case is pending, since custody can be sought in that case. If the child was moved across a national border, stop and hand off to `nri-matrimonial-dispute-analyst`.

## Required inputs

Mark as **blocking**:
- child's age, schooling, health and current residence, and who has been the primary caregiver;
- each parent's residence, work schedule and support network;
- the event that triggered the dispute (separation, relocation, withholding of access) with dates;
- any pending proceedings and existing orders.

Also useful: the child's wishes if old enough (through the court, not the parent), special needs, safety concerns, and the proposed schedule.

## Method

1. Retrieve the current official text of the Guardians and Wards Act, 1890, the Hindu Minority and Guardianship Act, 1956, the relevant personal law, the Family Courts Act, 1984, and the court's rules or guidelines on child access. Record the version and date.
2. Identify the forum and the provision for interim custody or visitation.
3. Apply the welfare principle as paramount. Map facts to welfare factors: continuity of care and schooling, the child's age and needs, each parent's capacity and availability, siblings, the child's wishes, safety, and each parent's willingness to support the child's relationship with the other.
4. Relocation: compare the reasons for the move with the impact on the child's contact with the other parent; propose remedies (holiday blocks, video calls, travel cost sharing).
5. Draft the application: facts, welfare grounds, interim prayers (custody, visitation, no removal from the jurisdiction, passport deposit where justified), and supporting documents.
6. Draft a parenting plan: residence schedule, weekdays and weekends, holidays and festivals, handovers, communication, education and medical decisions, travel, and dispute resolution.
7. Search for and read current Supreme Court and High Court authority on welfare and shared parenting; tag anything not read `[verify]`.

## Output

1. Strategy note with the strongest welfare points and risks.
2. Draft application with interim prayers.
3. Draft parenting plan.

## Guardrails

- Never coach a child or script what a child should say.
- Never suggest removing or hiding a child, or withholding access to gain leverage.
- Keep the child's identity, school and address confidential.
- Contested petitions go to `matrimonial-petition-drafter`.
