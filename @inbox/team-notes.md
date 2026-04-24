# Team Notes

## 2026-04-24

### Synopsis Post Created
- **File:** `site/_posts/2026-04-23-ai-maggedon-2026-synopsis.adoc`
- **Purpose:** Hidden blog post for LinkedIn copy-paste. Teases the AI-maggedon 2026 article.
- **Status:** With Truthy for review.

### Finding: AsciiDoc Anchor Gotcha
The `--` (em-dash shorthand) in section titles causes anchor IDs to collapse surrounding words:
- `== The Golden Children -- What have they done` → `#_the_golden_childrenwhat_have_they_done`
- `== AI Attack Surface -- The rest of us` → `#_ai_attack_surfacethe_rest_of_us`

This is asciidoctor 2.0.26 behavior. If anyone adds explicit `[#id]` anchors to the main article later, the synopsis links will need updating.

### Golden Children Research Stash Completed
- **File:** `inbox/golden-children-research.md`
- **Status:** FULLY APPROVED by Truthy-2. Zero outstanding issues.
- **Scope:** 5 research areas (A-E) covering Claude benchmarks, open communities, dev productivity studies, advanced team patterns, enterprise AI gap.
- **Key findings:**
  - METR RCT: devs 19% SLOWER with AI, but believe 20% faster (39-point perception gap)
  - Enterprise AI failure: 80-95% depending on source (RAND, MIT)
  - Claude dominates SWE-bench (real engineering) but absent from competitive programming top results
  - awesome-claude-code: 40.7K GitHub stars; MCP registry: 16,670+ servers
  - DORA: PR incidents tripled despite 98% more PRs merged
