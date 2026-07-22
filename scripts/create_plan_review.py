#!/usr/bin/env python3
"""Generate a mode-aware plan gate from the newest exported intake JSON."""
import json
import os
from html import escape
from pathlib import Path

PROJECT = "/Users/liushiyuwin/.pi/agent/skills/my-agent-sdk"


def newest_intake() -> Path:
    roots = [Path.cwd(), Path.home() / "Downloads"]
    files = [p for root in roots if root.exists() for pattern in ("my-agent-sdk-*-intake*.json", "my-agent-sdk-build-intake*.json") for p in root.glob(pattern)]
    if not files:
        raise SystemExit("未找到 intake JSON；请先在 HTML 中导出配置。")
    return max(files, key=lambda p: p.stat().st_mtime)


def main() -> None:
    source = newest_intake()
    data = json.loads(source.read_text(encoding="utf-8"))
    operation = data.get("operation", "create")
    lang = data.get("language", "TypeScript")
    target = data.get("project_path") or "./" + data.get("project_name", "agent")
    if operation == "improve":
        items = [
            f"只读复核 {target} 的依赖、入口、调用方与测试",
            f"保持现有行为：{'; '.join(data.get('requirements', [])) or '未涉及的行为'}",
            f"实现改进：{data.get('requested_changes') or '按确认目标修改'}",
            "仅修改目标所需文件，不重新初始化项目",
            "仅在当前官方 API 要求时升级 Agent SDK 依赖",
            "运行原有测试和一条针对改进目标的最小回归检查",
            "审查 diff，并输出逐 URL 与逐 demo 引用账本",
        ]
        action = "改进"
    else:
        files = (["package.json", "tsconfig.json", "src/index.ts"] if lang == "TypeScript" else ["pyproject.toml", "src/main.py"]) + [".env.example", ".gitignore", "README.md"]
        items = [
            f"在 {target} 初始化 {lang} 项目",
            f"使用 {data.get('tooling')} 安装最新稳定 Agent SDK",
            *[f"实现：{x}" for x in data.get("capabilities", [])],
            f"创建文件：{', '.join(files)}",
            "运行类型/语法检查与最小 smoke test",
            "输出逐 URL 与逐 demo 引用账本",
        ]
        action = "创建"
    rows = "".join(f'<label class="item"><input type="checkbox" checked value="{escape(x)}"><span>{escape(x)}</span></label>' for x in items)
    session = os.environ.get("TERM_SESSION_ID", "unknown")
    html = TEMPLATE.replace("__ROWS__", rows).replace("__COUNT__", str(len(items))).replace("__PROJECT__", PROJECT).replace("__SESSION_HTML__", escape(session)).replace("__SESSION_JSON__", json.dumps(session)).replace("__DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/")).replace("__ACTION__", action)
    output = Path("/tmp/my-agent-sdk-plan-review.html")
    output.write_text(html, encoding="utf-8")
    print(output)


TEMPLATE = r'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>my-agent-sdk 计划确认</title><style>*{box-sizing:border-box}body{margin:0;background:#f7f5ee;color:#1d1c18;font:16px/1.55 Georgia,serif}main{max-width:850px;margin:auto;padding:50px 22px 110px}h1,button{font-family:system-ui,sans-serif}h1{font-size:clamp(32px,6vw,58px);line-height:1.05}.item{display:flex;gap:12px;padding:15px;background:#fff;border:1px solid #ddd7c8;border-radius:10px;margin:9px 0}textarea{width:100%;min-height:90px;padding:12px;border:1px solid #c9c1af;border-radius:8px;font:inherit}footer{position:fixed;bottom:0;left:0;right:0;padding:14px;display:flex;gap:10px;justify-content:center;background:#f7f5eef2;border-top:1px solid #ddd7c8}button{border:0;border-radius:8px;padding:12px 17px;font-weight:700;cursor:pointer}.primary{background:#d16745;color:#fff}.secondary{background:#222622;color:#fff}.meta{font:12px/1.5 ui-monospace,monospace;color:#756f62;word-break:break-all;border-top:1px solid #ddd7c8;padding-top:15px}</style></head><body><main><p>MY-AGENT-SDK · __ACTION__实施门</p><h1>确认范围，再开始__ACTION__。</h1><p>取消勾选会从计划中移除；导出后 Pi 才会修改项目。</p><section>__ROWS__</section><label>补充要求<textarea id="notes" placeholder="例如：不要升级 React；必须保持现有 CLI 参数"></textarea></label><p id="status">已选择 __COUNT__ 项。</p><p class="meta">来源项目：my-agent-sdk · 绝对路径：__PROJECT__ · Pi session ID：__SESSION_HTML__</p></main><footer><button class="secondary" id="copy">复制确认提示词</button><button class="primary" id="export">导出并开始__ACTION__</button></footer><script>
const base=__DATA__,boxes=[...document.querySelectorAll('.item input')],status=document.querySelector('#status');function out(){return {...base,approved:true,approved_plan:boxes.filter(x=>x.checked).map(x=>x.value),plan_notes:document.querySelector('#notes').value,session_id:__SESSION_JSON__}}function render(){status.textContent=`已选择 ${boxes.filter(x=>x.checked).length} 项。`}boxes.forEach(x=>x.onchange=render);document.querySelector('#export').onclick=()=>{const b=new Blob([JSON.stringify(out(),null,2)],{type:'application/json'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download=`my-agent-sdk-${base.operation||'create'}-approved-plan.json`;a.click();URL.revokeObjectURL(u);status.textContent='计划已导出。回到 Pi，告诉我“开始”。'};document.querySelector('#copy').onclick=async()=>{await navigator.clipboard.writeText('开始。已确认计划：\n```json\n'+JSON.stringify(out(),null,2)+'\n```');status.textContent='已复制确认提示词。'};</script></body></html>'''

if __name__ == "__main__":
    main()
