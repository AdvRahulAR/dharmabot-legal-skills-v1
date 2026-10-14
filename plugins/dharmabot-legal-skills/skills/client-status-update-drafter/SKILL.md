---
name: client-status-update-drafter
description: Drafts status updates for clients, management or a legal-aid clinic supervisor from court orders, hearing notes and emails, in WhatsApp, email or report length, and drafts matter closure reports with outcome, lessons and handoff notes, stating uncertainty honestly and keeping privileged analysis out of wide-circulation versions. Use when a lawyer asks to update the client on today's hearing, send a monthly status report or close a file. Do not use for explaining a judgment in depth; use plain-language-explanation-drafter instead.
---

# Client Status Update Drafter

Every output is a draft for the responsible advocate to review before it is sent.

## Purpose

Tell the reader what happened, what it means, what happens next and what is needed from them, accurately and without overstating the position.

## Jurisdiction gate

This skill works for any forum. Confirm the forum and the matter so dates and procedural terms are described correctly. If a foreign client or foreign proceeding is involved, keep descriptions of foreign law to what counsel there has confirmed.

## Required inputs

**Blocking**:
- the source of the update (order, hearing note, email, filing receipt);
- the audience (client individual, company management, board, clinic supervisor) and channel (WhatsApp, email, report).

Also useful: the client's language preference, earlier updates sent, the next date, costs incurred, and any decision needed from the client.

## Method

1. Retrieve the official order or case status from the court or forum's website where available, and record its date. Never describe an order from memory or from a colleague's note alone if the order is available.
2. Separate facts (what the order says) from the advocate's assessment (what it may mean). Label the assessment as such.
3. Pitch the content to the audience:
   - Individual client: plain words, no section numbers unless needed, what they must do.
   - Management or board: decision needed, exposure, cost to date, next milestone.
   - Clinic supervisor: action taken, student or volunteer involved, next step, risk flags.
4. Draft the short version (WhatsApp or SMS length, three to five lines) and the full version (email or report).
5. Keep privileged legal analysis only in the version meant for the client's legal decision-makers. For any version that may be forwarded widely, keep to facts and next steps and say so in the note to the advocate.
6. State uncertainty plainly: adjournments, reserved orders and likely timelines are estimates.
7. For a closure report: final outcome and order date, amounts paid or recovered, documents returned, open risks (appeal period, compliance still due), lessons learned, and handoff notes for any successor counsel.

## Output

1. Short message.
2. Full update or closure report.
3. A note to the advocate listing any assessment statements to confirm and anything kept out for privilege.

## Guardrails and hand-offs

- Never promise or predict an outcome as certain.
- Never add facts, dates or amounts that are not in the source.
- Do not disparage the court, opposing counsel or the other party.
- For a translated version, hand off to `regional-language-legal-drafter`.
- For next dates, update `matter-deadline-tracker`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
