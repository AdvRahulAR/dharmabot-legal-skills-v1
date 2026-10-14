---
name: will-drafter
description: Drafts wills and codicils in India under the Indian Succession Act, 1925, or within Muslim personal law limits on bequests, with clear gifts, residuary clause, executors, guardians for minors, attestation and optional registration, and drafts simple private trusts under the Indian Trusts Act, 1882 for estate planning. Use when a lawyer asks for a will for an elderly client, a codicil changing a gift, a will with a testamentary trust, or steps to make a will harder to challenge. Do not use for intestate shares; use intestate-succession-share-calculator.
---

# Will Drafter

Every output is a draft for an advocate enrolled in India to check before execution.

## Purpose

Produce a clear, valid will that disposes only of what the testator can dispose of, and leaves evidence that will defeat a later challenge.

## Jurisdiction gate

Confirm the testator's religion, domicile and where the assets are. Muslim testators are generally limited to bequeathing one-third of the estate, and bequests to heirs need the other heirs' consent (confirm under the applicable school). Check whether a State uniform civil code governs testamentary succession for this testator (Uttarakhand in force; Gujarat's code reportedly received the President's assent in September 2026 and comes into force on a date the State notifies; Assam's bill was reportedly passed by the Assembly in May 2026, with assent not confirmed; check assent, commencement and coverage, including any Scheduled Tribe exclusion [verify]). For assets abroad, mark foreign succession points "to be confirmed by counsel qualified in [jurisdiction]".

## Required inputs

Mark as **blocking**:
- the testator's full name, age, religion and family members (spouse, children, parents);
- the list of assets and how each is held (self-acquired, inherited, HUF or coparcenary share, joint names, nominations);
- who gets what, executors, and guardians for minor children;
- the testator's health and capacity, and whether anyone who benefits is helping arrange the will.

## Method

1. Retrieve the current official text of the Indian Succession Act, 1925 (wills, execution, attestation, probate), the Registration Act, 1908 (optional registration of wills), the Indian Trusts Act, 1882 and the applicable personal law. Record the version and date. Note that the Repealing and Amending Act, 2025 is reported to have omitted section 213 on compulsory probate; confirm its commencement.
2. Classify each asset. A Hindu coparcener can bequeath only their interest in coparcenary property; HUF and jointly owned assets need care. Note that nominations in bank, insurance, shares or provident funds may not override the will; check current authority.
3. Draft: declaration and revocation of earlier wills; specific gifts with exact descriptions; conditions or life interests; residuary clause; executors and alternates with powers; guardians; trust provisions for minors or dependants; debts and expenses; and a clause on assets acquired later.
4. Testamentary trust or a separate private trust: trustees, beneficiaries, powers, distribution and termination.
5. Reduce challenge risk: record reasons for unequal or unexpected gifts; keep beneficiaries away from execution; two independent attesting witnesses who sign in the testator's presence; a medical certificate of capacity where age or illness raises doubt; consider video recording and registration.
6. Prepare execution instructions.
7. Hand off probate questions to `probate-succession-certificate-drafter`.

## Output

1. Draft will or codicil, and trust deed if asked.
2. Asset schedule and a note of assets the will cannot pass.
3. Execution checklist for testator and witnesses.

## Guardrails

- Never draft a will for a person whose capacity or free will is in doubt without flagging it to the advocate.
- Never let a beneficiary act as an attesting witness.
- Never state tax consequences as settled; refer to a tax adviser.
- The advocate supervises execution.
- Before anything is filed, sent or relied on, run `pre-filing-verification-checker` to verify every authority and quotation, and keep its log with the file.
