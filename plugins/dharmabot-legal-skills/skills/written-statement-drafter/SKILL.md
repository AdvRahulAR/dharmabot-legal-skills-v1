---
name: written-statement-drafter
description: Drafts a written statement under Order VIII of the Code of Civil Procedure for Indian civil and Commercial Courts, with preliminary objections, para-wise admissions and denials, additional pleas, set-off or counterclaim, and a statement of truth in commercial suits. Use when an advocate asks to draft a written statement, reply to a plaint, defence, counterclaim or set-off. Do not use for interlocutory applications such as rejection of plaint; use civil-interlocutory-application-drafter instead.
---

# Written Statement Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce a defence that answers every allegation specifically, raises every available objection now, and protects the defendant from deemed admissions and time bars.

## Jurisdiction gate

Confirm the suit is pending in an Indian court and note the court, State and whether it is a commercial suit. Check whether the plaint's jurisdiction, limitation or valuation can be attacked.

## Temporal gate

Record the date of service of summons with the plaint. In commercial suits the time for filing has a strict outer limit (believed to be 120 days from service, with no power to extend beyond it; confirm the Order VIII text as amended and current Supreme Court authority). In ordinary suits, note the basic period (believed to be 30 days, extendable in the court's discretion up to about 90 days for recorded reasons; confirm) and that late filing needs an application with reasons. Flag the deadline at the top of the draft.

## Required inputs

Mark as **blocking**:
- the plaint and all documents served with it;
- the date of service of summons;
- the defendant's instructions on each paragraph of the plaint;
- the defendant's own documents.

Also useful: any claim the defendant has against the plaintiff, prior correspondence, and details of other proceedings between the parties.

## Method

1. Retrieve the current official text of Order VIII CPC (including Commercial Courts Act amendments), Order VII Rule 11, the Limitation Act and the High Court's rules. Record the version and date.
2. Build a para-wise table: plaint paragraph · allegation · client instruction · admit, deny or not known · supporting document.
3. Draft preliminary objections only where grounded: jurisdiction, limitation, arbitration clause, non-joinder or misjoinder, valuation and court fee, bar by statute, res judicata, no cause of action.
4. Draft para-wise replies. Deny each fact specifically and state the defendant's version. In commercial suits, give reasons for each denial; a bare denial risks being treated as an admission.
5. Add additional pleas and the defendant's own facts.
6. Plead set-off (ascertained sum, legally recoverable) or a counterclaim with valuation, court fee and limitation, as the facts allow.
7. Add verification and, in commercial suits, the statement of truth and the documents affidavit.
8. Where a threshold point is strong, recommend a separate application (for example under Order VII Rule 11, or under the Arbitration Act to refer parties) and note the timing interplay with filing the written statement.

## Output

1. The draft written statement, with any counterclaim.
2. The para-wise instruction table.
3. A note: deadline, evasive denials still needing instructions, applications to file.

## Guardrails and hand-offs

- Never admit or deny a fact without the client's instruction.
- Flag every evasive or general denial for the advocate.
- Never invent authority; tag unread authority `[verify]`.
- Applications: `civil-interlocutory-application-drafter`. Formatting: `court-pleading-formatter`. Stress test: `adversarial-draft-reviewer`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
