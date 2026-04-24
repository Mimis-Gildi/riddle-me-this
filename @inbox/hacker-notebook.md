# Hacker Notebook

Session: 2026-04-24
Branch: 372-surviving-agentic-in-plebs

## Task 1: LinkedIn Synopsis Post

**Status:** Revision sent to Truthy for re-review.

**File:** `site/_posts/2026-04-23-ai-maggedon-2026-synopsis.adoc`

### First pass
- Read source article, style guide, reference post
- Verified AsciiDoc anchor IDs via asciidoctor
- Wrote synopsis: ~1231 chars, 5 topic teases
- Verified stats, 0 rendering warnings

### Truthy rejection (3 issues)
1. **CRITICAL:** 3 of 5 "Read more" links pointed to empty/TODO sections
2. Stats for topics 4-5 sourced from invisible `//` comments
3. "Golden few" blurb fabricated from section title alone

All valid catches. My self-check missed the obvious: I verified the anchors work but didn't check if the linked sections have visible content.

### Fix applied
- Removed section links from topics 3, 4, 5. Tease text stays (Team Lead instructed to tease from outline comments).
- Only sections 1 and 2 retain "→ Read more" links (both have written content).
- Fixed `hidden: false` → `hidden: true` (somehow flipped from my write).
- 3 total links now, all verified against rendered content.

### Lesson
Verify the DESTINATION, not just the link. A correctly-formed anchor to an empty section is worse than no link at all.

## Task 2: Golden Children Research Stash

**Status:** COMPLETE. Fully approved by Truthy-2 after 3 review rounds.

**File:** `inbox/golden-children-research.md`

### Research areas completed:
- A: Claude coding capabilities -- SWE-bench (#1), Aider, CodeELO (weak at competitive programming)
- B: Open communities -- awesome-claude-code (40.7K stars), MCP registry (16,670+ servers), OpenCode (95K stars)
- C: Developer productivity -- METR RCT (19% slower!), DX (121K devs, 10% gains), SO 2025 (trust down to 29%), DORA (incidents tripled)
- D: Advanced team patterns -- Agent Teams, Claude Cowork, Managed Agents, code review > generation for seniors
- E: The gap -- 80-95% enterprise AI failure rate, culture > tools, sloperator pattern, productivity paradox

### Key finding
The METR study is gold. 16 experienced devs, randomized controlled trial, 19% SLOWER with AI -- but believed 20% faster. 39-point perception gap. This is the heart of the "golden children vs everyone else" argument: the FEW who succeed have the culture and understanding to use AI where it works. The MANY believe the marketing and ship slop.

### Confidence notes
- All URLs verified via WebFetch or confirmed across multiple sources
- Vendor-published data flagged (Anthropic internal study)
- CodeELO paper: abstract verified, full PDF was binary/unreadable
- Discrepancy: Aider's own scores vs Anthropic-reported scores for Claude differ

### Review rounds
- Round 1: 14 approved, 4 rejected, 6 flagged
- Round 2: Truthy read stale `@inbox/` file, thought corrections missing. Root cause: two files at different paths.
- Round 3: All 10 corrections verified on disk + 2 new issues (Karpathy stars, Cowork framing) fixed. 8 clean approvals, 2 minor flags.
- Final: Both flags resolved (Faros uncertainty noted, introspection citation softened). Fully approved, zero outstanding.

### Lessons
1. The `@inbox/` vs `inbox/` dual-file confusion cost a full review cycle. Should have deleted the stale `@inbox/` copy immediately after the initial path fix.
2. Always verify my own edits with Read/Grep before reporting to the team. I did this and it saved me -- the proof was ready when challenged.
3. Truthy's catches were mostly valid. The fabricated DX quote, wrong CodeRabbit multipliers, and Faros/DORA misattribution were real errors my self-check missed.

## Task 3: Section 3 Footnotes + LLM-speak Fixes

**Status:** COMPLETE. All verified by Truthy-2 and rendering tested.

### Deliverables
1. **Footnote map:** `inbox/section3-footnote-map.md` -- 8 footnoted claims, 7 flagged unsourced claims
2. **6 new footnote declarations** added to article (lines 30-35): fn-metr, fn-dx, fn-codeelo, fn-awesome-cc, fn-mcp-registry, fn-skillkit
3. **8 footnote placements** in section 3 body
4. **4 LLM-speak fixes** in Claude block (lines 309, 311, 351-353)
5. **Line 260:** "ALL" softened to "Every independent study referenced here"

### Rendering test
- Jekyll build: zero errors, zero AsciiDoc warnings
- Stacked footnotes (line 260): rendered as [11],[12], both links work
- Table cell footnotes (lines 204/208/212): all rendered correctly inside `<td>`
- Total: 16 footnote definitions, all with working anchors

### Lesson
LLM-speak autopilot kicks in at bookend prose (opening/closing sentences of a block) while structured content (bullet lists) stays clean. Watch the transitions.
