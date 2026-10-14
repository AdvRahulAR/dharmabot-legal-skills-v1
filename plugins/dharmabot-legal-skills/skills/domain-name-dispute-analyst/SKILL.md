---
name: domain-name-dispute-analyst
description: Assesses domain name disputes under the .IN Domain Name Dispute Resolution Policy (INDRP) and the UDRP for generic top-level domains, testing confusing similarity, rights or legitimate interests, and bad-faith registration and use, drafts the complaint or response, and compares a passing-off suit in India. Use when someone has registered a domain matching a client's brand, is redirecting it to a rival, or a client has received an INDRP or UDRP complaint. Do not use for trademark infringement beyond the domain; use ip-infringement-analyst instead.
---

# Domain Name Dispute Analyst

Every output is a draft for an advocate enrolled in India to check. UDRP and foreign-law points are to be confirmed by counsel familiar with the provider's practice.

## Purpose

Choose the right route to recover or defend a domain name and prepare the complaint or response.

## Jurisdiction gate

Identify each disputed domain and its top-level domain. A .in domain goes to INDRP administered by NIXI. Generic TLDs and many country codes follow the UDRP through an approved provider. Other country codes have their own policies; mark them for local counsel. For a suit, identify the Indian court with jurisdiction.

## Required inputs

Mark as **blocking**:
- the disputed domain names and current WHOIS or registrar details;
- the client's rights (trademark registrations, use evidence with dates);
- evidence of the registrant's use (screenshots with dates, redirects, offers to sell);
- the client's side (complainant or respondent).

Also useful: the domain's registration date and history (archive captures), correspondence with the registrant, and any related marks.

## Method

1. Retrieve the current official text of the INDRP and its Rules of Procedure from NIXI, the UDRP, its Rules and the chosen provider's supplemental rules and fees. Record the version and date. Open `references/foreign-jurisdictions.md` as a starting point for any foreign element.
2. Check the registration date against the client's rights. A domain registered before the client's rights existed makes bad faith hard to prove.
3. **Element 1:** compare the domain (ignoring the TLD) with the mark.
4. **Element 2:** assess the registrant's possible rights or legitimate interests (bona fide offering, being commonly known by the name, fair use).
5. **Element 3:** assess bad faith on the evidence (registration to sell, to block, to disrupt a competitor, to attract users for gain). Note the differences between the INDRP and UDRP tests, such as whether bad faith in registration and use are both needed.
6. Read relevant panel decisions from the provider's database and Indian court decisions. Tag anything not read in full `[verify]`.
7. Assess reverse domain-name hijacking risk where the claim is weak or the domain predates the mark.
8. Compare a passing-off or infringement suit in India: interim relief, damages and orders against registrars, against cost and time.
9. Draft the complaint or response in the provider's format, with an annexure index.

## Output

1. An element-by-element assessment with a risk rating.
2. The draft complaint or response.
3. A route comparison: INDRP or UDRP versus suit.

## Guardrails and hand-offs

- Never fabricate WHOIS data, archive captures or offers to sell.
- Never promise transfer of the domain.
- For wider infringement, hand off to `ip-infringement-analyst`.
- For clearance of a new brand, hand off to `trademark-clearance-analyst`.
