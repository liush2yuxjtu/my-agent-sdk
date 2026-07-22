---
name: my-agent-sdk
description: 以引用驱动的交互流程创建新的或改进现有的 Claude Agent SDK 应用。凡用户要 scaffold/start/create Agent SDK 项目，或 upgrade/improve/refactor/fix 已有 Agent SDK 项目，都优先使用本技能。支持聊天内逐题交互与可预填、可导出的中文 HTML 表单；必须调用 new-agent-sdk 的需求与官方文档流程，并由 agent-sdk-dev 验证。
compatibility: 需要 read、bash、write/edit；macOS 用 open 打开 HTML；依赖本机已安装的 new-agent-sdk、agent-sdk-dev 与 html-artifacts 技能。
license: Apache-2.0
metadata:
  wrapper-target: new-agent-sdk
  modes: create, improve
  upstream: anthropics/claude-plugins-official/plugins/agent-sdk-dev/commands/new-sdk-app.md
---

# My Agent SDK

为 `new-agent-sdk` 增加双模式、双交互入口和引用账本：

- **create**：创建新的 Agent SDK 应用。
- **improve**：先只读理解已有 Agent SDK 项目，再按用户目标最小修改。
- **in-chat**：在聊天中一次问一个尚未回答的问题。
- **HTML form**：自动检测当前目录并预填表单，也可在浏览器中导入旧 JSON。

不要复制或替代底层 SDK 实现流程。

## 1. 必须加载的技能

完整读取并遵循：

- `/Users/liushiyuwin/.pi/agent/skills/new-agent-sdk/SKILL.md`
- `/Users/liushiyuwin/.pi/agent/skills/agent-sdk-dev/SKILL.md`
- `/Users/liushiyuwin/.pi/agent/skills/html-artifacts/SKILL.md`

`new-agent-sdk` 仍是需求、官方文档、版本核验和新项目实现的来源。`improve` 模式复用这些规则，但不得重新初始化或覆盖已有项目。

## 2. 智能判断模式

按用户意图自动选择，不要先让用户填命令参数：

- 出现“新建、创建、初始化、scaffold、start” → `create`。
- 出现“改进、升级、修复、重构、增加能力、已有项目” → `improve`。
- 当前目录已包含 `claude-agent-sdk` / `@anthropic-ai/claude-agent-sdk` 依赖或调用，且用户意图未明确 → 默认 `improve`。
- 仍无法判断时，只问一次：“创建新项目，还是改进现有项目？”

## 3. 选择交互入口

用户指定 HTML/表单/可视化时使用 HTML；用户指定聊天、当前环境无法打开浏览器，或只剩少量信息时使用 in-chat。用户未指定时：

- 已有项目 → 先检测并打开预填 HTML。
- 新项目 → 打开 HTML。
- 用户直接在聊天中给出答案 → 继续 in-chat，不强迫切换媒介。

### In-chat

一次只问一个尚未回答的问题。create 使用 `new-agent-sdk` 的六项需求；improve 依次确认：

1. 项目路径（若当前目录不是目标项目）。
2. 希望改变什么行为。
3. 哪些现有行为必须保持。
4. 是否允许依赖升级。
5. 需要新增或删除哪些能力。

已有答案直接预填并跳过。回答齐全后，在聊天中给出简短计划并等待明确确认。

### HTML form

不要要求用户拼 `--args`。若目标项目不是当前目录，先 `cd` 到目标目录，然后直接运行：

```bash
python3 /Users/liushiyuwin/.pi/agent/skills/my-agent-sdk/scripts/create_intake.py
open /tmp/my-agent-sdk-intake.html
```

脚本会智能检测当前目录：

- 发现 Agent SDK 依赖/调用 → 自动切到 `improve`，预填项目名、路径、语言、包管理器、SDK 版本和已检测能力。
- 未发现 → 使用 `create` 空白模板。
- 页面允许切换 create/improve、导入旧 JSON、继续编辑并导出。

表单必须保留：输入框、多选框、引用开关、实时 JSON、`复制为提示词` 和 `导出配置 JSON`。

## 4. Improve 模式先只读检查

编辑前必须检查真实项目，而不是只信预填：

1. 读取依赖清单、锁文件、运行时版本、入口点和测试命令。
2. 搜索 `query()`、streaming、AskUserQuestion、MCP、permissions、sessions、subagents、hooks 和 custom tools 的真实调用。
3. 找出所有即将修改函数的调用方。
4. 记录当前 SDK 版本与用户要求保持的行为。
5. 不读取或回显 `.env`、凭据和密钥值。

若目录不是 Agent SDK 项目，说明证据并让用户选择改为 create 或提供正确路径。

## 5. 引用要求

完整读取 `references/citations.md`。写代码前按实际能力逐页访问当前文档；每条设计决策紧跟对应具体 URL，不能只引用 overview。

逐项目引用 Anthropic demos，例如：

- `hello-world`：最小 `query()`。
- `simple-chatapp`：WebSocket 流式聊天。
- `ask-user-question-previews`：AskUserQuestion 阻塞往返。
- `research-agent`：子代理与 hooks。

同时引用 demo 仓库“仅供本地开发、不可直接用于生产”的警告。demo 与当前官方文档冲突时，以当前文档为准。

## 6. 计划确认

create 计划列出将创建的文件。improve 计划列出：

- 当前状态与目标差异。
- 将修改/新增/保持不变的文件。
- 依赖是否升级。
- 回归检查与回滚边界。

HTML 路径直接运行 `create_plan_review.py`；它会自动读取当前目录或 Downloads 中最新的 intake JSON 并生成 `/tmp/my-agent-sdk-plan-review.html`，不要求命令参数。未确认前不写项目。

## 7. 实施

### Create

把已确认答案交给 `new-agent-sdk`，严格执行其初始化、版本核验、安全和验证要求。

### Improve

复用 `new-agent-sdk` 的当前文档、依赖、安全和能力实现规则，但只做目标所需的最小 diff：

- 不重新初始化项目。
- 不覆盖现有配置。
- 不添加未请求能力。
- 先保留或补一条能证明目标行为的最小回归检查。
- 依赖升级必须由目标或当前官方 API 要求驱动。

两种模式都必须：隐藏 secret、提供取消/错误边界、真实完成 AskUserQuestion 同一 run 往返，并用 `agent-sdk-dev` 对应语言清单验证。

## 8. 交付

最终使用中文 HTML 报告：

```text
变更目标 → 当前/新实现 → 官方文档具体 URL → demo 具体项目 URL → 验证证据
```

报告 operation、SDK 版本、命令、修改路径、验证状态与剩余风险。验证失败时继续修复，不宣告成功。
