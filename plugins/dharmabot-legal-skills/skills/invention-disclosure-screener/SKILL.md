---
name: invention-disclosure-screener
description: Screens an invention disclosure under the Patents Act 1970 for novelty, inventive step and industrial application, the section 3 exclusions (including section 3(d) and section 3(k) with the current Computer Related Inventions Guidelines), prior-disclosure risks and grace periods, and inventorship and ownership, and recommends file, hold or trade secret. Use when engineers or founders ask whether an invention, software or AI model is patentable in India. Do not use for drafting the specification; use patent-specification-drafter instead.
---

# Invention Disclosure Screener

Every output is a draft screening review for a registered patent agent or advocate in India to check.

## Purpose

Decide whether an invention is worth filing in India, what could block it, and what to do first.

## Jurisdiction gate

Confirm the screening is for an Indian filing. If the client may file abroad or via PCT, note that novelty and patentable subject matter differ by country and mark those points for local counsel. Check whether the invention was made in India, because filing abroad first may need a foreign filing permit.

## Required inputs

Mark as **blocking**:
- a description of the invention: problem, solution, how it works and what is new;
- every public disclosure so far (papers, demos, pitch decks, websites, sales, open-source releases), with dates;
- the inventors and their relationship to the applicant (employees, consultants, university).

Also useful: known prior art, competing products, drawings, data showing improved efficacy, and funding or grant terms.

## Method

1. Retrieve the current official text of the Patents Act and Rules, the current Manual of Patent Office Practice and Procedure, and the current CRI Guidelines and any pharmaceutical or biotech guidelines. Record the version and date.
2. Build a short invention summary in claim-like terms: the features that make it work.
3. **Section 3 exclusions** (section 3 and its clauses 3(k) and 3(d) are believed to be the right provisions; confirm each against the official text): test each relevant clause. For software and AI, apply section 3(k) on computer programs per se and algorithms, and look for a technical effect or technical contribution as the CRI Guidelines and current High Court authority describe. For new forms of known substances, apply section 3(d) and its efficacy requirement. Read current authority before relying on it; tag anything not read in full `[verify]`.
4. **Novelty:** list the client's own disclosures and check the limited grace-period provisions (confirm which apply). Flag where a disclosure has likely destroyed novelty.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
5. **Inventive step and industrial application:** identify the closest known approach and what is non-obvious over it; note what a prior-art search must cover.
6. **Inventorship and ownership:** check employment and consultancy agreements and university or grant rules. Flag missing assignments.
7. Recommend file now (provisional), hold, publish defensively, or keep as a trade secret, with reasons.

## Output

1. A screening sheet: invention summary · exclusions · novelty risks · inventive-step view · ownership · recommendation.
2. Search instructions for a prior-art search.
3. Immediate actions (stop disclosures, sign assignments, file provisional).

## Guardrails and hand-offs

- Never present the screen as a patentability opinion or a prior-art search.
- Never invent prior art or patent numbers.
- For specification drafting, hand off to `patent-specification-drafter`.
- For launch risk from others' patents, hand off to `freedom-to-operate-analyst`.
