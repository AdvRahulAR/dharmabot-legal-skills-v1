---
name: foreign-ip-office-action-support-drafter
description: Drafts first-cut responses, for foreign attorneys to review and file, to trademark and patent office actions before the USPTO, UKIPO, EUIPO and other offices, covering likelihood-of-confusion and descriptiveness arguments, claim amendments and prior-art distinctions, and evidence lists, in the instructing attorney's format. Use when a US, UK or EU attorney asks for a draft response to a refusal or office action. Do not use for Indian trademark or patent filings; use trademark-examination-reply-drafter or patent-fer-reply-drafter.
---

# Foreign IP Office Action Support Drafter

Every output is a draft for the instructing foreign attorney to review, sign and file. It is not advice on foreign law.

## Purpose

Give the instructing attorney a well-reasoned first draft that addresses every ground in the office action, with evidence and amendments mapped.

## Jurisdiction gate

Identify the office (USPTO, UKIPO, EUIPO, EPO or another), the application, and the instructing attorney's qualification to act before it. Filing and signature stay with that attorney. Indian filings go to `trademark-examination-reply-drafter` or `patent-fer-reply-drafter`. Mark every foreign-law point "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the office action in full, with its issue date and response deadline;
- the application as filed (mark, goods and services, or claims and specification);
- the cited marks or prior art;
- the instructing attorney's format and any instructions on arguments or amendments.

Also useful: evidence of use or acquired distinctiveness, coexistence agreements, market evidence, and the inventor's or client's technical explanation.

## Method

1. Retrieve the current official text of the office's procedure manual and rules (for example the TMEP or MPEP for the USPTO, the UKIPO manuals, EUIPO guidelines), and confirm the response period and extension rules. Record versions and dates. Open `references/foreign-jurisdictions.md` for official sources.
2. Docket the deadline and any extension available; report it to the attorney for confirmation.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
3. List every ground in the action and plan a response to each. Do not skip formal objections.
4. **Trademarks.** For confusion refusals, build arguments on marks, goods or services, channels, purchasers and coexistence, using the office's test as stated in its manual. For descriptiveness, argue suggestiveness or acquired distinctiveness with evidence. Consider amendments to the specification.
5. **Patents.** Map each claim to the cited art, identify distinguishing features, propose amendments with support in the specification, and address clarity and support objections.
6. Draft the response in the attorney's format, with an evidence index.
7. Search for and read office decisions or case law the attorney may cite. Tag anything not read in full `[verify]`.

## Output

1. The draft response.
2. An issue table: ground · response · evidence · amendment.
3. A note for the attorney: deadline, risks, and choices that need their judgement.

## Guardrails and hand-offs

- Never file or communicate with the foreign office.
- Never add matter to a patent specification or invent evidence of use.
- For research on a foreign-law point, hand off to `foreign-law-research-memo-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
