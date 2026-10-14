# Defending a civil suit

**When to use:** a client has been served with summons, or learns a suit has been filed against them.
**Who it is for:** advocates acting for a defendant in a civil or commercial suit.

## Steps

1. `client-intake-conflict-screener`. Input: summons, plaint copy, client's account. Output: intake note and conflict result.
   **STOP:** advocate clears the conflict and accepts the brief.
2. `vakalatnama-appearance-drafter`. Output: vakalatnama or memo of appearance for the first date.
3. `limitation-calculator`. Input: date of service, type of suit (ordinary, commercial, summary). Output: last date for the written statement, or in a summary suit the dates to enter appearance and (after the summons for judgment is served) to apply for leave to defend, and the outer limit, with working.
   Enter it in `matter-deadline-tracker` immediately.
4. `litigation-chronology-builder`. Input: plaint, documents. Output: source-linked chronology.
5. `issue-spotting-analyst`. Input: plaint and chronology. Output: ranked issues, including maintainability, jurisdiction, limitation and valuation.
6. `litigation-strategy-planner`. Input: issues, client's goals. Output: defend, settle or counterclaim, and which threshold objections to take.
   **STOP:** advocate approves the defence strategy and preliminary objections.
7. If it is a summary suit under Order XXXVII: enter appearance within the time in the summons first (step 2), then use `summary-suit-order-xxxvii-drafter` once the summons for judgment is served. Output: leave-to-defend application. If leave is granted, return to step 8 for the written statement within the time the court fixes; otherwise skip to step 11.
8. `written-statement-drafter`. Input: approved strategy, plaint, documents. Output: written statement with preliminary objections, parawise reply, and any set-off or counterclaim.
   **STOP:** advocate approves the reply to each averment and any counterclaim.
9. `pleadings-matrix-builder`. Output: matrix of admissions, denials and likely issues, to check nothing is left unanswered.
10. Interim applications as needed, through `civil-interlocutory-application-drafter`: rejection of plaint, setting aside an ex parte order or decree under Order IX, condonation of delay if the written statement is late (in a commercial suit the outer limit is reportedly not extendable; confirm current authority), transfer, or amendment. Use `interim-injunction-application-drafter` for replies to an injunction application.
    **STOP:** advocate approves each application before filing.
11. If the suit is commercial: `order-xi-disclosure-planner`. Output: disclosure and admission-denial plan with dates.
12. `state-court-fee-calculator` if there is a counterclaim. Output: court fee with arithmetic.
13. `court-pleading-formatter` and `efiling-bundle-defect-checker`. Output: formatted, compliant filing.
14. `hearing-day-brief-builder`. Output: brief for the next listing.

## Deadlines to compute with `limitation-calculator`

- Written statement or leave-to-defend: ordinary and outer time limits from service.
- Limitation for any counterclaim.
- Disclosure and admission-denial dates in a commercial suit.

## Before filing

15. `pre-filing-verification-checker`. Input: written statement, applications and documents. Output: signed verification log. **STOP:** advocate signs the log, then files.
