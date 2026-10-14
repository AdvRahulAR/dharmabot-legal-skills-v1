---
name: healthcare-facility-compliance-checker
description: Checks compliance of Indian hospitals, clinics, diagnostic centres and telemedicine services under the Clinical Establishments Act 2010 or State equivalents, the PCPNDT Act 1994, the MTP Act 1971, the Transplantation of Human Organs and Tissues Act, the ART and Surrogacy Acts 2021, bio-medical waste rules, NMC and telemedicine guidelines and ABDM data norms. Use when a client is opening or auditing a hospital, scan centre, IVF clinic or teleconsultation platform. Do not use for drug or device licensing; use drugs-devices-regulatory-analyst.
---

# Healthcare Facility Compliance Checker

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Produce a gap list of the registrations, records and conduct rules a healthcare establishment must meet, and what to fix before opening or inspection.

## Jurisdiction gate

Confirm the establishment is in India and identify the State or UT and district. Some States adopted the Clinical Establishments Act 2010; others have their own nursing-home or clinical-establishment laws. PCPNDT, MTP and ART registrations are made with district or State appropriate authorities. Ask whether the client also operates online across States.

## Required inputs

Mark as **blocking**:
- the State and city;
- the type of establishment and services (beds, specialties, imaging, ultrasound, IVF, organ transplant, pharmacy, lab, teleconsultation);
- the registrations held or applied for.

Also useful: building and fire approvals, staff qualifications, equipment list, price list, consent forms, record-keeping systems and data flows.

## Method

1. Retrieve the current official text of the applicable State or central clinical establishments law and rules, the PCPNDT Act and Rules, the MTP Act and Rules, the THOTA and Rules, the ART and Surrogacy Acts and Rules, the Bio-Medical Waste Management Rules, the NMC conduct regulations and Telemedicine Practice Guidelines in force, and ABDM policies. Record versions and dates. Open `references/india-state-statutes.md` for the State's starting points.
2. Registration: identify the registering authority, category and standards; check display of registration and rates where the law requires.
3. **PCPNDT** (any ultrasound or imaging that could detect sex): registration of the centre and each machine, qualified operators, Form F and records, declarations, display boards, quarterly reports and retention periods. This is a high-risk area; defects can lead to sealing and prosecution.
4. **MTP, ART, surrogacy and transplant**: approval of the place, qualified providers, consent, registers and reporting.
5. Bio-medical waste: authorisation, segregation, tie-up with a common facility, and annual reports.
6. Professional and patient rights: qualified staff, informed consent, emergency care, records access, grievance redressal and price display.
7. Telemedicine and data: practitioner registration, identification, prescriptions limits, records, ABDM integration, and DPDP duties for health data.
8. Check State-specific items (fire NOC, pharmacy licence, radiation approval from AERB for X-ray and CT). Search for and read current authority on disputed points. Tag anything not read in full `[verify]`.

## Output

1. A compliance table: law · requirement · status · evidence · risk · fix.
2. A pre-opening or pre-inspection checklist.
3. A list of State registration specifics to confirm live.

## Guardrails and hand-offs

- Never treat a pending application as a registration.
- Never assist sex determination or advise on avoiding PCPNDT record-keeping.
- For applications, hand off to `licence-application-drafter`.
- For health-data compliance, hand off to `dpdp-compliance-gap-analyst`.
- Before delivery, send citations to `citation-verifier`.
