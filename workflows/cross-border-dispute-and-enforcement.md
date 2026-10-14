# Cross-border dispute and enforcement

**When to use:** an Indian client has a dispute with a foreign party (or a foreign client with an Indian party) and wants to recover money or enforce a judgment or award in India.
**Who it is for:** Indian advocates on cross-border matters, working with qualified foreign counsel where foreign law applies.

## Steps

1. `foreign-matter-scoping-analyst`. Input: contract, correspondence, parties' locations. Output: governing law, possible forums and who must advise on foreign law.
2. `foreign-client-engagement-checker` if the client is foreign; otherwise `client-intake-conflict-screener` and `engagement-letter-drafter`. Output: conflicts, permissions, FEMA and GST on fees, and the engagement letter.
   **STOP:** advocate accepts the brief and confirms foreign counsel is engaged for foreign-law questions.
3. `limitation-calculator`. Input: cause of action dates. Output: Indian limitation, with a flag that foreign limitation must come from foreign counsel.
4. `cross-border-contract-reviewer` and `arbitration-clause-reviewer`. Input: the contract. Output: dispute clause, seat and enforceability analysis.
5. `litigation-strategy-planner`. Input: scoping note and clause analysis. Output: arbitration, Indian court, foreign court or settlement, with where the assets are.
   **STOP:** advocate and client approve the forum and route.
6. If arbitration: `international-arbitration-planner` (seat, institution, interim relief), then `arbitration-invocation-notice-drafter` and `arbitral-proceedings-drafter`. Use `section-9-interim-relief-drafter` for interim relief from an Indian court.
7. If an Indian court: follow [civil-suit-to-first-hearing](civil-suit-to-first-hearing.md). If a UK court: `uk-pre-action-letter-drafter` for review by UK solicitors.
   **STOP:** advocate approves the notice or pleading before it is sent.
8. `cross-border-service-evidence-planner`. Output: route for serving documents and taking evidence abroad.
9. `document-legalisation-planner` and `legal-translation-verifier`. Output: notarisation, apostille or attestation steps, and checked translations.
10. `settlement-strategy-planner` at each stage. Output: settlement range against likely outcomes.
11. After a judgment or award: `foreign-judgment-award-enforcement-analyst`. Input: judgment or award, country, assets in India. Output: enforcement route (reciprocating territory, Convention award, or fresh suit) and defences to expect.
    **STOP:** advocate approves the enforcement route.
12. `execution-contempt-petition-drafter`. Output: execution or enforcement petition. Use `section-34-37-award-challenge-drafter` to resist a challenge to an India-seated award. A foreign-seated award is not challenged under section 34 in India; objections to its enforcement are under Part II of the Arbitration and Conciliation Act, 1996, handled with `foreign-judgment-award-enforcement-analyst`.
13. `india-entry-fema-structuring-analyst` or `dtaa-withholding-analyst` for repatriating or remitting recovered sums.

## Deadlines to compute with `limitation-calculator`

- Limitation for the claim in India and for filing enforcement or execution.
- Time to challenge an award, and time to answer service abroad. Enter them in `matter-deadline-tracker`.

## Before filing

14. `pre-filing-verification-checker`. Input: notice, petition or claim and annexures. Output: signed verification log. **STOP:** advocate signs, then files.
