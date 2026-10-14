# README images

Each image is a hand-written SVG (for GitHub) with a 2x PNG beside it for places that do not render SVG. They follow the Dharmabot AI visual identity: near-black background (#050505) with film grain and a soft cyan glow, electric cyan accent (#00e5ff), translucent cards with thin borders, and thin cyan connector lines. Type is Playfair Display italic with Space Grotesk for headlines, Inter for body text, JetBrains Mono for commands and skill ids, and Space Grotesk for letter-spaced labels and the DHARMABOT. wordmark. GitHub shows SVGs through `<img>`, which does not load web fonts, so each SVG embeds the subset of each font it uses as base64 WOFF2 (`@font-face`). Each SVG draws its own background, so it reads the same in GitHub light and dark mode.

| File | Size (1x) | Alt text |
| --- | --- | --- |
| `banner.svg` / `banner.png` | 1280 x 400 | Dharmabot Legal Skills: open-source AI skills for Indian lawyers. 317 skills in 39 packs, covering all States and UTs and cross-border work, for Claude Code, Codex and Antigravity. MIT licensed. |
| `skill-anatomy.svg` / `skill-anatomy.png` | 1280 x 1000 | How one skill works: user request, jurisdiction gate, temporal gate, required inputs, method (first retrieve the current official text), output as a draft for advocate review, and pre-filing verification, ending with the advocate checking, signing and filing. The gates stop and ask, or route to another skill. |
| `pack-map.svg` / `pack-map.png` | 1280 x 1146 | Map of all 39 packs and their skill counts, grouped into seven families: practice and research, transactions and corporate, safeguards and core tools, courts and disputes, people, property and family, regulatory, IP and sectors, and cross-border and languages. A bar on each row compares the pack with the largest pack (21 skills). |
| `workflow-civil-suit.svg` / `workflow-civil-suit.png` | 1280 x 1022 | The civil-suit-to-first-hearing workflow as one path of skills through six phases, from client-intake-conflict-screener to pre-filing-verification-checker and hearing-day-brief-builder, with advocate STOP checkpoints. |
| `install.svg` / `install.png` | 1280 x 640 | One repository installs into three agents: Claude Code through the plugin marketplace, OpenAI Codex as a plugin or in ~/.agents/skills, and Google Antigravity in ~/.gemini/config/skills or .agents/skills, with the install commands for each. |

Pack counts in `pack-map.svg` come from the `skills` list in `plugins/dharmabot-legal-skills/skill-registry.yaml`. Regenerate the image if that list changes.

Example use in the main README:

```markdown
![Dharmabot Legal Skills: open-source AI skills for Indian lawyers](docs/images/banner.svg)
```
