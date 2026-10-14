---
name: ai-incident-response-planner
description: Triages an incident caused by an AI system (harmful or false output, deepfake made on the platform, biased automated decision, prompt-injection misuse) and plans containment, evidence, notifications and remediation under the IT Act, 2000 and IT Rules on synthetic content, the Consumer Protection Act, 2019 and sector rules such as RBI's FREE-AI framework. Use when a chatbot or AI feature caused harm and a client asks what to do now. Do not use for a personal data breach (use data-breach-response-planner) or to write AI policy (use ai-governance-policy-drafter).
---

# AI Incident Response Planner

Every output is a draft plan for an advocate enrolled in India and the client's incident team to check.

## Purpose

Give the client a time-ordered plan for the first hours and days after an AI incident: what to stop, what to keep, whom to tell, and what to fix.

## Jurisdiction gate

Confirm the deployer or platform serves users in India, and identify its role: intermediary, significant social media intermediary, regulated financial entity, healthcare provider, or ordinary business. Note any users abroad; mark foreign duties (for example under the EU AI Act) "to be confirmed by counsel qualified in [jurisdiction]" and hand off to `eu-ai-digital-regulation-analyst`.

## Temporal gate

- MeitY amended the IT Rules on synthetically generated information in 2026 (reported as notified 10 February 2026). Reports say several takedown windows were shortened. Confirm the in-force text and each window.
- DPDP Rules, 2025 apply in phases (reported 13 November 2025, 13 November 2026 and 13 May 2027). If personal data is involved, record which phase applies on the incident date.
- Record the date and time the incident was detected; deadlines run from there.

## Required inputs

Mark as **blocking**: what happened (outputs, screenshots, logs); when it was detected; the system and who operates it (in-house model, vendor API, fine-tuned model); who was affected and how many; whether personal data was exposed; and the client's sector and regulator.

Also useful: the AI vendor contract, internal AI policy, model and prompt version history, complaints received, and media coverage.

## Method

1. Retrieve the current official text of the IT Act, the IT Rules as amended, any MeitY advisories on AI, the sector regulator's AI guidance, and the Consumer Protection Act provisions on unfair trade practice and misleading statements. Record versions and dates.
2. Classify the incident: harmful or false output; unlawful content (including synthetic intimate imagery or CSAM); discriminatory decision; security misuse; or out-of-scope use.
3. **Contain.** Suspend the feature or route, add guardrails, and stop further spread. Record each action with time.
4. **Preserve.** Freeze logs, prompts, model versions, configs and outputs; hand off to `legal-hold-preservation-planner`.
5. **Notify.** Build a notification matrix: regulator (sector regulator, CERT-In if a cyber incident, Data Protection Board if a personal data breach), affected users, customers under contract, insurers, and platforms hosting the content. Confirm each trigger and deadline from current text.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.)
6. **Remedy users.** Correct false information given (for example a wrong loan rate), honour or explain transactions made on it, and assess consumer claims.
7. **Unlawful content.** Apply intermediary takedown and reporting duties; hand off to `it-rules-intermediary-compliance-checker`.
8. **Root cause and fixes.** Record the cause, the control that failed, and the change made.
9. Draft holding statements and user notices that are accurate and avoid admissions beyond the facts.

## Output

1. Incident triage note with classification.
2. Action timeline: step · owner · deadline · status.
3. Notification matrix with draft notices.
4. Remediation and lessons-learned list for `ai-governance-policy-drafter`.

## Guardrails and hand-offs

- Never state a reporting deadline from memory.
- Never advise deleting logs or outputs.
- If personal data is involved, hand off to `data-breach-response-planner`.
- Do not guarantee that no liability arises.
- Before any notice is sent to a regulator or user, hand off to `pre-filing-verification-checker`.
