---
name: skill-cartridge-daily
description: Create or revise a dated, ready-to-publish Xiaohongshu carousel about an Agent Skill, a Codex/Claude Code/WorkBuddy tip, or a light AI tooling topic using the Skill卡带 new-album visual system. Use for daily topic selection, source and GitHub checking, human Chinese copy, carousel production, visual revisions, export, delivery packaging, and skill catalog updates.
---

# Skill 卡带·每日发行

Produce one light, playful Xiaohongshu post that tired people can understand and try without feeling they have opened another work tutorial. The post should still reward technical readers with accurate sources and install details.

## Start with one compact interaction

If the user already named a topic, do not ask them to choose it again. Otherwise, research current web/social recommendations and GitHub weekly momentum. During the account launch phase, prioritize approachable Skills that help Xiaohongshu creators make, style, organize, or remix content: design, imagery, video, writing, playful utilities, and other visible five-minute wins. Aim the voice and examples primarily at women creators and beginners without resorting to gender stereotypes or default pink styling. Limit programmer-only topics to roughly one issue per week. Among candidates that pass this audience and fun filter, prioritize one-week momentum over lifetime totals. Offer exactly three short candidates. For each candidate, state the fun payoff in one sentence; keep research notes private.

Ask at most one compact round of optional choices covering:

- topic, only when not supplied;
- audience lean: beginner, mixed, or technical;
- one optional visual adjustment.

Use sensible defaults if the user says “按建议”, “直接做”, or gives no preference. Do not turn the daily workflow into a questionnaire.

## Create the dated workspace

Use the current date in `Asia/Shanghai`, not UTC. Create the issue with:

```powershell
python skills/skill-cartridge-daily/scripts/new_daily_issue.py <slug> --root .
```

This creates:

- `content/daily/YYYY-MM-DD/<slug>/` for working files and renders;
- `deliveries/YYYY-MM-DD/<slug>/` for publish-ready files only.

Never overwrite an existing issue. If the same topic is being revised, continue in its existing directory.

## Research before writing

Read [references/editorial-system.md](references/editorial-system.md) before selecting, verifying, or writing a topic.

For Skill posts, open the canonical GitHub repository and read the relevant `README`, `SKILL.md`, releases/commits, and install instructions. Use the upstream repository or official product docs as the factual authority; social posts are leads, not proof. Record URLs, access date, exact claims, install path, and any uncertainty in `sources.md`.

Do not publish a topic if its core function or usage cannot be supported by a credible source. Choose another topic instead of filling a slide with a failed test or disclaimer.

## Write for play, not homework

Build a 6–8 page story. Use eight pages when the real result, beginner setup, or visual pacing needs more room; never shrink useful text merely to stay at seven. Lead with a specific fun result, show one five-minute play, give a copyable prompt or tiny recipe, explain what happened, state who will enjoy it, and include platform-appropriate installation or next action.

Every post that recommends a specific Skill, tool, framework, or GitHub project must end with a detailed cassette release card. This final page is mandatory and cannot be replaced by a generic closing quote. Use only source-supported facts: topic name and one-line function, catalog number, maintainer, canonical source, pinned release/tag/commit when traceable, publication date, supported entry points, primary play, and one practical usage reminder. Keep the closing interaction as a small strip on the same page. If a field cannot be verified, substitute a more useful verified field or omit that cell; never invent data or print internal uncertainty.

Write Chinese like a sharp friend sharing a small discovery after work:

- short spoken sentences, concrete nouns, and verbs people use in conversation;
- one idea per page;
- humor from the actual function, not memes pasted on top;
- enough detail to try it immediately;
- no corporate tutorial voice, inflated claims, fake personal experience, or generic AI filler.

Do not make every sentence polished, balanced, or complete. Natural fragments, uneven sentence lengths, and one restrained aside are welcome when they sound better aloud. Avoid repeated AI-shaped constructions such as “不是 A，而是 B”, “听起来……其实……”, “只需三步”, “一键解锁”, “值得收藏”, and tidy three-part parallel lists. Never start from a definition when a concrete moment can start the story.

Before laying out the carousel, perform the human-voice pass in [references/editorial-system.md](references/editorial-system.md). Delete any sentence that could be pasted unchanged onto ten other AI tools. Replace abstractions with one visible action, object, input, or reaction. Preserve accurate technical names and commands, but explain them in ordinary Chinese around the code.

Do not title the recurring sections “推荐 Skill”, “玩法提案”, or other stiff labels. Name each page for the story being told.

## Build the cassette release

Read [references/visual-system.md](references/visual-system.md) before creating or revising the carousel.

Treat every post as a new cassette single in the same label catalog, not another recolor of yesterday's template. Before designing, compare the last three covers and choose a visibly different issue art direction. Keep the label identity in the catalog mark, micro-metadata, typography discipline, and final release card; let the hero medium, composition, palette, lighting, and page rhythm change with the Skill.

When the configured GPT-IMAGE-2 workflow is available, every recommendation issue must use at least two original, feature-specific images. Give them different editorial jobs: normally one scroll-stopping cover hero and one inner-page function, transformation, or payoff scene. Do not satisfy the rule with two near-duplicate decorative backgrounds. Ask the image model for artwork without lettering, logos, UI, or pseudo-text, then add all accurate Chinese copy and metadata in HTML/CSS so it stays readable and editable. The authentic Codex result page remains separate and must never be replaced by generated artwork.

Create or update the issue HTML/CSS, export consecutive `1080 × 1440` PNG files, and inspect both full size and `270 × 360` thumbnails. Revise weak hierarchy, illegible copy, awkward wrapping, duplicated ideas, and anything that looks like an unfinished mockup.

Keep the detailed final card visually consistent across releases: warm-paper stock, compact cassette metadata, a two-column fact grid, one dark release strip, and a small next-play prompt. Adapt field labels to the topic without changing the recognizable card family.

For each Skill issue, when the official example is safe and feasible, run one smallest useful case in Codex and include one page showing the authentic result. Keep the test isolated, save the underlying artifact or screenshot as internal evidence, and use only the clean result in public output. If Codex cannot produce a result, do not fabricate or label a source image as hands-on; use a clearly sourced upstream example instead or choose another topic.

For this user's configured GPT-IMAGE-2 CLI workflow, the credential is exposed as `AGTCLOUD_API_KEY` and the OpenAI-compatible Base URL is `https://api.agtcloud.ai/v1`. Map the credential to `OPENAI_API_KEY` only inside the generation process, set that Base URL for the same process, and never print or store the secret in project files.

If AGTCloud returns HTTP 429 `rate_limit_exceeded` for the `gpt-image` limit, treat it as a temporary throttle rather than a credential failure. Honor the response's retry delay, add a small three-second buffer, and retry the unchanged request up to two times. Do not switch models, lower quality, or generate duplicate variants merely because of this throttle. Previously completed images remain valid and must not be regenerated.

## Keep public output final-only

Read [references/output-contract.md](references/output-contract.md) before packaging.

Public images and `小红书文案.md` must never contain process labels such as “已核验”, “未跑通”, “V2”, “S3”, “AI 生成”, “非运行截图”, model/API errors, QA notes, or test failures. Keep those details in `sources.md` only.

Treat the user's writing directions and the production method as backstage instructions, not publishable copy. Never tell readers that the copy is “人话”, “像人写的”, “不 AI”, “AI 生成”, or “机器输出”, and do not narrate prompting, rewriting, or model use. Avoid editorial-workflow labels such as “回源”, “核验”, or “翻译成人话” on public pages. Show the concrete reader-facing action instead: where the item was found, what the maintainer says, what the reader can try, and what source link is available.

The delivery directory contains only:

- numbered final PNGs;
- `小红书文案.md`;
- an optional contact sheet.

Do not include drafts, alternate covers, internal prompts, source notes, HTML, or QA images.

## Finish the issue

Write a Xiaohongshu caption with an opening hook, the five-minute play, a light interaction prompt, and restrained relevant hashtags. Avoid duplicating every carousel sentence.

Add or update the topic in `data/skills.json`. Preserve the existing schema and include canonical source links and platform install distinctions. Then run:

```powershell
npm run validate
npm run catalog -- check
```

Report the dated delivery directory, page count, topic, and any source limitation that affects what the user may claim. Offer one compact micro-adjustment round for copy or visual tone; revise the existing issue rather than creating another dated folder.
