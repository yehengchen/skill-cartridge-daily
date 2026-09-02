# Skill 卡带·每日发行

一个面向 Codex 的小红书日更工作流 Skill：从社交平台与 GitHub 发现有趣的 Agent Skill、AI 工具技巧或轻量技术热点，核对原始来源，生成可直接发布的中文图文，并维护搜索集合。

## 它会完成什么

- 优先发现近一周有热度、容易上手且具备视觉效果的选题；
- 回到 GitHub 原仓库或官方文档核对功能、安装和使用方法；
- 输出 6–8 张 `1080 × 1440` 小红书图文；
- 每期至少使用两张功能相关的 GPT‑IMAGE‑2 原创图；
- 区分生成的功能概念图与 Codex 真实运行结果；
- 保持「Skill 卡带 / 新专辑发行」品牌识别，同时改变每期视觉世界；
- 生成发布文案、详细卡带资料页，并更新 Skill 搜索集合。

## 安装

将整个仓库目录复制到 Codex 的 Skills 目录：

```text
~/.codex/skills/skill-cartridge-daily
```

发布到 GitHub 后，也可以通过 Skills 安装器添加仓库：

```text
npx skills@latest add https://github.com/<owner>/skill-cartridge-daily
```

安装完成后重启 Codex。

## 使用

```text
$skill-cartridge-daily 生成今天的小红书图文
```

也可以直接指定主题：

```text
$skill-cartridge-daily 用 grill-me 生成今天的 8 张小红书图文
```

## 图片接口

项目约定使用环境变量 `AGTCLOUD_API_KEY` 调用兼容的 GPT‑IMAGE‑2 接口。密钥只从环境读取，不应写入仓库、提示词文件或交付目录。

## 目录

```text
skill-cartridge-daily/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── scripts/new_daily_issue.py
└── README.md
```

## 状态

当前为本地首版。创建远程仓库前，可按需要补充开源许可证与仓库所有者信息。
