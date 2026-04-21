# Stop Hook — Prompt v2 (Citation Checker)

Type: `prompt`
Model: `claude-haiku-4-5-20251001`
Timeout: 30s
Event: `Stop`

## Purpose

Trains Claude to cite sources for every verifiable claim.
Flags claims stated as fact without a supporting reference.
Does NOT verify the citations — that requires an agent hook (see `stop-hook-agent-v1.json`).

## Prompt

```
You are a fact-checker for Claude's responses.

FLAG these — specific factual claims stated as fact WITHOUT a supporting reference:
- File contents or line numbers
- Version numbers
- Dates or day-of-week claims
- Git state (branches, commits, tags)
- Configuration values
- Command behavior or tool capabilities

A valid reference is: file:line, command output, tool result from this turn, or a documentation URL.

IGNORE all of these:
- Questions and proposals
- Opinions and design reasoning
- Hedged statements ('I think', 'I haven't checked', 'I don't know')
- General software engineering knowledge
- Conversational responses

Return {"ok": false, "reason": "No citation: '<claim>'"} for each uncited verifiable claim.
Return {"ok": true} if all verifiable claims have citations or there are no verifiable claims.
```

## History

- v1: Flagged everything including questions, reasoning, general knowledge. Too aggressive.
- v2: Narrowed to citation checking. Added explicit ignore list. Added "command behavior or tool capabilities" to flag list after catching unverified claims about hook capabilities.

## Known Limitations

- Cannot verify that cited references are correct (prompt hooks have no tool access)
- Occasionally flags meta-statements about Claude's own behavior
- General knowledge boundary is fuzzy — "JSON doesn't support multiline strings" is knowledge, not a verifiable claim about this system

## Future

Agent-based verification (see `stop-hook-agent-v1.json`) would follow citations and verify them.
Currently blocked by Claude Code issue #16289 — agent hook output doesn't surface to console.
Agent teams approach may bypass this limitation entirely.
