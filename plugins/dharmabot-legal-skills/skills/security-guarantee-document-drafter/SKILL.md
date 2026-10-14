---
name: security-guarantee-document-drafter
description: Drafts and analyses Indian security packages, covering mortgages under the Transfer of Property Act, hypothecation, pledges of shares and movables, assignment of receivables, and corporate and personal guarantees under the Indian Contract Act, with perfection steps such as stamping, registration, ROC charge filing, CERSAI and depository pledge. Use when a lawyer asks for a mortgage by deposit of title deeds, hypothecation deed, share pledge or guarantee, or asks how to perfect security. Do not use for the facility agreement itself; use facility-agreement-reviewer.
---

# Security and Guarantee Document Drafter

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Draft the security and guarantee documents for a facility, and list every step needed to make the security valid, enforceable and ranked correctly.

## Jurisdiction gate

Confirm Indian law governs. Identify the State or UT where each immovable property sits and where each document will be executed. Stamp duty, registration and the treatment of a mortgage by deposit of title deeds (including notified towns and memorandum of entry practice) vary by State. If any asset or guarantor is outside India, mark the foreign-law points for counsel qualified there.

## Required inputs

Mark as **blocking**:
- the facility documents or sanction letter (amount, lender, borrower);
- each asset to be secured, with its owner and location (for land, the title documents and survey details);
- each guarantor, and whether it is a company, LLP or individual;
- the ranking intended (exclusive, first pari passu, second charge) and any existing charges.

Also useful: board and shareholder resolutions, the company's charge register, depository details for shares, and existing lenders' consents.

## Method

1. Retrieve the current official text of the Transfer of Property Act, the Indian Contract Act chapter on guarantees, the Companies Act charge and loan provisions, the CERSAI rules, the depository regulations on pledge, and the State stamp and registration law. Record versions and dates. Open `references/india-state-statutes.md` as a starting point for the State law.
2. Choose the security form for each asset: mortgage (simple, English, by deposit of title deeds), hypothecation of movables and receivables, pledge of goods or shares (depository pledge for dematerialised shares), or assignment.
3. Check the security provider's capacity and approvals. For companies, check the provisions on loans to directors and on loans, guarantees and security limits (believed to be sections 185 and 186 of the Companies Act, 2013; confirm), and special resolutions where required.
4. Draft each document: parties, recitals, secured obligations, charging clause, covenants, enforcement, power of attorney where needed, further assurance, and release.
5. For guarantees, address co-extensive liability, continuing guarantee, waiver of surety defences on variation and time given to the principal debtor, revocation, and demand mechanics. Note that waivers may be read narrowly; search for and read current authority and tag it `[verify]` if not read in full.
6. Prepare the perfection checklist: stamping (hand off to `state-stamp-duty-calculator`), registration within time where required, ROC charge filing (hand off to `roc-secretarial-compliance-checker`), CERSAI filing, depository pledge creation, and notices to debtors for receivables.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
7. Check priority against existing charges, statutory first charges and any intercreditor or pari passu arrangement.

## Output

1. Draft documents for each security and guarantee.
2. A perfection checklist: document, step, authority, deadline source, responsibility, status.
3. A short note on capacity, approvals, ranking risks and gaps in title.

## Guardrails and hand-offs

- Never state a stamp duty amount or filing deadline from memory.
- Do not draft security over assets the provider does not own or cannot charge, such as exempt agricultural land, without flagging it.
- Facility terms go to `facility-agreement-reviewer`.
- Never invent case law. Run `citation-verifier` before delivery.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
