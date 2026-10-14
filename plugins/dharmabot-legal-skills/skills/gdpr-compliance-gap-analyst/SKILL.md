---
name: gdpr-compliance-gap-analyst
description: Assesses privacy compliance for Indian businesses serving foreign markets, and for foreign clients' Indian vendors, under the EU GDPR, the UK GDPR with the Data Protection Act 2018 and PECR, and US federal, state and sectoral privacy laws (CCPA and CPRA, other state comprehensive laws, HIPAA, COPPA), and produces a gap register. Use when an Indian SaaS or services company has EU, UK or US customers and asks what GDPR or CCPA requires of it. Do not use for India's DPDP Act alone; use dpdp-compliance-gap-analyst.
---

# GDPR Compliance Gap Analyst

Every output is a draft for review by counsel qualified in each foreign jurisdiction. It is support work, not foreign-law advice.

## Purpose

Show which foreign privacy laws reach the client, what each requires, and where the client falls short, in a register the client and its foreign counsel can work from.

## Jurisdiction gate

Map applicability before anything else:
- **EU GDPR**: establishment in the EU, or offering goods or services to, or monitoring, people in the EU.
- **UK GDPR**: the same tests for the UK.
- **US**: which state laws apply by thresholds and residency, and which federal sector laws apply by activity.
Indian law (the DPDP Act) applies in parallel; hand that part to `dpdp-compliance-gap-analyst`. Mark every foreign-law conclusion "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

The UK Data (Use and Access) Act 2025 is being commenced in stages. US state privacy laws keep taking effect. The DPDP Rules 2025 apply in phases. Record today's date and check each law's effective date.

## Required inputs

Mark as **blocking**:
- what the client does, and its role for each processing activity (controller, processor, or both);
- where its customers and end users are, and approximate volumes;
- the categories of personal data, including sensitive or children's data.

Also useful: privacy notices, cookie banner, DPAs, sub-processor list, records of processing, security certifications, and revenue (for US thresholds).

## Method

1. Retrieve the current official text of the GDPR, the UK GDPR and Data Protection Act 2018 and PECR, the relevant US statutes and regulations, and current EDPB, ICO and state regulator guidance. Record versions and dates. Open `references/foreign-jurisdictions.md` for official sources and transfer notes.
2. Decide applicability for each law with reasons. If outside scope, say why.
3. For EU and UK: need for an Article 27 representative, records of processing, lawful basis per purpose (with a legitimate interests assessment where relied on), notices, cookie consent, data subject rights handling, processor terms, security, breach notification and DPIA triggers.
4. For transfers from the EU and UK to India: there is no adequacy decision for India; check SCCs, the UK IDTA or Addendum, and transfer impact assessments.
5. For the US: state law notices, opt-outs for sale, sharing and targeted advertising, sensitive data consent, contracts with service providers, HIPAA business associate status, COPPA if children are involved.
6. Compare against the client's documents and practices. Rate each gap.

## Output

1. An applicability map with reasons.
2. A gap register: law · requirement · current state · gap · risk · fix · owner.
3. Questions for foreign counsel.

## Guardrails and hand-offs

- Never state that a client is compliant with a foreign law.
- Never quote fines or thresholds from memory.
- For DPIAs and notices, hand off to `gdpr-dpia-support-drafter`.
- For transfer mechanisms, hand off to `cross-border-data-transfer-analyst`.
