# Hacker Notebook

Session: 2026-04-25
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

## Task 4: Research Post Conversion + Section 4 Research

**Status:** Flags fixed, sent to Truthy for re-verification.

### Research post created
- Converted `inbox/golden-children-research.md` (markdown) to `site/_posts/2026-04-23-ai-maggedon-2026-research.adoc` (AsciiDoc)
- Hidden blog post (hidden: true, search: false) for editorial transparency
- Approved by Truthy-2 on first pass

### Section 4 research (10 claims)
- All 10 claims researched and verified against primary sources
- Key correction: Snyk 36% is ANY security flaw, not prompt injection specifically (2.6%)
- Added to research post with 9 subsections, source verification entries, and corrections log

### Truthy-2 review: APPROVED with 3 FLAGS
1. **Palo Alto quote inflated** -- fixed externally (Team Lead)
2. **Gartner 40% no URL** -- fixed: added Gartner newsroom press release URL (Aug 2025)
3. **Ransomware dwell time unsourced** -- fixed: Mandiant M-Trends 2025 (6 days) + Sophos 2025 (4 days) with URLs

### Lesson
The "file modified since read" error hit twice. External edits happening between my read and edit attempts. Always re-read immediately before editing shared files.

## Task 5: Section 4 Draft for Vadim

**Status:** Written, sent to Truthy for LLM-speak scan. Awaiting review.

**File:** `inbox/section4-draft.md`

### Structure
- DarkConf opening with `[VADIM:]` marker (unattributed, his voice)
- Stats cascade: 91% can't stop agents, 89% YoY increase, SANS #1 technique, 8-min breach
- OpenClaw case study: 9 CVEs, Snyk corrected numbers, sandbox-off defaults
- Punchline connector `[VADIM:]` marker (ties Section 3 wizards to Section 4 attack surface)

### Decisions
- Excluded Darktrace 92% (wrong stat for the TODO's claim; actual is 76%)
- Corrected Snyk 36% conflation
- Corrected Palo Alto quote inflation
- Kept short per Team Lead's instruction

## Task 7: Section 2 LLM Tortured Language Scan

**Status:** Complete. Sent to Team Lead.

**Scope:** Lines 125-208, section "2. Stage Zero Monetization: Google Deterministic AI"

### Findings

Section is very clean. Vadim's authentic voice throughout -- em-dashes, hacker vocabulary, direct confrontation, real anecdotes (MATILDA 2017, partner call), opinions stated flat, specific technical terms (DDD Aggregate, trunk-based-development). Only 1 low-severity flag identified.

**Flag 1 (LOW):** Line 200, "Time is on their side." -- stock cliche after an otherwise sharp metaphor. Not technically LLM-speak but worth noting as a weaker close.

**Cleared items (considered and rejected):**
- Line 175-176 triple list ("edge cases, regulatory constraints, competitive secret sauce") -- concrete enumeration, not empty triple-beat
- Line 169 "thing of beauty" -- opinion stated flat per style guide
- Line 205 "Not because X -- because Y" -- explicitly listed as Vadim signature pattern in style guide
- Line 171 "almighty" -- sarcastic/ironic, hacker humor
- Line 138 "futuristic" -- ironic contrast with "yesterday's ideas"
- Lines 192-195 semicolon list -- Vadim's documented thought-unit delimiter style

### Assessment
This section reads as Vadim writing at full power. The voice is consistent, the argument is specific, the technical knowledge is real (DDD, trunk-based, Borg), and the humor is authentic (Python the snake, the wink emoji on line 178). No graduation-speech cadence, no motivational framing, no reversible dualities. Clean.

## Task 6: Section 5 Draft for Vadim

**Status:** Written, sent to Truthy for LLM-speak scan.

**File:** `inbox/section5-draft.md`
**Primary source:** `inbox/my-bff-claude.md`

### Structure
- Anchor concept: LLM calls are atomic and stateless
- Tier 0: Naked model (wild vs civilized), enterprise $2M burn
- Tier 1: Chatbot (service vs orchestrated sub-tiers)
- Tier 2: Coding agent (architecture table: CC vs OpenCode vs Aider)
- Tier 3: Autonomous agent (OpenClaw architecture, Heartbeat, skills)
- Tradeoff table: tier / autonomy / oversight / risk surface
- Gap thesis connecting back to sections 3 and 4

### Excluded (noted for Vadim)
- Model terminology deep-dive (quantization, reified)
- Local self-hosting details
- Yggdrasil vs OpenClaw comparison (promotional)
- Infrastructure changes since 2024 (prompt caching, KV mgmt)
- Convergence point (CC adding Tier 3, OpenClaw adding Tier 2)

## Task 8: Truthy Review Fixes (Section 4 + Section 5)

**Status:** Fixed and sent for re-verification.

### Section 4 fixes (CRITICAL)
1. **7 missing footnote declarations** -- wrote to `inbox/section4-footnotes-for-article.md` for team-lead to insert into article header after line 37. All 7 URLs sourced from research post.
2. **Typo fix** -- line 423 `{2fn-ci-2026}` → `{fn-ci-2026}` (stray `2`). Also in deliverable for team-lead.
3. **Research post Palo Alto quote** -- fixed line 340: "potential biggest" → "a potent insider threat"
4. **my-bff-claude.md Snyk stat** -- fixed 3 instances: line 311, 444, 572-573. All now correctly say "36.82% any security flaw; 2.6% prompt injection"
5. **my-bff-claude.md Palo Alto** -- fixed line 312
6. **golden-children-research.md Palo Alto** -- fixed line 262
7. **Synopsis post** -- fixed line 37-38 (both Snyk stat and Palo Alto quote)

### Section 5 fixes
1. **FLAG 1** -- `section5-draft.md` line 94: "40+ model providers" → "12+ model providers" (research stash says 12+ API providers, 40+ is plugin configs)
2. **FLAG 2** -- `section5-draft.md` line 70: "98.4% runs on your machine" → "Nearly all of it runs on your machine" (no derivation for specific percentage)

### Verification
- Grep sweep confirmed zero stale "potential biggest insider" or "36% prompt injection" references in content files
- All remaining hits are meta-commentary in notebooks/draft notes (correct)

## Task 9: Section 2 Diligent Critique

**Status:** Sent to team-lead for routing to Truthy.

### Findings (12 total)
- **CRITICAL (1):** Line 161 "Apple tried to match this play a decade ago with Alexa" -- Alexa is Amazon's product, not Apple's
- **HIGH (3):** Line 221 trailing validation question; line 147 missing comma (amphiboly); line 144 "three companies" unnamed
- **MEDIUM (4):** Line 129 tense mismatch; lines 141-142 dangling modifier; line 203 "fluke" unclear; line 155 "subtly and covertly" tautological + contradicts "in plain sight"
- **LOW (4):** Line 148 vague "real assets"; lines 128-129 unsourced event; lines 213-217 ambiguous attribution; line 207 Deus Ex Machina usage

### Cleared (7 items)
Considered and rejected as false flags: line 127 rhetorical question, line 170 "thing of beauty", line 172 "almighty", line 191 contrast structure, line 209 "Not because... -- because...", semicolon list, wink emoji. All confirmed as Vadim's authentic voice per style guide.

### Assessment
The DDD Aggregate → dependency → identity consumption argument (lines 172-186) is the strongest writing in the article. Section reads as Vadim at full power except for the Apple/Alexa error and a few grammar issues.

## Task 10: "Random Hacker" Attribution Research

**Status:** COMPLETE. Sent to team-lead.

### Finding
"Random Hacker" (lines 213-217) is a well-established hacker culture convention from the Jargon File. "J. Random Hacker" = composite archetype of any typical hacker. Appendix B of the Jargon File is the canonical source. Attribution is culturally correct for our audience.

### Note
catb.org had TLS cert error; confirmed through Wikipedia and multiple secondary sources all pointing to Jargon File.

## Task 11: Section 2 Ultra-Diligent Final Pass

**Status:** Sent to Truthy for filtering.

### Findings (16 total)
- **CRITICAL (0):** Previous critical (Apple/Alexa) was fixed to Siri.
- **HIGH (3):** Line 136 missing noun after "pragmatic"; card metaphor mapping (H2) and self-contradiction lines 170 vs 201 (H3)
- **MEDIUM (5):** Line 129 amphiboly; line 144 "behoves" construction + British spelling; line 157 "upsidedown" spelling; lines 155/207 covert vs plain sight; line 179 "safe keeping" grammar
- **LOW (8):** Timing vagueness, decade imprecision, mixed idiom, undefined "lifer", stock cliché, Deus Ex Machina usage, trailing validation, compressed grammar
- **CLEARED (10):** All Vadim voice patterns verified

### Lesson
Re-reading after edits catches what the first pass missed. The Apple/Alexa fix proves the value of the pipeline.

## Task 12: Section 3 Full Critique

**Status:** Sent to Truthy for filtering.

### Findings (24 total)
- **CRITICAL (1):** Lines 272-274 "That score" pronoun ambiguity creates OPPOSITE meaning (reads as AI in top 5% when arguing AI is weak)
- **HIGH (5):** Line 228 inverted word order; line 346 thesis oversimplifies evidence; lines 392-399 six unsourced geographic claims; lines 401-407 unsourced repo methodology; line 411 "culminated into"
- **MEDIUM (7):** Line 225 hedging; line 228 tense shift; line 270 missing article; line 274 unsourced 16-year-olds claim; line 308 double "incredibly" (LLM-speak); line 386 awkward gerund; line 417 tautological enablement
- **LOW (11):** Minor grammar, unsourced claims, catalog voice shift, trailing validation
- **CLEARED (8):** All swap-tested contrasts passed

### Key insight
Two distinct quality zones: lines 223-388 strong (well-sourced case analysis), lines 390-423 weakest part of article (dense unsourced claims about global hacker demographics).

## Task 13: Section 3 Claims Catalog (Post-Rewrite)

**Status:** Sent to Truthy for verification.

### Scope
Fresh catalog of EVERY factual claim in Section 3 (lines 230-448) after Vadim's significant rewrite. Four categories: SOURCED, PERSONAL, UNSOURCED, COMMON KNOWLEDGE.

### Changes observed from Vadim's rewrite
- "That score" ambiguity FIXED (line 282)
- "incredibly wanting" → "equally wanting" (line 326, LLM-speak fixed)
- "faster" → "happier" in thesis (line 364)
- "culminated into" → "culminated in" (line 429)
- "enablement enables" tautology fixed (line 436)
- Lines 279-288 EXPANDED with Codeforces analysis
- Lines 424-425 "uptick" → "jump"/"hike"

### Catalog summary
- **13 SOURCED** -- all with verified footnote IDs
- **11 PERSONAL** -- all with adequate framing signals (1 borderline: line 322 unnamed community)
- **25 UNSOURCED** -- two major clusters:
  - Lines 279-302: AI capability characterizations (reasonable but unsourced)
  - Lines 410-432: Geographic distribution + repo methodology (strongest claims, zero sources)
- **7 COMMON KNOWLEDGE** -- audience-appropriate
- **7 ANALYSIS/CONCLUSIONS** -- derived from evidence, varying strength

### Highest-risk items
U4-U9: Geographic claims with specific ratios (US 1/10 of Prague, Prague/Cluj-Napoca as hacker culture capitals, India crisis, China exceeds all others combined)
U10-U13: Repo methodology with specific multipliers (10x forking, 10x imitations, ~100 conventional, ~50 mobile era)

### Verification done
- Codeforces ranking system: Confirmed Candidate Master = level 5 of 10, 1900-2099, top ~5% via WebSearch
- Cluj-Napoca: Confirmed "Silicon Valley of Eastern Europe" for IT outsourcing but NOT verified as "capital of Hacker Culture"
- All 13 footnote IDs verified against declarations in lines 19-37

## Task 14: Hacker Culture Geography Research

**Status:** COMPLETE. Sent to team-lead.

### Three claims researched
1. **"about 1/10 as compared to Prague"** -- Direction CORRECT, ratio actually understated. IOI per capita: Czech Republic 9.2 medals/million vs US 0.38 = ~24:1. HackerRank: CZ #7-9, US #28. No single published source for the exact 1/10 ratio.
2. **"Prague, the previous capital of the Hacker Culture"** -- STRONG evidence. Slush Pool (first Bitcoin mining pool, 2010), Trezor (first hardware wallet, 2013), Paralelní Polis (2014-2026, CLOSED March 2026), HCPP conference (Stallman, ESR spoke), brmlab hackerspace. Called "crypto-anarchist capital of 21st century" by multiple publications.
3. **"Cluj-Napoca, the current capital of the Hacker Culture"** -- WEAKEST claim. Romania's competitive programming is world-class (#2-3 IOI all-time, olympiad since 1978), Cluj has strong IT density (20K devs in 300K city). But "capital of Hacker Culture" conflates IT outsourcing hub with hacker culture. No hackerspaces found in Cluj, no crypto projects, no CTF teams, DefCamp is primarily Bucharest.

### Key data points
- IOI all-time: China #1 (146), Poland #2 (135), Romania #3 (135), Korea #4 (131), US #7 (127), Czech Republic #18 (99)
- Romania national olympiad in informatics founded 1978 (11 years before IOI)
- Romania founded CEOI (1994), hosted it in Cluj-Napoca twice (1994, 2000)
- Paralelní Polis closed March 2, 2026 -- "previous" is literally correct
- China: 2.27M active open source developers, state-backed open source policy
- US ICPC participation is "sharply declining" per published academic research

### Lesson
"Silicon Valley of Eastern Europe" ≠ "capital of Hacker Culture." IT outsourcing density and hacker culture are different things. Prague has hackerspace-to-crypto-innovation pipeline evidence. Cluj has IT company density evidence. The distinction matters.
