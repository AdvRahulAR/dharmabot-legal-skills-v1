# Templates

## dharmabot-profile.md

A practice profile that tells the skills who you are and how you work: your State, courts, languages, citation style, formatting, contract playbook positions, when to stop and ask, and your confidentiality settings.

**How to use it**

1. Copy `dharmabot-profile.md` into the working folder you open in Claude Code, Codex or Antigravity (the folder where you keep the matter you are working on, or a parent folder you always work from).
2. Fill in the placeholders in `[square brackets]`. Delete sections that do not apply. Leave a field blank rather than guessing.
3. Keep the file name `dharmabot-profile.md` so the skills can find it.

**What reads it**

- `legal-task-router` reads the profile first. It uses your State, courts and practice type to pick skills and forums, and your confidentiality settings to decide whether to run `client-data-redaction-checker` before any client document is processed.
- Other skills can read it if it is present in the working folder: drafting skills use your formatting, language and house style; `court-pleading-formatter` and `efiling-bundle-defect-checker` use your court list; `playbook-contract-reviewer` and the contract drafters use your playbook positions; `citation-verifier` and the research skills use your citation style; `limitation-calculator` can use your home State for local holidays and court vacations.
- If the profile is missing, the skills still work. They ask for what they need.
- A matter's own instructions always override the profile.

**What must not go in it**

The profile is a description of your practice, not of any client. **Do not put client names, matter details, case numbers, opposing parties, fee arrangements or any other client confidential information in it.** It may be read by every skill on every matter, and it may be shared with colleagues or committed to a repository. Keep client information in the matter folder, and redact it before AI processing if your settings say so.
