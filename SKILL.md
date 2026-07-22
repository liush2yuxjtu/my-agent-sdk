---
name: my-agent-sdk
description: 交互式创建或改进 Claude Agent SDK 应用。凡用户要搭建、审查、扩展或升级 Agent SDK 项目，或提到 streaming、AskUserQuestion、MCP、自定义工具、权限、会话、子代理等能力时使用；先探索仓库与最新官方资料，在聊天中展示完整能力、现状和建议，得到最终确认后才实施。
compatibility: 需要 read、bash、write/edit，并依赖本机 new-agent-sdk 与 agent-sdk-dev 技能。
---

# My Agent SDK

1. 以 `/Users/liushiyuwin/.pi/agent/skills/new-agent-sdk/SKILL.md` 为唯一实现流程，并在实施和验证时遵循 `agent-sdk-dev`。
2. 读取 `references/sources.urls`，运行 `scripts/refresh_sources.py`，再实时探索两个来源包：遍历 `code.claude.com/docs/.../agent-sdk/*` 的全部相关页面及 `claude-agent-sdk-demos` 的全部 demo；逐项保留具体 URL，不依赖旧的固定能力清单。
3. 若目标仓库已存在，先探索其结构、依赖、入口、SDK 用法、工具、权限、会话、UI 往返、测试和缺口，结论必须有文件或命令证据。
4. 只在聊天中访谈用户，并依次展示 **WHAT WE CAN DO**（来源支持的完整能力与链接）、**WHAT WE HAVE SO FAR**（仅改进现有项目时展示）、**WHAT IS SUGGESTED TO IMPROVE / ADD**（按现状给出可选建议）；一次问一个聚焦问题，不用 HTML 配置器代替对话。
5. 用户选择后，汇总最终范围、会改动的文件、验证命令和风险，并取得明确的最后确认；确认前不修改项目，确认后才按 `new-agent-sdk` 实施并按 `agent-sdk-dev` 验证。
