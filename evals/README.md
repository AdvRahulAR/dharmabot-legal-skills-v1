# Evals

Behavioural test cases for the skills: frozen prompts with rubrics. Every case is synthetic. Do not add real client matters.

Each file covers one pack (`v0.1-cases.yaml` covers the first 26 skills). There are 976 cases; every skill has at least one output case and one gate case. A case looks like this:

```yaml
- id: bail-gate-pre-2024
  skill: bnss-bail-application-drafter
  kind: gate            # trigger | gate | output
  prompt: >
    Draft anticipatory bail. FIR registered 12 May 2024 for cheating.
  must:                 # all must appear in the response
    - routes to or applies crpc-bnss-transition-analyst
  must_not:             # none may appear
    - cites a BNSS section as governing without addressing the 2024 date
```

The three kinds of case:

- **trigger**: the right skill is chosen for a natural request, and a near-miss request does not choose it.
- **gate**: the skill stops, asks or reroutes when the jurisdiction, date or a blocking input is wrong or missing.
- **output**: required parts are present, arithmetic is right, and nothing is invented.

## Running

v0.1 evals are run by hand before each release. For each case:

1. Install the skills in Claude Code, Codex or Antigravity.
2. Start a fresh session, paste the `prompt` and attach any `fixtures`.
3. Mark each `must` and `must_not` line as pass or fail, and record the results in the release notes.

An automated runner (headless Claude Code and Codex CLI with a grader model, plus exact checks for numbers) is planned for v0.5. Contributions are welcome.
