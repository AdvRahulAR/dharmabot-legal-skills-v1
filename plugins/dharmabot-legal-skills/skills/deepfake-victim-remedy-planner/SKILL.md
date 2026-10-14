---
name: deepfake-victim-remedy-planner
description: Builds a remedy plan for a person harmed by a deepfake, morphed image or AI impersonation in India, covering platform takedown under the IT Rules, 2021 as amended, Grievance Appellate Committee escalation, the cyber crime portal and police complaint, BNS and IT Act offences, and civil options such as personality-rights and John Doe injunctions, with evidence capture. Use when a client's morphed or fake video, image or voice clone is circulating online. Do not use to draft the police complaint (use cyber-crime-complaint-drafter) or the injunction (use interim-injunction-application-drafter).
---

# Deepfake Victim Remedy Planner

Every output is a draft plan for an advocate enrolled in India to check and act on with the client.

## Purpose

Give the victim a same-day and same-week plan that gets content down fast, preserves evidence, and keeps criminal and civil options open.

## Jurisdiction gate

Confirm the victim is in India or the content is accessible in India. Identify the State and police jurisdiction for the complaint and the High Court for civil relief. Note platforms based abroad; Indian law still applies to intermediaries serving Indian users. Where the victim is a child, apply POCSO reporting duties and hand off to `pocso-case-analyst` for the prosecution side.

## Temporal gate

- BNS offences apply to acts on or after 1 July 2024; earlier acts fall under the IPC. If any posting predates that, run `crpc-bnss-transition-analyst`.
- MeitY amended the IT Rules on synthetically generated information in 2026 (reported 10 February 2026), reportedly shortening several takedown windows. Confirm the in-force window for intimate imagery and impersonation, which before the amendment was believed to be 24 hours under Rule 3(2)(b).

## Required inputs

Mark as **blocking**: the URLs, handles, group names and platforms where the content appears; when the victim learned of it; whether the content is sexual or intimate; the victim's age; and whether the creator or uploader is known.

Also useful: screenshots, messages with the suspect, earlier complaints, and the victim's public profile (relevant to personality rights).

## Method

1. Retrieve the current official text of the IT Rules as amended, relevant IT Act and BNS provisions, and the platform's grievance and reporting pages. Record versions and dates.
2. **Today: evidence.** Capture each URL with date, time and full-page screenshot; record usernames and IDs; save message headers. Do not download or forward sexual content more than the record needs. Plan a certificate for electronic evidence under the BSA.
3. **Today: takedown.** Send requests to each platform's grievance officer under the IT Rules, citing the category of content. Use in-app reporting too. Track acknowledgements and time.
4. **Today: cyber complaint.** File on the National Cyber Crime Reporting Portal and note the acknowledgement. Hand the formal complaint to `cyber-crime-complaint-drafter`.
5. **This week: escalation.** If the platform fails to act, escalate to the Grievance Appellate Committee and record the failure, which may affect safe harbour.
6. **This week: civil relief.** Assess a suit for injunction (including against unknown persons), personality or privacy rights, and defamation. Hand the application to `interim-injunction-application-drafter`.
7. **Offences.** List candidate BNS and IT Act offences for the police to consider, marked "confirm section from the official text".
8. **Victim support.** Note confidentiality of identity, women's helplines and legal aid options.

## Output

1. Action plan: today, this week, next steps, each with owner and status.
2. Draft takedown request template and evidence log.
3. A remedies note covering criminal, civil and platform routes.

## Guardrails and hand-offs

- Never promise removal within any time.
- Never publish or circulate the content further, even to "prove" it.
- Never name the victim in any public document.
- For platform duties analysis, hand off to `it-rules-intermediary-compliance-checker`.
- Before any complaint or notice is sent, hand off to `pre-filing-verification-checker`.
