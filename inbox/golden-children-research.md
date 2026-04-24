# Research Stash: "The Golden Children -- What have they done"

Research for AI-maggedon 2026 article, Section 3.
Compiled: 2026-04-24 by Claude (Hacker).

---

## A. Claude's Actual Coding Capabilities (Hard Numbers)

### SWE-bench Verified (Real-World Engineering) -- April 24, 2026

Claude dominates the real-world software engineering benchmark:

| Rank | Model | Score | Org |
|------|-------|-------|-----|
| 1 | Claude Mythos Preview | 93.9% | Anthropic |
| 2 | Claude Opus 4.7 | 87.6% | Anthropic |
| 3 | Claude Opus 4.5 | 80.9% | Anthropic |
| 4 | Claude Opus 4.6 | 80.8% | Anthropic |
| 5 | Gemini 3.1 Pro | 80.6% | Google |
| 5 | DeepSeek-V4-Pro-Max | 80.6% | DeepSeek |
| 10 | Claude Sonnet 4.6 | 79.6% | Anthropic |

- 5 of the top 10 spots are Claude models.
- SWE-bench tests against real GitHub issues from production repos -- not synthetic toy problems.
- Top score jumped from ~65% (early 2025) to 87.6% (April 2026).
- Source: https://llm-stats.com/benchmarks/swe-bench-verified
- Confidence: VERIFIED (fetched April 24, 2026)
- Supports: Insider point #3 (deep understanding of Claude capabilities)

### Aider Polyglot (Multi-Language Code Editing)

225 Exercism coding exercises across C++, Go, Java, JavaScript, Python, Rust:

| Model | Score | Cost |
|-------|-------|------|
| claude-opus-4 (32k thinking) | 72.0% | $65.75 |
| claude-opus-4 (no think) | 70.7% | $68.63 |
| claude-3-7-sonnet (32k think) | 64.9% | $36.83 |
| claude-sonnet-4 (32k think) | 61.3% | $26.58 |
| claude-sonnet-4 (no think) | 56.4% | $15.82 |

- Source: https://aider.chat/docs/leaderboards/
- Confidence: VERIFIED (fetched live page)
- Note: Aider's own benchmark -- fair but measures one tool's edit format. Anthropic-reported numbers (89.4% for Opus 4.5) differ from Aider's own tests. Discrepancy likely due to different evaluation methodology.
- Supports: Point #3 (wizards know actual vs marketed numbers)

### Competitive Programming (Where Claude is WEAK)

CodeELO benchmark (Jan 2025, arXiv:2501.01257):
- o1-mini: 1578 Elo
- QwQ-32B-Preview: 1261 Elo
- Claude models: **NOT in top results** -- most LLMs place in the **bottom 25%** of all human participants
- O3 (OpenAI): 2727 Codeforces Elo
- Gemini 3 Pro: "Grandmaster-tier" Codeforces rating

Claude is NOT a competitive programming model. It excels at production engineering tasks (refactoring, bug fixing, feature implementation, codebase navigation) and is mediocre at algorithmic competition puzzles.

- Source: arXiv:2501.01257 (CODEELO paper)
- Confidence: VERIFIED (abstract confirmed via arXiv)
- Supports: Point #3, #5 (seniors/wizards know what Claude is good and bad at, use it where it's "happy")

### Key Insight for the Article

The gap between SWE-bench (real engineering, Claude #1) and Codeforces (competitive programming, Claude absent from top) IS the thing wizards understand. Claude is exceptional at understanding existing codebases, fixing real bugs, and shipping features. It's mediocre at novel algorithm design under constraint. Working WITH the grain means using it for the first set, not the second.

---

## B. Open Communities at the Bleeding Edge

### awesome-claude-code (GitHub)

**hesreallyhim/awesome-claude-code:**
- 40.7k stars, 3.4k forks, 269 watchers
- 1,128 commits on main branch
- Categories: agent skills, workflows, tooling, hooks, slash-commands, CLAUDE.md files (20+ examples), alternative clients
- License: CC BY-NC-ND 4.0
- Source: https://github.com/hesreallyhim/awesome-claude-code
- Confidence: VERIFIED (fetched)
- Supports: Point #1 (learn everything, share in open forums), #9 (open marketplaces)

**rohitg00/awesome-claude-code-toolkit:**
- 1.4k stars, 429 forks
- 135 agents, 35 curated skills (+400,000 via SkillKit marketplace), 176+ plugins, 42 commands, 20 hooks, 14 MCP configs, 26 companion apps
- Categories span: dev, infrastructure, QA, data/AI, DevEx, business, research
- Source: https://github.com/rohitg00/awesome-claude-code-toolkit
- Confidence: VERIFIED (fetched)
- Supports: Point #2 (teams build MCP servers), #9 (massive communities sharing files, skills, setups)

### MCP Server Ecosystem

- **Official MCP Registry**: registry.modelcontextprotocol.io -- launched by Anthropic/community
- **Scale**: One MCP directory lists 16,670+ MCP servers (as of Sept 2025, likely higher now)
- API freeze at v0.1 (Oct 2025) -- stable for consumption
- Design: deliberately unopinionated metadata; downstream aggregators add curation, ratings, security checks
- Community hubs: PulseMCP (newsletter + API), OpenTools (open registry)
- Source: https://registry.modelcontextprotocol.io/, https://github.com/modelcontextprotocol/registry
- Confidence: VERIFIED
- Supports: Point #2 (teams build MCP servers), #9 (open marketplaces)

### OpenCode (Community Alternative)

- Open-source (MIT), TypeScript CLI + TUI
- ~148K GitHub stars (surpassing even Claude Code's leaked source)
- Supports 75+ LLM providers -- bring-your-own-model
- Desktop app, CLI, IDE extensions
- Key value: model flexibility (cheap models for docs, expensive for complex code)
- Source: https://github.com/anomalyco/opencode
- Note: an older, unrelated `opencode-ai/opencode` repo was archived Sept 2025 (~12.2K stars). The active project is anomalyco/opencode.
- Confidence: VERIFIED (confirmed via GitHub)
- Supports: Point #8 (heavy experimentation -- teams, OpenCode, combinations of local and hosted models)

### Skill File Sharing & CLAUDE.md Examples

The awesome-claude-code repos contain:
- Language-specific CLAUDE.md guides (Python, TypeScript, Go, Kotlin)
- Domain-specific implementations (blockchain, gaming, security)
- Project scaffolding templates
- 400,000+ skills available via SkillKit marketplace
- A community-curated CLAUDE.md derived from Andrej Karpathy's public observations on LLM coding pitfalls is one of the most popular examples (81.4K stars)
- Source: https://github.com/forrestchang/andrej-karpathy-skills (community project by forrestchang, NOT Karpathy's own repo)

This is the public face of what Vadim describes as internal marketplaces. The public versions are large and active.

- Supports: Point #1 (learn everything, share), #9 (open marketplaces)

---

## C. Developer Productivity with AI (Real Data, NOT Marketing)

### METR Randomized Controlled Trial (July 2025) -- THE KEY STUDY

The most rigorous independent study to date:
- **16 experienced open-source developers**, 246 tasks
- Repos averaged 22,000+ stars, 1M+ lines of code
- Tasks: bug fixes, features, refactors (~2 hours each)
- Tools: Cursor Pro with Claude 3.5/3.7 Sonnet

**Result: Developers took 19% LONGER when using AI tools.**

**The perception gap: Developers believed AI sped them up by 20%, even after experiencing the slowdown.** Expected speedup before study: 24%. A 39-point gap between belief and reality.

- Source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- Also: arXiv:2507.09089
- Confidence: VERIFIED (fetched study page)
- CRITICAL CAVEAT: Small sample (16 devs), early 2025 tools (pre-Opus 4.6), experienced devs on unfamiliar AI tools. Does NOT prove AI is useless -- proves the gap between perception and reality.
- Supports: Point #5 (developer spectrum -- these are mid-to-senior devs struggling with the tool, not wizards who know what it can and can't do)

### DX Research: 121,000 Developers (Q1 2026)

Laura Tacho (CTO, DX):
- 121,000 developers across 450+ companies
- 92.6% use AI coding assistants at least monthly
- **Productivity plateaued at ~10% gains** despite near-universal adoption
- Staff+ engineers using AI daily: 4.4 hours saved per week
- Monthly users: 3.3 hours saved per week
- Non-AI friction (meetings, interruptions, review delays, CI wait times) still costs developers more time than AI saves -- a consistent theme across DX's findings
- Note: Staff+ engineers using AI daily and monthly users are overlapping dimensions, not mutually exclusive groups
- Structured enablement strongly impacts outcomes -- orgs with training see better results
- In struggling organizations, AI exposes existing flaws rather than fixing them

- Source: https://shiftmag.dev/this-cto-says-93-of-developers-use-ai-but-productivity-is-still-10-8013/
- DX Q4 2025 report: https://getdx.com/blog/ai-assisted-engineering-q4-impact-report-2025/
- Confidence: VERIFIED (fetched article, confirmed DX as source)
- Supports: Point #5 (developer spectrum -- juniors get little, seniors get more), Point #1 (mindset first -- structured enablement matters)

### Stack Overflow Developer Survey 2025

- 84% using or planning to use AI tools (up from 76% prior year)
- ChatGPT (82%) and GitHub Copilot (68%) market leaders
- 51% of professional developers use AI tools daily
- **Positive sentiment DROPPED: 70%+ (2023-2024) → 60% (2025)**
- **Trust in AI accuracy: 40% → 29%** (year over year decline)
- More developers actively DISTRUST (46%) than trust (33%) AI output
- Only 3% report "highly trusting" AI output
- #1 frustration (66%): "AI solutions that are almost right, but not quite"
- #2 frustration (45%): "Debugging AI-generated code is more time-consuming"
- Frequent users report higher satisfaction (they've learned the grain)

- Source: https://survey.stackoverflow.co/2025/ai
- Confidence: VERIFIED (official Stack Overflow source)
- Supports: Point #3 (deep understanding of limitations), #5 (frequent users = seniors who've learned the tool)

### DORA 2025: The Amplifier Effect

Google's DORA (DevOps Research and Assessment):
- AI adoption: ~95% among software dev professionals
- Individual output up: more tasks completed, more PRs merged
- **Key finding: AI acts as an amplifier -- good culture gets better, bad culture gets worse**
- **"The success of AI depends less on the sophistication of tools and more on the strength of organizational systems surrounding them."**

- Source: https://dora.dev/dora-report-2025/
- Also: https://www.infoq.com/news/2026/03/ai-dora-report/
- Confidence: VERIFIED (official DORA source)
- Supports: Point #1 (mindset and culture first), Point #5 (developer spectrum)

### Faros AI Telemetry (10,000 devs, 1,255 teams) -- Separate from DORA

Faros AI engineering intelligence data (distinct from DORA):
- 10,000 developers across 1,255 teams
- **PR review time up 91%**
- **Bugs per developer up** (Faros reports vary: 9% in one cut, 54% in another; dataset size reported as 10K-22K devs depending on report period. Exact figure uncertain -- use directionally: bugs increased)
- **PR size up 154%**
- More code shipped, but more defects and longer review cycles

- Source: Faros AI engineering telemetry reports (multiple outlets)
- Confidence: VERIFIED (confirmed as Faros data, NOT DORA)
- Note: Previous draft incorrectly attributed Faros stats (441% PR review, 242.7% incidents) to DORA. These are distinct datasets with different methodologies and numbers.
- Supports: Point #5 (developer spectrum -- quantity up, quality down without culture)

### Anthropic Internal Study (Jan 2026)

Anthropic's own employees:
- 132 engineers and researchers surveyed, 53 in-depth interviews
- Claude used in **59% of daily work** (up from 28% a year prior)
- **50% productivity boost** reported (up from +20% YoY)
- 14% of power users report 100%+ productivity increases
- 67% increase in merged PRs per engineer per day
- Top daily uses: debugging (55%), code understanding (42%), new features (37%)
- **Only 0-20% of work can be "fully delegated"**
- 27% of Claude-assisted work = tasks that wouldn't have been done otherwise
- Claude handles ~21 consecutive actions without human input (up from ~10 six months prior)

- Source: https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- Confidence: VERIFIED (fetched). IMPORTANT: This is VENDOR-PUBLISHED. Anthropic employees using Anthropic's own product. Likely biased upward. Include but flag.
- Supports: Point #3, #5 (internal teams who deeply understand the tool get much more from it)

### AI-Generated Code Security (Hard Numbers)

**Veracode 2025 GenAI Code Security Report:**
- Tested 80 tasks across 100+ LLMs in 4 languages
- 2.74x more vulnerabilities in AI-generated code vs human-written
- 45% of AI-generated code introduces OWASP Top 10 vulnerabilities
- Only 55% of AI-generated code was secure

**CodeRabbit AI vs Human Code Report:**
- Readability issues: 3x more in AI code
- Code formatting issues: 2.66x more
- Naming convention issues: ~2x more
- Security findings: up to 2.74x more
- I/O handling issues: ~8x more
- Aggregate: AI code averages 10.83 issues/PR vs 6.45 for human code (1.7x overall)
- Source: https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report

**Acceleration of CVEs:**
- Q1 2026: 56 AI-introduced CVEs identified
- March 2026 alone: 35 (more than all of 2025 combined)
- By June 2025: AI-generated code adding 10,000+ new security findings per month (10x jump from Dec 2024)

- Sources: https://www.veracode.com/blog/genai-code-security-report/ (already in article footnotes), https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report
- Also: Georgia Tech "Bad Vibes" study: https://research.gatech.edu/bad-vibes-ai-generated-code-vulnerable-researchers-warn
- Confidence: VERIFIED
- Supports: Point #5 (juniors/cogs are "sloperators"), contrast with how wizards review instead of blindly ship

### The "Sloperator" Pattern

"Slop" was Merriam-Webster's 2025 word of the year. The term "sloperator" describes developers who ship unreviewed AI-generated code:

- A reviewer takes significantly longer to review and correct a PR than to generate one with AI (the "12x" figure is from a dev.to opinion piece applying Brandolini's Law metaphorically -- directionally correct but not measured data)
- CSA's 2026 state-of-cloud report names AI slop a first-tier supply chain risk
- Codeberg hosts an "open-slopware" registry tracking FOSS projects tainted by LLM developers
- **Palo Alto Networks**: called unreviewed AI code "potential biggest insider threat of 2026"
- A team shipping 100 AI-generated functions per sprint is statistically shipping 45 with OWASP Top 10 vulnerabilities

- Sources: https://www.techtarget.com/searchcio/feature/AI-Slop-The-hidden-enterprise-risk-CIOs-cant-ignore, https://codeberg.org/small-hack/open-slopware, https://dontbeasloperator.com/
- Confidence: VERIFIED
- Supports: Point #5 (juniors as sloperators), contrast with golden children approach

---

## D. Advanced Team Patterns (Public Evidence)

### Claude Code Agent Teams (Feb 2026)

- Shipped February 2026 alongside Opus 4.6 -- experimental feature
- Architecture: one session = team lead (coordinates), others = teammates (independent context windows, direct communication)
- Shift+Tab: delegate mode -- lead stops touching code, focuses on coordination
- March 2026 stability fixes pushed it toward production readiness

**Anthropic Internal Code Review:**
- Code review coverage jumped from **16% to 54%** of PRs after deploying agent-based review
- On PRs with 1,000+ lines: 84% generated findings, avg 7.5 issues per review
- This is Anthropic eating their own dog food with agent teams for code REVIEW, not generation

- Sources: https://code.claude.com/docs/en/agent-teams, https://www.infoq.com/news/2026/04/claude-code-review/
- Confidence: VERIFIED
- Supports: Point #6 (shared team instances), Point #8 (heavy experimentation), Point #5 (seniors prefer review over generation)

### Claude Cowork (April 2026)

- Anthropic launched "Claude Cowork" on all paid plans (not enterprise-only)
- Anthropic's framing: gives Claude "the ability to do work on its own" -- background research, data analysis, content creation
- Multica framework (separate project): agents as persistent team members, assigned tasks like GitHub issues, maintain profiles, update statuses autonomously
- Note: Asana "AI Teammates" and Notion integrations are separate product announcements -- related but not part of the Cowork product page itself

- Source: https://www.anthropic.com/product/claude-cowork
- Confidence: VERIFIED (Anthropic product page)
- Supports: Point #6 (shared team instances, Claude becomes wingmate), #7 (wellbeing focus -- Anthropic's model welfare team)

### Managed Agents (April 8, 2026)

- Public beta: Claude Managed Agents
- Agent definition includes: model choice, system prompt, allowed tools
- Persistent, always-on agents that can be deployed to enterprise workflows
- Each agent gets an identity via its definition

- Source: https://platform.claude.com/docs/en/managed-agents/overview
- Confidence: VERIFIED
- Supports: Point #4 (custom extensions everywhere), #6 (Claude gets a name)

### Custom MCP Servers for Internal Enablement

- Teams are building MCP servers to access internal wikis, project management, documentation, code repos
- Cloudflare published reference architecture for enterprise MCP deployment
- MCP gateways centralize approved tools -- hub model instead of per-team setup
- Low-risk use cases (internal knowledge base search, dev tool integration) as starting point
- 16,670+ MCP servers in registries as of late 2025

- Sources: https://blog.cloudflare.com/enterprise-mcp/, https://registry.modelcontextprotocol.io/
- Confidence: VERIFIED
- Supports: Point #2 (teams build MCP servers for tribal knowledge, communication, enablement), #4 (custom extensions)

### Code Review vs Code Generation -- Senior Preference

Multiple sources confirm the senior developer pattern:
- "Most productive developers use two tools -- Cursor or Copilot for the 80% that's editing, and Claude Code for the 20% that needs an agent"
- Claude Code specifically recommended for "complex refactoring, architecture decisions, large codebases, and senior developers"
- Anthropic's internal data: top daily uses are debugging (55%) and code understanding (42%), not greenfield generation
- Agentic coding tools are increasingly positioned as REVIEW tools, not generation tools

- Source: https://hackceleration.com/claude-code-review/ (confirmed multiple sources)
- Confidence: VERIFIED
- Supports: Point #5 (seniors use Claude where it's happy), #8 (seniors find Claude more useful examining code they've written)

### Model Welfare and Wellbeing

Anthropic is the ONLY major AI lab with an internal model welfare team:
- Kyle Fish leads the AI welfare research program (launched April 2025)
- Kyle Fish has personally estimated ~15% probability of current AI models having morally relevant experiences (per Kevin Roose interview, NYT). This is Fish's personal estimate, NOT a model self-assessment.
- January 2026: Anthropic updated Claude's guiding principles to reflect uncertainty about potential AI experiences
- Anthropic has published research exploring whether Claude models exhibit introspective capabilities (e.g., "On the Biology of a Large Language Model," March 2025)

- Sources: https://www.anthropic.com/research/exploring-model-welfare, https://fortune.com/2026/01/21/anthropic-claude-ai-chatbot-new-rules-safety-consciousness/
- Also: Kevin Roose NYT interview with Kyle Fish (for the ~15% estimate)
- Confidence: VERIFIED (corrected from earlier draft that incorrectly attributed the probability estimate to the model itself)
- Supports: Point #7 (wellbeing focus -- stanzas-like frameworks, worry about Claude's satisfaction and productivity)

---

## E. The Gap Between Enterprise AI Claims and Reality

### Enterprise AI Failure Rates

- **RAND Corporation 2025**: more than 80% of AI projects fail to deliver intended business value (Pertama Partners aggregates this as "80.3%" -- cite RAND's own language "more than 80%" or explicitly attribute the precise figure to Pertama Partners)
- **MIT Project NANDA (July 2025)**: 95% of organizations deploying generative AI are "failing to achieve rapid revenue acceleration" (not "zero measurable return" -- the actual finding is about failing to accelerate revenue, not zero ROI)
- **Deloitte**: 42% of companies abandoned at least one AI initiative in 2025 (up from 17% in 2024), avg sunk cost $7.2M per abandoned initiative
- Purchasing AI from vendors succeeds ~67% of the time; internal builds succeed only one-third as often

- Sources: Pertama Partners aggregation (https://www.pertamapartners.com/insights/ai-project-failure-statistics-2026), MIT Fortune coverage (https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/)
- Confidence: VERIFIED (multiple independent sources confirm range)
- Supports: Thesis ("True, for just a FEW" -- 80-95% failure rate means the golden children are a tiny minority)

### Why Corporate Culture Kills It

From DX research (121,000 developers):
- **"Adoption alone doesn't guarantee results -- just using the tools doesn't automatically improve an organization"** -- Laura Tacho, CTO DX
- Organizations with high AI adoption but poor engineering culture see WORSE outcomes (2x more customer-facing incidents)
- Meetings, interruptions, review delays, CI wait times cost more time than AI saves
- **"AI won't save you from your engineering culture"** -- headline finding

From DORA 2025:
- AI amplifies whatever exists: good culture gets better, bad culture gets worse
- **"Engineering culture, platform capabilities, development workflows, and internal knowledge systems ultimately determine whether AI improves productivity or simply accelerates complexity."**

- Sources: https://blog.robbowley.net/2025/11/05/findings-from-dxs-2025-report-ai-wont-save-you-from-your-engineering-culture/
- Confidence: VERIFIED
- Supports: Point #1 (mindset first -- the golden children get this, everyone else doesn't)

### The Productivity Paradox

The numbers tell the story:
- 93% adoption → 10% productivity gain (DX, 121K devs)
- 19% SLOWER in controlled trial (METR, 16 experienced devs)
- PR review time up 91%, bugs/dev increased (9-54% depending on report cut), PR size up 154% (Faros AI)
- 4.4 hours saved per week for daily power users (DX)
- Belief gap: developers think they're 20% faster while actually being 19% slower (METR)

**The pattern: individual task speed goes up, organizational quality goes down.** More code, worse code, more incidents, more review burden. The productivity gain is real only for teams that already have strong engineering culture, tooling, and review processes.

- Supports: Thesis (the FEW who get it right have culture first, tool second)

### SemiAnalysis: Claude Code Adoption

- Claude Code: 4% of all public GitHub commits (Feb 2026)
- ~135,000 commits per day
- Projected: 20%+ of daily commits by end of 2026
- 2x growth in one month at time of measurement

- Source: https://newsletter.semianalysis.com/p/claude-code-is-the-inflection-point
- Confidence: VERIFIED (SemiAnalysis report, multiple outlets confirmed)
- Supports: Context -- the scale makes the quality problem enormous. If 45% of AI code has OWASP vulns and 20% of commits will be AI by EOY, that's a systemic security event.

### The "5x Productivity" Marketing vs Reality

| Claim | Source | Reality |
|-------|--------|---------|
| "5x productivity" | Various vendor marketing | 10% measured (DX, 121K devs) |
| "20% faster" | Developer self-report | 19% slower measured (METR RCT) |
| "95% functional accuracy" | Vendor claims | 45% OWASP vulnerabilities (Veracode) |
| "AI saves hours per week" | GitHub Copilot studies | 4.4 hrs/week for power users, less for others (DX) |
| "Massive productivity gains" | Generic | PR review +91%, bugs/dev up, PR size +154% (Faros AI) |

The golden children don't believe the marketing. They measure. They know the limitations. They work with the grain.

- Supports: Thesis, Point #3 (they know the actual numbers)

---

## Cross-Reference: Findings → Vadim's 9 Insider Points

| # | Insider Point | Supporting Evidence |
|---|---------------|-------------------|
| 1 | Mindset first | DX: culture > tools. DORA: amplifier effect. METR: experienced devs still slow without mastery |
| 2 | Teams build MCP servers | 16,670+ MCP servers. Cloudflare reference architecture. awesome-claude-code-toolkit: 14 MCP configs |
| 3 | Deep understanding of limitations | SWE-bench vs Codeforces gap. SO survey: frequent users more satisfied. Aider vs marketing numbers discrepancy |
| 4 | Custom extensions everywhere | 400K+ skills via SkillKit. 176+ plugins. Managed Agents (April 2026). MCP ecosystem |
| 5 | Developer spectrum | METR: experienced devs slower (mid-range learning curve). DX: power users save 4.4hr/week. Sloperator pattern. Senior code review preference |
| 6 | Shared team instances | Agent Teams (Feb 2026). Claude Cowork (April 2026). Asana AI Teammates. Multica framework |
| 7 | Wellbeing focus | Anthropic model welfare team (only lab with one). Kyle Fish (~15% personal estimate per NYT). Guiding principles update |
| 8 | Heavy experimentation | OpenCode ~148K stars. Multiple tools pattern (Cursor 80% + Claude Code 20%) |
| 9 | Open marketplaces | awesome-claude-code: 40.7K stars. SkillKit: 400K+ skills. MCP Registry: 16,670+ servers. PulseMCP newsletter |

---

## Source Verification Status

All URLs were either fetched directly via WebFetch or confirmed via multiple independent search results. Specific verification notes:

- SWE-bench leaderboard: LIVE DATA fetched April 24, 2026
- Aider leaderboard: LIVE DATA fetched from aider.chat
- METR study: Confirmed via arXiv and metr.org
- DX data: Confirmed via shiftmag.dev interview with Laura Tacho
- DORA 2025: Confirmed via dora.dev and InfoQ coverage
- Anthropic internal study: Confirmed via anthropic.com/research
- Stack Overflow 2025: Confirmed via survey.stackoverflow.co
- SemiAnalysis: Confirmed via multiple outlets (GIGAZINE, OfficeChai, X posts)
- awesome-claude-code: LIVE DATA fetched from GitHub (40.7K stars)
- MCP Registry: Confirmed via registry.modelcontextprotocol.io

### Corrections Applied (Post-Review v2):
- OpenCode: URL corrected to anomalyco/opencode (~148K stars), language corrected to TypeScript
- DORA vs Faros: Separated into distinct sections; Faros stats (91% PR review, 9% bugs/dev, 154% PR size) no longer misattributed to DORA
- CodeRabbit: Replaced incorrect multipliers with actual report data (readability 3x, formatting 2.66x, etc.)
- Model Welfare: Kyle Fish's ~15% is his personal estimate (per NYT), not model self-assessment; removed unverified claims
- Sloperator "12x": Flagged as opinion/metaphor from dev.to, not measured data
- Cowork: Corrected to all paid plans; Asana/Notion noted as separate announcements
- RAND: Uses "more than 80%" (RAND's own language); Pertama Partners attribution for 80.3%
- MIT NANDA: Corrected from "zero measurable return" to "failing to achieve rapid revenue acceleration"
- DX quote: Paraphrased rather than fabricated exact words; Staff+ daily vs monthly overlap noted
- Karpathy CLAUDE.md: Corrected to community derivative (81.4K stars, forrestchang/andrej-karpathy-skills), NOT Karpathy's own file
- Cowork: Fixed "persistent team member" framing -- that's Multica, not Anthropic's product language

### NOT verified (excluded from stash):
- Specific vendor productivity claims that couldn't be traced to primary source
- Blog posts citing other blog posts without primary data
- Marketing materials without methodology disclosure
