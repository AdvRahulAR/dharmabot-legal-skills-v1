---
name: trademark-examination-reply-drafter
description: Drafts replies to Indian trademark examination reports under the Trade Marks Act 1999, answering section 9 distinctiveness and descriptiveness objections with acquired-distinctiveness evidence and section 11 citations distinguished on marks, goods and trade channels, and requesting hearing, amendment or consent. Use when a client has received an examination report, a TM objection or a citation of prior marks. Do not use for opposing a third party's advertised mark; use trademark-opposition-drafter instead.
---

# Trademark Examination Reply Drafter

Every output is a draft for an advocate or registered trademark agent in India to check and file.

## Purpose

Overcome the Registry's objections with a focused reply, supported by real evidence, filed within time.

## Jurisdiction gate

Confirm the report issued from the Indian Trade Marks Registry and record the application number, class and office. For an international registration designating India, note the different response process and timelines.

## Required inputs

Mark as **blocking**:
- the examination report, with its date of issue or dispatch;
- the application as filed (mark, class, specification, user claim);
- details of each cited mark (owner, status, goods) from the Registry record.

Also useful: evidence of use (sales, advertising spend, media, surveys), any consent or co-existence agreement, and the client's other registrations.

## Method

1. Retrieve the current official text of the Trade Marks Act and Rules, the Registry's examination manual, and the application's current status on the Registry website. Record the version and date.
2. Compute the reply deadline from the report (reported as one month, with consequences of non-reply including abandonment; confirm from the Rules and the report). Use `limitation-calculator` if helpful, and flag urgency at the top.
3. **Section 9 objections:** argue inherent distinctiveness (suggestive not descriptive, coined combination, overall impression); then acquired distinctiveness under the proviso with evidence tied to dates before filing. Offer a disclaimer or specification limit only on instructions.
4. **Section 11 objections:** for each citation, distinguish on marks as a whole, goods and services, trade channels and consumers; check the citation's status (abandoned, removed, opposed); plead honest concurrent use with evidence where facts support it; propose a consent letter where available.
5. Consider amending the specification to remove overlap, keeping the client's core goods.
6. Search for and read current authority supporting each argument. Tag anything not read in full `[verify]`.
7. Request a hearing in the alternative.
8. Draft any supporting affidavit of use, with exhibits indexed.

## Output

1. The draft reply with headings by objection.
2. A citation comparison table.
3. A draft affidavit of use and exhibit list, where needed.
4. A deadline note and a hearing-preparation checklist.

## Guardrails and hand-offs

- Never fabricate or inflate evidence of use or sales figures.
- Never invent a case, citation or Registry decision.
- If the mark is published and opposed, hand off to `trademark-opposition-drafter`.
- If the mark needs refiling in a better form, hand off to `trademark-application-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
