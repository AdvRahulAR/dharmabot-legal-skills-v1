---
name: document-legalisation-planner
description: Plans the notarisation, apostille or consular attestation, translation and stamping needed for a document moving between India and another country. Covers Indian documents for use in the US, UK, EU, Singapore (Apostille) or the UAE (attestation chain), and foreign documents for use in India, including powers of attorney for Indian property and affidavits for Indian courts. Use when someone asks "how do I get this apostilled", "can my client sign the POA in Dubai", or needs a document accepted abroad. Do not use for the legal content of the document itself.
---

# Document Legalisation Planner

Every output is a draft for an advocate enrolled in India to check. Requirements change and vary by authority; confirm with the receiving authority.

## Purpose

Give a step-by-step route, in the right order, for getting a document accepted in another country, with the authority at each step, the documents needed and the pitfalls.

## Jurisdiction gate

Identify the country where the document is signed, the country where it will be used, and the receiving authority (court, registry, bank, employer, sub-registrar). Read `references/foreign-jurisdictions.md` for Apostille Convention status. India, the US, the UK, Singapore and EU member States are parties; the UAE was not at the last check.

## Required inputs

Mark as **blocking**:
- the document type (power of attorney, affidavit, degree, company document, court document, contract);
- where it will be signed and where it will be used;
- who will use it, and for what.

Also useful: the receiving authority's written requirements, deadlines, and the signer's identity documents.

## Method

1. Retrieve the current requirements from official sources: the Ministry of External Affairs (apostille and attestation, including which documents need prior attestation by a State authority), the foreign country's mission in India or foreign ministry, and the HCCH status table.
2. **Indian document for use abroad.**
   - **Apostille country:** notarisation or issuing-authority attestation, then any required State-level attestation, then the MEA apostille.
   - **UAE:** notarisation, then MEA attestation, then UAE Embassy attestation in India, then UAE Ministry of Foreign Affairs attestation in the UAE. Add certified Arabic translation where the authority requires it.
3. **Foreign document for use in India.**
   - From an Apostille country: notarise and apostille there.
   - From the UAE: notarise, then UAE MOFA, then the Indian Mission.
   - For a power of attorney or deed for Indian property or court use, check s.33(1)(c) of the Registration Act, 1908, which covers authentication of a power of attorney executed abroad (by a notary, court, judge, magistrate, or Indian consul or vice-consul), and the State stamp law's time limit to pay duty after the document arrives in India. Hand off to `state-stamp-duty-calculator`. Some States and sub-registrars have extra format requirements; check them.
4. **Translation:** where the receiving authority needs one, specify certified or sworn translation. Hand off checking to `legal-translation-verifier`.
5. Give the order of steps, the expected documents at each step, and realistic points of failure (wrong signatory, missing State attestation, expired ID, inconsistent names).

## Output

1. A step table: step · authority · what to submit · notes.
2. A document checklist for the signer.
3. Stamping and registration steps in India, if relevant.
4. Points to confirm with the receiving authority.

## Guardrails

- Do not state fees or processing times unless taken from a current official page, with the date.
- Do not suggest bypassing attestation or using unofficial agents for official steps.
