---
name: product-recall-planner
description: Plans a product recall in India end to end, covering whether it is mandatory, recall class, regulator, trade and consumer notices, timelines and reports, under the FSS (Food Recall Procedure) Regulations, 2017, the Medical Devices Rules, 2017 and CDSCO guidance, the Motor Vehicles Act and CCPA powers. Use when a batch fails a lab test, a defect or adverse event is reported, or a regulator orders a recall. Do not use to reply to a show-cause notice (use regulator-notice-reply-drafter) or assess liability claims (use product-liability-analyst).
---

# Product Recall Planner

Every output is a draft plan for an advocate enrolled in India and the company's quality and regulatory team to check.

## Purpose

Give the client a dated, owner-assigned recall plan that meets the regulator's process and protects evidence.

## Jurisdiction gate

Identify the product type and the regulator: FSSAI and the State Food Safety Commissioner for food; CDSCO and State licensing authority for drugs, cosmetics and medical devices; MoRTH for motor vehicles; CCPA for consumer goods generally; BIS for products under quality control orders. Note the States where the product was sold. For exports, mark foreign recall duties "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**: the product, batch or lot numbers and quantities; the defect or test result (with the lab report); date of discovery; distribution footprint (States, channels, online sellers); and any regulator communication received.

Also useful: complaints and adverse event reports, the company's recall SOP, distributor contracts, insurance policy, and retained samples.

## Method

1. Retrieve the current official text of the applicable recall regulation, rules, guidelines and forms (FSSAI, CDSCO, MoRTH or CCPA websites and eGazette). Record versions and dates.
2. Decide whether the recall is mandatory or voluntary, and who must be told and by when. Confirm every timeline from the current text.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. Classify the hazard (recall class or level) using the regulator's criteria, with reasons.
4. Set the recall depth: consumer, retail, or wholesale level.
5. Draft notices:
   - initial intimation to the regulator;
   - trade notice to distributors, retailers and marketplaces;
   - consumer notice (press, website, app, social media) in plain language and the needed Indian languages.
6. Plan logistics: stop sale, quarantine, return routes, reconciliation of quantities, destruction or reprocessing with witnessed records.
7. Plan reporting: progress reports and the final recall report in the prescribed format; effectiveness checks.
8. Preserve evidence: retain samples, freeze batch records, issue a legal hold through `legal-hold-preservation-planner`.
9. Note liability exposure for `product-liability-analyst`: consumer claims, class actions, contract claims against suppliers, insurance notice.
10. Draft internal and external communications that avoid admissions beyond the facts.

## Output

1. Recall decision memo with classification and reasons.
2. Action plan table: step · owner · deadline · status.
3. Draft regulator intimation, trade notice and consumer notice.
4. Evidence and reporting checklist.

## Guardrails and hand-offs

- Never state a recall timeline from memory; quote the current text.
- Never advise delaying a mandatory recall or understating the hazard.
- Keep admissions factual; route media statements through counsel.
- For labelling defects in food, hand off to `food-product-labelling-compliance-checker`; for drugs and devices, `drugs-devices-regulatory-analyst`.
- Before any notice is sent to a regulator, hand off to `pre-filing-verification-checker`.
