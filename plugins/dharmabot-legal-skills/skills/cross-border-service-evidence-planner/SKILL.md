---
name: cross-border-service-evidence-planner
description: Plans service of summons and court documents, and taking of evidence, across borders between India and the US, UK, EU, Singapore (Hague Service and Evidence Conventions) and the UAE (bilateral agreement or letters of request). Covers serving an Indian suit on a defendant abroad, serving foreign proceedings on a party in India, commissions and letters of request for witnesses and documents, and timelines. Use when a defendant or witness is abroad, or a foreign court needs service or evidence in India. Do not use for domestic service.
---

# Cross-Border Service and Evidence Planner

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Choose a valid route for service or evidence that the court will accept and that will not undermine later enforcement, and set out the documents and timeline.

## Jurisdiction gate

Identify the court where proceedings are pending, the country where service or evidence is needed, and the type of proceeding (civil or commercial; criminal matters follow different mutual legal assistance routes). Read `references/foreign-jurisdictions.md` for Hague Service and Evidence Convention status. India, the US, the UK, Singapore and all EU member States are parties to the Service Convention. Some EU States (for example Austria, Belgium and Ireland) are not parties to the Evidence Convention. The UAE is a party to neither. Confirm each State on the HCCH status table.

## Required inputs

Mark as **blocking**:
- the court and case;
- the person to be served or examined, and their address or location;
- the documents to be served, or the evidence needed;
- deadlines.

Also useful: whether the person will accept service voluntarily, and the contract's agreed service or process-agent clause.

## Method

1. Retrieve current sources: the HCCH status table and India's declarations (Central Authority, objections to postal and other channels), the Code of Civil Procedure provisions on service outside India and on commissions and letters of request, the Ministry of Law and Justice procedure, the court's rules, and any bilateral agreement (for the UAE, the India–UAE agreement on judicial cooperation in civil and commercial matters; confirm its current text).
2. **Service abroad from an Indian court.** Compare routes:
   - through the Central Authority under the Hague Service Convention;
   - under a bilateral agreement;
   - through diplomatic channels;
   - by the contract's agreed method or process agent, where the court permits;
   - by email or electronic service, where the court permits and the destination country does not object.

   Note that the destination country's objections matter for later enforcement there.
3. **Service in India of foreign proceedings.** Explain the route through the Indian Central Authority, and the effect of India's objection to postal service on recognition of a foreign judgment in India (link to `foreign-judgment-award-enforcement-analyst`).
4. **Evidence.** Choose between letters of request under the Hague Evidence Convention or a bilateral agreement, commissions, video-link evidence where the court allows it, and voluntary depositions. Check the destination's rules on pre-trial discovery requests.
5. **Translations.** List documents needing translation into the destination's language; hand off to `legal-translation-verifier`.
6. Build a timeline with realistic durations, marked as estimates, and fallback steps.

## Output

1. The recommended route, with legal basis and alternatives.
2. Document list (request forms, translations, copies).
3. Timeline and follow-up steps.
4. Risks to later enforcement.

## Guardrails

- Confirm treaty status and declarations from the HCCH and Ministry sources before relying on them.
- Do not suggest a service method that the destination country prohibits.
- Criminal matters: say that mutual legal assistance treaties and the Ministry of Home Affairs route apply instead, and stop. Do not give a civil route, document list, timeline or fallbacks; at most offer `extradition-mutual-legal-assistance-analyst`.
