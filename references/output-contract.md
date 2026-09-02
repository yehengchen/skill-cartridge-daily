# Output contract

## Directory layout

Use Shanghai local date:

```text
content/daily/YYYY-MM-DD/<slug>/
├── assets/              # source and generated artwork
├── png/                 # current full-resolution renders
├── brief.md             # chosen angle and audience
├── sources.md           # internal source and verification notes
├── copy.md              # page-by-page copy
├── image-prompts.md     # internal image directions
├── carousel.html        # when HTML/CSS rendering is used
└── styles.css           # when separated from HTML

deliveries/YYYY-MM-DD/<slug>/
├── 01-cover.png
├── 02-....png
├── ...
├── 小红书文案.md
└── contact-sheet.png    # optional
```

Use a short lowercase ASCII slug with hyphens. Revisions remain inside the same dated topic directory.

## Delivery directory allowlist

Only copy final public artifacts into `deliveries/`:

- final `1080 × 1440` PNG pages with consecutive two-digit numbers;
- `小红书文案.md`;
- optional contact sheet.

Keep these out of `deliveries/`:

- HTML/CSS and scripts;
- alternate covers, drafts, `v2`/`final-final` files;
- source notes and verification logs;
- raw image prompts;
- thumbnails and visual QA output;
- failed screenshots or API/model error output.

## Public-content ban list

Before delivery, scan public images and caption for process language. Remove:

- `已核验`, `未跑通`, `V2`, `S3`;
- `AI 生成`, `非运行截图`;
- API errors, policy errors, stack traces;
- internal QA, uncertainty, or test-failure prose;
- claims of hands-on testing that did not occur.

If an important limitation affects the public play, phrase the actual supported boundary naturally. Keep editorial verification detail in `sources.md`.

## Caption structure

`小红书文案.md` should be ready to paste and contain:

1. a short hook not identical to the cover;
2. the relatable situation;
3. the five-minute play and copyable prompt/instruction;
4. the useful outcome and who it suits;
5. a light question or invitation;
6. a restrained set of relevant hashtags;
7. canonical source link when the publishing format allows it, otherwise a clear repository name for comments/profile notes.

Do not insert internal production notes into the caption.

## Required final page for recommendations

When the note recommends a concrete Skill, tool, framework, or repository, the highest-numbered PNG must be the detailed cassette release card described in `visual-system.md`. Confirm that its source, maintainer, version/release/commit, compatibility, and safety wording agree with `sources.md`. The final card is part of the publish-ready sequence, not an optional appendix.
