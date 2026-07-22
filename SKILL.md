---
name: my-agent-sdk
description: 以可导出的中文 HTML 配置器包装并驱动 new-agent-sdk，创建或初始化 Claude Agent SDK 应用。凡用户要搭建、脚手架化、启动 Claude Agent SDK 项目，或涉及 streaming、AskUserQuestion、MCP、自定义工具、权限、会话、子代理时，都优先使用本技能；它会强制给出 Anthropic 官方逐功能 URL 引用和 claude-agent-sdk-demos 逐 demo 引用。
compatibility: 需要 read、bash、write/edit；macOS 用 open 打开 HTML；依赖本机已安装的 new-agent-sdk、agent-sdk-dev 与 html-artifacts 技能。
license: Apache-2.0
metadata:
  wrapper-target: new-agent-sdk
  upstream: anthropics/claude-plugins-official/plugins/agent-sdk-dev/commands/new-sdk-app.md
---

# My Agent SDK

用 HTML 完成需求收集和计划确认，再把结构化答案交给 `new-agent-sdk` 执行。不要复制或改写底层脚手架流程；本技能只增加交互、引用和交付层。

## 1. 先加载底层技能

完整读取并遵循：

- `/Users/liushiyuwin/.pi/agent/skills/new-agent-sdk/SKILL.md`
- `/Users/liushiyuwin/.pi/agent/skills/agent-sdk-dev/SKILL.md`
- `/Users/liushiyuwin/.pi/agent/skills/html-artifacts/SKILL.md`

`new-agent-sdk` 是实现流程的唯一来源。若本技能与它冲突，以安全、官方文档时效性和验证要求更严格者为准。

## 2. 用 HTML 收集需求

不要在聊天里逐题询问。运行：

```bash
python3 /Users/liushiyuwin/.pi/agent/skills/my-agent-sdk/scripts/create_intake.py \
  --output /tmp/my-agent-sdk-intake.html \
  --session-id "${TERM_SESSION_ID:-unknown}"
open /tmp/my-agent-sdk-intake.html
```

配置器必须保留：

- 输入框：项目名、自定义用途、项目目录、可增删的额外约束。
- 单选：TypeScript/Python、起点、包管理器。
- 多选框：streaming、AskUserQuestion、MCP、permissions、sessions、subagents、custom tools 等。
- **官方文档逐 URL 引用矩阵**：显示页面标题、完整 URL、用途与“纳入引用”开关。
- **Anthropic demos 逐项目引用矩阵**：显示具体项目 URL、可借鉴点与“纳入引用”开关。
- 引用矩阵的表格、开关、增删行和导出文案沿用 skill-creator eval HTML 的直接、可编辑风格。
- 明确的状态摘要、校验提示、`导出构建配置 JSON` 按钮和 `复制为提示词` 按钮；导出的 JSON 必须携带所选引用账本。

请用户完成配置并点击导出。读取 `~/Downloads/my-agent-sdk-intake*.json` 中最新文件。若浏览器禁止下载，让用户使用“复制为提示词”并粘贴回来。

这份 JSON 已回答 `new-agent-sdk` 的需求问题，因此按其“已回答则跳过”规则直接进入计划；不要重复询问。

## 3. 逐 URL 核验官方资料

在写代码前，访问并按所选能力逐页核验。不能只引用 overview：

- 总览：<https://code.claude.com/docs/zh-CN/agent-sdk/overview>
- 快速开始：<https://code.claude.com/docs/zh-CN/agent-sdk/quickstart>
- 代理循环：<https://code.claude.com/docs/zh-CN/agent-sdk/agent-loop>
- 自定义工具/MCP：<https://code.claude.com/docs/zh-CN/agent-sdk/custom-tools>
- 流式输出：<https://code.claude.com/docs/zh-CN/agent-sdk/streaming-output>
- 会话：<https://code.claude.com/docs/zh-CN/agent-sdk/sessions>
- 权限：<https://code.claude.com/docs/zh-CN/agent-sdk/permissions>

只引用实际核验过的页面。每条设计决策后紧跟对应页面链接，而不是把所有链接堆在文末。

## 4. 逐 demo 引用实现先例

完整读取 `references/citations.md`。按能力给出具体 demo 链接与借鉴点：

- 最小 `query()`：`hello-world`
- WebSocket + 流式聊天：`simple-chatapp`
- `AskUserQuestion` 浏览器阻塞往返：`ask-user-question-previews`
- 子代理编排与 hooks：`research-agent`

不要把 demos 当生产规范。必须同时引用仓库根 README 的“仅本地演示、不要直接用于生产”警告，并说明哪些部分需要生产加固。

## 5. 用 HTML 确认计划

根据导出的 JSON 与已核验资料，生成一个自包含计划确认 HTML：

- 列出项目路径、文件清单、能力与验证命令。
- 每项计划用复选框；保留一个“补充要求”输入框。
- 提供 `导出确认 JSON` 和 `复制确认提示词`。
- 清晰标注来源项目名、绝对路径和当前 Pi session ID。
- 使用短而具体的 UX 文案，如“导出并开始创建”，不要用“提交”。

打开 HTML，等待用户导出确认；未确认前不要创建项目文件。这一步落实 `new-agent-sdk` 的计划确认门。

## 6. 调用 new-agent-sdk 实施

把已确认 JSON 作为已回答需求，严格执行 `new-agent-sdk`：

1. 核验 npm/PyPI 最新稳定版本。
2. 只实现所选能力。
3. `.env.example` 不含真实 secret，`.env` 进入忽略列表。
4. 有界错误处理和取消。
5. `AskUserQuestion` 必须完成同一次 SDK run 的 UI 阻塞往返；不能用普通助手文本冒充。
6. 完成后按 `agent-sdk-dev` 对应语言清单验证。

## 7. 输出引用账本

最终交付使用中文 HTML，并在“为什么这样实现”中逐条写：

```text
设计决策 → 官方文档具体 URL → 对应 demo 具体 URL → 本项目采用/未采用的部分
```

至少包含一个官方页面和一个具体 demo；涉及多项能力时逐项引用。报告 SDK 版本、执行命令、输出路径、验证状态与剩余风险。

## 8. 失败边界

- 官方页面不可访问：暂停实现并报告具体 URL 与错误，不用记忆替代。
- demo 与官方文档冲突：采用当前官方文档，并标注 demo 仅作结构参考。
- HTML 导出缺失或计划未确认：不开始创建项目。
- 验证失败：继续修复，不宣告成功。
