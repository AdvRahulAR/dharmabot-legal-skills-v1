---
name: in-house-request-triage-screener
description: Triages incoming legal requests for in-house teams in India, classifying the request, giving a fast answer where the position is settled, rating risk by severity and likelihood under Indian contract, commercial and regulatory law, and routing it to the right approver or specialist skill. Use when the business asks whether something is a problem, wants a quick legal view on deal terms, or needs to know who must approve. Do not use for a full contract review; use playbook-contract-reviewer instead.
---

# In-house Request Triage Screener

Every output is a draft triage note for in-house counsel to review before it goes to the business.

## Purpose

Give the business a short, usable answer quickly, and make sure high-risk or fact-poor requests reach the right lawyer instead of being answered on thin information.

## Jurisdiction gate

- Confirm the company, the counterparty and the governing law of the deal or activity.
- Note the State where relevant (stamp duty, shops and establishments, local licences).
- If foreign law governs or a foreign regulator is involved, route to `foreign-matter-scoping-analyst` rather than answering.

## Required inputs

**Blocking**:
- what the business wants to do, with the actual terms or document;
- the deadline the business is working to;
- the company's own approval matrix or delegation of authority, if one exists.

Also useful: deal value, the counterparty and their bargaining power, the company's playbook positions, and past exceptions granted.

## Method

1. Retrieve the company playbook and approval matrix, and the current official text of any law the request turns on (India Code, regulator sites). Record versions and dates.
2. Classify the request: contract term, new product or feature, marketing claim, employment, data, regulatory, dispute or notice, corporate approval, or other.
3. Check whether the position is settled by the playbook. If yes, answer in two or three lines and cite the playbook clause.
4. If not settled, rate risk:
   - severity: financial exposure, regulatory penalty, reputational harm, precedent value;
   - likelihood: how often it goes wrong in practice and what controls exist.
   Combine into low, medium or high.
5. For common commercial asks, test the obvious points. Example: extended payment terms (cash flow, credit risk, any statutory payment timelines that bind the company if the supplier is a registered MSME) and uncapped liability (exposure, insurance cover, carve-outs in the playbook).
6. Escalate instead of answering where facts are missing, the risk is high, a regulator or court is involved, or the request needs a sign-off above the requester.
7. Name the approver under the matrix and the next skill if specialist review is needed.

## Output

1. Triage note: request · category · short answer or "escalated" · risk rating · approver · next step.
2. Conditions or fallback positions the business can offer.
3. Facts still needed.

## Guardrails and hand-offs

- Do not give a clean answer where facts are missing; ask or escalate.
- Do not override the approval matrix.
- Do not state penalties, rates or thresholds without the retrieved source.
- Route contract reviews to `playbook-contract-reviewer`, launches to `product-launch-legal-reviewer`, and regulatory questions to `regulatory-applicability-analyst`.
