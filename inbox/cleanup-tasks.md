# Infantilization Article — Cleanup Tasks

Line numbers refer to `site/_posts/2026-07-30-infantilization.adoc` as of 2026-07-30.
Execute after the draft is complete.

## Structural

- [x] **Move or anchor the definition of "Corporate Infantilization" (L87).**
  DONE 2026-07-31: definition moved up, compressed, after the three-analogy paragraph;
  the Fixing section now calls back with "the infantilizing parent-child dynamic."
  The term is the title and is used for ~50 lines before being defined. The definition also
  reads like a pasted dictionary/AI passage with no attribution — either rewrite it in the
  author's voice or attribute the source. Options: define early (right after the opening
  analogies), or keep late placement deliberately but attribute.

- [ ] **Reconsider section order: "Fixing Accountability Problems" precedes the evidence.**
  Current flow is problem → fix → evidence (diagrams). Diagnosis-then-cure is stronger:
  problem → the two diagrams → what they expose → how to fix it. Right now the reader gets
  the medicine before seeing the X-ray. If the order stays, add a bridging sentence so the
  fix section doesn't read as premature.

- [ ] **Fix the dangling antecedent "the said unicorn above" (L124).**
  The only prior unicorn is generic ("practically at every rising unicorn," L108). "Said"
  points to a specific one never introduced. Either introduce a concrete unicorn earlier or
  change to "a unicorn like that."

- [ ] **Write the missing back half: Diagram B's mirror explanation + maturity contrast.**
  The article currently ends at Diagram B with no prose after it. B needs its own
  "What is TOLD" paragraph (the infantile mirror of A's), then the maturity-contrast
  section, leading to the interview-questions payoff — the root thesis of the article.

## Logical

- [x] **Resolve the intermediate-service contradiction (L60 vs Diagram A).**
  RESOLVED 2026-07-31: the "missing behavior owner" paragraph after Diagram B's story
  (Strangler Fig, minimalistic domain) supplies the distinction.
  L60 says the problem is "easily fixed by an intermediate service -- that service doesn't
  remedy the root cause," yet Diagram A's competent answer *is* services (ACL, aggregate
  service). The unstated distinction: a bolted-on band-aid service vs. an owned aggregate
  that models the actor and the intended effect. Spell it out — a hostile reader will quote
  L60 against the diagram.

- [ ] **Guard the happy-5-y-o irony (L104).**
  The article condemns treating employees as children, then advises "talk as if you were a
  happy 5-y-o." The difference — chosen playfulness among peers vs. imposed parent-child
  dynamic — is real but never stated. One sentence closes the hole.

- [ ] **Ground or soften the unicorn universal (L108).**
  "Practically at every rising unicorn one finds a core team that behaves exactly this way"
  is a universal claim with no example or source. Either name one or scope it to lived
  observation ("every core team I've seen up close").

## Argument Form

- [ ] **Name the common mechanism behind the opening analogy chain (L40–46).**
  Dictatorship → single-earner marriage → workplace asserts a pattern without stating what
  unites the three. The mechanism — someone else absorbs your agency until you stop
  exercising it — is implied but never written. One sentence turns three anecdotes into an
  argument.

## The Architecture Story Explanation (L135–144)

- [ ] **Restructure the "What is TOLD" block.**
  The root thesis — *value comes from changing the state of the user* — and the punchline —
  *"The Aggregate decides HOW MUCH to show and that is all it will send!"* — are buried in
  one 9-line italic block with six em-dashes. Break into 2–3 short paragraphs; let the
  punchline close. The UX/UI split (UX owned by the aggregate; UI judged purely on fidelity
  of presentation) deserves its own sentence — it's the novel framing.
  Also: drop "clear as day" (filler); fix spurious commas in "faithfully, and accurately,".

## LinkedIn Hook Alignment

- [ ] **Make the TWO questions explicit in the text.**
  Candidate pair already in the article: L36 "How DID you make those disciplined teams?" and
  L51 "You get too much data in your React single page application. How to load it?" If the
  LI hook promises TWO interview questions, the article must visibly present both as such.
  Also reconcile with L119 "ONE architecture quirk" — one quirk, two questions; both lines
  should tell the same arithmetic.

- [ ] **Tighten the hook phrasing.**
  "How do you know the entire company IT maturity from TWO interview questions?" →
  "How do you read an entire company's IT maturity from TWO interview questions?"
  ("read" echoes "Architecture Tells All.")

## New Sections (added 2026-07-31)

- [ ] **Unify the question arithmetic across the article and the LI hook.**
  L119 says "ONE architecture quirk," L179 says "a single interview questions," the LI hook
  promises TWO interview questions. Pick the number and make all three agree; L179 also has
  the singular/plural mangle either way.

- [ ] **Rebuild the garbled Owl callback (L168).**
  "Is it something that paginates and reduces stuffing of the React Owl mad? NO!" — doesn't
  parse. The Owl callback is worth keeping; the sentence needs rebuilding.

- [ ] **L169:** "And If I were" — stray capital "If."

- [ ] **Heading grammar (L177):** "Interview: Is a TWO way Street!" — either
  "An Interview Is a Two-Way Street!" or keep stylization deliberately.

- [ ] **L197:** "Thinking back at these team" → "teams."

- [ ] **Seal the "it happened!" hole in the closing.**
  L188's interviewer insists the breach happened; the article never gives the mature team's
  answer to that. One clause: the mature team repairs the values breach — it doesn't build
  coping machinery for the occurrence. Without it, option one reads as refusing the
  hypothetical, which is exactly what the naive answerer did.

## Mechanical

- [ ] **L21 (owl caption attribute):** "If you React Read Model" → "If your"; "Qwl" → "Owl";
  untangle the double negative "can't hoot as this Owl can't."
- [ ] **L41:** "In political science references are about dictatorships" — broken; add the
  missing article/verb ("references are to dictatorships" or rewrite).
- [ ] **L45:** "lose connection with one other" → "with one another."
- [ ] **L56:** "the scenario all always wrong from architectural domain" — broken; rewrite
  ("the scenario is always wrong from the architectural domain").
- [ ] **L66:** "quiet common" → "quite common."
- [ ] **L98:** "preceptions-based-judging" → "perceptions-based judging."
- [ ] **L100:** "tensons" → "tensions."

## Verified Non-Issues

- `{hacker-culture}` attribute — defined in `site/_config.yml:185`; renders correctly.
