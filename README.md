# my-agent-sdk

> **尽览官方能力，一站创建与升级 Agent。**  
> *Explore every official capability. Build or improve in one flow.*

用**聊天内交互**或**可预填、可导出的中文 HTML 配置器**创建新的或改进现有的 Claude Agent SDK 应用。已有项目会自动检测语言、包管理器、SDK 版本和能力；两种模式都沿用 `new-agent-sdk` 的官方文档与实现规则。

> `my-agent-sdk` 不重写脚手架逻辑。它明确依赖并调用 **[`new-agent-sdk`](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/agent-sdk-dev/commands/new-sdk-app.md)**；该流程来自 Anthropic 官方 [`agent-sdk-dev` 插件](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/agent-sdk-dev)。

**在线配置器：<https://liush2yuxjtu.github.io/my-agent-sdk/>**

## 为什么需要这个包装层

`new-agent-sdk` 负责新项目的正确创建；`my-agent-sdk` 增加：

1. **双模式**：create 新项目；improve 现有项目且不重新初始化。
2. **双交互入口**：聊天中一次问一个问题，或使用 HTML 表单。
3. **智能预填**：在已有项目目录直接运行脚本，无需拼 `--args`。
4. **引用与计划门**：确认后才实施，并由 `agent-sdk-dev` 验证。

```text
用户 → create / improve → in-chat / HTML form → 引用账本
     → new-agent-sdk 规则 → agent-sdk-dev 验证 → HTML 交付
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
用 my-agent-sdk 创建一个 TypeScript 客服 Agent，聊天里问我。
```

或：

```text
用 my-agent-sdk 改进当前 Agent SDK 项目，打开预填表单。
```

HTML 模式不需要命令参数。在新目录或已有项目目录直接运行：

```bash
python3 ~/.pi/agent/skills/my-agent-sdk/scripts/create_intake.py
open /tmp/my-agent-sdk-intake.html
```

每次访谈固定展示：

1. **WHAT WE CAN DO**：两套来源当前提供的完整能力与链接。
2. **WHAT WE HAVE SO FAR**：已有项目的真实实现，或新项目状态。
3. **WHAT IS SUGGESTED TO IMPROVE / ADD**：基于差距的最小建议。
4. **FINAL CONFIRMATION**：用户确认后才写文件。

落地页的“改进现有项目”会在当前页打开完整配置器；使用同一个 `intake.html` iframe，避免复制表单和功能漂移，并保留“全屏打开”入口。

配置器支持：

- create / improve 切换
- 现有项目的语言、包管理器、SDK 版本与能力自动预填
- 导入旧 JSON 后继续填写
- 项目信息输入框和能力多选框
- 自动刷新并展示 30 个官方文档逐 URL、8 个 demo 逐项目引用开关
- 可增删约束、实时 JSON、复制提示词和导出

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

## 演示视频与 HTML 推介包

- [中文落地页与中文 WebM](https://liush2yuxjtu.github.io/my-agent-sdk/)
- [English landing page and WebM](https://liush2yuxjtu.github.io/my-agent-sdk/en/)
- [中文 Pi 会话回放页](artifacts/pi-session-demo-zh.html)
- [English Pi session playback](artifacts/pi-session-demo-en.html)
- [交互式推介片](artifacts/pitch-video.html)
- [GitHub Pages 落地页](artifacts/index.html)
- [旧版产品落地页](artifacts/landing-page.html)
- [键盘控制推介幻灯片](artifacts/pitch-slides.html)
- [触发评测编辑器](artifacts/eval-review.html)

## 结构

```text
my-agent-sdk/
├── SKILL.md
├── README.md
├── artifacts/
├── evals/
├── references/sources.urls
├── references/citations.md
├── references/source-packs.json
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
