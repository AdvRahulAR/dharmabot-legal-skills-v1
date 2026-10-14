---
name: founders-agreement-drafter
description: Drafts founders' agreements for Indian startups under the Indian Contract Act 1872 and the Companies Act 2013, covering equity split, reverse vesting and good and bad leaver terms, roles and time commitment, IP assignment to the company, decision-making and deadlock, confidentiality, non-solicit and exit. Use when co-founders want a founders' agreement, a vesting schedule, leaver clauses or IP assignment before or after incorporation. Do not use for investor documents; use shareholders-agreement-drafter instead.
---

# Founders Agreement Drafter

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Record what the founders have agreed in a form that is enforceable, consistent with the company's articles, and ready for investor diligence.

## Jurisdiction gate

- Confirm the company is, or will be, incorporated in India, and the founders' residency. A non-resident founder brings FEMA issues on subscription and transfer: flag for `india-entry-fema-structuring-analyst`.
- If the company is not yet formed, plan incorporation with `company-incorporation-planner` and draft the agreement to be adopted by the company on incorporation.
- Record the State of execution for stamp duty.

## Required inputs

- **Blocking:** founders' names (synthetic in examples), equity split, and whether the company exists.
- **Blocking:** the vesting terms (period, cliff, acceleration) and what happens to unvested shares on exit.
- Useful: roles and titles, time commitment, salary, existing IP each founder brings, prior employer obligations, and any agreed decision rules.

## Method

1. Retrieve the current official text of the Indian Contract Act 1872 (including the restraint-of-trade provision), the Companies Act 2013 provisions on transfer of shares and buy-back, the Copyright Act 1957 on assignment formalities, and the State stamp schedule. Record the version and date.
2. Choose the reverse-vesting mechanism. Shares are usually issued upfront, with unvested shares subject to a transfer obligation. Explain the options (transfer to other founders or a nominee at a fixed price, or buy-back) and their Companies Act limits.
3. Draft the clauses:
   - equity, capital contribution and vesting schedule with cliff;
   - good leaver and bad leaver definitions and prices;
   - roles, responsibilities and full-time commitment;
   - IP: present assignment to the company of founder-created IP and pre-incorporation work, with moral rights waiver to the extent permitted; schedule of excluded prior IP;
   - decision-making, reserved founder matters, deadlock and escalation;
   - confidentiality and non-solicit;
   - non-compete during engagement only; note that post-exit non-competes are largely void under the Contract Act and give a narrow non-solicit instead;
   - transfer restrictions (lock-in, ROFR, tag) until a priced round;
   - dispute resolution (arbitration seat).
4. Check consistency with the AOA. Terms that must bind the company or restrict transfers should also go into the articles; list them.
5. Flag tax on share transfers at below fair value for a CA.
6. Compute stamp duty with `state-stamp-duty-calculator`.

## Output

1. Founders' agreement draft.
2. Vesting schedule table.
3. List of AOA amendments needed.
4. Founder IP assignment deed or schedule, handed to `ip-assignment-licence-drafter` if separate.

## Guardrails and hand-offs

- Do not pick an equity split for the founders; present options and trade-offs only.
- Do not draft a post-exit non-compete as enforceable.
- Cap table effects go to `cap-table-calculator`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
