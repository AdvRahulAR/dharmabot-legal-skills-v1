---
name: cheque-dishonour-case-drafter
description: Handles cheque dishonour under sections 138 to 148 of the Negotiable Instruments Act, 1881 and e-mandate dishonour under the Payment and Settlement Systems Act, 2007, drafting the statutory demand notice, the complaint, the interim compensation application and deposit applications in appeal, with deadlines and territorial jurisdiction. Use when a cheque bounced, the drawer has not paid after notice, or a client needs a s.138 complaint or reply. Do not use for a civil recovery suit on the same debt; use summary-suit-order-xxxvii-drafter.
---

# Cheque Dishonour Case Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Take a dishonoured cheque or e-mandate from return memo to complaint, with every statutory step and deadline checked.

## Jurisdiction gate

Confirm the cheque is drawn on an account in India, or the e-mandate is under an Indian payment system. Identify the payee's bank branch where the cheque was presented or the account is maintained, as this decides territorial jurisdiction (believed to be s.142(2) NI Act; confirm).

## Temporal gate

Each step runs from the previous one: cheque validity, return memo, notice, service, payment window, complaint. Get all dates before drafting; compute them with `limitation-calculator`.

## Required inputs

**Blocking**: the cheque (date, amount, drawer, account); the return memo with date and reason; date the payee received the memo; the debt or liability the cheque was for, with documents; and the drawer's addresses.

For a company drawer: the directors and officers in charge, and their roles. For a reply: the notice received and the client's account.

## Method

1. Retrieve the current official text of NI Act ss.138 to 148, s.25 of the Payment and Settlement Systems Act, 2007, any Supreme Court practice directions on s.138 trials, and the relevant court's rules. Record source and date.
2. Check the ingredients: legally enforceable debt, presentation within validity, dishonour for a covered reason, notice within the statutory period from receiving information of return (believed 30 days; confirm), failure to pay within the payment window (believed 15 days from receipt of notice; confirm).
3. Draft the notice: cheque details, return reason, demand for the cheque amount, addresses for all drawers and company officers, and modes of service with proof.
4. Compute the complaint deadline (believed one month from the cause of action; confirm) and flag any delay needing condonation.
5. For companies, plead the role of each director under s.141 specifically. Do not array non-executive or independent directors without material.
6. Draft the complaint with the verification affidavit, list of documents and witness list. Note the court fee with `state-court-fee-calculator` where the State charges ad valorem.
7. Draft an interim compensation application under s.143A and, at appeal, a deposit application under s.148, with the percentages confirmed from the text.
8. Flag defences: security cheque, time-barred debt, no liability, material alteration, notice defects, stop-payment, and the presumption under s.139 and its rebuttal. Search for and read current authority; tag anything unread `[verify]`.

## Output

1. A date chart with each statutory deadline.
2. The demand notice.
3. The complaint, affidavit, documents list and s.143A application.
4. A defence-risk note.

## Guardrails and hand-offs

- Never back-date a notice or alter dates.
- Demand the cheque amount clearly and separately. If interest or costs are claimed, list them as distinct items; an omnibus demand that blurs the cheque amount risks invalidating the notice (read current Supreme Court authority).
- Never promise conviction or recovery. For parallel civil recovery, use `summary-suit-order-xxxvii-drafter`.
- For a version in an Indian language, use `regional-language-legal-drafter`; for layout, `court-pleading-formatter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
