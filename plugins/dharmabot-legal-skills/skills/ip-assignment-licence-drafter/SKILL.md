---
name: ip-assignment-licence-drafter
description: Drafts and reviews IP assignments, licences and technology transfer agreements under Indian law, covering copyright assignment formalities, trademark assignment with or without goodwill, patent assignment and recordal, exclusive and non-exclusive licences, field and territory limits, royalties, sublicensing, improvements and quality control, with stamp duty, withholding tax and FEMA flags. Use when a client needs a founder-to-company IP assignment, a software or brand licence, or a technology transfer agreement. Do not use for a general commercial MSA; use msa-sow-drafter instead.
---

# IP Assignment Licence Drafter

Every output is a draft for an advocate enrolled in India to check before execution.

## Purpose

Transfer or license IP cleanly, so that ownership is provable, recordal is possible, and payment and use terms are enforceable.

## Jurisdiction gate

Confirm the governing law and the State of execution (stamp duty varies by State). If either party is outside India, flag FEMA, withholding tax and the treaty position, and mark foreign-law points for local counsel.

## Required inputs

Mark as **blocking**:
- the parties, their legal status and the State where the document will be signed;
- the IP to be transferred or licensed, identified precisely (registration and application numbers, software modules, works);
- whether the assignor or licensor actually owns it today, with evidence;
- the consideration or royalty structure.

Also useful: existing licences or encumbrances, open-source components in software, and the business purpose.

## Method

1. Retrieve the current official text of the Copyright Act (assignment and licence provisions), the Trade Marks Act (assignment and registered user or licence provisions), the Patents Act (assignment and licence in writing, registration), the Designs Act, the State stamp law, and current FEMA and income-tax provisions on royalties. Record the version and date.
2. Verify the chain of title. Flag IP not yet owned by the assignor, such as freelancer work without assignment or a founder's pre-incorporation work, and fix it first.
3. **Assignment:** draft operative words of present assignment, schedule of IP, rights in all media and territories, moral-rights waiver or non-assertion where allowed, further-assurance and power of attorney for recordal, and warranties.
4. For trademarks, decide assignment with or without goodwill and check the advertisement and approval requirements for assignment without goodwill.
5. **Licence:** grant, exclusivity, field and territory, term, sublicensing, royalties and audit, improvements and grant-back, quality control for trademarks, confidentiality, IP enforcement, termination and post-termination use.
6. **Technology transfer:** add know-how delivery, training, acceptance and source-code escrow where relevant.
7. Flag recordal with the Trade Marks Registry, Patent Office or Copyright Office, and the forms and time to confirm.
8. Flag stamp duty with `state-stamp-duty-calculator`, and withholding tax and FEMA on cross-border royalties.

## Output

1. The draft assignment, licence or agreement with schedules.
2. A chain-of-title note and recordal checklist.
3. A tax, stamp and FEMA flag list.

## Guardrails and hand-offs

- Never draft an assignment of IP the assignor cannot show it owns without flagging it.
- Never state stamp rates or tax rates from memory.
- For cross-border structuring, hand off to `india-entry-fema-structuring-analyst`.
- To log the transferred assets, hand off to `ip-portfolio-tracker`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
