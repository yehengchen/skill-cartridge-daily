# Editorial system

## Topic range

Keep Agent Skills as the main lane. During launch, favor design, imagery, video, writing, playful utilities, and light practical Skills that a Xiaohongshu creator or beginner can enjoy immediately. Aim examples primarily at women creators without stereotypes, forced beauty/fashion assumptions, or automatic pink styling. Programmer-only Skills should occupy no more than roughly one issue per week; keep strong technical finds for that slot or a later collection. Occasionally publish a useful Codex, Claude Code, or WorkBuddy trick, or one simple model/framework news item with an immediate hands-on angle.

## Launch-phase traffic priority

While the account is building its first audience, treat fun and shareability as the first editorial gate. A candidate should have a benefit that is guessable in one glance, a five-minute play with a visible result, and a feature-specific visual joke that can stop the scroll. Use weekly GitHub momentum and recent maintenance to rank candidates that already pass this gate; do not fill an early slot with a worthy but visually flat utility merely because it has more Stars.

Use social media, newsletters, discovery sites, GitHub trending/activity, and community discussion to find leads. Treat [Awesome Skill](https://awesomeskill.ai/) as a recurring discovery index for searchable categories, recently listed Skills, and popularity clues. It is a lead source only: follow each candidate back to its canonical GitHub repository, then verify the relevant `README`, `SKILL.md`, fixed commit or release, and current installation instructions before publishing. Never reuse an Awesome Skill description or install instruction as the final factual authority. Do not treat popularity alone as proof. Avoid a complicated news roundup; one post should deliver one clear play.

## Freshness and momentum

For an ordinary daily issue, start from GitHub Trending for **This week** and favor useful topics with the fastest seven-day Star growth. Lifetime Star count is context, not the ranking signal.

Capture the following internally at selection time:

- Stars gained this week from GitHub Trending;
- current total Stars;
- latest meaningful commit or release date;
- whether the newly popular feature can be tried in five minutes;
- whether the repository exposes a clear canonical `README`, `SKILL.md`, and install/use path.

Prefer candidates that combine strong weekly velocity, activity within roughly seven days, a clear functional change or newly visible use case, and a playful visual story. A repository does not need to have been created during the week; the goal is to catch current acceleration rather than reward age.

Move mature projects with high lifetime Stars but weak current momentum into a future roundup or evergreen collection. Do not spend a normal daily slot on them merely because their total Star count is impressive. If GitHub Trending does not expose a trustworthy weekly number, describe momentum qualitatively in internal notes instead of inventing a delta.

## Source hierarchy

Verify every public functional or installation claim against the strongest available source:

1. canonical GitHub repository files, releases, commits, and examples;
2. official product documentation or official announcements;
3. maintainer posts and credible demos;
4. community posts only as discovery or clearly attributed experience.

For a repository, confirm the owner, repository URL, license when relevant, recent state, exact feature, prerequisites, and current usage or install instructions. Follow links from the repository instead of copying third-party instructions. Never invent an installation command from a familiar pattern.

Record in internal `sources.md`:

- canonical URL and access date;
- relevant file, release, or documentation page;
- supported public claims;
- exact install/use commands copied from upstream;
- uncertainty, platform caveats, or untested status.

Public copy may confidently state only what those sources support. “Verified” is an internal editorial state, not a badge for the carousel.

## Platform installation distinctions

- **Codex:** Use an upstream installer only when the project explicitly supports Codex or installs standard Agent Skills into a location Codex reads. Otherwise link the canonical repository and give the documented manual path.
- **Claude Code:** Use an upstream command only when Claude Code support is explicit. Do not present a Codex-only command as universal.
- **WorkBuddy:** Prefer “下载/复制本地 Skill 文件夹，或导入 ZIP” unless WorkBuddy documentation confirms a different installer. Never imply the same CLI command works merely because the Skill format looks similar.
- **No trusted install command:** Give the canonical GitHub link and a plain-language manual instruction. Accuracy is more useful than a suspicious one-liner.

Do not claim hands-on testing unless it actually happened in the named environment. Lack of local testing does not need to appear in public artwork; describe only source-supported behavior and keep the note internal.

## Human copy

The reader is tired and scrolling for relief. Make the post feel like finding a clever toy, not receiving homework.

Prefer:

- “我把一个想法丢进去，它先反问到我没法糊弄自己。”
- “五分钟玩法：拿你拖了最久的那个需求试一次。”
- “适合：脑子里有东西，但一打开空白文档就想逃的人。”

Avoid:

- “赋能工作流”“效率提升 300%”“建议收藏”；
- fictional first-person testing or fabricated screenshots;
- paragraph-heavy explanations;
- repeated praise without showing a play;
- labels such as “推荐 Skill” or “玩法提案”.

## Default 6–8 page arc

Adapt the arc to the topic; do not mechanically print these labels:

1. **Cover:** feature becomes a curiosity gap and one striking physical metaphor.
2. **The loop:** show the ordinary frustration and the new playful behavior.
3. **Five-minute play:** give one specific input/task.
4. **Copyable prompt:** short, usable, and visually scannable.
5. **What it changes:** show the result or feature mechanics with a concrete example.
6. **Who it fits + install:** separate Codex, Claude Code, and WorkBuddy correctly.
7. **Optional breathing room:** use an extra page for the authentic result, beginner explanation, or a second visible variation when combining it would make another page crowded.
8. **Detailed release card:** for every concrete recommendation, close with the standard two-column cassette card: identity, maintainer, canonical source, traceable version/release/commit, publication date, supported entry points, primary play, usage reminder, and a small next-play prompt. Use verified facts only and adapt labels when the topic is not a Skill. In a seven-page issue, this card is page 7.

Fewer pages are acceptable when the idea is simple. More pages are not a substitute for stronger storytelling.
