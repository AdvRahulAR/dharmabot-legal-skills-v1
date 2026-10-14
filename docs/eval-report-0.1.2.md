# Eval report 0.1.2

Measured behaviour of the skills on the **criminal-bnss** and **cross-border** packs. The other 38 packs have not been run. The skills remain alpha. This report is the evidence behind that label, and it is not a quality mark.

## Headline

- **50 of 142 cases passed (35%).**
- 14 of the failing cases refer to an attached file (an FIR, contract or term sheet) that the runner cannot supply, so they cannot pass as written. Leaving them out, **50 of 128 passed (39%)**.
- The expected skill did not fire in 40 cases (28%).
- Cost: $46.01. Run date 2026-10-15, Claude Code 2.1.296, run model: Claude Code's default, grader model: sonnet.

## How it was run

`scripts/run_evals.py` sent each case's prompt to a fresh headless Claude Code session in an empty folder, with only this plugin loaded (`--setting-sources project`, no personal plugins). A case passes only if the expected skill fired and a second model call marked every `must` and `must_not` line as met. The grader is a model, not a lawyer. I read 16 of its verdicts (13 failures, 3 passes): most were fair, and a few were strict (for example "flag the NDPS bar at the top" failed when it appeared a few lines down). Treat the numbers as indicative.

## Results

| Pack | Passed | Total |
| --- | --- | --- |
| criminal-bnss | 26 | 74 |
| cross-border | 24 | 68 |

| Kind | Passed | Total |
| --- | --- | --- |
| gate | 31 | 70 |
| output | 19 | 71 |
| trigger | 0 | 1 |

## Why cases failed

| Reason | Cases |
| --- | --- |
| Expected skill did not fire | 34 |
| Skill fired, but a section or period was stated without a hedge, or a required hand-off or flag was missing | 28 |
| Skill fired, but another required item was missing | 16 |
| Needs an attachment the runner cannot supply | 14 |

## The date and hours cases (the main fix of 0.1.0 and 0.1.1)

30 cases test date arithmetic, count mismatches and hours deadlines. 4 passed. `date_calc.py` was run in 19 of them. When the dates disagree with the stated count, the model usually does notice. The failures were mostly of three kinds:

1. **The skill never fired**, so the model counted by hand. Short factual questions are the weak spot.
2. **The period was stated as settled** (for example the BNSS s.187(3) 60 days) without "believed" or "confirm", against the house standard.
3. **The mismatch was flagged, then relied on.** The model asked which figure was right and in the same answer carried on using one of them.

## Known limitations

- `data-breach-response-planner` does not fire on a quick "were we within time to report to CERT-In?" question. Three description changes did not fix it.
- Some gate cases (vague prompts such as "Compound the rape case") are answered by asking for the missing inputs without calling a skill. That is often the right behaviour, but the runner counts it as a miss.
- Statutory section numbers and periods are still sometimes stated flat when the skill is not engaged or its hedging step is skipped.
- Results vary between runs. A single run per case is not a stable measure.

## What this means for use

Use the skills as checklists and first drafts, with every section number, period and authority checked against the official text. Do not rely on a skill having fired: name it in the prompt (in Claude Code, `/dharmabot-legal-skills:<skill>`; in Codex, `$<skill>`) when the answer matters.

## Cases that failed

**Expected skill did not fire (34)**

`arbitration-gate`, `arrest-rights-advisor-date-calc`, `arrest-rights-advisor-date-mismatch`, `chargesheet-review-analyst-date-calc`, `chargesheet-review-analyst-date-mismatch`, `chargesheet-review-analyst-gate`, `cheque-dishonour-case-drafter-date-mismatch`, `concordance-gate`, `contract-us-enforceability`, `criminal-appeal-revision-drafter-date-calc`, `criminal-appeal-revision-drafter-date-mismatch`, `criminal-appeal-revision-drafter-gate`, `criminal-compounding-application-drafter-gate`, `cross-border-contract-reviewer-section-hedge-gate`, `cross-border-data-transfer-analyst-section-hedge-gate`, `crpc-bnss-transition-analyst-section-hedge-gate`, `document-legalisation-planner-section-hedge-gate`, `foreign-ip-office-action-support-drafter-gate`, `foreign-law-contract-support-reviewer-gate`, `gdpr-compliance-gap-analyst-gate`, `gdpr-compliance-gap-analyst-section-hedge-gate`, `india-entry-fema-structuring-analyst-date-calc`, `india-entry-fema-structuring-analyst-date-mismatch`, `legalisation-gate`, `legalisation-uae-poa`, `lpo-needs-protocol`, `ndps-case-analyst-date-mismatch`, `pmla-proceedings-analyst-date-mismatch`, `pmla-proceedings-analyst-gate`, `pmla-proceedings-analyst-proviso-gate`, `pocso-case-analyst-hours-mismatch`, `scoping-split-work`, `uae-difc-adgm-law-mapper-section-hedge`, `uae-difc-adgm-law-mapper-section-hedge-gate`

**Skill fired, but a section or period was stated without a hedge, or a required hand-off or flag was missing (28)**

`bail-date-mismatch`, `bail-default-bail-close`, `bsa-electronic-evidence-certificate-drafter-section-hedge`, `bsa-electronic-evidence-certificate-drafter-section-hedge-gate`, `cheque-dishonour-case-drafter-date-calc`, `cheque-dishonour-case-drafter-output`, `concordance-trigger`, `criminal-complaint-drafter-output`, `criminal-compounding-application-drafter-output`, `cross-border-contract-reviewer-section-hedge`, `cross-border-data-transfer-analyst-section-hedge`, `crpc-bnss-transition-analyst-section-hedge`, `discharge-application-drafter-date-calc`, `document-legalisation-planner-section-hedge`, `enforcement-difc-judgment-track-a`, `enforcement-dubai-award-track-b`, `eu-ai-digital-regulation-analyst-output`, `fema-land-border`, `fir-quashing-petition-drafter-output`, `foreign-client-engagement-checker-section-hedge`, `foreign-client-engagement-checker-section-hedge-gate`, `gdpr-compliance-gap-analyst-section-hedge`, `international-arbitration-planner-date-calc`, `ndps-case-analyst-date-calc`, `pmla-proceedings-analyst-proviso-classes`, `pocso-case-analyst-hours-calc`, `uk-pre-action-letter-drafter-date-calc`, `undertrial-release-screener-date-calc`

**Skill fired, but another required item was missing (16)**

`chargesheet-review-analyst-output`, `cheque-dishonour-case-drafter-gate`, `criminal-appeal-revision-drafter-output`, `discharge-application-drafter-gate`, `enforcement-date-mismatch`, `enforcement-gate`, `enforcement-us-judgment`, `extradition-mutual-legal-assistance-analyst-output`, `foreign-ip-office-action-support-drafter-date-calc`, `foreign-memo-no-invented-cases`, `pocso-case-analyst-gate`, `sentencing-mitigation-analyst-date-calc`, `sentencing-mitigation-analyst-date-mismatch`, `service-gate-criminal`, `uk-pre-action-letter-drafter-date-mismatch`, `undertrial-release-screener-output`

**Needs an attachment the runner cannot supply (14)**

`bail-default-bail-accrued`, `bail-default-gate-blocking-inputs`, `bail-special-statute`, `fir-ingredients-gate`, `fir-ingredients-quote`, `foreign-ip-office-action-support-drafter-output`, `foreign-law-contract-support-reviewer-output`, `gdpr-compliance-gap-analyst-output`, `gdpr-dpia-support-drafter-output`, `lpo-output`, `pmla-proceedings-analyst-date-calc`, `pmla-proceedings-analyst-output`, `uk-pre-action-letter-drafter-output`, `us-discovery-support-planner-output`
