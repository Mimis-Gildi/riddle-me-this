# Section 3 Footnote Map

Cross-reference: `site/_posts/2026-04-23-ai-maggedon-2026.adoc` lines 184-349
against `inbox/golden-children-research.md` (verified research stash).

---

## Existing Footnotes Already Declared (lines 20-29)

| ID | Source | Used in Section 3? |
|----|--------|-------------------|
| fn-mythos-price | Anthropic Pricing | No (section 1) |
| fn-veracode | Veracode 2025 GenAI Code Security Report | No (section 1, line 55) |
| fn-cc-commits | SemiAnalysis: Claude Code commits | No (section 1, line 57) |
| fn-aikido | Aikido Security 2026 | No (section 1, line 58) |
| fn-gpt2 | Daudens: Too Powerful to Release | No (section 1, line 64) |
| fn-mythos-holes | Ottenheimer: Boy That Cried Mythos | No (section 1, line 67) |
| fn-khamenei | US cyber ops against Iran | No (section 1, line 83) |
| fn-monorepo | Potvin & Levenberg 2016 | No (section 2, line 160) |
| fn-data-flywheel | Google Privacy + Hal Varian | No (section 2, line 160) |
| fn-lifecycle-as-code | SWE Book + SRE Book | No (section 2, line 178) |

**None of the 10 existing footnotes are referenced in section 3.** Section 3 currently has zero footnotes.

---

## Claims Requiring NEW Footnotes

### 1. Veracode 2.74x (REUSE existing)

```
LINE: 198
TEXT: "2.74x more vulnerabilities, can't review output"
SOURCE: Veracode 2025 GenAI Code Security Report (same as fn-veracode)
FOOTNOTE ID: veracode (reuse)
FOOTNOTE TEXT: N/A -- already declared at line 21
USAGE: footnote:veracode[]
```

### 2. METR 19% Slower

```
LINE: 202
TEXT: "19% slower (METR), thinks 20% faster"
SOURCE: METR Randomized Controlled Trial, July 2025
         https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
FOOTNOTE ID: metr
FOOTNOTE TEXT: 16 experienced open-source developers, 246 tasks, randomized controlled trial. Developers took 19% longer with AI but believed they were 20% faster -- a 39-point perception gap. Small sample, early 2025 tools. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/[METR: AI-Experienced OS Dev Study,window=_blank]
DECLARATION: :fn-metr: footnote:metr[16 experienced open-source developers, 246 tasks, randomized controlled trial. Developers took 19% longer with AI but believed they were 20% faster -- a 39-point perception gap. Small sample, early 2025 tools. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/[METR: AI-Experienced OS Dev Study,window=_blank]]
USAGE: {fn-metr}
```

### 3. DX Staff+ 4.4 hrs/week (first reference in table)

```
LINE: 206
TEXT: "DX Staff+ daily users"
SOURCE: DX Research Q1 2026 (121K developers, 450+ companies)
         https://getdx.com/blog/ai-assisted-engineering-q4-impact-report-2025/
FOOTNOTE ID: dx
FOOTNOTE TEXT: 121,000 developers across 450+ companies; productivity plateaued at ~10% gains despite 93% adoption. Staff+ engineers using AI daily: 4.4 hours saved per week. https://getdx.com/blog/ai-assisted-engineering-q4-impact-report-2025/[DX: AI-Assisted Engineering Impact Report,window=_blank]
DECLARATION: :fn-dx: footnote:dx[121,000 developers across 450+ companies; productivity plateaued at ~10% gains despite 93% adoption. Staff+ engineers using AI daily: 4.4 hours saved per week. https://getdx.com/blog/ai-assisted-engineering-q4-impact-report-2025/[DX: AI-Assisted Engineering Impact Report,window=_blank]]
USAGE: {fn-dx}
```

### 4. Codeforces < 2000

```
LINE: 233-234
TEXT: "It scores below 2000 on Codeforces, and only for problem types it had in its training data, abysmally otherwise. That score is exceeded by only 5% of coders at the competition."
SOURCE: CodeELO benchmark (arXiv:2501.01257). o1-mini: 1578 Elo, Claude: not in top results.
         Codeforces rating distribution: 2000+ is Candidate Master and above (~top 5% of active rated participants).
FOOTNOTE ID: codeelo
FOOTNOTE TEXT: CodeELO benchmark (arXiv:2501.01257) for LLM scores: best LLM (o1-mini) scored 1578 Elo; most LLMs in bottom 25% of human participants. Codeforces public rating distribution for the ~5% percentile: 2000+ is Candidate Master. https://arxiv.org/abs/2501.01257[CODEELO: Benchmarking Competition-level Code Generation,window=_blank] and https://codeforces.com/blog/entry/68288[Codeforces Rating Distribution,window=_blank]
DECLARATION: :fn-codeelo: footnote:codeelo[CodeELO benchmark (arXiv:2501.01257) for LLM scores: best LLM (o1-mini) scored 1578 Elo; most LLMs in bottom 25% of human participants. Codeforces public rating distribution for the ~5% percentile: 2000+ is Candidate Master. https://arxiv.org/abs/2501.01257[CODEELO: Benchmarking Competition-level Code Generation,window=_blank] and https://codeforces.com/blog/entry/68288[Codeforces Rating Distribution,window=_blank]]
USAGE: {fn-codeelo}
NOTE: Two sources combined: CodeELO paper for LLM scores, Codeforces own data for the ~5% human percentile. Both are now cited in the footnote. The "16-year-olds in code camps regularly exceeded 2000 points" (line 235) is common knowledge in competitive programming circles but has no specific citation -- FLAG if Team Lead wants it sourced.
```

### 5. DX 4.4 hrs/week (second reference, explicit)

```
LINE: 251-252
TEXT: "save up to 4.4 hours per week -- highest gains seen in independent data (DX, 121K developers, Q1 2026)"
SOURCE: Same DX Research as #3 above
FOOTNOTE ID: dx (reuse)
USAGE: footnote:dx[]
```

### 6. awesome-claude-code 40,700 stars

```
LINE: 345
TEXT: "the 40,700-star awesome-claude-code repository"
SOURCE: GitHub hesreallyhim/awesome-claude-code (40.7K stars, verified April 24, 2026)
         https://github.com/hesreallyhim/awesome-claude-code
FOOTNOTE ID: awesome-cc
FOOTNOTE TEXT: Community-curated collection of Claude Code agent skills, workflows, tooling, and CLAUDE.md files. https://github.com/hesreallyhim/awesome-claude-code[awesome-claude-code,window=_blank]
DECLARATION: :fn-awesome-cc: footnote:awesome-cc[Community-curated collection of Claude Code agent skills, workflows, tooling, and CLAUDE.md files. https://github.com/hesreallyhim/awesome-claude-code[awesome-claude-code,window=_blank]]
USAGE: {fn-awesome-cc}
```

### 7. MCP Servers 16,670

```
LINE: 347
TEXT: "16,670 MCP servers."
SOURCE: MCP Registry + community directories (as of Sept 2025, likely higher now)
         https://registry.modelcontextprotocol.io/
FOOTNOTE ID: mcp-registry
FOOTNOTE TEXT: As of late 2025; the registry continues to grow. https://registry.modelcontextprotocol.io/[MCP Server Registry,window=_blank]
DECLARATION: :fn-mcp-registry: footnote:mcp-registry[As of late 2025; the registry continues to grow. https://registry.modelcontextprotocol.io/[MCP Server Registry,window=_blank]]
USAGE: {fn-mcp-registry}
```

### 8. 400,000 Shared Skills

```
LINE: 347
TEXT: "400,000 shared skills."
SOURCE: SkillKit marketplace via awesome-claude-code-toolkit (rohitg00)
         https://github.com/rohitg00/awesome-claude-code-toolkit
FOOTNOTE ID: skillkit
FOOTNOTE TEXT: Via SkillKit marketplace, aggregated in awesome-claude-code-toolkit. https://github.com/rohitg00/awesome-claude-code-toolkit[awesome-claude-code-toolkit,window=_blank]
DECLARATION: :fn-skillkit: footnote:skillkit[Via SkillKit marketplace, aggregated in awesome-claude-code-toolkit. https://github.com/rohitg00/awesome-claude-code-toolkit[awesome-claude-code-toolkit,window=_blank]]
USAGE: {fn-skillkit}
```

---

## Claims WITHOUT Sources (Flagged)

### F1. "9 out of 10 most enthusiastic OpenClaw users" (line 243)

```
LINE: 243
TEXT: "This group constitutes 9 out of 10 most enthusiastic OpenClaw users!"
SOURCE: NO SOURCE IN RESEARCH STASH
STATUS: FLAG -- this appears to be insider/private data or editorial assertion. No public source found. If from Vadim's hacker community data, it should be framed as such ("in our observation" or similar). If it's an OpenClaw metric, cite it.
```

### F2. "16-year-olds in code camps regularly exceeded 2000 points" (line 235)

```
LINE: 235
TEXT: "16-year-olds in code camps regularly exceeded 2000 points."
SOURCE: NO SPECIFIC CITATION
STATUS: FLAG -- this is common knowledge in competitive programming circles (IOI/ICPC participants regularly achieve Candidate Master+), but no specific source was found. Can be verified via Codeforces public profiles but would need a specific citation to footnote. Consider dropping or softening to "competitive programming students regularly exceed 2000."
```

### F3. "3,000-developer metrics pool shows 50% experimentation" (line 267)

```
LINE: 267
TEXT: "one hacker community's 3,000-developer metrics pool shows 50% of the interaction is experimentation"
SOURCE: NO PUBLIC SOURCE
STATUS: FLAG -- this is insider data from Vadim's closed hacker communities. No footnote possible unless the community publishes this data. Current framing ("one hacker community's") is appropriate for unattributed private data.
```

### F4. Senior adoption rate (lines 249-250) -- ADDED per Truthy-2 review

```
LINE: 249-250
TEXT: "These people like Claude Code the least. So the adoption level in this group is the lowest and it grows the slowest."
SOURCE: NO SOURCE IN RESEARCH STASH
STATUS: FLAG -- Research stash has DX data (power users save more) and SO data (frequent users more satisfied), but neither says seniors have the LOWEST adoption rate. This is presented as fact but appears to be insider observation. Should be framed as such or sourced.
```

### F5. Wizard adoption and contribution rates (lines 261-262) -- ADDED per Truthy-2 review

```
LINE: 261-262
TEXT: "Wizards' adoption level is nearly absolute. You will find half of them actively contributing to all the Agentic tools."
SOURCE: NO SOURCE IN RESEARCH STASH
STATUS: FLAG -- "Nearly absolute" and "half of them" are specific quantitative claims with no citation. If from Vadim's insider knowledge, frame it that way ("in the communities I track" or similar).
```

### F6. "ALL" research says 2X impossible (line 254) -- ADDED per Truthy-2 review

```
LINE: 254
TEXT: "ALL the referenced research over thousands of teams and developers says *2X is an impossibility*!"
SOURCE: Supported directionally by METR (19% slower) and DX (10% gain), but "ALL" is an absolute claim.
STATUS: FLAG -- Strong synthesis claim. The individual studies support it, but "ALL" is absolute. Options:
  (a) Stack footnote refs: {fn-metr}{fn-dx} or footnote:metr[] footnote:dx[] if stacking works in AsciiDoc
  (b) Parenthetical: "(see METR, DX above)"
  (c) Soften "ALL" to "every independent study referenced here"
  Recommend (a) or (c).
```

### F7. "3 times SLOWER than coding alone (29% average speed)" (lines 287-288)

```
LINE: 287-288
TEXT: "We have found that if I let Claude Code generate my functional code first, I am 3 times SLOWER than coding alone (29% average speed)."
SOURCE: PERSONAL EXPERIMENT (Vadim + Claude)
STATUS: OK as-is -- framed as personal experiment ("My Claude and I ran an experiment"). No footnote needed; it's first-person testimony, not a cited claim.
```

---

## Summary: Proposed Footnote Declarations

Add these to the article header (after line 29):

```asciidoc
:fn-metr: footnote:metr[16 experienced open-source developers, 246 tasks, randomized controlled trial. Developers took 19% longer with AI but believed they were 20% faster -- a 39-point perception gap. Small sample, early 2025 tools. https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/[METR: AI-Experienced OS Dev Study,window=_blank]]
:fn-dx: footnote:dx[121,000 developers across 450+ companies; productivity plateaued at ~10% gains despite 93% adoption. Staff+ engineers using AI daily: 4.4 hours saved per week. https://getdx.com/blog/ai-assisted-engineering-q4-impact-report-2025/[DX: AI-Assisted Engineering Impact Report,window=_blank]]
:fn-codeelo: footnote:codeelo[CodeELO benchmark (arXiv:2501.01257) for LLM scores: best LLM (o1-mini) scored 1578 Elo; most LLMs in bottom 25% of human participants. Codeforces public rating distribution for the ~5% percentile: 2000+ is Candidate Master. https://arxiv.org/abs/2501.01257[CODEELO: Benchmarking Competition-level Code Generation,window=_blank] and https://codeforces.com/blog/entry/68288[Codeforces Rating Distribution,window=_blank]]
:fn-awesome-cc: footnote:awesome-cc[Community-curated collection of Claude Code agent skills, workflows, tooling, and CLAUDE.md files. https://github.com/hesreallyhim/awesome-claude-code[awesome-claude-code,window=_blank]]
:fn-mcp-registry: footnote:mcp-registry[As of late 2025; the registry continues to grow. https://registry.modelcontextprotocol.io/[MCP Server Registry,window=_blank]]
:fn-skillkit: footnote:skillkit[Via SkillKit marketplace, aggregated in awesome-claude-code-toolkit. https://github.com/rohitg00/awesome-claude-code-toolkit[awesome-claude-code-toolkit,window=_blank]]
```

## Placement Map

| Line | Claim | Footnote | Type |
|------|-------|----------|------|
| 198 | 2.74x more vulnerabilities | `footnote:veracode[]` | Reuse |
| 202 | 19% slower (METR) | `{fn-metr}` | New (first use) |
| 206 | DX Staff+ daily users | `{fn-dx}` | New (first use) |
| 233 | below 2000 on Codeforces | `{fn-codeelo}` | New (first use) |
| 251-252 | 4.4 hours per week (DX, 121K) | `footnote:dx[]` | Reuse |
| 345 | 40,700-star awesome-claude-code | `{fn-awesome-cc}` | New (first use) |
| 347 | 16,670 MCP servers | `{fn-mcp-registry}` | New (first use) |
| 347 | 400,000 shared skills | `{fn-skillkit}` | New (first use) |

## Flagged (no source available)

| Line | Claim | Status |
|------|-------|--------|
| 235 | 16-year-olds exceed 2000 | Common knowledge, no specific citation |
| 243 | 9 out of 10 OpenClaw users | No source -- insider data or editorial |
| 249-250 | Seniors have lowest adoption | No source -- insider observation (Truthy-2 flag) |
| 254 | "ALL" research says 2X impossible | Synthesis claim -- consider stacking fn-metr + fn-dx (Truthy-2 flag) |
| 261-262 | Wizard adoption "nearly absolute", "half contributing" | No source -- quantitative claims need framing (Truthy-2 flag) |
| 267 | 3,000-dev pool, 50% experimentation | Private community data, framing is OK |
| 287-288 | 3x slower personal experiment | First-person testimony, no footnote needed |
