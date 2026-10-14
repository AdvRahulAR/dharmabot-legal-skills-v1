---
name: legal-notice-drafter
description: Drafts pre-litigation legal notices under Indian law (money demand, breach of contract, termination, and notice to Government under section 80 of the Code of Civil Procedure) and replies to notices received, after assessing the allegations, exposure and admission risk. Use when an advocate asks to send a legal notice, demand notice or notice of breach, or to reply to a notice or counter-notice. Do not use for cheque dishonour demand notices; use cheque-dishonour-case-drafter instead.
---

# Legal Notice Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Produce a clear, proportionate notice or reply that preserves the client's position, avoids damaging admissions and sets up the next step (suit, arbitration, mediation or settlement).

## Jurisdiction gate

Confirm the dispute is governed by Indian law and note the State, the parties' locations and any dispute-resolution clause. If the contract names a foreign law or seat, stop and hand off to `foreign-matter-scoping-analyst`. If the addressee is the Government or a public officer acting officially, apply the statutory notice requirement for suits against Government (believed to be section 80 CPC; confirm from the official text), including the waiting period before suit and the leave route where urgent relief is needed, and any special statute with its own notice rule.

## Required inputs

Mark as **blocking**:
- the client's and addressee's correct names, status and addresses;
- the contract, invoices, ledger or other source documents;
- the amount or relief claimed and how it is computed;
- for a reply, the full notice received and its date of receipt.

Also useful: earlier correspondence, part-payments, acknowledgments, and the client's commercial goal (recover, terminate, negotiate, or preserve rights only).

## Method

1. Retrieve the current official text of every provision relied on (Indian Contract Act, CPC, Limitation Act, any special statute) from India Code, and record the version and date.
2. Analyse the facts: obligations, breach, amount due, interest basis (contractual rate first, otherwise flag that the rate needs a legal basis), and the dispute clause.
3. Check limitation with `limitation-calculator`. Note whether an acknowledgment or part-payment extends time. Never imply a notice itself stops time running.
   - Compute periods from the actual dates using `scripts/date_calc.py`. If the user's stated count disagrees with the dates, flag the discrepancy and ask which is right before relying on either. (`--start` with `--period` gives a last date; `--to` counts the days elapsed between two dates.) Run it with `python3`, or with `py -3` on Windows, where `python`/`python3` may open the Microsoft Store instead.
   - Show the script's commands and output in your response. Present every period, last date and section number as believed and to be confirmed against the official text, in tables and headlines as well as in notes, and tag [verify] where it was not checked against a primary source. If the user's stated count and the dates disagree, show each result as conditional on the user's answer, and do not draft on, or rely on, either figure until they reply.
4. For a demand notice, draft: parties and capacity of the advocate; brief facts; documents relied on; breach; amount with a computation table; a realistic compliance period; the remedies the client may pursue; and a without-prejudice settlement line only if instructed.
5. For a reply, first produce a notice analysis table: allegation · documents · client's version · risk of admission · proposed response. Then draft para-wise replies. Deny specifically, avoid vague "denied in toto" lines, and reserve rights. Do not volunteer facts not needed.
6. Calibrate tone. Firm and factual, no abuse, no exaggeration.
7. Remove any threat of criminal prosecution used to press a civil payment. If the facts genuinely suggest an offence, note it separately for the advocate, not in the notice.
8. Add dispatch notes: registered post with acknowledgment, courier, and email where the contract allows; keep proof of dispatch and delivery.

## Output

1. The draft notice or reply, on the advocate's letterhead format.
2. For a reply, the allegation analysis table.
3. A cover note: limitation position, admissions risk, missing documents, and the recommended next step.

## Guardrails and hand-offs

- Never state amounts, dates or facts the client has not confirmed.
- Never threaten criminal proceedings to coerce a civil payment.
- Never promise the client that the addressee will pay.
- Next steps: `plaint-drafter` for a suit, `pre-institution-mediation-advisor` for commercial disputes, `arbitration-invocation-notice-drafter` where an arbitration clause applies.
- For a version in an Indian language, hand off to `regional-language-legal-drafter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
