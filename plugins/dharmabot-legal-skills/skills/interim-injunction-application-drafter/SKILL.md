---
name: interim-injunction-application-drafter
description: Drafts interim applications in Indian civil and commercial suits under Order XXXIX (temporary and ad-interim injunctions), Order XL (receiver), Order XXXVIII (attachment before judgment) and section 151 of the Code of Civil Procedure, built on prima facie case, balance of convenience and irreparable harm, with urgency affidavit and undertakings. Use when an advocate asks for a stay, temporary injunction, status quo, receiver or attachment before judgment. Do not use for interim relief in arbitration; use section-9-interim-relief-drafter instead.
---

# Interim Injunction Application Drafter

Every output is a draft for an advocate enrolled in India to check and sign.

## Purpose

Draft an interim application that states the full facts, meets the legal test, and asks for relief the court can actually grant and police.

## Jurisdiction gate

Confirm a suit is filed or being filed in an Indian court with jurisdiction. Note the State and court. Check statutory bars on injunctions (for example under the Specific Relief Act for certain infrastructure contracts, or special statutes) and whether an arbitration clause routes interim relief elsewhere.

## Required inputs

Mark as **blocking**:
- the plaint or draft plaint;
- the documents showing the plaintiff's right and the threatened act;
- the urgency facts and dates (when the plaintiff learnt of the threat);
- any earlier proceedings, orders or undertakings between the parties;
- facts adverse to the plaintiff.

## Method

1. Retrieve the current official text of Orders XXXVIII, XXXIX and XL CPC, sections 94, 95 and 151 CPC, the Specific Relief Act provisions on injunctions, and any High Court rules on ex parte relief. Record the version and date.
2. Choose the relief: prohibitory or mandatory injunction, status quo, receiver, attachment before judgment, or security. Mandatory interim relief needs a stronger case; say so.
3. Build the three-part case from the record: prima facie case; balance of convenience; irreparable harm not compensable in money. Add delay, conduct and public interest.
4. For attachment before judgment, plead specific facts that the defendant intends to obstruct or delay execution by disposing of or removing property. General apprehension is not enough.
5. For a freezing or search-type order (Mareva or Anton Piller type), explain the exceptional basis, the risk of dissipation or destruction, and offer safeguards. Treat as rare relief.
6. For ad-interim ex parte relief, explain why notice would defeat the purpose, and draft for compliance with the rule requiring copies to be sent after the order (believed to be Order XXXIX Rule 3; confirm).
7. Draft the supporting affidavit and an undertaking as to damages where appropriate.
8. Search for and read current Supreme Court and jurisdictional High Court authority on the test applied. Tag unread authority `[verify]`.

## Output

1. The draft application with prayer, supporting affidavit and urgency note.
2. A disclosure checklist confirming adverse facts are stated.
3. A proposed order the court could sign.

## Guardrails and hand-offs

- Never suppress adverse facts, earlier orders or pending proceedings. Suppression can cost the relief and the suit.
- Never overstate urgency.
- Plaint: `plaint-drafter`. Affidavits of evidence later: `evidence-affidavit-drafter`. Formatting: `court-pleading-formatter`.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
