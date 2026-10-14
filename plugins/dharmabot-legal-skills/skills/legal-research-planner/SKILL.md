---
name: legal-research-planner
description: Breaks an Indian legal question into issues and sub-issues and builds a sourced research plan listing the statutes, rules, notifications and leading judgments to check, the official sources (India Code, eGazette, Supreme Court and High Court websites, regulator sites) and search terms, flagging recent changes such as the BNS, BNSS, BSA, Labour Codes and Income-tax Act 2025. Use when a lawyer asks to plan research, scope a research question or list what to look up. Do not use to write the answer; use research-memo-drafter instead.
---

# Legal Research Planner

Every output is a draft research plan for the advocate or supervising counsel to review; it states no conclusions.

## Purpose

Make research complete and efficient: every issue identified, every primary source named, and every recent change in law flagged before anyone starts writing.

## Jurisdiction gate

- Confirm the question is under Indian law and identify the State or UT where State laws, rules or High Court practice may differ.
- Note which High Court's decisions bind the forum, and which are only persuasive.
- If any part turns on foreign law, list it separately for `foreign-law-research-memo-drafter`.

## Temporal gate

Record the date of the relevant events. Where the law changed (for example the criminal codes from 1 July 2024, the Labour Codes, the Income-tax Act 2025, the Mediation Act 2023, the DPDP Rules), plan research on both the old and new law and on the transition and savings provisions. Check whether each new law is in force and from when.

## Required inputs

**Blocking**:
- the question as the advocate frames it;
- the key facts and dates;
- the forum and the client's position (claimant, respondent, adviser).

Also useful: the deadline, research databases available, and authorities already known.

## Method

1. Retrieve the current official text of each statute and rule likely to apply from India Code, the eGazette or the regulator's site, and record the version and date. Note any pending amendment or bill.
2. Split the question into issues and sub-issues. Write each as a yes or no question where possible.
3. For each issue, list:
   - statutory provisions and rules (names first; section numbers only as "believed to be", to be confirmed);
   - notifications, circulars and regulator guidance;
   - the kind of judgments needed (Constitution Bench, larger bench, jurisdictional High Court) and how to find them;
   - secondary sources (Law Commission reports, committee reports, commentaries).
4. Draft search terms and Boolean strings for SCC Online, Manupatra, Indian Kanoon and court websites, including old and new provision names.
5. Flag traps: overruled or referred decisions, pending reference to a larger bench, conflicting High Courts, recent renumbering.
6. Add a research log template: source · date accessed · version · result · read in full (yes or no).
7. Set the order of work: statute first, then binding authority, then persuasive authority, then secondary.

## Output

1. Issue tree.
2. Source table: issue · source · where to get it · priority · status.
3. Search terms.
4. Research log template.
5. Open questions for the advocate.

## Guardrails and hand-offs

- Do not state conclusions or predict outcomes.
- Do not list a case as authority unless it is known to exist; otherwise describe what to search for. Tag uncertain items `[verify]`.
- Hand off writing to `research-memo-drafter`, provision analysis to `statutory-interpretation-analyst`, and citation checks to `citation-verifier`.
