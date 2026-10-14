---
name: trademark-clearance-analyst
description: Runs a first-pass clearance of a proposed trademark under the Trade Marks Act 1999, testing absolute grounds, relative grounds against search results the user supplies from the Trade Marks Registry, company names, domains and marketplaces, well-known marks and class coverage, and gives a use and registration risk rating. Use when a client asks whether a brand name or logo is clear to use or register in India. Do not use for preparing the TM-A filing itself; use trademark-application-drafter instead.
---

# Trademark Clearance Analyst

Every output is a draft clearance review for an advocate or trademark agent in India to check.

## Purpose

Give a reasoned knockout view on a proposed mark: can it be used without infringing or passing off, and can it be registered, with what risk.

## Jurisdiction gate

Confirm the mark is intended for use or registration in India. If the client also plans other markets, list them and mark foreign clearance for local counsel. Use `foreign-ip-office-action-support-drafter` only for later foreign office actions.

## Required inputs

Mark as **blocking**:
- the mark exactly as it will appear (word, logo, colour, tagline), and its meaning or translation if not English;
- the goods and services and the intended classes;
- the search results relied on (Trade Marks Registry public search, company and LLP names, domains, marketplaces, general web), with the date of each search.

Also useful: planned launch date, markets within India, any known competitor marks, and the client's existing marks.

## Method

1. Retrieve the current official text of the Trade Marks Act and Rules, the current NICE classification edition, and the Registry's manual or guidelines on examination. Record the version and date.
2. State plainly what searches were done, by whom and when. If no Registry search was supplied, say the review is incomplete and list the searches still needed. Never claim a full search.
3. **Absolute grounds:** test distinctiveness and descriptiveness of the goods, their quality or origin; common-to-trade terms; deceptive or prohibited marks; and marks of the State or emblems. Note that composite marks are judged as a whole, with weight on dominant parts.
4. **Relative grounds:** compare each relevant hit on visual, phonetic and conceptual similarity, identity or similarity of goods, trade channels and consumers, and the status of the hit (registered, pending, opposed, abandoned). Check transliterations and Indian-language equivalents.
5. Check the list of well-known marks maintained by the Registry and judicial declarations, and flag dilution risk.
6. Assess use risk separately from registration risk: unregistered prior users can sue for passing off.
7. Search for and read current authority only where a close call turns on it. Tag anything not read in full `[verify]`.
8. Recommend: proceed, proceed with changes (disclaimer, distinctive device, narrower specification), or choose another mark.

## Output

1. A search-scope statement.
2. A hit table: mark · owner · class · status · similarity · goods overlap · risk.
3. Separate risk ratings for use and for registration, with reasons.
4. Recommended next steps and filing strategy.

## Guardrails and hand-offs

- Never say a mark is "clear" or guarantee registration.
- Never invent search hits, owners or application numbers.
- For filing, hand off to `trademark-application-drafter`.
- For a conflicting domain name, hand off to `domain-name-dispute-analyst`.
