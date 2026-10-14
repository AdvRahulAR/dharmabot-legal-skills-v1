---
name: patent-fer-reply-drafter
description: Drafts responses to Indian patent First Examination Reports and hearing written submissions under the Patents Act 1970, covering claim amendments within section 59, novelty and inventive-step arguments against cited documents, section 3 objections, sufficiency, unity and formal requirements, within the statutory response period, and replies to pre-grant oppositions. Use when a client has received an FER, a hearing notice or a pre-grant opposition in India. Do not use for drafting a fresh specification; use patent-specification-drafter instead.
---

# Patent FER Reply Drafter

Every output is a draft for a registered Indian patent agent to review, sign and file.

## Purpose

Put the application in order for grant by answering every objection, with amendments that are allowed and arguments that are supported.

## Jurisdiction gate

Confirm the FER issued from the Indian Patent Office and record the application number, office and examiner. For a corresponding foreign family, collect foreign prosecution history, which may need to be disclosed, but mark foreign-law points for local counsel.

## Required inputs

Mark as **blocking**:
- the FER (or hearing notice or opposition), with its date of issue;
- the specification and claims as filed and as currently on record;
- copies of each cited document (D1, D2 and so on).

Also useful: status of foreign counterparts and their allowed claims, the inventor's technical comments, and experimental data.

## Method

1. Retrieve the current official text of the Patents Act and Rules, the Manual of Patent Office Practice and Procedure, the CRI Guidelines where relevant, and the application's file on the Patent Office website. Record the version and date.
2. Compute the response deadline (reported as six months from the FER, extendable on request; confirm the period and extension rules). Use `limitation-calculator`. Flag urgency at the top.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
3. Build an objection table from the FER: number · objection · provision · response plan.
4. **Amendments:** propose claim amendments by way of disclaimer, correction or explanation, within section 59 (believed to be the section; confirm against the official text). Check each amended claim has basis in the specification as filed; flag any amendment that adds matter or broadens scope.
5. **Novelty and inventive step:** map each claim feature against D1, D2 and others; identify differences; argue technical effect and why the skilled person would not combine the documents. Avoid admissions that may be used later.
6. **Section 3 objections** (section 3 and its clauses 3(k) and 3(d) are believed to be the right provisions; confirm each against the official text): argue technical contribution (for 3(k)) or efficacy with data (for 3(d)), as the facts allow.
7. Address sufficiency, clarity, unity, and formal requirements (Form 3 updates, priority documents, proof of right, Form 1 corrections).
8. Search for and read current authority supporting each legal argument. Tag anything not read in full `[verify]`.
9. For a hearing, draft written submissions to follow within the period allowed. For a pre-grant opposition, draft a reply statement with evidence.

## Output

1. The draft FER response with amended claims (clean and marked-up).
2. The objection table.
3. A deadline and hearing-preparation note.

## Guardrails and hand-offs

- Never invent experimental data or technical effects.
- Never mischaracterise cited documents.
- Filing and signing are done by the applicant or a registered patent agent, not by this skill. An advocate who is not a patent agent is believed to be limited to appearing at hearings; confirm from the Patents Act.
- For a refiled or divisional application, hand off to `patent-specification-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
