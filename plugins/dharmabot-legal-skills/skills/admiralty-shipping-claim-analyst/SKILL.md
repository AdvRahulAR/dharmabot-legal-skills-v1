---
name: admiralty-shipping-claim-analyst
description: Analyses maritime claims involving India, including arrest of vessels under the Admiralty (Jurisdiction and Settlement of Maritime Claims) Act 2017 (maritime claims, liens, security), charterparty and bill of lading disputes under the Carriage of Goods by Sea Act 2025, the Bills of Lading Act 2025 and Hague-Visby rules, cargo damage, demurrage, and London or Singapore arbitration clauses. Use when a client asks whether it can arrest a ship in an Indian port or claim for cargo loss or demurrage. Do not use to plan the arbitration itself; use international-arbitration-planner.
---

# Admiralty Shipping Claim Analyst

Every output is a draft for an advocate enrolled in India to check.

## Purpose

Decide whether the claim is a maritime claim that supports arrest in India, what security can be obtained, and which law and forum govern the merits.

## Jurisdiction gate

Identify where the vessel is (port and State) and the High Court with admiralty jurisdiction over those waters under the 2017 Act. Map the law for each issue: Indian law for arrest and procedure; the law of the charterparty or bill of lading for the merits (often English law with London arbitration, or Singapore). Mark foreign-law points "to be confirmed by counsel qualified in [jurisdiction]".

## Temporal gate

The Carriage of Goods by Sea Act 2025 and the Bills of Lading Act 2025 replaced older statutes. Check their commencement and transition provisions against the date of shipment and the bill of lading. Record the dates of shipment, discharge and delivery.

## Required inputs

Mark as **blocking**:
- the vessel's name, IMO number, current port and expected departure;
- the claim type and amount, with the contract (charterparty, bill of lading, booking note);
- who owns or demise-charters the vessel now, and who was liable when the claim arose;
- the dates of delivery or expected delivery of cargo.

Also useful: survey reports, notices of claim, P&I correspondence, letters of indemnity, and any letter of undertaking offered.

## Method

1. Retrieve the current official text of the Admiralty Act 2017 and the relevant High Court admiralty rules, the carriage-of-goods and bills-of-lading statutes, and any notification on courts. Record versions and dates. Open `references/foreign-jurisdictions.md` for the foreign law sources and enforcement position.
2. Classify the claim under the Act's list of maritime claims and decide whether it carries a maritime lien. Lien claims may follow the vessel to a new owner; ordinary claims usually need the owner's personal liability at the time of arrest. Check sister-ship arrest rules.
3. Test urgency: the vessel's sailing time, the evidence of the claim's prima facie strength, and counter-security risks for wrongful arrest.
4. Merits: identify carrier, shipper and consignee; apply the Hague-Visby defences, package limitation and the one-year time bar for cargo claims (confirm and compute with `limitation-calculator`). For demurrage, check laytime, notice of readiness and exceptions.
5. Arbitration clause: arrest for security is usually available despite a London or Singapore clause. Note the risk of a stay of the merits.
6. Security: bank guarantee, P&I letter of undertaking, or payment into court; wording to accept.
7. Search for and read current Supreme Court and High Court admiralty authority. Tag anything not read in full `[verify]`.

## Output

1. An arrest assessment: claim category · lien · liability of current owner · court · risks.
2. A merits note with time bars and governing law for each issue.
3. A document list for the arrest application and a security checklist.

## Guardrails and hand-offs

- Never overstate a claim to obtain arrest; wrongful arrest carries liability.
- Never present English or Singapore law as settled; hand off to `foreign-law-research-memo-drafter`.
- For the arbitration, hand off to `international-arbitration-planner`.
- Before delivery, send citations to `citation-verifier`.
