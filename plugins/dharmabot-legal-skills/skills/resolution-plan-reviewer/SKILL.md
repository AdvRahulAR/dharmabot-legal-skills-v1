---
name: resolution-plan-reviewer
description: Reviews resolution plans under the Insolvency and Bankruptcy Code, 2016 and the CIRP Regulations for applicant eligibility under section 29A, mandatory contents, treatment of operational and dissenting financial creditors, CIRP costs, implementation and monitoring, and the limits of the CoC's commercial wisdom. Use when an RP, CoC member, resolution applicant or creditor asks to check a plan before the vote, test section 29A risk, or challenge a CoC decision. Do not use for commercial viability or the liquidation waterfall; use liquidation-waterfall-calculator for the waterfall.
---

# Resolution Plan Reviewer

Every output is a review for an advocate or insolvency professional in India to check.

## Purpose

Test whether a resolution plan meets the Code and Regulations and whether the CoC's process and vote will withstand challenge.

## Jurisdiction gate

Confirm the plan is in a CIRP or PPIRP before an NCLT in India. If the applicant or its connected persons are foreign, mark foreign-law points (for example on disqualification abroad) for counsel qualified there.

## Temporal gate

Check the IBC and CIRP Regulations as they stood when the plan was submitted and when it is voted on. Regulation amendments in 2025 and the IBC (Amendment) Act, 2026 (provisions reported in force from 26 May 2026) may change contents, withdrawal or voting rules; confirm what applied on each date.

## Required inputs

Mark as **blocking**:
- the resolution plan and its annexures;
- the request for resolution plans and the evaluation matrix;
- the applicant's section 29A affidavit and group structure;
- the list of creditors and admitted claims.

Also useful: the information memorandum, liquidation and fair values (with confidentiality kept), CoC minutes and any objections.

## Method

1. Retrieve the current official text of the IBC (including section 29A, section 30 and section 31; confirm numbering) and the CIRP Regulations on plan contents and approval. Record versions and dates.
2. Test section 29A for the applicant and every connected person: NPA status, wilful defaulter, disqualifications, guarantees invoked and unpaid, and the MSME relaxations. Mark gaps in disclosure.
3. Check mandatory contents: payment of CIRP costs, minimum payment to operational creditors and dissenting financial creditors as the Code requires, management and control, implementation schedule, supervision, sources of funds, and the statement on how stakeholder interests are dealt with.
4. Check compliance with the request for resolution plans and any performance security.
5. Check the CoC vote: quorum, voting share, related-party exclusion, and recorded reasons. Note that courts give deference to the CoC's commercial wisdom but review legal compliance (for example Committee of Creditors of Essar Steel v. Satish Kumar Gupta, Supreme Court, 2019; confirm current treatment).
6. Check how the plan deals with claims not submitted, guarantees, tax and statutory dues, and pending litigation. Search for and read current authority; tag unread authority `[verify]`.

## Output

1. A compliance table: requirement, plan reference, compliant or not, note.
2. A section 29A risk note for the applicant and connected persons.
3. Points for the CoC or for an objection or appeal.

## Guardrails and hand-offs

- Do not give an opinion on commercial viability or value; the CoC decides that.
- Never disclose liquidation or fair value to applicants.
- Waterfall checks go to `liquidation-waterfall-calculator`; challenges to `nclt-nclat-appeal-drafter`; timelines to `cirp-ppirp-timeline-checker`.
- Never invent case law. Run `citation-verifier` before delivery.
