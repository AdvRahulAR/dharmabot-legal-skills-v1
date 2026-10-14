---
name: it-rules-intermediary-compliance-checker
description: Checks intermediary duties and safe harbour under the Information Technology Act, 2000 and the IT (Intermediary Guidelines and Digital Media Ethics Code) Rules, 2021 as amended, including grievance officers and the Grievance Appellate Committee, takedown timelines, significant social media intermediary duties, and the 2026 rules on synthetically generated information. Use when a platform, app or AI tool asks about IT Rules compliance, deepfake labelling, takedown orders or safe harbour. Do not use for online money games; use online-gaming-regulatory-analyst instead.
---

# IT Rules Intermediary Compliance Checker

Every output is a draft review for an advocate enrolled in India to check.

## Purpose

Tell the platform which intermediary duties apply, where it falls short, and what that means for safe harbour.

## Jurisdiction gate

- Confirm the service is an intermediary for the content in question, and whether it also publishes its own content (safe harbour does not cover that).
- Identify the category: ordinary intermediary, significant social media intermediary (registered-user threshold notified by MeitY; believed to be 50 lakh users in India; confirm), publisher of news or online curated content, or a service enabling synthetic media.
- A foreign platform serving Indian users is within scope; record its Indian presence and officers.

## Temporal gate

Record the date of each act or order. The 2021 Rules have been amended several times. Check the version in force on each date:
- 2022 (Grievance Appellate Committee and related duties);
- 2023 (online gaming and the fact-check unit; the fact-check provision was reported struck down by the Bombay High Court in 2024; confirm current status);
- late 2025 (reported limits on which officers may issue takedown intimations; confirm);
- 2026 amendment on synthetically generated information, reported notified on 10 February 2026 and in force from 20 February 2026.
List pending drafts and advisories separately as not law.

## Required inputs

**Blocking**:
- a description of the service, features (upload, messaging, livestream, generative AI tools) and Indian user numbers;
- the current terms of use, privacy policy and grievance page;
- any takedown order, notice or blocking direction received, with its date and issuer.

Also useful: content moderation workflow, transparency reports, and labelling or watermarking tools in use.

## Method

1. Retrieve the current official text of the IT Act (the safe harbour provision, believed to be section 79, and blocking powers), the 2021 Rules with every amendment, and current MeitY advisories (eGazette, meity.gov.in). Record version and date.
2. Classify the service and list duties by category.
3. Due diligence: rules and user agreement in English or Eighth Schedule languages, periodic user reminders, prohibited content categories, and reasonable efforts against listed content.
4. Grievance mechanism: grievance officer details, acknowledgement and resolution periods (the 2026 amendment reportedly cut general resolution to 7 days; confirm), and the GAC appeal route.
5. Orders and takedowns: time to act on court or government orders (reportedly 3 hours after the 2026 amendment) and on complaints about non-consensual intimate imagery (reportedly 2 hours). Check who may lawfully issue each notice, and the Sahyog portal process, with current litigation on it.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates. For a period in hours, give `--start` with a time, for example `--start 2026-10-15T14:30 --period 6h`.)
6. SSMI duties: Chief Compliance Officer, nodal contact and resident grievance officer in India, monthly compliance reports, voluntary verification, proactive tools, and first-originator identification for messaging (note the challenges pending against it).
7. Synthetic media: definition and exclusions; prominent visible or audible labels; persistent metadata or identifiers that users cannot strip; user declarations and SSMI technical verification; warnings to users; and measures against prohibited synthetic content.
8. Data retention after takedown and for investigations; cooperation with lawful requests.
9. Assess safe harbour risk for each gap, and hand terms redrafting to `ecommerce-platform-terms-checker` where the service sells goods or services.

## Output

1. Classification note with reasons.
2. Compliance matrix: duty · provision (to confirm) · status · gap · fix · owner.
3. Takedown and grievance timeline table for the operations team.
4. Synthetic media checklist.
5. Pending drafts and litigation watch list.

## Guardrails and hand-offs

- Never advise on evading or delaying a lawful order. Challenges to an order go through proper legal remedies; hand to `writ-petition-drafter`.
- Mark advisories as advisories, and drafts as not law.
- Free speech and constitutional challenges go to `constitutional-validity-analyst`.
