# De-LLMing old posts

Small task. ~3 minutes per article. Light, surgical — not academic.

## Team

- **@hacker** — analyzes
- **@truthy** — validates @hacker's findings, returns any issues
- **@main** — coordinator, receives progress updates, runs final human review

Method: adversarial. Every @hacker ↔ @truthy interaction is also reported to @main.
When no disagreements remain, @truthy tells @main the article is ready for human review.

Disagreement cap: 3 per item (first article — to be tuned). After the 3rd, the dissenter escalates to @main for resolution.

## Execution

- Vadim names the article to @main. @main assigns it to the agents and conducts the work.
- One article at a time.
- Stop and standby at each **Stop** marker below.

## Working document

Path: `inbox/llm-tortured-language-detection_<post-file-name>.md`.

Both Step 1 and Step 2 outputs go here. First person needing it creates it.

Concurrent editing:

- Reread the document before each edit.
- Never edit the same section as the other agent. The workflow keeps you separated — you finish a paragraph and notify; the other validates.
- Each of you may keep a personal notes section in the doc.

---

## Step 1 — Article-level analysis

Read the whole article (argument extraction needs the full thing).

1. Identify key points — one line each.
2. Write a concise summary, including the formal argument form. Reference: `site/rdd13r-style-guide.yml`.
3. Evaluate validity and strength of the argument.
4. Rate the article critically. Baseline: average Medium tech blogger.

**Stop.** Wait for keep/remove decision from Vadim.

---

## Step 2 — LLM-tortured language detection

Only if the article stays.

Reference: `~/.claude/memories/15-LLMTorturedLanguage.md` (the 12 patterns).

### First pass — find and confirm

One paragraph at a time. @hacker writes findings into the working document, then notifies @truthy to validate.
Move to the next paragraph only when both agree (or the disagreement cap is reached).

### Second pass — replacements

After the entire article is processed:

1. Keep the article body and the author's style in mind.
2. Adversarially produce the top 3 replacement suggestions for each confirmed tortured sentence/phrase.
3. Add the top 3 to the working document.

**Stop.** @truthy notifies @main for final human review.
