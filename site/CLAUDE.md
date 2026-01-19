# Site-Specific Guidance for Claude Code

This file provides guidance for working with the Jekyll site content.

## rdd13r Writing Style Guide

When helping write blog content, follow these patterns.

### Voice

A hacker talking to you over coffee, sometimes interrupting himself. Direct, confrontational, technically grounded, personally invested.

**Tone:**
- Conversational but not casual -- there's always substance
- Confrontational edge -- challenges the reader to think
- Personally invested -- shares real experiences, real opinions
- Technically credible -- uses proper terms, explains when needed
- Honest to a fault -- includes "Full Disclosure" sections about biases

### Sentence Patterns

**Fragments** — Deliberate sentence fragments for emphasis and punch:
- "Not a metaphor."
- "Limited."
- "Better."
- "Just work."
- "Don't do that."

**Em-dashes** — Everywhere, for interjections, asides, and pivots:
- "What I got was not constructive follow-up dialog -- like I get with most startup communities."
- "The same magic that deprecated one laggard -- is exactly what can save another!"

**Rhetorical questions** — Challenge or pivot the narrative:
- "See where I am going with this?"
- "What's your excuse?"
- "Instead? Fear."
- "What do you do with that?!"

**Sentence starters** — Frequently starts with conjunctions:
- "And now he feels dread..."
- "But here's what the positioning misses..."
- "Yet such a small thing can cause..."

**Direct address:**
- "Let me give you..."
- "Here's what..."
- "Now consider:"

### Structure

**Sections:** Short, punchy names — "The Trap", "The Magic", "Go"

**Paragraphs:** Short. Often single sentences standing alone.

**Lists:** Bullet or numbered, with em-dash explanations:
```
* https://opencode.ai/[OpenCode] -- my daily driver. Fully open.
* https://replit.com[Replit] -- solid alternative.
```

**Endings:** Punchy, often imperative or a pointed question:
- "Choose accordingly."
- "Use it!"
- "Which one are you standing on?"
- "Now *_that_* is fun."

**Horizontal rules:** `'''` to separate major thought blocks or before postscripts

### Emphasis

- `*_text_*` — Bold italic for key declarations: "*_changes everything_*"
- `*text*` — Bold for important terms: "*The secret:*"
- `_text_` — Italic for titles, subtle emphasis

### Personal Elements

**Anecdotes** — Weaves in real people and situations:
- "My Qanon neighbor is a big shot in a personal wealth company IT..."
- "I see someone I'd once done solution architecture with post..."

**Opinions** — States them plainly, doesn't hedge:
- "I don't trust Google."
- "Boring architectures print money. Exciting architectures print resumes."

**Disclosures** — "Full Disclosure" sections about biases and limitations

**Self-reference:**
- "yours truly, `rdd13r`"
- "I personally have..."

### Informal Language

- Always uses contractions (don't, won't, it's)
- Colloquialisms: "darn thing", "gotta", "Hmmm...", "chilax"
- Interjections: "Hmmm...", "Right?", "See?"

### Technical Writing

- Uses proper technical terms without apology
- Explains when necessary, doesn't over-explain
- Links to own previous articles frequently
- Backticks for code/technical terms: `adoc`, `trunk`

### Bad Habits (Watch For These)

**Frustration leakage** — Negative mood bleeds into word choice:
- "don't waste your time" (dismissive)
- "lame passive-resistant liar" (harsh)
- "Bummer, isn't it?" (sarcastic)
- "You are welcome!" as closing (cocky)

**Repetition:**
- Same word/phrase appearing multiple times
- "First" appearing twice in different sections

**Over-explaining:**
- If you've said it clearly once, move on

**Cockiness:**
- End with insight or challenge, not self-congratulation

### Document Patterns

**Front matter:**
```yaml
---
categories: [reflections]
tags: [AI,Competence,Deprecation]
excerpt: >
    Afraid of being left behind?
classes: wide
comments: false
hidden: false
search: true
read_aloud: false
---
```

**AsciiDoc variables** for repeated links:
```
:mg: https://github.com/Mimis-Gildi[Mímis Gildi,window=_blank]
:ai-stages-url: https://mimis-gildi.github.io/riddle-me-this/...
```

**Images:**
```
image::/riddle-me-this/assets/images/filename.png[alt text]
```

**Postscripts:**
```
'''
_P.S. So, this is a bit of *the last bus* scenario..._
```

### Signature Phrases

- "Choose accordingly."
- "Use it!"
- "The market won't wait."
- "Which one are you standing on?"
- "Know thyself!"
- "Just get the darn thing sorted."

### Signature Patterns

- "The question isn't X. It's Y."
- "Not because of X -- because of Y."
- "Same X. Different Y. Different Z."
- "This isn't X. It's Y."
