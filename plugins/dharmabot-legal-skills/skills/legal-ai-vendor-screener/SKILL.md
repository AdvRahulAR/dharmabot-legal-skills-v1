---
name: legal-ai-vendor-screener
description: Screens AI tools an Indian law firm, chamber or legal department plans to use, covering training on client data, retention, data location and sub-processors, security, privilege and confidentiality under the BCI Rules and the Bharatiya Sakshya Adhiniyam, DPDP Act processor terms, citation safeguards and exit, with a red-amber-green summary. Use when a lawyer asks "evaluate this legal AI tool", "vendor questionnaire for an AI research product" or "is it safe to put client files in this tool". Do not use for AI contracts of non-legal business clients; use ai-vendor-contract-reviewer instead.
---

# Legal AI Vendor Screener

Every output is a review for the managing partner, general counsel or supervising advocate to check.

## Purpose

Decide whether a legal practice can safely put client material into an AI tool, on what settings and terms, and what to negotiate or refuse.

## Jurisdiction gate

Confirm the buyer is an Indian practice or legal team. Record where the vendor is established and where data is processed. Foreign-law terms (for example a US governing-law clause) are flagged "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

DPDP Act, 2023 duties are being brought into force in phases under the DPDP Rules, 2025. Check which apply on today's date. Check for any notified restriction on transfers outside India.

## Required inputs

Mark as **blocking**:
- the tool name, plan or tier, and deployment (cloud, private cloud, on-premise);
- the vendor's terms of service, privacy policy, data processing terms and security documentation;
- the intended use and the kind of client data involved.

Also useful: size of the practice, client contract restrictions on AI or offshoring, and existing IT policies.

## Method

1. Retrieve the current official text of the DPDP Act and Rules, the CERT-In directions on incident reporting and logs, the BCI Rules on confidentiality, and the Bharatiya Sakshya Adhiniyam provisions on professional communications. Record version and date. Retrieve the vendor documents current today and record their dates.
2. Issue or complete a questionnaire covering:
   - model training on customer data, and opt-out by default or on request;
   - retention, deletion on request and at exit, and backups;
   - data location, sub-processors and transfer mechanisms;
   - certifications (for example ISO 27001, SOC 2) with report dates;
   - access controls, encryption, single sign-on, audit logs, and staff access by the vendor;
   - breach notice time and cooperation;
   - legal requests from governments and how the client is told;
   - output safeguards (source links, citation checking, hallucination controls);
   - liability, indemnity, IP in outputs, and exit and data export.
3. Test the terms against each answer. Note where the terms contradict marketing claims.
4. Assess privilege and confidentiality exposure: who can read prompts and outputs, and whether disclosure to the vendor risks waiver arguments.
5. Check whether the vendor will sign processor terms that meet DPDP duties.
6. Rate each area red, amber or green, with the fix for every red and amber.

## Output

1. Completed or draft vendor questionnaire.
2. Red-amber-green summary table: area · finding · source clause · rating · action.
3. Recommended settings and use limits (for example "no client identifiers; use `client-data-redaction-checker` first").
4. Negotiation points for the contract.

## Guardrails and hand-offs

- Rely only on documents read. Mark vendor claims without written support "unverified".
- Do not certify a tool as compliant. This is a risk screen.
- Ethics questions go to `professional-conduct-advisor`.
- Contract review for non-legal business clients goes to `ai-vendor-contract-reviewer`.
