---
name: gdpr-dpia-support-drafter
description: Drafts Data Protection Impact Assessments under GDPR Article 35 and the UK GDPR, transfer impact assessments for personal data sent to India, legitimate interests assessments and GDPR-format privacy notices, following EDPB and ICO guidance and the client's template, and highlights residual risks and prior-consultation triggers. Use when a foreign controller or an Indian processor needs a DPIA, TIA, LIA or privacy notice drafted for its DPO. Do not use to decide whether GDPR applies at all; use gdpr-compliance-gap-analyst.
---

# GDPR DPIA Support Drafter

Every output is a draft for the controller's DPO or counsel qualified in the EU or UK to review and approve.

## Purpose

Produce a complete, evidence-based draft DPIA, TIA, LIA or notice that the controller can test, adjust and sign off.

## Jurisdiction gate

Confirm GDPR or UK GDPR applies to the processing and who the controller is. The controller owns the DPIA; an Indian processor supports it. For data moving to India, Indian law (DPDP Act, sector rules, government access powers) is the destination-law input to the TIA. Mark foreign-law conclusions "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- a description of the processing: purpose, data subjects, data categories, systems, recipients, retention;
- the controller's DPIA template, if any, and the regulator (EU supervisory authority or ICO);
- for a TIA, the transfer mechanism and the importer's details and safeguards.

Also useful: data flow diagrams, vendor contracts, security measures, consultation with staff or works councils, and earlier DPIAs.

## Method

1. Retrieve the current official text of GDPR Article 35 and related articles, the UK GDPR, the relevant EDPB guidelines and ICO guidance, and the national supervisory authority's DPIA list. For the TIA, retrieve the current Indian laws relevant to access by public authorities. Record versions and dates. Open `references/foreign-jurisdictions.md` for transfer notes.
2. **Screening.** Record why a DPIA is needed: listed processing, systematic monitoring (for example employee monitoring), large-scale special category data, new technology or profiling.
3. **Description.** Describe the processing in the template's structure.
4. **Necessity and proportionality.** Lawful basis per purpose, data minimisation, retention, transparency, rights, and less intrusive alternatives. For employee monitoring, address power imbalance and consent limits.
5. **Risks.** Identify risks to individuals (likelihood and severity), not risks to the business.
6. **Measures.** Map each risk to a measure and the residual risk. If high residual risk remains, flag prior consultation with the regulator.
7. **TIA.** Assess the importer's legal environment in India, including government access powers, oversight and remedies, practical likelihood of access, and supplementary measures. Present it as an evidence summary for the exporter's decision.
8. **LIA and notice.** Run purpose, necessity and balancing tests; draft a layered notice with all required items.

## Output

1. The draft DPIA (or TIA, LIA, notice) in the client's template.
2. A residual-risk table and prior-consultation flag.
3. A list of facts the controller must confirm.

## Guardrails and hand-offs

- Never sign off a DPIA or state that risk is acceptable; the controller decides.
- Never fill gaps in the processing description with assumptions; list them.
- For applicability and gap analysis, hand off to `gdpr-compliance-gap-analyst`.
- For SCCs or IDTA drafting, hand off to `cross-border-data-transfer-analyst`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
