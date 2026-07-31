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

- [x] **Reconsider section order: "Fixing Accountability Problems" precedes the evidence.**
  DONE 2026-07-31: Fixing section moved after the Interview section's spouse dialogue;
  bridge sentence "So what does one do about it?" added; closing 11-teams paragraph is
  now the Fixing section's coda.
  Current flow is problem → fix → evidence (diagrams). Diagnosis-then-cure is stronger:
  problem → the two diagrams → what they expose → how to fix it. Right now the reader gets
  the medicine before seeing the X-ray. If the order stays, add a bridging sentence so the
  fix section doesn't read as premature.

- [x] **Fix the dangling antecedent "the said unicorn above" (L124).**
  DONE 2026-07-31: changed to "a rising unicorn tells itself" — required by the reorder,
  since the old referent moved below the reference.
  The only prior unicorn is generic ("practically at every rising unicorn," L108). "Said"
  points to a specific one never introduced. Either introduce a concrete unicorn earlier or
  change to "a unicorn like that."

- [x] **Write the missing back half: Diagram B's mirror explanation + maturity contrast.**
  DONE 2026-07-31: Infantile mirror story, side-by-side contrast, perspective paragraph,
  and the "reading you their architecture diagram out loud" hinge are all in.
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

- [x] **Guard the happy-5-y-o irony (L104).**
  DONE 2026-07-31: conduct rule #1 expanded (plain words, proof of mastery) plus a full
  guard paragraph (imposed smallness in grand words vs. chosen plainness from competence,
  tail-recursion test, business experts need no translation).
  - [x] Typo in new text L217/218: "of intelligence" — DONE 2026-07-31.

- [ ] **Ground or soften the unicorn universal (L108).**
  "Practically at every rising unicorn one finds a core team that behaves exactly this way"
  is a universal claim with no example or source. Either name one or scope it to lived
  observation ("every core team I've seen up close").

## Argument Form

- [x] **Name the common mechanism behind the opening analogy chain (L40–46).**
  DONE 2026-07-31: "The mechanism is the same in all three: someone else absorbs your
  agency, quietly, until you stop exercising it -- and then nobody remembers whose it was."

## The Architecture Story Explanation (L135–144)

- [x] **Restructure the "What is TOLD" block.**
  DONE 2026-07-31 by Vadim, by decoration: breath-break after the header, punchlines
  broken out and bolded in both blocks. "Clear as day" remains — his call, kept.
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

- [x] **Unify the question arithmetic across the article and the LI hook.**
  DECIDED 2026-07-31: ONE interview question (the React one; the spouse dialogue is its
  translation). "TWO way Street" = interviewer sizes candidate, candidate sizes company.
  Article already agrees (L88 ONE quirk, L171 single question, heading two-way).
  - [x] LI hook + post drafted 2026-07-31: "What does a candidate learn about your
    company from ONE interview question?" — full draft in
    inbox/linkedin-corporate-infantilization.adoc, pending Vadim's rewrite + article URL.
  - [ ] Optional: one clause in the Interview section naming the interviewer's lane
    (they think they're sizing you; the question hands you their org chart).

- [x] **Rebuild the garbled Owl callback (L168).**
  DONE 2026-07-31: "paginates and stops stuffing the React Owl mad" — minimal rebuild;
  Vadim may still rephrase.

- [x] **L169:** "And If I were" — DONE 2026-07-31.

- [x] **Heading grammar (L177):** DONE 2026-07-31 by Vadim: "Interview: Is a TWO-way
  Street! What does the candidate read?" — hyphenated and subtitled.

- [x] **L197:** "Thinking back at these team" → "teams." DONE 2026-07-31.

- [x] **Seal the "it happened!" hole in the closing.**
  DONE 2026-07-31: "when the impossible does happen once -- they don't build coping
  machinery for it. They repair the value that let it in." Closes the article.

## Mechanical — ALL DONE 2026-07-31 (single sweep)

- [x] **L141:** "none of the people patterns"; "An engineer … under their belt."
- [x] **L151:** "When a healthy-culture engineer hears."
- [x] **L21:** "If your React Read Model"; "Qwl" → "Owl" (Vadim), comma untangles the negative.
- [x] **L41:** "In political science, the references are to dictatorships."
- [x] **L45:** "the couple lose connection with one another," (+ comma after "doesn't work").
- [x] **L56/62:** "the scenario is always wrong from the architectural domain."
- [x] **L66:** "quiet" removed by Vadim ("Yes, common indeed").
- [x] **L98:** "perceptions-based judging."
- [x] **L100:** "tensions."
- [x] **L171:** "a single interview question" (grammar only — the ONE/TWO arithmetic
  decision remains open above).

## Verified Non-Issues

- `{hacker-culture}` attribute — defined in `site/_config.yml:185`; renders correctly.
