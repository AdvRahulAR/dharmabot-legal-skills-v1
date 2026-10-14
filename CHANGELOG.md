# Changelog

## 0.1.0 (2026-10-14), alpha

First public release. Law as of 14 October 2026. Every skill was reviewed for legal accuracy after drafting; none has yet been signed off by an enrolled advocate.

**317 skills in 39 packs**, covering the full range of Indian legal work, all 36 States and Union Territories, Indian languages, and cross-border work with the US, UK, UAE, EU and Singapore. The full list is in [docs/CATALOGUE.md](docs/CATALOGUE.md).

**Coverage**
- Mapped against more than 700 skills in published legal skill collections:
  - Anthropic's claude-for-legal and knowledge-work legal plugin;
  - Rohas Nagpal's Legal AI Skills;
  - Lawve and Lawvable;
  - UK, US and Indian repositories.
- A second gap analysis (October 2026) covered daily court practice, tribunals and recent regulation. From 117 suggestions, 54 new skills were added and 57 were already covered.
- New packs:
  - court craft (cause lists, e-filing defects, vakalatnama, adjournment, condonation, restoration, amendment, substitution, compromise, caveat, mentioning, hearing-day briefs);
  - tribunal practice;
  - client documents;
  - sectoral regulatory (RBI digital lending and Master Directions, FEMA compounding, SEBI AIFs and others);
  - emerging technology and climate (DPDP consent managers, dark patterns, carbon credits, deepfake remedies);
  - AI practice safeguards;
  - review and analysis (tabular review, pleadings matrix).

**Safeguards**
- `pre-filing-verification-checker` checks every authority and quotation against an official source and keeps a log. Every drafting skill hands off to it, following the Supreme Court's ruling in *Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd.* (2026 INSC 668) that citing unverified AI-generated judgments is misconduct.
- `client-data-redaction-checker` pseudonymises client data before AI processing.
- Temporal gates handle recent changes:
  - the IBC (Amendment) Act, 2026;
  - the Income-tax Act, 2025;
  - the Labour Codes;
  - the DPDP Rules phasing;
  - the 2026 IT Rules amendment;
  - the Online Gaming Act;
  - the Press Note 3 relaxation;
  - the omission of compulsory probate.

**Workflows and profile**
- Ten matter recipes in `workflows/`, each with STOP checkpoints for the advocate.
- `legal-task-router` chooses skills and recipes.
- A practice profile template in `templates/dharmabot-profile.md`.

**Reference tables**
- `shared/references/india-state-statutes.md`: court fees, stamp, tenancy, High Court, rules of practice and official languages for every State and UT. Unverified rows are marked.
- `shared/references/foreign-jurisdictions.md`: India's treaty position with the US, UK, UAE, EU and Singapore, official sources, professional rules and data-protection regimes.

**Tooling**
- Plugin manifests for Claude Code and Codex.
- An install script for Codex, Antigravity and Claude Code that can install single packs.
- A build script that generates metadata, the catalogue and copies of shared references.
- A validator that checks:
  - the skill standard;
  - hand-offs, and the skills named in workflows;
  - eval coverage;
  - personal data.
- Unit tests for the bundled scripts, and 639 behavioural eval cases.
- README images in `docs/images/`.
