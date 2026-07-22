# Claude Agent SDK 引用索引

核验日期：2026-07-22。入口页实际链接出以下 Agent SDK 中文页面；使用时按能力逐 URL 引用，不能只引用 overview。

## code.claude.com/docs/zh-CN/agent-sdk/*

### 核心与语言
- [overview](https://code.claude.com/docs/zh-CN/agent-sdk/overview) — 产品边界与核心能力
- [quickstart](https://code.claude.com/docs/zh-CN/agent-sdk/quickstart) — 最小可运行入口
- [agent-loop](https://code.claude.com/docs/zh-CN/agent-sdk/agent-loop) — 消息生命周期、工具与上下文
- [typescript](https://code.claude.com/docs/zh-CN/agent-sdk/typescript) / [python](https://code.claude.com/docs/zh-CN/agent-sdk/python) — 各语言 API
- [migration-guide](https://code.claude.com/docs/zh-CN/agent-sdk/migration-guide) — 旧版 SDK 迁移
- [typescript-v2-preview](https://code.claude.com/docs/zh-CN/agent-sdk/typescript-v2-preview) — 实验性 V2 API，引用时必须标注预览状态

### 输入、输出与状态
- [user-input](https://code.claude.com/docs/zh-CN/agent-sdk/user-input) — AskUserQuestion 与用户交互
- [streaming-output](https://code.claude.com/docs/zh-CN/agent-sdk/streaming-output) — 实时流式输出
- [streaming-vs-single-mode](https://code.claude.com/docs/zh-CN/agent-sdk/streaming-vs-single-mode) — 输入模式选择
- [structured-outputs](https://code.claude.com/docs/zh-CN/agent-sdk/structured-outputs) — 结构化结果
- [sessions](https://code.claude.com/docs/zh-CN/agent-sdk/sessions) — continue、resume、fork
- [session-storage](https://code.claude.com/docs/zh-CN/agent-sdk/session-storage) — 会话持久化
- [file-checkpointing](https://code.claude.com/docs/zh-CN/agent-sdk/file-checkpointing) — 文件检查点

### 工具与扩展
- [custom-tools](https://code.claude.com/docs/zh-CN/agent-sdk/custom-tools) — 进程内 MCP 工具
- [mcp](https://code.claude.com/docs/zh-CN/agent-sdk/mcp) — MCP 服务器
- [permissions](https://code.claude.com/docs/zh-CN/agent-sdk/permissions) — 权限模式与规则
- [hooks](https://code.claude.com/docs/zh-CN/agent-sdk/hooks) — 生命周期拦截
- [subagents](https://code.claude.com/docs/zh-CN/agent-sdk/subagents) — 子代理
- [skills](https://code.claude.com/docs/zh-CN/agent-sdk/skills) / [plugins](https://code.claude.com/docs/zh-CN/agent-sdk/plugins) — 扩展机制
- [claude-code-features](https://code.claude.com/docs/zh-CN/agent-sdk/claude-code-features) — 复用 Claude Code 功能
- [modifying-system-prompts](https://code.claude.com/docs/zh-CN/agent-sdk/modifying-system-prompts) — 系统提示词
- [slash-commands](https://code.claude.com/docs/zh-CN/agent-sdk/slash-commands) — 斜杠命令
- [todo-tracking](https://code.claude.com/docs/zh-CN/agent-sdk/todo-tracking) — Todo 跟踪
- [tool-search](https://code.claude.com/docs/zh-CN/agent-sdk/tool-search) — 工具搜索

### 生产运行
- [hosting](https://code.claude.com/docs/zh-CN/agent-sdk/hosting) — 托管拓扑
- [secure-deployment](https://code.claude.com/docs/zh-CN/agent-sdk/secure-deployment) — 安全部署
- [observability](https://code.claude.com/docs/zh-CN/agent-sdk/observability) — 可观测性
- [cost-tracking](https://code.claude.com/docs/zh-CN/agent-sdk/cost-tracking) — 成本追踪

完整、可刷新的 URL 快照见 [`source-packs.json`](source-packs.json)。

## anthropics/claude-agent-sdk-demos/{project}

仓库：[anthropics/claude-agent-sdk-demos](https://github.com/anthropics/claude-agent-sdk-demos)，核验 commit [`826b268`](https://github.com/anthropics/claude-agent-sdk-demos/commit/826b268506a5f3707623c9e6140b200befcbebae)。

- [hello-world](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world) — 最小 `query()`、消息迭代、cwd、工具白名单
- [hello-world-v2](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/hello-world-v2) — 实验性 `send()`/`stream()`、多轮与恢复
- [ask-user-question-previews](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/ask-user-question-previews) — `canUseTool` 经 WebSocket 阻塞往返、HTML preview 净化
- [simple-chatapp](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/simple-chatapp) — React + Express + WebSocket 流式聊天
- [research-agent](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/research-agent) — 子代理编排、hooks、`parent_tool_use_id`
- [email-agent](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/email-agent) — IMAP 业务代理
- [excel-demo](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/excel-demo) — Electron 桌面端与表格代理
- [resume-generator](https://github.com/anthropics/claude-agent-sdk-demos/tree/main/resume-generator) — WebSearch + docx 单任务代理

## 强制边界

必须同时引用[仓库根 README](https://github.com/anthropics/claude-agent-sdk-demos#readme)的生产警告：这些是 Anthropic demo，仅供本地开发，不应直接部署到生产或规模化使用。demo 与当前官方文档冲突时，以当前官方文档为准。
