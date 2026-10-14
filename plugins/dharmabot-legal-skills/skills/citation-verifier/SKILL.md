---
name: citation-verifier
description: Checks every case citation, statutory reference and quotation in a legal draft against the actual source text, using an exact-match script for quotations and recording a hash of each source checked. Use before filing or sending any brief, petition, opinion or memo, when someone asks "check my citations", or after another AI skill has produced authorities. Do not use to find new authorities; this skill only verifies those already cited.
---

# Citation Verifier

Every output is a verification report for the advocate who signs the document to review.

## Purpose

Catch invented, misquoted or misattributed authorities before they reach a court or client. AI tools can produce convincing citations that do not exist; this skill assumes nothing is correct until checked.

## Jurisdiction gate

Works for any jurisdiction. Note the forum, because it decides which citation formats are acceptable.

## Required inputs

Mark as **blocking**: the draft (or the list of citations and quotations to check).

For each authority, the source text if the user has it (a judgment PDF or text, statute text). Otherwise the skill will try to retrieve it from official or reliable sources (the Supreme Court and High Court websites, India Code, the Gazette, or a database the user has access to).

## Method

1. Extract every reference from the draft into a list: case names with citations, neutral citations, statute sections, rules, notifications, and every passage in quotation marks with its pinpoint (paragraph or page).
2. For each case, retrieve the judgment text. Confirm the case exists, the parties and the court, the date, and that the citation (volume, reporter, page or neutral citation) belongs to that case.
3. For each quotation, save the source text to a file and run the bundled script:

   ```
   python3 scripts/check_quote.py --source judgment.txt --quote "exact words quoted"
   ```

   It reports `EXACT`, `EXACT_AFTER_NORMALISING` (differences only in spacing, quote marks or line breaks) or `NOT_FOUND`, the paragraph and page markers near the match, and a SHA-256 hash of the source file. Do not "repair" a quotation that is `NOT_FOUND`; report it.
4. Check the pinpoint: the quoted passage is at the paragraph or page cited.
5. Check that the proposition the draft attributes to the authority is actually what the passage says, and whether it is the holding or only an observation, a dissent, or a submission recorded by the court.
6. For statutes, confirm the section exists in the current text, the wording quoted matches, and the provision is in force (not repealed, renumbered or stayed). For the new criminal codes, check old and new numbering with `ipc-bns-concordance-mapper`.
7. Where the user can access a citator or later-treatment search, check that the case has not been overruled or doubted; otherwise say this was not checked.

## Output

A table: reference · status (verified / wrong citation / misquoted / wrong pinpoint / proposition not supported / not found / not checked) · details · source and hash. Then a short list of the corrections needed, most serious first.

## Guardrails

- Never mark something verified unless you actually read the source text.
- Never invent a replacement citation for one that failed. Suggest how the advocate can find a correct authority instead.
- Record the date each source was checked.
