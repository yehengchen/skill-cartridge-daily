# Visual system: Skill cassette new release

## Core direction

Every issue should look like a new single released by the same independent label: tactile cassette culture, editorial clarity, and one playful feature-specific scene. It should not look like a generic AI poster or a software dashboard.

Base palette:

- ink black `#0D0D0D`;
- warm paper `#F3EBDD`;
- acid green `#B9FF4F`;
- one issue-specific accent only when it improves the metaphor.

Use a heavy Chinese display face for hooks and a monospaced face for small English metadata. Recommended recurring micro-labels include `NEW DROP`, `SIDE A`, `SIDE B`, `TRACK`, catalog number, runtime, and date. Treat these as packaging details, not the main message.

## Daily variation

The account should feel like one record label releasing different artists, not one template receiving new words. Before designing a new issue, inspect the previous three covers and write a short comparison in `image-prompts.md`. The new issue must differ from its immediate predecessor on at least three of these axes:

- image medium: editorial photo, tactile collage, clay/miniature set, risograph, ink, 3D product still life, paper sculpture, or another suitable treatment;
- dominant palette and material family;
- hero composition and camera angle;
- lighting and shadow language;
- feature metaphor or hero object;
- information rhythm across the inner pages.

Do not reuse the same cover grid, cassette angle, sticker placement, or hero crop in consecutive issues. Keep recognition through the label mark, catalog number, restrained micro-metadata, confident Chinese hooks, and the standard final release card. Everything else may follow the personality of the featured Skill.

## Turn function into a visual joke

Choose a real function and convert it into a tactile scene. Examples:

- a questioning Skill becomes a cassette that refuses to play until the listener answers;
- context cleanup becomes tangled tape wound neatly onto a pencil;
- parallel agents become a multi-track recorder with clearly separated tracks;
- token saving becomes a short mixtape with dead air physically cut out.

The visual should make the benefit guessable before the caption is read. Prefer objects, gestures, tension, transformation, and cause-and-effect. Avoid decorative robots, glowing brains, fake terminal/UI screenshots, floating app icons, neon blue-purple gradients, and meaningless circuitry.

## Image generation

When GPT-IMAGE-2 is configured, use at least two original, feature-specific assets in every recommendation issue. One should normally carry the cover; the other should make a function, transformation, or payoff visible on an inner page. Select both scenes from the Skill's behavior instead of repeating a generic cassette render, and make their editorial roles and compositions meaningfully different. Each generated image should make its part of the story guessable before any copy is read.

Generate artwork without any words, letters, UI, logos, or pseudo-text. Leave intentional negative space for HTML/CSS typography. Ask for tactile detail, believable shadows, a clear focal subject, and a 3:4 portrait composition. Vary materials beyond paper and black plastic when the topic supports it.

Record the final generation prompt, model, size, and saved asset path in `image-prompts.md`. If a live request fails, do not put the failure in public output; retry only under the configured throttle rule and keep the previous completed asset intact.

Before export, confirm both generated assets appear in the final numbered sequence. An unused file in `assets/` does not count toward the two-image requirement.

Never use generated lettering as final copy. Add all title, installation, prompts, and metadata with HTML/CSS.

## Layout and hierarchy

- Canvas: `1080 × 1440` pixels, 3:4.
- Keep main copy within a generous safe area; do not crowd the bottom UI zone.
- One dominant hook per page; aim for a readable first glance under one second.
- Use strong contrast, decisive scale changes, and short line lengths.
- Keep body copy sparse enough to read at `270 × 360`.
- Installation pages may be denser, but separate each platform visibly.
- Use real examples or clearly illustrative scenes; never place an error or unfinished-state card in the public sequence.

## Function clarity gate

Every recommendation issue must contain at least one page that makes the complete behavior visible as `真实输入 → Skill 动作 → 可见输出`. A reader should not need the caption to understand what changed.

Design this page in two reading layers:

- beginner layer: one large input, one plain-language action, and one visible result that can be understood in one second;
- technical layer: the actual prompt, output structure, useful parameter, export format, or operational boundary in smaller supporting copy.

Use authentic results whenever the issue claims a Codex test. If a full screenshot becomes unreadable at `270 × 360`, crop a real functional region and keep the original artifact as internal evidence. Never rebuild it as fake UI. Generated artwork may explain a metaphor or payoff, but it cannot replace the real result or the functional explanation.

When space is tight, remove secondary labels and decorative copy before shrinking the core input, action, or output. The functional page fails review if the Skill name is clear but its behavior is not.

## Detailed final card

Every recommendation carousel ends with the same recognizable cassette release card on warm paper. Preserve this visual grammar across issues:

- topic mark, name, and one-line function at the top;
- a ruled two-column grid of concise, source-supported facts;
- a dark release strip for provenance context;
- a small bordered prompt for the next play or reader interaction;
- `CREDITS` metadata and the final page number as quiet packaging details.

The grid should normally cover catalog number, maintainer, canonical source, pinned release/tag/commit, publication date, supported entry points, primary play, and one practical usage reminder. Adapt labels for tools, frameworks, or news topics. Do not force unverified values into the layout, and do not turn the card into an internal QA report.

## Final visual check

Inspect every page at full resolution and as a `270 × 360` thumbnail. Confirm:

- cover topic and payoff remain obvious;
- no title is lost against the artwork;
- Chinese wrapping has no orphaned punctuation or awkward single characters;
- repeated packaging labels do not compete with the message;
- the feature metaphor changes meaningfully across the story;
- page numbers are consecutive;
- no internal status, version marker, generated pseudo-text, or QA residue appears.
