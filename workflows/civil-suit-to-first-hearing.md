# Civil suit to first hearing

**When to use:** a client wants to sue for money, possession, injunction or specific performance and you need to take the matter from first meeting to the first listing.
**Who it is for:** litigating advocates and juniors acting for a plaintiff in a civil court, commercial court or High Court on its original side.

## Steps

1. `client-intake-conflict-screener`. Input: the client's account and documents. Output: intake note, parties list and conflict result.
   **STOP:** advocate clears the conflict check and accepts the brief.
2. `engagement-letter-drafter`. Input: intake note, scope and fee. Output: engagement letter. **STOP:** advocate and client sign.
3. `limitation-calculator`. Input: cause of action dates, relief sought. Output: last date to file, with working and any exclusions.
4. `litigation-chronology-builder`. Input: documents. Output: source-linked list of dates.
5. `litigation-strategy-planner`. Input: chronology, intake note. Output: route (notice first, suit, summary suit, arbitration) and forum.
   **STOP:** advocate approves the route, forum and reliefs.
6. If commercial: `commercial-suit-filing-checker` (specified value, commercial court) and `pre-institution-mediation-advisor` (whether pre-institution mediation applies or urgent relief allows skipping it). Output: filing-eligibility note.
7. `legal-notice-drafter` if a pre-suit notice is needed. Output: notice. **STOP:** advocate approves before it is sent.
8. `damages-interest-calculator`. Input: claim heads. Output: quantified claim with interest working.
9. `plaint-drafter`. Input: approved route, chronology, quantum. Output: plaint, list of documents, verification.
   **STOP:** advocate approves the causes of action and prayer before formatting.
10. `interim-injunction-application-drafter` or `civil-interlocutory-application-drafter` if urgent or ancillary relief is needed. Output: application and supporting affidavit.
11. `state-court-fee-calculator`. Input: valuation and reliefs, State. Output: court fee with arithmetic.
12. `court-pleading-formatter`, then `vakalatnama-appearance-drafter`. Output: formatted plaint and vakalatnama.
13. `efiling-bundle-defect-checker`. Input: formatted bundle. Output: compliant e-filing paper book; after scrutiny, a fix list for any registry objection with the refiling date.
14. Caveat check (before moving any interim application): search the court's caveat register for a caveat lodged by the defendant under section 148A CPC (manual step). A caveat lapses after a fixed period from lodging (believed to be 90 days; confirm), so check it is still in force. If it is, serve notice of the application and copies on the caveator before moving, and file proof of service. Use `civil-interlocutory-application-drafter` for any caveat-related application.
15. `service-of-process-tracker`. Output: summons, process fee and service log.
16. `hearing-day-brief-builder`. Input: case file and cause list. Output: one-page brief for the first hearing.

## Deadlines to compute with `limitation-calculator`

- Limitation for the suit (from the cause of action, with any acknowledgment or part payment).
- Refiling time after registry objections.
- Time for service and steps after the first order. Enter every date in `matter-deadline-tracker`.

## Before filing

17. `pre-filing-verification-checker`. Input: final plaint, applications, annexures and court-fee working. Output: signed verification log. **STOP:** advocate signs the log, then files.
