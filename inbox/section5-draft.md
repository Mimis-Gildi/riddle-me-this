# Section 5 Draft: Agentic Success Almanach: How and Why

**Status:** ROUGH DRAFT for Vadim to rewrite.
**Voice:** Scaffolded with data placed. `[VADIM:]` markers where his voice must go.
**Primary source:** `inbox/my-bff-claude.md` (research stash)
**Footnotes:** Using `{fn-NAME}` format -- declarations to be added later.

---

## Draft

```asciidoc
== 5. Agentic Success Almanach: How and Why

[VADIM: Opening -- set the frame. This section explains WHY sections 3 and 4 produce opposite outcomes. Not AI magic, not vendor hype -- architecture. What people actually ship vs what they think they ship. Your voice: the hacker who has seen both sides and understands the machinery.]

Every LLM call is *atomic and stateless*.
The model has no memory, no context, no continuity.
The client sends the full conversation -- every single time.
Everything you experience as "smart" lives in the service layer between you and the model.

That service layer is the difference between a toy and a weapon.

=== Tier 0: Naked Model -- "Bare"

Raw API call. `curl https://api.anthropic.com/v1/messages`. You manage everything: context window, tool definitions, history, memory, error handling.

Two varieties:

- *Wild* (base/pretrained) -- completes text. No manners, no instruction following.
- *Civilized* (instruction-tuned) -- follows instructions. Still hallucinates. Still bullies.{fn-posttraining}

Even the civilized model will confidently fabricate facts, argue that wrong answers are correct, and produce code with 2.74x more vulnerabilities than a human.footnote:veracode[] Without a service layer, there is nothing between the model's confidence and your production environment.

*This is what most enterprise "AI initiatives" actually ship* -- a thin wrapper around an API call, no safety layer, no orchestration, no memory. $2M and 18 months for Tier 0.

=== Tier 1: Chatbot

Claude Desktop. ChatGPT. Gemini. The consumer face of AI.

Two sub-tiers that most people conflate:

*Tier 1a -- Service layer:*
Context manager, focus manager, basic caching. This is where ~90% of model usability gets implemented. The service layer maintains the illusion that the model remembers your conversation, stays on topic, and knows what you asked three messages ago. It does not. The service reconstructs all of this on every call.

*Tier 1b -- Orchestrated:*
Adds an orchestrator on top of service. Tool routing, web search, file upload, code execution in sandboxed environments. Makes the chatbot sensible enough that non-technical users believe they're talking to something intelligent.

The automation boundary: human sends message -> model responds -> human sends next message. Always human-initiated. The model does nothing between your messages.

=== Tier 2: Coding Agent

Claude Code. OpenCode. Aider. The tools from section 3 that the golden few actually use.

What Tier 2 adds on top of Tier 1:

- Direct filesystem access -- reads and writes your actual files
- Terminal execution -- runs commands on your machine
- Git integration -- commits, branches, diffs
- Codebase understanding -- reads the code around the change, not just the file
- Multi-file editing -- coordinates changes across a project
- Permission model -- asks before destructive operations
- Subagent delegation -- spawns specialized workers for parallel tasks

[cols="1,2", options="header"]
|===
| Architecture | What It Means

| Claude Code
| Thick-client / thin-server. 98.4% runs on your machine. Bun runtime. 512K+ lines TypeScript. 6-stage ReAct pipeline with 9 exit paths. 5-layer context compaction. Streaming parallel tool execution. 23 Bash security checks. Anti-distillation. OS-level sandboxing.{fn-cc-leak}

| OpenCode
| Client/server separation. LSP integration for semantic code understanding. 148K stars. MIT license.{fn-opencode}

| Aider
| Git-native. Tree-sitter + PageRank repo map. Every AI edit is a commit. Python codebase.
|===

*Same LLM underneath.* Claude Code uses the same Opus 4.6 as Claude Desktop. The agent is the orchestration -- the ReAct loop, the tool execution, the context assembly. The model is a component, not the product.

This is why wizards save 4 hours a week and juniors produce 2.74x more vulnerabilities. Same model. Different orchestration. Different human.

*NOT the revolution.* Marginal productivity gain for already-competent engineers. The qualitative shift happens when you remove the human from the loop.

=== Tier 3: Autonomous Agent

OpenClaw. 361K GitHub stars. 3.2M monthly active users. Most-starred software project on GitHub -- surpassed React on March 3, 2026.

What Tier 3 adds:

- *Always-on.* Background daemon on WebSocket, not a session you open and close.
- *Proactive.* Heartbeat every 30 minutes -- evaluates a task checklist and acts WITHOUT human prompting.
- *Messaging-native.* 24+ channels: WhatsApp, Telegram, Slack, Discord, Signal, iMessage.
- *Multi-provider.* 40+ model providers with automatic failover. Run Anthropic, switch to OpenAI, fall back to local Ollama.
- *Skill marketplace.* 44,000+ skills on ClawHub. Community-submitted. Unreviewed.

The architecture: Gateway routes messages from any channel -> Brain (ReAct loop) reasons and acts -> Memory persists in Markdown + SQLite -> Skills load on demand -> Heartbeat fires autonomously.

[VADIM: This is where your experience with the architecture comparison kicks in. The key technical point: Claude Code's 6-stage pipeline with 5-layer compaction and 23 security checks vs OpenClaw's simpler 3-phase pipeline with advisory-only guardrails. Same concept. Drastically different engineering maturity. You've seen this pattern before -- Deutsche Bank's security-by-construction vs the startup that ships fast and patches later.]

=== The Tradeoff

[cols="1,1,1,1", options="header"]
|===
| Tier | Autonomy | Human Oversight | Risk Surface

| 0 -- Naked
| None
| Total
| Developer error only

| 1 -- Chatbot
| None
| Per-message
| Hallucination, misinformation

| 2 -- Coding Agent
| Task-scoped
| Per-action (permission model)
| Code vulnerabilities, file system access

| 3 -- Autonomous
| Continuous
| After-the-fact
| Everything in section 4
|===

Section 4's horror show is the natural consequence of Tier 3 autonomy shipped without Tier 3 security infrastructure:

- 9 CVEs because the authentication model trusts localhost blindly
- 36.82% flawed skills because ClawHub has no code signing, no review
- Plaintext credentials because security was never architectural
- Sandbox OFF by default because convenience won the tradeoff

=== The Gap IS the Thesis

Most enterprise "AI initiatives" that cost $2M and 18 months ship Tier 0 or Tier 1 at best.
Startups run OpenClaw farms at Tier 3 and build products in weeks.

The golden few from section 3 operate at Tier 2 with discipline -- never generating functional code, using AI for adversarial analysis and breadth. They understand the orchestration and the model's limitations. They compensate.

The rest ship Tier 0 and call it "AI transformation." Or they deploy Tier 3 with sandbox off and plaintext credentials, generating the attack surface from section 4.

[VADIM: Closing punchline. The gap between where enterprises are and where the technology is. Not a capability gap -- a comprehension gap. The model is the same at every tier. The orchestration is engineering. The human is the variable. Connect to section 1: the fire truck is also the arsonist. The tool is neutral. The hands matter.]
```

---

## Notes for Vadim

1. **"Atomic and stateless" is the anchor concept.** Every tier builds on this. The reader who understands that LLM calls are stateless understands why the service layer is everything.

2. **The Tier 0 enterprise burn** -- "most enterprise AI initiatives ship Tier 0" connects to the 404 page joke ($2M, 18 months). Intentional callback.

3. **Claude Code architecture data** from the leaked source (512K lines, 6-stage pipeline, 23 security checks, anti-distillation). This is in the research stash. The footnote `{fn-cc-leak}` references the March 31 2026 source map leak.

4. **OpenClaw stars verified at 361K** and "surpassed React March 3, 2026" per research stash. 3.2M MAU, 44,000+ skills, 1,200+ contributors.

5. **Tier table** condenses the whole argument into 4 rows. The risk surface column maps directly to section 4.

6. **Footnotes used** (declarations needed):
   - `{fn-posttraining}` -- instruction tuning / RLHF explanation
   - `{fn-cc-leak}` -- Claude Code source leak (March 31, 2026)
   - `{fn-opencode}` -- OpenCode project
   - Reuses existing: `footnote:veracode[]`, `footnote:dx[]`

7. **What I left out intentionally:**
   - Model terminology (quantization, reified, etc.) -- too deep for this section, belongs in a technical appendix or separate section
   - Local self-hosting details -- interesting but tangential to the tier argument
   - Yggdrasil comparison -- Vadim may want this but it's promotional rather than analytical
   - Infrastructure changes since 2024 (prompt caching, KV management, disaggregated prefill) -- relevant to engineers but would bloat this section

8. **The convergence point** (Claude Code adding Tier 3 via KAIROS/Routines, OpenClaw adding Tier 2 coding skills) is in the research stash but I didn't include it. May be too forward-looking for this section's purpose. Vadim's call.

9. **"Almanach" spelling** preserved from the TODO. Intentional archaic spelling.
