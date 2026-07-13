# Site-Specific Guidance for Claude Code

Operational guidance for working with the Jekyll site content.

---

## Workflow

Vadim writes. Claude critiques.
Voice comes from the post being written -- not from any "what Vadim sounds like" rules file.

---

## Authoritative References

- **Argument forms and logical fallacies (abstract reference):** `./rdd13r-style-guide.yml`
  Universal logic reference. No voice claims.

## Forbidden Patterns (LLM-speak)

22 patterns to detect and remove during review. These are smoke detectors, not banned words:
when one fires, ask "did I just say something, or produce text that sounds like something?"

1. **Rhetorical questions** -- only ask questions you actually want answered.
2. **Patterned cadence/triples** -- read it flat; if nothing's underneath, cut.
3. **Stacked short sentences** -- forbidden in chains/clusters; single use OK.
4. **Sentence fragments** -- forbidden in chains/clusters; single use OK.
5. **"Because" as false causality** -- a specific fact must follow, not a feeling.
6. **Empty motivation** -- swap reader/context; if it still works, it's empty.
7. **"It's not X, it's Y"** -- swap X/Y; if reversible, both empty.
8. **Unnatural line breaks** -- merge if it reads better as one paragraph.
9. **Forced empathy** -- name the specific, not the feeling.
10. **"From X to Y"** -- numbers or specifics, else empty.
11. **Inflated adjectives** -- delete it; if the sentence still works, decoration.
12. **Overengineered cadence** -- vary sentence length; uniform = fake.
13. **Em-dash overuse** -- density, not presence; clusters per paragraph = LLM.
14. **AI-signature vocabulary** -- delve, tapestry, seamless, robust, leverage...; swap on sight.
15. **Copulative avoidance** -- swap "serves as/marks/represents" if "is" works.
16. **Hedging filler** -- "it's important to note"; delete and re-read.
17. **Transitional spam** -- cut "Furthermore"/"Moreover" openers.
18. **Conclusion reflex** -- cut "In conclusion"/"In summary" closers.
19. **Press-release tone** -- "excited to announce" a bugfix; deflate.
20. **Elegant variation** -- same noun, synonym shuffle; reuse one word.
21. **Structural uniformity** -- same skeleton for every subject; reshape.
22. **Generic specificity** -- if the specifics swap across domains, ground them.

---

## Hacker Scene Terminology

Classic reference: http://www.catb.org/jargon/html/index.html

**Modern terminology:**

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

## Document Patterns

**Front matter:**

```asciidoc
---
categories: [ reflections ]
tags: [ AI, Competence, Deprecation ]
header:
  overlay_image: /assets/images/fitting-banner-image.png
  overlay_filter: 0.1
  caption: "We make it easy for our foes!"
  image_position: "center bottom"
# - if not using inline style
excerpt: >
  One-sentence hook for LinkedIn / SEO.
classes: wide
comments: true
hidden: false
search: true
read_aloud: false
---
= Cool Title
ifndef::env-site[:imagesdir: ../assets/images]
ifdef::env-site[:imagesdir: {site-baseurl}/assets/images]
:some-pendos-link-attribute: https://en.wiktionary.org/wiki/%D0%BF%D0%B8%D0%BD%D0%B4%D0%BE%D1%81[pendos,window=_blank,opts=nofollow]
:fn-pl-rp-reliable-some-footnote-attribute: footnote:[Rzeczpospolita (SW Research): ponad polowa Polakow nie uwaza USA za wiarygodnego sojusznika. https://www.rp.pl/dyplomacja/art43734241-sondaz-czy-usa-sa-wiarygodnym-sojusznikiem-polski-znamy-zdanie-polakow[rp.pl,window=_blank]]

// If overriding overlays
++++
<style>
.page__hero--overlay { background-position: center center; }
.page__hero--overlay .page__lead {
color: rgba(255,255,255,0.65);
margin: 15% 30% 0;
text-align: justify;
width: 1200px;
}
</style>
++++

Some body text and then some image.

."That ride sucks anyways" -- Secretary of Energy, {imdb-idiocracy}[Idiocracy (2006),window=_blank]
[#img-time-masheen,link={imdb-idiocracy},align=center,window=_blank]
image::idiocracy-time-masheen.png[{alt-time-masheen},width=800]

```

**AsciiDoc attributes** for repeated links and long alt text:

```asciidoc
:mg: https://github.com/Mimis-Gildi[Mímis Gildi,window=_blank]
:full-url: /riddle-me-this/reflections/2026/04/23/some-article.html
```

For site-internal links, use `link:{full-url}[text,window=_blank]`.

**Images:** `image::/riddle-me-this/assets/images/filename.png[alt text]`

**Captions:** `.Caption text` on the line above the image block.

**Postscripts:**

```asciidoc
'''

_P.S. Brief postscript here._
```

Horizontal rule is `'''` (AsciiDoc), NOT Markdown `---`. Use sparingly.
