# my-agent-sdk

用**可导出的中文 HTML 配置器**包装 Claude Agent SDK 官方脚手架流程：先选择项目需求、能力与证据，再把结构化配置交给 `new-agent-sdk` 创建和验证应用。

> `my-agent-sdk` 不重写脚手架逻辑。它明确依赖并调用 **[`new-agent-sdk`](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/agent-sdk-dev/commands/new-sdk-app.md)**；该流程来自 Anthropic 官方 [`agent-sdk-dev` 插件](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/agent-sdk-dev)。

**在线配置器：<https://liush2yuxjtu.github.io/my-agent-sdk/>**

## 为什么需要这个包装层

`new-agent-sdk` 负责正确创建项目；`my-agent-sdk` 补充三个交付门：

1. **HTML 需求门**：项目名、语言、包管理器、能力多选和自定义要求。
2. **引用门**：按功能选择 `code.claude.com` 的具体页面和 `claude-agent-sdk-demos` 的具体项目。
3. **HTML 计划门**：用户导出确认后，才把需求交给 `new-agent-sdk` 实施，并由 `agent-sdk-dev` 验证。

```text
用户 → HTML intake → 引用账本 → HTML 计划确认
     → new-agent-sdk → agent-sdk-dev 验证 → HTML 交付
```

## 依赖关系

| 依赖 | 作用 | 上游 |
|---|---|---|
| `new-agent-sdk` | 收集已回答需求、核验当前 SDK 文档、创建项目 | [Anthropic `new-sdk-app.md`](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/agent-sdk-dev/commands/new-sdk-app.md) |
| `agent-sdk-dev` | TypeScript/Python SDK 验证清单 | [Anthropic `agent-sdk-dev`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/agent-sdk-dev) |
| `html-artifacts` | 自包含、可交互、可导出的 HTML | 本地 Pi skill |
| `skill-creator` | 技能结构、触发评测和打包 | 本地 Pi skill |

运行前请确保本机存在：

```text
~/.pi/agent/skills/new-agent-sdk/SKILL.md
~/.pi/agent/skills/agent-sdk-dev/SKILL.md
~/.pi/agent/skills/html-artifacts/SKILL.md
```

## 安装

```bash
git clone https://github.com/liush2yuxjtu/my-agent-sdk.git \
  ~/.pi/agent/skills/my-agent-sdk
```

也可以从 Releases 下载 `my-agent-sdk.skill`。

## 使用

对 Pi 说：

```text
用 my-agent-sdk 创建一个 TypeScript 客服 Agent。
需要 streaming、AskUserQuestion 和 sessions，使用 npm。
```

技能会打开 [`artifacts/intake.html`](artifacts/intake.html)。配置器支持：

- 项目信息输入框和能力多选框
- 24 个 Agent SDK 中文文档的逐 URL 引用开关
- 8 个 Anthropic demo 的逐项目引用开关
- 能力到引用的自动推荐
- 可增删约束、实时 JSON 预览
- “复制为提示词”和“导出构建配置 JSON”

## 引用策略

### 官方文档：逐 URL

不是只引用 overview。不同能力分别连接对应页面，例如：

- [`/quickstart`](https://code.claude.com/docs/zh-CN/agent-sdk/quickstart)
- [`/agent-loop`](https://code.claude.com/docs/zh-CN/agent-sdk/agent-loop)
- [`/custom-tools`](https://code.claude.com/docs/zh-CN/agent-sdk/custom-tools)
- [`/user-input`](https://code.claude.com/docs/zh-CN/agent-sdk/user-input)
- [`/streaming-output`](https://code.claude.com/docs/zh-CN/agent-sdk/streaming-output)
- [`/sessions`](https://code.claude.com/docs/zh-CN/agent-sdk/sessions)
- [`/permissions`](https://code.claude.com/docs/zh-CN/agent-sdk/permissions)
- [`/subagents`](https://code.claude.com/docs/zh-CN/agent-sdk/subagents)

完整索引见 [`references/citations.md`](references/citations.md)。

### Anthropic 示例：逐项目

- [`hello-world`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world)
- [`hello-world-v2`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world-v2)
- [`ask-user-question-previews`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/ask-user-question-previews)
- [`simple-chatapp`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/simple-chatapp)
- [`research-agent`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/research-agent)
- [`email-agent`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/email-agent)
- [`excel-demo`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/excel-demo)
- [`resume-generator`](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/resume-generator)

Anthropic 在[仓库 README](https://github.com/anthropics/claude-agent-sdk-demos#readme)中明确说明：这些 demo 仅供本地开发，不应直接部署到生产或规模化使用。

## HTML 推介包

- [交互式推介片](artifacts/pitch-video.html)
- [产品落地页](artifacts/landing-page.html)
- [键盘控制推介幻灯片](artifacts/pitch-slides.html)
- [触发评测编辑器](artifacts/eval-review.html)

## 结构

```text
my-agent-sdk/
├── SKILL.md
├── README.md
├── artifacts/
├── evals/
├── references/citations.md
└── scripts/
```

## 验证

```bash
python3 -m py_compile scripts/*.py
python3 /path/to/skill-creator/scripts/quick_validate.py .
```

已验证 HTML 内联 JavaScript、引用覆盖、配置导出，以及能力到文档/demo 的自动选择。

## License

Apache-2.0。上游 Anthropic 项目和示例仍分别受其自身许可证约束。
