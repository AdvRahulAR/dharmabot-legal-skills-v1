---
name: pil-drafter
description: Assesses and drafts public interest litigation under Articles 32 and 226 following the Supreme Court and High Court PIL rules on bona fides, petitioner credentials, prior representations and research basis, and complaints to the NHRC, State Human Rights Commissions and statutory commissions for women, children, Scheduled Castes and Scheduled Tribes. Use when a client or NGO wants to file a PIL on pollution, civic failure or rights violations, or approach a human rights commission. Do not use for environmental claims better placed before the National Green Tribunal; use ngt-application-drafter.
---

# PIL Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Decide whether a genuine public interest petition, a commission complaint or another forum fits best, and draft a petition that the court will treat as bona fide and well researched.

## Jurisdiction gate

Confirm the issue arises in India and identify the State, district and authorities responsible. Choose between the Supreme Court and the jurisdictional High Court. Record the court's PIL rules (format, petitioner's declaration, credentials, deposit if any).

## Required inputs

**Blocking**: the public problem with evidence (photos, reports, data, news only as a lead); the petitioner's identity, credentials and lack of private interest; prior representations to authorities and any replies; and the relief sought.

Also useful: RTI replies, expert reports, earlier orders on the same issue, and the statutes and schemes that impose the duty.

## Method

1. Retrieve the current official text of the court's PIL rules, the statutes imposing the duty (for example environment, municipal or welfare laws), and the Protection of Human Rights Act, 1993 and commission regulations if a commission is considered. Record source and date.
2. Forum check: is a statutory forum better (NGT for environmental disputes, a commission for an individual rights violation, a regulator for sectoral issues)? Is the same issue already pending or decided? Search cause lists and earlier orders.
3. Bona fides: confirm the petitioner has no personal, political or commercial interest; disclose any connection. Read the court's guidance on frivolous PILs (for example State of Uttaranchal v. Balwant Singh Chaufal, Supreme Court, 2010; confirm current treatment).
4. Prior representation: confirm representations were made and enough time given; if not, recommend making one first. Use `rti-application-appeal-drafter` to obtain records.
5. Research basis: each factual claim tied to a document; separate verified facts from news reports.
6. Duty and breach: identify the statutory or constitutional duty, the authority bound, and how it failed.
7. Relief: specific, enforceable directions (survey, action plan, timelines, monitoring committee), not general exhortation.
8. For a commission complaint, check the commission's time limit and jurisdiction, including the bar on matters pending before another commission or court.
9. Search for and read current authority. Tag anything unread `[verify]`.

## Output

1. A forum and maintainability note.
2. The PIL (synopsis, list of dates, facts, grounds, prayer, petitioner's declaration and affidavit) or the commission complaint.
3. An evidence index and a list of respondent authorities.

## Guardrails and hand-offs

- Warn against publicity-driven, political or private-interest petitions; the court may impose costs.
- Never present news reports as verified facts.
- Protect the identity of victims where the law requires.
- For an individual grievance, use `writ-petition-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
