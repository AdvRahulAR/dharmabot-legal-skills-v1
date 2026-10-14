---
name: hr-policy-handbook-drafter
description: Drafts employee handbooks and workplace policies for Indian employers, covering code of conduct, leave and holidays by State, attendance and remote work, IT and data use, grievance redressal, whistleblowing and disciplinary rules, aligned with standing orders under the Industrial Relations Code 2020 where they apply. Use when a client asks for an employee handbook, a leave policy, a remote-work policy or a handbook update. Do not use for a POSH policy or Internal Committee setup; use posh-compliance-advisor instead.
---

# HR Policy Handbook Drafter

Every output is a draft for an advocate enrolled in India to check before it is adopted.

## Purpose

Produce a handbook or set of policies that is lawful in every State where the employer operates, consistent with any standing orders, and practical to run.

## Jurisdiction gate

List every State or UT where the employer has staff. Leave, holidays, working hours, night work for women and Shops and Establishments rules vary by State. If a policy will apply to staff outside India, mark those parts for local counsel.

## Temporal gate

The Labour Codes are reported to be in force from 21 November 2025, with central and State rules notified in stages. Check the current position on standing orders, leave and working hours under the Codes and each State's rules before drafting. Note where old State rules may still apply in transition.

## Required inputs

Mark as **blocking**:
- the States and headcount in each, and whether any site is a factory or has workers covered by standing orders;
- the current handbook or policies, if any (for a diff);
- the policies requested.

Also useful: certified standing orders, existing practices on leave and attendance, IT systems used for monitoring, and union or works-committee arrangements.

## Method

1. Retrieve the current official text of the Industrial Relations Code and rules on standing orders, the OSH Code, the Code on Wages, each State's Shops and Establishments law and holiday rules, the DPDP Act and Rules, and any State festival-holiday law. Record the version and date of each.
2. Check whether the establishment crosses the standing-orders threshold under the IR Code. If so, the handbook must not conflict with certified or model standing orders. Note conflicts.
3. Build a State matrix for leave, holidays, hours, overtime and women's night-work permissions.
4. Draft each policy with purpose, scope, rules, process and owner. Typical set: code of conduct; leave and holidays; attendance and hybrid work; IT, devices and monitoring; data protection for employee data; anti-harassment and equal opportunity; grievance redressal; whistleblower; gifts, conflicts and anti-bribery; travel and expenses; disciplinary rules.
5. For monitoring and employee data, describe processing in a way that fits the DPDP Act notice and purpose requirements. Hand off gaps to `dpdp-compliance-gap-analyst`.
6. For an update, produce a diff against the current handbook and label each change as legal requirement, best practice or business choice.
7. Flag policies that need consultation, notice or consent before change, such as changes to service conditions for workers covered by the IR Code.

## Output

1. The draft handbook or policies.
2. The State matrix.
3. A change log for updates, and a list of items needing consultation or notice.

## Guardrails and hand-offs

- Do not reduce any statutory entitlement in a policy.
- Do not state leave numbers or thresholds as settled; mark each "confirm from the State rules".
- For the POSH policy and Internal Committee, hand off to `posh-compliance-advisor`.
- For registers, returns and establishment compliance, hand off to `labour-codes-compliance-checker`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
