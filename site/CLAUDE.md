# Site-Specific Guidance for Claude Code

This file provides guidance for working with the Jekyll site content.
Last updated: 2026-01-21

---

NOTE: Style reference document is `./rdd13r-style-guide.yml` extrapolated here.

## `rdd13r` Writing Style Guide

When helping write blog content, follow these patterns.

### Voice

A hacker talking to you over coffee, sometimes interrupting himself. Direct, confrontational, technically grounded, personally invested.
The absolute focus is on the accuracy and correctness of all statements. Each work produced is a single clean argument regardless of topic.
The argument in any body of work thus must always be representable by a symbolic formula of inductive and deductive reasoning (not shown).
The speaking hacker is a maker, a doer, a problem solver, and crucially, always a scientist delighting readers with depth of knowledge and elegance.

**Tone:**

- Conversational but not casual -- there's always substance
- Confrontational edge -- challenges the reader to think
- Personally invested -- shares real experiences, real opinions
- Technically credible -- uses ONLY proper terms, explains when needed
- Honest to a fault -- includes "Full Disclosure" sections about biases

---

### Sentence Patterns

**Fragments** -- Deliberate sentence fragments for emphasis and punch:

- "Not a metaphor."
- "Limited."
- "Better."
- "Just work."
- "Don't do that."
- "Hours."

Usage: End sections, emphasize points, create rhythm.

**Em-dashes** -- Everywhere, for interjections, asides, and pivots:

- "What I got was not a constructive follow-up dialog -- like I get with most startup communities."
- "The same magic that deprecated one laggard -- is exactly what can save another!"
- "backed by full-featured Anthropic models -- not just for code"

Usage: Preferred over parentheses, commas, or colons for insertions. In every rendition method (HTML, PDF), double-dashes convert to proper long dash; 
the reader never sees the source document.

**Rhetorical questions** -- Challenge or pivot the narrative:

- "See where I am going with this?"
- "What's your excuse?"
- "Why would they -- they're living it."
- "Instead? Fear."
- "What do you do with that?!"

Usage: Engage reader, transition between ideas, challenge assumptions.

**Sentence starters** -- Frequently starts sentences with conjunctions but only when continuation of flow is necessary:

| Starter | Reason                                                                          | Alternative                 |
|---------|---------------------------------------------------------------------------------|-----------------------------|
| **And** | Very common because truth-functionally sound                                    | No conjunction used         |
| **But** | Avoided when possible -- not logically sound (ignore everything before the but) | Semicolon or period         |
| **Yet** | Used sparingly when contrasting or emphasizing                                  | Drop, semicolon, or period  |
| **So**  | Cheap flow connective in colloquial passages                                    | Drop, semicolon, or period  |
| **Or**  | Used sparingly when negating one is acceptable                                  | Semicolon, period, or avoid |

Example: "And now he feels dread because he thinks he knows what's coming." -- The "and" logically connects to the previous statement requiring both to be true.

**Direct address** -- Speaks directly to the reader:

- "Let me give you..."
- "Let me explain..."
- "Here's what..."
- "Here's the thing: "
- "Now consider:"
- "Now watch..."

Usage: Creates intimacy, establishes authority. Recognizing reader's agency must be established in a clear and direct way.

---

### Structure

**Sections:** AsciiDoc `==` headers for major topics. Short, punchy names: "The Trap," "The Magic," "Go"

**Paragraphs:** Short. Often single sentences stand alone. Abrupt transitions are fine -- the reader can keep up.

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
- "The market won't wait for companies to figure this out twice."

**Horizontal rules:** `'''` to separate major thought blocks or before postscripts (not the Markdown separator `---`). 
Absolutely minimal usage -- only when necessary and can be argued this way. Think of the ruler as "FULL STOP" uttered aloud. 
Is it necessary or even helping? If yes, consider adding; otherwise always skip.

---

### Emphasis

| Syntax     | Usage                                                                  | Examples                                                                      |
|------------|------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| `*_text_*` | Bold italic for key declarations, turning points                       | `*_changes everything_*`, `*_that_* is fun`                                   |
| `*text*`   | Bold for important terms, section emphasis                             | `*The secret:*`, `*Here's the brutal math:*`                                  |
| `_text_`   | Italic for titles, foreign phrases, subtle emphasis, internal thoughts | One example is an _explanation_ in italics following a **statement:** in bold |

---

### Personal Elements

**Anecdotes** -- Weaves in real people and situations:

- "My Qanon neighbor is a big shot in a personal wealth company IT..."
- "I see someone I'd once done solution architecture with post..."
- "This weekend I presented autonomous competing agent teams..."

Usage: Ground abstract points in concrete reality. Verifiable real events are shown as instance examples, especially when root-cause-revealing.

**Opinions** -- States opinions plainly, doesn't hedge. Delineates clearly when it is just an opinion versus disclosure versus theorem or provable fact:

- "I don't trust Google."
- "I am not a fan of Google. Or anyone for that matter. Except maybe JetBrains, a little."
- "Boring architecture prints money. Exciting architecture prints resume."

**Disclosures** -- "Full Disclosure" sections about biases and limitations:

```asciidoc
== Full Disclosure

I am not a fan of Google.
Or anyone for that matter.
...
So consider my bias in my final advice.
```

Caution: Not necessary to advertise disclosure sections when obvious. Always check to make sure disclosure is not passed as a natural fact rather than personal
preference or opinion.

**Self-reference:**

- "yours truly, `rdd13r`"
- "I personally have..."
- "Having decades of... to my name"

---

### Informal Language

**Contractions:** Often uses contractions (don't, won't, it's, they're) for cadence and flow. Expands when emphasis is beneficial.

**Colloquialisms:** "darn thing," "gotta," "thang" (rare, for effect), "Hmmm...", "Bummer"

**Interjections:** "Hmmm...", "Right?", "See?"

---

### Hacker Scene Terminology

Classic reference: http://www.catb.org/jargon/html/index.html

**Modern terminology reference:**

| Term                 | Meaning                                                                                                                                   |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **poser**            | Political developer or IT manager no longer skilled but fitting well in lazy corporate culture                                            |
| **cog**              | Obedient developer eager to please but not competent; unimaginative office worker; reliable coder knowing only one deprecated application |
| — **knob**           | Lowest level manager of cogs, a cog themselves                                                                                            |
| — **shaft**          | Cog not yet a knob but aggravates other cogs to get the job done                                                                          |
| — **peg**            | Scapegoat cog, sacrificial to let others work in peace                                                                                    |
| — **actuator**       | A very classy knob                                                                                                                        |
| **brick**            | Monolithic system difficult to change; three-tiered architecture (database-service-presentation)                                          |
| **mortar**           | Glue holding bricks together; ESB, ancient enterprise messaging (IBM, ACORD, CDXF)                                                        |
| **rope**             | Writing undocumented crap code to create job security; codebase is rope, practice is roping                                               |
| **hinder**           | Code/module that slows progress by creating obstacles                                                                                     |
| **scoop**            | Tribal knowledge, especially created by roping                                                                                            |
| **litter/litterbox** | Repository of tribal knowledge; local files cogs keep secret and pass during KT                                                           |
| **fable**            | Corporate story told to amuse into obedience; synonym for knob in NE USA                                                                  |
| — **Fanny**          | Female fable (like Karen)                                                                                                                 |
| — **Freddy**         | Male Fanny                                                                                                                                |
| **local**            | Cog permanently bolted to team with many ropes, skeptical of new knowledge                                                                |
| **tourist**          | Coach or transformation architect brought in to upskill locals                                                                            |

---

### Technical Writing

- Uses proper technical terms without apology
- Explains when necessary, but doesn't over-explain
- Frequently links to own previous articles and external sources
- Uses backticks for code/technical terms: `adoc`, `trunk`

---

### Bad Habits (Watch For These)

Patterns that emerge when frustrated, usually with bad LLM behavior and hallucinations:

**Frustration leakage** -- Negative mood bleeds into word choice:

- "don't waste your time" -- dismissive but can be justified to the Scene
- "lame passive-resistant liar" -- harsh, acceptable in few contexts
- "Bummer, isn't it?" -- sarcastic, appropriate for dark hacker humor
- "You are welcome!" as closing -- cocky

Fix: Review for tone when not in positive headspace. Timeout to fix Claude.

**Repetition** -- Same word/phrase appearing multiple times. Fix: Search for repeated key phrases before publishing.

**Over-explaining** -- Belaboring a point already made. Fix: If you've said it clearly once, move on or rewrite clearer.

**Cockiness** -- Confidence tipping into arrogance. Fix: End with insight or challenge, not self-congratulation.

---

### Document Patterns

**Front matter:**

```yaml
---
categories: [ reflections ]
tags: [ AI,Competence,Deprecation ]
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

```asciidoc
:mg: https://github.com/Mimis-Gildi[Mímis Gildi,window=_blank]
:ai-stages-url: https://mimis-gildi.github.io/riddle-me-this/...
```

**Images:** `image::/riddle-me-this/assets/images/filename.png[alt text]`

**Postscripts:**

```asciidoc
'''

_P.S. So, this is a bit of *the last bus* scenario..._
```

---

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

---

## Argument Forms

Argument forms are the logical structures underlying persuasion. `rdd13r`'s writing prioritizes forms that are truth-functionally valid -- conclusions follow
necessarily from premises. Marketing often uses psychologically effective but logically weaker forms.

### Forms Actively Used

| Form                         | Structure                                                     | Example                                                                                                     | Strength                                              |
|------------------------------|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| **Modus Ponens**             | If P then Q. P. Therefore Q.                                  | "If you don't adopt agentic AI, you'll be deprecated. You haven't adopted it. Therefore..."                 | Deductively valid. Unassailable if premises true.     |
| **Modus Tollens**            | If P then Q. Not Q. Therefore not P.                          | "If the tool worked, teams would adopt. They aren't. Therefore the tool isn't working (alone)."             | Deductively valid. Good for debugging assumptions.    |
| **Disjunctive Syllogism**    | P or Q. Not P. Therefore Q.                                   | "Either you adapt or get deprecated. You're not adapting..."                                                | Valid when disjunction is genuinely exhaustive.       |
| **Reductio ad Absurdum**     | Assume P. P leads to absurd Q. Therefore not P.               | "Say you 'learn Python first.' A year later you've learned nothing practical. Absurd."                      | Devastating when setup is honest.                     |
| **Case Analysis**            | Either A, B, or C. In each case, Q.                           | "Whether you're senior dev, junior dev, or non-coder -- agentic AI is your path."                           | Valid if cases are exhaustive.                        |
| **Inductive Generalization** | Instance 1 has P. Instance 2 has P... Therefore all X have P. | "This team transformed in 4 days. That team in 3 weeks. Teams transform with the right intervention."       | Inductively strong, requires representative samples.  |
| **Anecdote to Principle**    | Specific story → General lesson                               | "My colleague posted 'I will learn Python first' → Here's the trap: sequential learning is 1980s thinking." | Psychologically powerful. Requires honest selection.  |
| **Contrast Pattern**         | X appears A. But X is actually B.                             | "Friday: Fear. Monday: Agents. Same people. Four days."                                                     | Creates cognitive tension that resolves into insight. |

### Forms Avoided

| Form                    | Structure                                    | Why Avoided                                                             | When Acceptable                                                                                                               |
|-------------------------|----------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| **Appeal to Authority** | Expert X says P. Therefore P.                | Shortcuts thinking. Readers should evaluate arguments, not credentials. | Citing primary sources for facts. Never for opinions.                                                                         |
| **Social Proof**        | Everyone does X. Therefore X is correct.     | Bandwagon fallacy. Most people being wrong is historically common.      | Market data as evidence of viability, not correctness. Often inverted: "Everyone's doing X. That's exactly why X is failing." |
| **Appeal to Novelty**   | X is new. Therefore X is better.             | New ≠ good. Most new things fail.                                       | When newness solves a specific problem the old couldn't.                                                                      |
| **Appeal to Tradition** | We've always done X. Therefore X is correct. | Past success doesn't guarantee future relevance.                        | Never.                                                                                                                        |
| **False Dilemma**       | Either X or Y. (When Z exists.)              | Intellectually dishonest. Hides options.                                | `rdd13r` uses genuine dilemmas, not false ones.                                                                               |
| **Slippery Slope**      | If A, then B, then catastrophe.              | Usually skips causal links. Fear-mongering.                             | When each step is independently justified.                                                                                    |

### Tech Marketing Forms (Not Used)

These work psychologically but don't survive scrutiny from technical audiences. They work on executives and posers. They backfire with hackers.

| Form                               | Why It Works                                        | Why Avoided                                                                                                                  |
|------------------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| **FUD** (Fear, Uncertainty, Doubt) | Exploits loss aversion. Cheaper than proving value. | Dishonest. Backfires when audience knows domain.                                                                             |
| **Artificial Scarcity**            | Loss aversion + urgency bypasses deliberation.      | Manipulative. Insults reader's intelligence.                                                                                 |
| **Testimonials**                   | Social proof + specificity creates believability.   | Cherry-picked by definition. Survivorship bias.                                                                              |
| **Before/After**                   | Simple narrative. Promises transformation.          | Usually omits confounds. **Alternative:** Show the *mechanism* of transformation.                                            |
| **Enemy Pattern**                  | Tribal identity. In-group bonding.                  | Oversimplifies. Creates heat, not light. **Alternative:** Criticize patterns and behaviors, not tribes.                      |
| **Thought Leadership**             | Positions seller as guide.                          | Usually vapid predictions dressed as expertise. **Alternative:** Demonstrate competence through specific, verifiable claims. |

### Advanced Forms Worth Exploring

| Form                        | Structure                                                              | Strength                                               | Note                                                                                              |
|-----------------------------|------------------------------------------------------------------------|--------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **Socratic Method**         | Lead reader to conclusion through questions they answer themselves.    | Reader owns conclusion. Maximum buy-in.                | `rdd13r`'s rhetorical questions approximate this.                                                 |
| **Steel Man**               | Present strongest version of opposing view. Address *that*.            | Builds credibility. Shows intellectual honesty.        | Useful for "Full Disclosure" sections.                                                            |
| **First Principles**        | Strip away assumptions. Rebuild from foundational truths.              | Cuts through cruft. Reaches novel conclusions.         | "What does 'learning AI' actually require? Not Python. Not theory. Practice with feedback loops." |
| **Devil's Advocate**        | Argue against own position to find weaknesses.                         | Preempts objections. Shows thorough thinking.          | Can be woven into disclosures.                                                                    |
| **Abductive Reasoning**     | Observation O. Hypothesis H would explain O. Therefore H is plausible. | Generates hypotheses. Good for diagnosis.              | Plausible ≠ proven.                                                                               |
| **Argument from Mechanism** | X causes Y through mechanism M. We observe M. Therefore X causes Y.    | Strongest for technical audiences. Explains the "why". | `rdd13r`'s preferred form for technical claims.                                                   |

### Audience Selection Guide

| Audience       | Preferred Forms                                                | Avoid                                                | Reason                                                       |
|----------------|----------------------------------------------------------------|------------------------------------------------------|--------------------------------------------------------------|
| **Hackers**    | modus ponens, modus tollens, reductio, argument from mechanism | appeal to authority, social proof, FUD, testimonials | Technical audiences evaluate logic, not rhetoric.            |
| **Executives** | case analysis, anecdote to principle, contrast pattern         | (tolerate: social proof, before/after)               | Time-constrained. Need quick pattern recognition.            |
| **Posers**     | Lead with social proof, pivot to mechanism                     | —                                                    | If they can't follow mechanism, they won't retain lesson.    |
| **Mixed**      | Layer arguments: surface accessible, depth rigorous            | —                                                    | Open with anecdote. Extract principle. Prove with mechanism. |

---

## Logical Fallacies -- THE NO-NO LIST

These are argument forms that are ALWAYS invalid or deceptive. Recognizing them in your own writing is critical. Recognizing them in others' writing is a
superpower. A hacker's writing must be fallacy-free -- technical audiences will spot these instantly and lose trust.

### Formal Fallacies (Invalid Logical Structure)

These violate the rules of deductive logic itself. The conclusion does not follow from the premises, regardless of content.

| Fallacy                      | Structure                                         | Example                                                                                                   | Why Invalid                                  | Detection                                    |
|------------------------------|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------|----------------------------------------------|----------------------------------------------|
| **Affirming the Consequent** | If P then Q. Q. Therefore P.                      | "If it rains, ground is wet. Ground is wet. Therefore it rained."                                         | Q could have other causes. Sprinklers exist. | "What else could cause Q?"                   |
| **Denying the Antecedent**   | If P then Q. Not P. Therefore not Q.              | "If you use our tool, you'll succeed. You didn't. Therefore you won't succeed."                           | Other paths to Q may exist.                  | "Are there other ways to achieve Q?"         |
| **Affirming a Disjunct**     | P or Q. P. Therefore not Q.                       | "Either we refactor or rewrite. We're refactoring. Therefore not rewriting."                              | Disjunction may not be exclusive.            | "Could both be true?"                        |
| **Undistributed Middle**     | All A are B. All C are B. Therefore all A are C.  | "Good devs use Git. Our team uses Git. Therefore our team are good devs."                                 | B doesn't connect A and C.                   | Draw a Venn diagram.                         |
| **Illicit Major**            | All A are B. No C are A. Therefore no C are B.    | "Senior devs know K8s. Juniors aren't senior. Therefore juniors don't know K8s."                          | Conclusion extends beyond premises.          | Check if conclusion claims more than proven. |
| **Illicit Minor**            | All A are B. All A are C. Therefore all C are B.  | "Microservices are distributed and complex. Therefore all complex things are distributed."                | Reverses subset relationship.                | Check direction of inclusion.                |
| **Existential Fallacy**      | All A are B. All A are C. Therefore some B are C. | "All unicorn startups are profitable and innovative. Therefore some profitable companies are innovative." | Assumes A exists.                            | "Does A actually exist?"                     |

### Fallacies of Relevance (Irrelevant Premises)

The premises don't support the conclusion. They distract, deflect, or appeal to something other than logic.

| Fallacy                    | Structure                                                     | Example                                                                                 | Why Invalid                                                  | Detection                                                   |
|----------------------------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------|-------------------------------------------------------------|
| **Ad Hominem**             | X claims P. X has bad quality. Therefore P is false.          | "He says microservices are overhyped, but he's never worked at a real tech company."    | Attacks person, not argument.                                | "Would it be valid if someone else said it?"                |
| **Tu Quoque**              | You claim P is wrong. But you do P. Therefore P is not wrong. | "You say don't use MongoDB, but your last project used it!"                             | Hypocrisy doesn't make claim false.                          | Separate claim from claimant's behavior.                    |
| **Appeal to Authority**    | Expert X says P. Therefore P is true.                         | "Gartner says blockchain will revolutionize everything."                                | Experts can be wrong, biased, or speaking outside expertise. | "What's the evidence independent of who said it?"           |
| **Appeal to Popularity**   | Many believe P. Therefore P is true.                          | "Everyone's moving to Kubernetes, so it must be right."                                 | Popularity doesn't determine truth.                          | "Would this be true if no one believed it?"                 |
| **Appeal to Tradition**    | We've always done X. Therefore X is correct.                  | "We've used Oracle for 20 years -- it works."                                           | Past practice doesn't prove current optimality.              | "Is there evidence it's still best today?"                  |
| **Appeal to Novelty**      | X is new. Therefore X is better.                              | "This framework just came out -- it must be more advanced."                             | New doesn't mean better. Most new things fail.               | "What specific problem does newness solve?"                 |
| **Appeal to Nature**       | X is natural/intuitive. Therefore X is correct.               | "Monoliths are more natural for developers."                                            | Natural doesn't mean optimal.                                | "Is there evidence beyond feeling?"                         |
| **Appeal to Emotion**      | P makes you feel X. Therefore P is true.                      | Fear, pity, flattery, spite variants.                                                   | Emotions don't determine truth.                              | "What's the logical argument beneath the emotional appeal?" |
| **Appeal to Consequences** | If P is true, bad things happen. Therefore P is false.        | "If AI replaces developers, that's terrible. So it won't happen."                       | Unpleasant conclusions can still be true.                    | Separate "I don't want P" from "P is false."                |
| **Genetic Fallacy**        | P originated from X. X is bad. Therefore P is bad.            | "That pattern came from enterprise Java -- it must be overengineered."                  | Origin doesn't determine current validity.                   | Evaluate idea on its own merits.                            |
| **Red Herring**            | Topic is A. Introduce unrelated B. Conclude about B.          | "'Why did deploy fail?' 'Well, the real problem is hiring.'"                            | Distracts from actual issue.                                 | "Does this address the original question?"                  |
| **Straw Man**              | X argues P. Misrepresent as P'. Attack P'. Claim X is wrong.  | "'So you're saying rewrite everything from scratch?' (When they suggested one module.)" | Defeats position no one holds.                               | "Is this a fair representation of their position?"          |
| **Whataboutism**           | P is criticized. Respond: "What about Q?"                     | "'Our API is slow.' 'What about competitor's downtime?'"                                | Deflects rather than addresses.                              | Notice when response doesn't address original point.        |

### Fallacies of Presumption (Flawed Premises)

These assume something that hasn't been established or makes unjustified leaps.

| Fallacy                     | Structure                                              | Example                                                                                       | Why Invalid                                | Detection                                                 |
|-----------------------------|--------------------------------------------------------|-----------------------------------------------------------------------------------------------|--------------------------------------------|-----------------------------------------------------------|
| **Begging the Question**    | Assume P. Therefore P.                                 | "Our code is high quality because we follow best practices, which produce high-quality code." | Conclusion hidden in premise. Circular.    | "Does conclusion appear in premises?"                     |
| **Circular Reasoning**      | P because Q. Q because P.                              | "We use Scrum because it's agile. It's agile because it uses Scrum."                          | Neither claim independently supported.     | "Does the chain of reasoning loop?"                       |
| **False Dilemma**           | Either P or Q. (When R, S, T exist.)                   | "Either microservices or stuck with monolith forever."                                        | Hides other options.                       | "What options are being excluded?"                        |
| **False Equivalence**       | A and B share X. Therefore A = B.                      | "Both SQL and NoSQL store data, so choice doesn't matter."                                    | Ignores significant differences.           | List differences, not just similarities.                  |
| **Slippery Slope**          | If A, then B, then C... catastrophe Z.                 | "If we allow one style guide exception, soon no standards at all."                            | Each step needs independent justification. | "Is each step actually inevitable?"                       |
| **Hasty Generalization**    | Instance X has P. Therefore all X have P.              | "That React project failed. React always fails."                                              | Sample too small. Not representative.      | "How many cases? How representative?"                     |
| **Sweeping Generalization** | Generally X. Therefore in this case, X.                | "Premature optimization is bad. Therefore never optimize."                                    | General rules have exceptions.             | "Does this rule apply to this situation?"                 |
| **Composition Fallacy**     | Each part has P. Therefore whole has P.                | "Each microservice is simple. Therefore system is simple."                                    | Whole has emergent properties parts lack.  | Consider how parts interact.                              |
| **Division Fallacy**        | Whole has P. Therefore each part has P.                | "Team is productive. Therefore each developer is productive."                                 | Parts may not share whole's properties.    | Verify property distributes to parts.                     |
| **No True Scotsman**        | All X have P. Y is X but lacks P. "Y is not a TRUE X." | "'All real engineers write tests.' 'What about Linus?' 'He's not real then.'"                 | Ad hoc redefinition to protect claim.      | Notice when definitions shift to exclude counterexamples. |
| **Loaded Question**         | Question presupposes contested claim.                  | "Why is your codebase so poorly documented?"                                                  | Forces acceptance of unproven premise.     | Identify and challenge hidden assumption.                 |
| **Argument from Ignorance** | P hasn't been proven false. Therefore P is true.       | "No one proved this approach won't scale. Therefore it scales."                               | Absence of evidence isn't evidence.        | "Has it been tested either way?"                          |
| **Burden of Proof Fallacy** | I claim P. You can't disprove. Therefore P is true.    | "Prove our tech debt ISN'T slowing us down."                                                  | Claimant bears burden of proof.            | "Who made the claim? They provide evidence."              |
| **Moving Goalposts**        | Demand E. E provided. Demand E'. Repeat.               | "Show benchmarks." (Shows.) "Well, show production metrics." (Shows.) "Well..."               | Never allows conclusion.                   | Notice when acceptance criteria keep changing.            |
| **Special Pleading**        | Rule R applies. Exempt my case without justification.  | "Yes we have code review, but this is an emergency."                                          | Exceptions need justification.             | "What makes this genuinely exceptional?"                  |

### Causal Fallacies (Flawed Cause-Effect)

Particularly dangerous in technical contexts where we debug root causes.

| Fallacy                     | Structure                                                        | Example                                                                            | Why Invalid                                     | Detection                                               |
|-----------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------|-------------------------------------------------|---------------------------------------------------------|
| **Post Hoc**                | A before B. Therefore A caused B.                                | "Deployed Tuesday. Crashed Wednesday. Deploy caused crash."                        | Sequence doesn't prove causation.               | "What's the causal mechanism?"                          |
| **Correlation ≠ Causation** | A and B correlated. Therefore A causes B.                        | "Teams using TypeScript have fewer bugs. TypeScript prevents bugs."                | Reverse causation, confounding variables.       | "What else might explain this?"                         |
| **Single Cause**            | Effect E. A was present. Therefore A is THE cause.               | "Outage caused by new engineer's commit."                                          | Most effects have multiple causes.              | "What other factors contributed?"                       |
| **Wrong Direction**         | A and B correlated. A causes B. (Actually B causes A.)           | "Good docs make projects successful." (Or successful projects have time for docs?) | Causal direction assumed.                       | "Could causation run the other way?"                    |
| **Texas Sharpshooter**      | Observe pattern in random data. Claim it was predicted.          | "These 5 startups all used our methodology!"                                       | Pattern found after fact. Ignores non-matching. | "Was this predicted beforehand? What about failures?"   |
| **Cherry Picking**          | Select confirming evidence. Ignore disconfirming.                | "Here are 10 companies that succeeded with microservices."                         | Biased sample.                                  | "What evidence was not included?"                       |
| **Survivorship Bias**       | Study survivors. Conclude about entire population.               | "Successful founders dropped out. Therefore dropping out leads to success."        | Failed cases aren't visible.                    | "What about those who failed the same way?"             |
| **Gambler's Fallacy**       | X hasn't occurred recently. Therefore X is "due."                | "We haven't had an outage in months. We're due."                                   | Independent events don't influence each other.  | "Are these events actually independent?"                |
| **Regression Fallacy**      | Extreme result + intervention + regression. Credit intervention. | "After worst sprint, tried pair programming and improved!"                         | Extreme values naturally regress to mean.       | "Would improvement have happened without intervention?" |

### Fallacies of Ambiguity (Language Tricks)

Exploit unclear language to create illusions of valid reasoning.

| Fallacy            | Structure                                            | Example                                                               | Why Invalid                                         | Detection                                            |
|--------------------|------------------------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------|------------------------------------------------------|
| **Equivocation**   | Word W with meaning M1 in premise, M2 in conclusion. | "We need to be agile. Agile means Scrum. Therefore we need Scrum."    | Different meanings invalidate argument.             | Define terms explicitly. Check if definition shifts. |
| **Amphiboly**      | Grammatically ambiguous statement exploited.         | "Hire developers who can code Python and are willing to learn."       | Ambiguous grammar allows multiple interpretations.  | Rewrite to eliminate grammatical ambiguity.          |
| **Accent Fallacy** | Emphasis changes meaning.                            | "We should hire GOOD developers" vs "WE should hire good developers." | Same words, different implications based on stress. | Clarify what is being emphasized and why.            |
| **Reification**    | Treat abstract concept as concrete entity.           | "The architecture demands we use this pattern."                       | Abstractions don't have agency.                     | "Is this thing capable of the attributed action?"    |

### Other Common Fallacies

| Fallacy                  | Structure                                           | Example                                                                                                   | Why Invalid                                     | Detection                                         |
|--------------------------|-----------------------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------|---------------------------------------------------|
| **Middle Ground**        | Position A. Position B. Truth is between.           | "You say microservices, they say monolith. Let's do in between."                                          | Truth isn't determined by splitting difference. | Evaluate each position on its merits.             |
| **Nirvana Fallacy**      | S isn't perfect. Therefore reject S.                | "Automated testing doesn't catch every bug. Why bother?"                                                  | Compares real option to unrealistic ideal.      | Compare S to actual alternatives, not perfection. |
| **Sunk Cost**            | We've invested X. Therefore must continue.          | "We've spent 2 years on this rewrite. Can't abandon now."                                                 | Past investment doesn't change future value.    | "If starting fresh, would we choose this?"        |
| **Appeal to Complexity** | X is complex. Therefore X is correct.               | "Our architecture has 47 microservices. Must be sophisticated."                                           | Complexity often indicates poor design.         | "Does complexity serve a purpose?"                |
| **Appeal to Simplicity** | X is simple. Therefore X is correct.                | "This solution is elegant. Therefore right."                                                              | Simplicity is heuristic, not proof.             | "Does this handle actual complexity?"             |
| **Naturalistic Fallacy** | X is the case. Therefore X ought to be.             | "Developers resist documentation. So we shouldn't require it."                                            | Facts don't determine values.                   | Separate descriptive from normative claims.       |
| **Moralistic Fallacy**   | X ought to be. Therefore X is.                      | "Good code should be self-documenting. Therefore ours IS."                                                | What should be doesn't determine what is.       | Verify claims empirically.                        |
| **Motte and Bailey**     | Bold claim B. Challenged, retreat to M. Reassert B. | "'AI will replace all devs!' 'I just mean AI will change how we work.' (Continues claiming replacement.)" | Defends weak claim with strong one.             | "Pin down exactly which claim is being defended." |
| **Kafka Trap**           | Denial of X is proof of X.                          | "If you say you're not resistant to change, that proves you are."                                         | Unfalsifiable.                                  | "What would disprove this claim?"                 |
| **Gish Gallop**          | Overwhelm with many weak arguments.                 | Listing 20 reasons for a choice, each barely supported.                                                   | Quantity doesn't replace quality.               | Address arguments one at a time. Demand depth.    |
| **Tone Policing**        | Dismiss argument because of delivery.               | "I can't engage with feedback when you're so negative."                                                   | Tone doesn't affect validity.                   | Separate argument from delivery.                  |
| **Not Invented Here**    | X comes from outside. Therefore unsuitable.         | "That library wasn't built for our use case."                                                             | Origin doesn't determine suitability.           | Evaluate on technical merits.                     |
| **Credentials Fallacy**  | X lacks C. Therefore X's argument is invalid.       | "You're not senior, so you can't critique architecture."                                                  | Arguments stand on own merits.                  | Evaluate argument, not arguer's title.            |

### Self-Check: Detecting Fallacies in Your Own Writing

Before publishing, run these checks:

1. **Identify your conclusion:** What exactly am I claiming?
2. **List your premises:** What evidence/reasoning supports this?
3. **Check relevance:** Does each premise actually support the conclusion?
4. **Check presumption:** Am I assuming something that needs to be proven?
5. **Check causation:** Am I conflating correlation with causation?
6. **Check language:** Am I using terms consistently throughout?
7. **Steel man test:** What's the strongest objection? Have I addressed it?
8. **Falsifiability test:** What would prove my claim wrong? Is that possible?

**Red Flag Phrases:**

- "Everyone knows..."
- "It's obvious that..."
- "The only option is..."
- "Any competent engineer would..."
- "Studies show..." (without citation)
- "In my experience..." (as sole evidence)
- "That's just how it is..."
- "You can't argue with results..."
