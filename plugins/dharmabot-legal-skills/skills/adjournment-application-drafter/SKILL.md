---
name: adjournment-application-drafter
description: Drafts adjournment applications in Indian civil suits under Order XVII of the Code of Civil Procedure (sufficient cause, the three-adjournment limit, costs, stricter Commercial Courts timelines) and in criminal trials under the Bharatiya Nagarik Suraksha Sanhita, 2023, with supporting documents and an offer of costs. Use when a witness is ill, counsel is unavailable, or a party asks for time and the advocate needs a draft that states the cause honestly. Do not use for other interlocutory applications; use civil-interlocutory-application-drafter.
---

# Adjournment Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Draft an adjournment application that states a genuine cause with proof, offers to mitigate prejudice, and warns the advocate early when the court is unlikely to grant it.

## Jurisdiction gate

Confirm the matter is before an Indian court. Record the court, State, case type and stage. Identify whether it is a commercial suit under the Commercial Courts Act, 2015, an ordinary civil suit, or a criminal trial. Note any High Court practice direction on adjournments.

## Temporal gate

For criminal trials, check whether the BNSS or the Code of Criminal Procedure, 1973 governs. If the case began before 1 July 2024, run `crpc-bnss-transition-analyst` first.

## Required inputs

Mark as **blocking**:
- the court, case number and the date and purpose of the next hearing;
- the reason for adjournment, with the supporting document (medical certificate, travel record, death certificate);
- the number of adjournments already taken by this party and at what stage;
- any order fixing a time-bound schedule or a last opportunity.

## Method

1. Retrieve the current official text of Order XVII CPC, the Commercial Courts Act and its amendments to the CPC, the BNSS provision on postponement and adjournment (believed to be section 346; confirm from the official text), and any High Court practice direction. Record the source and date.
2. Count prior adjournments from the order sheet. Flag the limit in Order XVII on adjournments to a party, and the stricter position in commercial suits and during evidence. The Supreme Court has read the limit as yielding only in exceptional cases beyond the party's control (for example Salem Advocate Bar Association v. Union of India, 2005; confirm current treatment).
3. Test the cause: is it beyond the party's control, recent, and supported by a document? Flag a weak or self-created cause plainly.
4. Draft the application: case details, stage, the cause with dates, the document relied on, why a short date will cure it, the prejudice to the other side and how it is met, and the proposed date range.
5. Offer costs where proper, and propose steps that keep the trial moving (for example examining another witness first, video-conference evidence).
6. For criminal trials, address the policy of day-to-day trial once evidence begins, the custody of the accused, and any victim's interest.
7. Attach an affidavit if the forum requires one.

## Output

1. The adjournment application with affidavit and document list.
2. A one-paragraph risk note: likelihood of refusal, costs exposure, and whether the right to lead evidence may close.
3. A suggested message for the client through `client-status-update-drafter`.

## Guardrails and hand-offs

- Never invent illness, travel or any fact. State only what the client confirms with documents.
- Remind the advocate of the duty to the court; this skill does not plan delay tactics.
- Diarise the next date through `matter-deadline-tracker`.
- Other interlocutory relief goes to `civil-interlocutory-application-drafter`.
- Before anything is filed or sent, hand off to `pre-filing-verification-checker`. The Supreme Court has said that an advocate who cites AI-generated judgments without verifying them commits misconduct (Pooja Ramesh Singh v. Jammu and Kashmir Bank Ltd., 2026 INSC 668, decided 2 July 2026; read the judgment before citing it).
