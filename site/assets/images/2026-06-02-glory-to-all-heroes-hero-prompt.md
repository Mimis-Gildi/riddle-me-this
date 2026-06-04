# Hero image — working prompt

Source: `2026-06-02-glory-to-all-heroes-hero.png`
Model: ChatGPT (GPT-4o image), generated 2026-06-03 ~03:03 AM
Second pass (first pass had American flag too small / obscured)

## Prompt as run

> A wide cinematic horizontal photograph for a memorial blog header. A weathered dark
> granite slab fills the lower two-thirds of the frame, viewed from a low oblique angle
> so the stone recedes into shallow depth of field. Late golden-hour light rakes across
> the surface from the right — warm, soft, reverent. Faint moss in the crevices.
>
> Arranged on the stone in the lower-left third: a small evergreen pine wreath bound with
> a black silk ribbon and a single sprig of red viburnum berries. Beside the wreath, three
> flags of approximately equal visible size laid side by side with care, none obscuring
> the others:
>
> 1. Foreground center: a ceremonial American flag in the regulation triangular fold,
>    large and prominently visible, the blue star field uppermost and fully readable,
>    the red and white stripes clearly visible along the folded edges.
> 2. To its left: a folded Ukrainian flag, blue-over-yellow horizontal bands visible at
>    the fold.
> 3. To its right: a UPA flag — deep crimson red on top, matte black below — laid open
>    flat behind the other two, framing them without covering them. The brass
>    lion-and-trident challenge coin rests on the UPA flag's red half.
>
> No people, no faces, no inscriptions on the stone, no text anywhere. The upper-right
> third of the frame is dark negative space — soft out-of-focus stone wall and a hint of
> evergreen — leaving room for title text overlay.
>
> Style: photorealistic with a subtle painterly grade, cinematic color, low contrast,
> quiet reverent mood. Fine grain. Soft vignette. No glare, no high-key highlights.
> Aspect ratio 16:6, wide letterbox crop.

## Decisions encoded

- **Ravens patch deliberately omitted.** Doxes both 10th SFG and Ukrainian intel. Bad
  idea. The post honors them through prose only.
- **Azov via Lion of Galicia, not Wolfsangel.** DALL-E content filters refuse Wolfsangel
  and Black Sun. The Lion of Galicia is the Azov Special Operations Detachment crest,
  reads clearly as Azov to anyone who knows, registers as "regimental coin" to anyone who
  doesn't. Honors without billboarding — fits Ravens-adjacent OPSEC instinct.
- **UPA flag colors front-and-center.** Vadim: "all patches they use are in UPA colors."
- **American flag foreground.** First pass buried it under the UPA flag. For a Memorial
  Day-anchored "Glory to ALL Our Heroes" piece by an American, that ordering fought the
  title.

## Knobs for regeneration

- DALL-E sometimes flips the UPA flag (black on top). If it does, force: *"deep crimson
  red rectangle on top, equal-size matte black rectangle on bottom, horizontal split,
  the red is the upper half, nothing else on the flag."*
- If it hallucinates a fourth flag or text on the stone, add: *"exactly three folded
  flags, no others, no writing on the stone, no banner, no inscription."*
- For a larger American flag: change "approximately equal visible size" to "the American
  flag larger than the others."
