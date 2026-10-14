# Property purchase due diligence

**When to use:** a client is buying land, a house, a flat or a commercial unit, whether resale or from a developer.
**Who it is for:** property advocates acting for a buyer, including NRI and OCI buyers, and lenders' panel advocates.

## Steps

1. `client-intake-conflict-screener`. Input: property details, seller, price, source of funds. Output: intake note and conflict result.
   **STOP:** advocate accepts the brief and agrees the scope (title period, searches, site visit).
2. `property-title-diligence-analyst`. Input: title deeds, parent documents, revenue records. Output: title chain and title report with gaps.
3. `encumbrance-certificate-analyst`. Input: encumbrance certificates for the search period. Output: reconciliation with the title chain and unexplained entries.
4. `land-records-mutation-advisor`. Input: revenue records. Output: mutation status, land use, conversion and any land restrictions.
5. If the property is in a new project: `rera-project-compliance-checker` (registration, approvals, disclosures) and `builder-buyer-agreement-reviewer` (allotment letter or agreement).
6. If it is in a housing society: `cooperative-society-dispute-analyst` for membership, transfer and NOC issues.
7. If the seller inherited the property: `intestate-succession-share-calculator` to confirm all heirs are joining or have released.
   **STOP:** advocate approves the title report and the list of requisitions before anything is signed.
8. `legal-notice-drafter` for a public notice inviting objections, if the profile or lender requires one. **STOP:** advocate approves before publication.
9. `sale-deed-drafter`. Input: approved title report, agreed terms. Output: agreement to sell and sale deed.
   **STOP:** advocate and client approve the drafts.
10. `state-stamp-duty-calculator`. Input: instrument, consideration, guidance value, State. Output: stamp duty and registration fee with arithmetic.
11. `contract-execution-stamping-checker`. Output: execution, e-stamping and registration steps, witnesses and documents for the sub-registrar.
12. If the buyer or seller is an NRI or OCI: `nri-property-transaction-checker` (FEMA, tax deduction, repatriation) and `power-of-attorney-drafter` for a POA executed abroad, with `document-legalisation-planner` for notarisation, apostille or consulate attestation and adjudication on arrival.
    **STOP:** advocate approves the POA text and the legalisation route.
13. `land-records-mutation-advisor` after registration. Output: mutation application steps in the buyer's name.

## Deadlines to compute with `limitation-calculator`

- Time to present a document for registration after execution.
- Time to adjudicate and stamp a POA or deed executed abroad after it is received in India.
- Payment and completion dates under the agreement to sell. Enter them in `matter-deadline-tracker`.

## Before registration

14. `pre-filing-verification-checker`. Input: sale deed, stamp-duty working, title report. Output: signed verification log. **STOP:** advocate signs the log before the parties go to the sub-registrar.
