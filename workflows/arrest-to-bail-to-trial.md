# Arrest to bail to trial

**When to use:** a client or their family calls after an arrest, a summons or an FIR, and you will act for the accused through bail and trial.
**Who it is for:** criminal defence advocates, legal aid counsel and LADCS lawyers.

## Steps

1. `arrest-rights-advisor`. Input: what happened (summons, arrest, remand), dates and times. Output: the person's rights at each stage and immediate steps, including default bail timelines.
2. `client-intake-conflict-screener`. Output: intake note and conflict result. **STOP:** advocate accepts the brief. Use `legal-aid-eligibility-screener` if the accused may qualify for free legal aid.
3. `vakalatnama-appearance-drafter`. Output: vakalatnama for the remand court.
4. `crpc-bnss-transition-analyst`. Input: date of offence, FIR, stage. Output: whether old or new codes govern each stage.
5. `ipc-bns-concordance-mapper` if the FIR cites the old codes or mixes them. Output: mapped provisions to check.
6. `fir-ingredients-analyst`. Input: FIR. Output: ingredient-by-ingredient test of each offence alleged.
   **STOP:** advocate approves the theory of the defence before any bail draft. If the FIR discloses no offence, consider `fir-quashing-petition-drafter`.
7. Special statutes as applicable: `ndps-case-analyst`, `pocso-case-analyst` or `pmla-proceedings-analyst`.
8. `bnss-bail-application-drafter`. Input: approved grounds, ingredients analysis, antecedents. Output: regular or anticipatory bail application.
   **STOP:** advocate approves the grounds and conditions offered.
9. `limitation-calculator`. Output: default bail date, and any appeal period a special statute gives against a bail order (an ordinary bail refusal is usually met by a fresh application to a higher court, not an appeal; confirm). Enter them in `matter-deadline-tracker`.
10. `superdari-property-release-drafter` if a vehicle or property was seized. Output: interim custody application.
11. `chargesheet-review-analyst`. Input: police report and documents. Output: gaps, defects and defence points.
12. `bsa-electronic-evidence-certificate-drafter` review: check the prosecution's electronic-record certificates for defects.
13. `discharge-application-drafter`. Input: chargesheet analysis. Output: discharge application.
    **STOP:** advocate decides whether to seek discharge or reserve points for trial.
14. `undertrial-release-screener` if the accused remains in custody for long. Output: release eligibility note.
15. Trial preparation: `criminal-trial-readiness-checker` (evidence, witnesses), `witness-summons-list-drafter` (defence witnesses), `cross-examination-planner` (each prosecution witness), `court-exhibit-translation-drafter` for vernacular exhibits.
16. `sentencing-mitigation-analyst`. Output: mitigation and plea-bargaining options, prepared in parallel.
17. `hearing-day-brief-builder` before each listing.

## Deadlines to compute with `limitation-calculator`

- Default bail eligibility date from first remand.
- Any special-statute appeal against a bail order; revision against framing of charge; appeal against conviction.

## Before filing

18. `pre-filing-verification-checker` before every bail, discharge or quashing filing. **STOP:** advocate signs the verification log, then files.
