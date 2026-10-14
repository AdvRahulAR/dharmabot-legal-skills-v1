# GST notice to appeal

**When to use:** a client receives a GST show-cause notice, demand, scrutiny or audit observation, and the matter may go to appeal.
**Who it is for:** tax advocates and in-house tax teams working with the client's chartered accountant.

## Steps

1. `client-intake-conflict-screener`. Input: the notice, returns, and client's explanation. Output: intake note and conflict result.
   **STOP:** advocate accepts the brief and agrees the split of work with the CA.
2. `limitation-calculator`. Input: date of notice and the reply period it states. Output: reply deadline, and whether the notice itself was issued within time, with working.
   Enter it in `matter-deadline-tracker`.
3. `gst-transaction-analyst`. Input: transactions in issue. Output: analysis of supply, classification, place of supply and input tax credit.
4. If goods are detained in transit: `gst-detention-release-drafter`. Output: reply and release application. This runs first if goods are held.
5. `gst-notice-reply-drafter`. Input: notice and transaction analysis. Output: issue-wise analysis and grounds of reply, including jurisdiction and limitation points.
   **STOP:** advocate approves the grounds before the full reply is drafted.
6. `gst-notice-reply-drafter`. Output: full reply with annexures and a personal hearing request.
   **STOP:** advocate and client approve the reply and the factual statements in it.
7. `citation-verifier`. Input: reply. Output: every circular, notification and judgment checked against source.
8. `pre-filing-verification-checker` on the reply. **STOP:** advocate signs the log, then files on the portal.
9. `hearing-day-brief-builder` for the personal hearing.
10. After the order: `limitation-calculator`. Input: date of communication of the order. Output: appeal deadline and condonable period.
11. `litigation-strategy-planner`. Input: order. Output: appeal, rectification, writ or payment, with pre-deposit cost.
    **STOP:** advocate approves the remedy.
12. `tax-appeal-grounds-drafter`. Input: order, reply, approved remedy. Output: appeal with grounds, statement of facts, pre-deposit working and stay request.
    **STOP:** advocate approves the grounds of appeal.
13. If a writ is chosen instead (jurisdictional error, breach of natural justice): `writ-petition-drafter`.
14. `regulatory-appeal-planner` for the next tier if the first appeal fails.

## Deadlines to compute with `limitation-calculator`

- Reply to the show-cause notice and any extension sought.
- Time limit for the department to issue the notice and pass the order.
- First appeal from communication of the order, and the condonable period.

## Before filing

15. `pre-filing-verification-checker` on the appeal or writ. **STOP:** advocate signs the verification log, then files.
