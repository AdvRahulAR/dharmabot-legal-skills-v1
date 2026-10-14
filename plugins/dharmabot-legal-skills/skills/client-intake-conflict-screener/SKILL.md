---
name: client-intake-conflict-screener
description: Turns a client's call notes, email or walk-in story into a structured intake note for an Indian law practice and builds the list of names to run through the conflict register, flagging possible conflicts under the Advocates Act, 1961 and the Bar Council of India Rules. Use when a new client or matter comes in and you need an intake note, a conflict list, limitation red flags or the likely practice area. Do not use for merits advice or fee terms; use engagement-letter-drafter once the conflict check is cleared.
---

# Client Intake and Conflict Screener

Every output is a draft intake note and conflict list for an advocate enrolled in India to review and decide on.

## Purpose

Capture a new enquiry accurately, spot urgency and limitation risk early, and give the firm a complete list of names to check for conflicts before any advice is given.

## Jurisdiction gate

- Confirm the dispute or transaction is governed by Indian law or will be heard by an Indian court, tribunal or authority.
- Record the State or UT and district, because forum, court fees, stamp duty and local laws (rent control, land records) vary by State.
- If a foreign party, foreign law or a foreign forum is involved, flag it and suggest `foreign-matter-scoping-analyst`.

## Required inputs

**Blocking**: the client's full name (and entity type if not an individual), every opposing or connected party named in the story, and what the client wants done. Without these the conflict check cannot run; ask for them.

Also useful: the date the dispute arose and key dates since, documents held, any notice received or sent, any pending case number, who referred the client, and the client's means (for legal aid routing).

## Method

1. Retrieve the current official text of the rules that govern conflicts and acceptance of briefs: the Advocates Act, 1961 and the BCI Rules on standards of professional conduct (Part VI, Chapter II), from the BCI website or India Code. Record the version and date. Do not quote rule numbers from memory; tag any you cite `[verify]`.
2. Read the narrative once for facts only. Separate what the client says happened from what the documents show.
3. Build the intake note: client and contact channel; parties and their roles; a dated chronology; documents held and missing; the relief sought; urgency (arrest risk, eviction, demolition, hearing date, notice reply window); and the likely practice area.
4. Flag limitation and time-critical points as questions, not conclusions. Pass any date that needs computing to `limitation-calculator`.
5. Build the conflict list. Include the client, all opposing parties, their group companies, directors or promoters, family members named, guarantors, insurers, opposing advocates and key witnesses. Add spelling and script variants (for example Hindi or Marathi spellings, initials, former company names).
6. Describe how to run the list against the firm's register: current clients, former clients, matters where the firm advised the other side, and personal or financial interests of the team.
7. Classify each hit: no conflict, possible conflict needing partner review, or likely bar (for example the firm earlier advised or appeared for the opposite party in the same or a connected matter). Do not decide waivers.
8. If the client may qualify for free legal services, suggest `legal-aid-eligibility-screener`.

## Output

1. Intake note (one page) with chronology table: date · event · source (client said / document).
2. Conflict search list with variants, grouped by role.
3. Conflict result table: name · hit · nature · proposed action.
4. Open questions for the client and documents to request.
5. Recommended next step: `engagement-letter-drafter`, `matter-plan-builder`, or decline with a neutral letter.

## Guardrails and hand-offs

- Give no view on merits, chances of success or likely compensation at intake.
- Do not invent dates, parties or document contents; mark gaps as gaps.
- Never decide a conflict or waiver; the responsible advocate decides and records it.
- Keep intake notes confidential; do not copy them into shared knowledge banks.
- Do not solicit work or promise outcomes in any follow-up message.
