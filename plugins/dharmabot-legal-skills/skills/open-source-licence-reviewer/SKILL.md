---
name: open-source-licence-reviewer
description: Classifies open-source and source-available licences in a codebase or dependency list (permissive, weak and strong copyleft, network copyleft, source-available, and AI model licences with use restrictions), identifies obligations triggered by distribution or network use, notices and attribution, and conflicts with proprietary or contract terms, and produces a remediation list. Use when a client shares a dependency list, or SBOM and asks what they must do before shipping an app, SaaS or model. Do not use for drafting an IP assignment or licence; use ip-assignment-licence-drafter instead.
---

# Open Source Licence Reviewer

Every output is a draft review for an advocate or supervising counsel to check, with engineering confirming the technical facts.

## Purpose

Tell the product team which licences are in the product, what each requires given how the product is shipped, and what to fix.

## Jurisdiction gate

Open-source licences are applied the same way across countries in most cases, but enforcement turns on copyright and contract law where the product is distributed. Record the client's home country and main markets. Where enforcement or remedies matter, mark points "to be confirmed by counsel qualified in [jurisdiction]"; for India, check the Copyright Act, 1957.

## Required inputs

**Blocking**:
- the dependency data: an SBOM, lockfile, scanner output or list with package, version and declared licence;
- how the product is delivered: mobile app, desktop, embedded device, SaaS only, on-premise, or model weights;
- whether the client modified any open-source component, and how components are linked or combined.

Also useful: customer contracts with open-source clauses, app store terms, and the client's open-source policy.

## Method

1. Retrieve the official licence text for each licence at the exact version used, from the project's own licence file and the SPDX or OSI reference. Record version and date.
2. Build an inventory: package · version · declared licence · licence found in files · linkage · modified · distributed or network-only.
3. Classify each licence: permissive (for example MIT, BSD, Apache-2.0); weak copyleft (LGPL, MPL, EPL); strong copyleft (GPL); network copyleft (AGPL); source-available (for example BSL, SSPL, Elastic), which is not open source; and model licences with use or user-count restrictions.
4. Decide what triggers obligations. Distribution includes shipping a mobile app or device. Network use matters for AGPL. Internal use alone usually triggers little.
5. List obligations per component: licence and copyright notices, NOTICE files, source offers, modification notices, relinking rights for LGPL, patent clauses, and no added restrictions.
6. Find conflicts: known incompatibilities (for example GPL-2.0-only with Apache-2.0), copyleft components in proprietary code, app store terms that clash with copyleft, and customer contracts promising "no copyleft".
7. Model licences: check acceptable-use policies, field-of-use bans, user thresholds and attribution, and whether outputs or fine-tunes carry restrictions.
8. Flag unknown, missing or custom licences for manual review.
9. Prepare remediation: replace, isolate, obtain a commercial licence, release source, or add notices.

## Output

1. Licence inventory table with risk rating.
2. Obligations checklist per distribution channel.
3. Conflict list.
4. Remediation plan with owners, and a draft attribution or NOTICE file.

## Guardrails and hand-offs

- Do not scan code yourself unless the dependency data is supplied; never guess a licence from a package name.
- Never advise removing or hiding licence notices.
- Do not state foreign-law enforcement as settled.
- Licences or assignments to draft go to `ip-assignment-licence-drafter`; infringement claims to `ip-infringement-analyst`.
