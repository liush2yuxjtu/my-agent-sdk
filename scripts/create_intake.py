#!/usr/bin/env python3
"""Generate the citation-driven my-agent-sdk intake HTML."""
from argparse import ArgumentParser
from html import escape
from pathlib import Path
import json

PROJECT = "/Users/liushiyuwin/.pi/agent/skills/my-agent-sdk"
DOCS = [
    ("overview", "Agent SDK 概览", "产品边界与核心能力", "core"),
    ("quickstart", "快速开始", "TypeScript/Python 最小入口", "core"),
    ("agent-loop", "代理循环", "消息生命周期、工具执行和上下文", "core"),
    ("typescript", "TypeScript SDK", "TypeScript API 与类型", "language"),
    ("python", "Python SDK", "Python API 与类型", "language"),
    ("user-input", "处理用户输入", "AskUserQuestion 与交互往返", "interaction"),
    ("streaming-output", "流式输出", "实时文本、工具调用与最终结果", "interaction"),
    ("streaming-vs-single-mode", "流式与单次模式", "输入模式选择", "interaction"),
    ("sessions", "使用会话", "continue、resume 与 fork", "state"),
    ("session-storage", "会话存储", "会话持久化", "state"),
    ("structured-outputs", "结构化输出", "受 schema 约束的结果", "interaction"),
    ("custom-tools", "自定义工具", "进程内 MCP 工具与 schema", "tools"),
    ("mcp", "MCP", "连接外部 MCP 服务器", "tools"),
    ("permissions", "权限", "权限模式与 allow/deny", "safety"),
    ("hooks", "Hooks", "工具调用生命周期拦截", "safety"),
    ("subagents", "子代理", "专门代理与委派", "tools"),
    ("skills", "Skills", "代理技能加载", "tools"),
    ("plugins", "Plugins", "插件扩展", "tools"),
    ("file-checkpointing", "文件检查点", "文件变更回退", "production"),
    ("hosting", "托管", "部署拓扑与运行环境", "production"),
    ("secure-deployment", "安全部署", "生产安全边界", "production"),
    ("observability", "可观测性", "日志、指标与追踪", "production"),
    ("cost-tracking", "成本追踪", "用量与成本", "production"),
    ("typescript-v2-preview", "TypeScript V2 预览", "实验性 Session API", "experimental"),
]
DEMOS = [
    ("hello-world", "最小 query()、消息迭代、cwd 与工具白名单", "minimal"),
    ("hello-world-v2", "实验性 V2 send()/stream()、多轮与恢复", "sessions"),
    ("ask-user-question-previews", "AskUserQuestion 经 WebSocket 阻塞往返与 HTML 预览", "ask"),
    ("simple-chatapp", "React + Express + WebSocket 流式聊天环", "streaming"),
    ("research-agent", "Lead/Researcher/Analyst/Writer 子代理编排与 hooks", "subagents"),
    ("email-agent", "IMAP 邮件业务代理；仅本地演示", "business"),
    ("excel-demo", "Electron 桌面端与表格代理集成", "desktop"),
    ("resume-generator", "WebSearch + docx 生成的单任务代理", "business"),
]


def main() -> None:
    p = ArgumentParser()
    p.add_argument("--output", required=True)
    p.add_argument("--session-id", default="unknown")
    a = p.parse_args()
    html = (TEMPLATE.replace("__SESSION_HTML__", escape(a.session_id))
            .replace("__SESSION_JSON__", json.dumps(a.session_id))
            .replace("__PROJECT__", PROJECT)
            .replace("__DOCS__", json.dumps([
                {"slug": s, "title": t, "description": d, "group": g,
                 "url": f"https://code.claude.com/docs/zh-CN/agent-sdk/{s}"}
                for s, t, d, g in DOCS], ensure_ascii=False))
            .replace("__DEMOS__", json.dumps([
                {"project": n, "description": d, "tag": tag,
                 "url": f"https://github.com/anthropics/claude-agent-sdk-demos/tree/main/{n}"}
                for n, d, tag in DEMOS], ensure_ascii=False)))
    Path(a.output).write_text(html, encoding="utf-8")
    print(Path(a.output).resolve())


TEMPLATE = r'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>my-agent-sdk · 引用驱动配置台</title><style>
*{box-sizing:border-box}body{margin:0;background:#faf9f5;color:#171713;font:15px/1.55 Georgia,"Noto Serif SC",serif}main{max-width:1180px;margin:auto;padding:34px 22px 120px}h1,h2,h3,button,th,.chip,.tab{font-family:ui-sans-serif,system-ui,sans-serif}h1{font-size:clamp(34px,6vw,68px);line-height:.95;letter-spacing:-.04em;margin:8px 0 14px}.lede{max-width:75ch;color:#676258;font-size:18px}.topbar{display:flex;gap:8px;flex-wrap:wrap;margin:24px 0}.tab{border:1px solid #ddd7c9;background:white;color:#24231f;border-radius:99px;padding:9px 14px;cursor:pointer}.tab.active{background:#1c1c19;color:#fff}.panel{background:white;border:1px solid #e2ddd1;border-radius:10px;padding:20px;margin:16px 0;box-shadow:0 2px 8px #211a0b0a}.formgrid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px}.wide{grid-column:1/-1}label>span{display:block;font:700 13px system-ui,sans-serif;margin-bottom:6px}input[type=text],textarea,select{width:100%;border:1px solid #ccc5b6;border-radius:7px;padding:10px 11px;background:#fff;font:inherit}textarea{min-height:82px;resize:vertical}input:focus,textarea:focus,select:focus{outline:3px solid #d9775728;border-color:#d97757}.capgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}.cap{border:1px solid #ddd7c9;border-radius:7px;padding:10px;background:#fbfaf6}.cap:has(input:checked){border-color:#d16d4c;background:#fff3ed}.cap input{accent-color:#d16d4c}.section-head{display:flex;justify-content:space-between;gap:14px;align-items:end;margin-top:28px}.section-head p{margin:0;color:#777166}.badge{font:700 12px system-ui,sans-serif;background:#ece8de;border-radius:99px;padding:5px 9px;white-space:nowrap}table{width:100%;border-collapse:collapse;background:white;border-radius:9px;overflow:hidden;border:1px solid #e1dbce}th{background:#1b1b18;color:#faf9f5;padding:11px;text-align:left;font-size:13px}td{padding:11px;border-bottom:1px solid #ece8de;vertical-align:top}tr:nth-child(even) td{background:#fbfaf6}tr:hover td{background:#f5f1e9}.cite-title{font-weight:700}.url{display:block;color:#a54b30;font:12px/1.45 ui-monospace,monospace;word-break:break-all;margin-top:3px}.desc{color:#666157}.toggle{position:relative;display:inline-block;width:44px;height:24px}.toggle input{opacity:0;width:0;height:0}.slider{position:absolute;inset:0;background:#aaa69c;border-radius:24px;cursor:pointer}.slider:before{content:"";position:absolute;width:18px;height:18px;left:3px;bottom:3px;background:#fff;border-radius:50%;transition:.15s}.toggle input:checked+.slider{background:#d16d4c}.toggle input:checked+.slider:before{transform:translateX(20px)}.req{display:grid;grid-template-columns:1fr auto;gap:8px;margin:8px 0}.delete{background:#eee9df;color:#6d3020}.summary{background:#1d211d;color:#f4efe4;border-radius:9px;padding:16px;white-space:pre-wrap;max-height:360px;overflow:auto;font:12px/1.55 ui-monospace,monospace}.warning{border-left:4px solid #d16d4c;padding:10px 14px;background:#fff4ee;color:#5d3326}.footerbar{position:fixed;bottom:0;left:0;right:0;background:#faf9f5ed;backdrop-filter:blur(10px);border-top:1px solid #ddd7c9;padding:13px 22px;display:flex;gap:10px;justify-content:center;align-items:center;z-index:5}.footerbar button{border:0;border-radius:7px;padding:11px 16px;font-weight:750;cursor:pointer}.primary{background:#d16d4c;color:#fff}.secondary{background:#1d211d;color:#fff}.status{color:#6c675d;font-size:13px}.provenance{border-top:1px solid #ddd7c9;padding-top:15px;color:#766f64;font:11px/1.5 ui-monospace,monospace;word-break:break-all}@media(max-width:850px){.formgrid{grid-template-columns:1fr 1fr}.capgrid{grid-template-columns:1fr 1fr}.citation-table th:nth-child(2),.citation-table td:nth-child(2){display:none}}@media(max-width:560px){.formgrid{grid-template-columns:1fr}.capgrid{grid-template-columns:1fr}.wide{grid-column:auto}.footerbar{flex-wrap:wrap}.status{width:100%;text-align:center}main{padding-bottom:160px}}
</style></head><body><main><p class="badge">MY-AGENT-SDK → NEW-AGENT-SDK</p><h1>用证据配置你的 Agent。</h1><p class="lede">先写项目意图，再勾选能力与引用。导出的 JSON 同时包含构建需求、官方文档逐 URL 账本和 Anthropic 示例逐项目账本。</p>
<div class="topbar"><button class="tab active" data-target="brief">① 项目</button><button class="tab" data-target="docs">② 官方文档</button><button class="tab" data-target="demos">③ 示例项目</button><button class="tab" data-target="export-section">④ 检查并导出</button></div>
<section class="panel" id="brief"><h2>项目需求</h2><div class="formgrid"><label><span>项目名</span><input id="project" type="text" placeholder="例如 support-agent"></label><label><span>语言</span><select id="language"><option>TypeScript</option><option>Python</option></select></label><label><span>包管理器</span><select id="tooling"><option>npm</option><option>pnpm</option><option>yarn</option><option>bun</option><option>uv</option><option>pip</option><option>poetry</option></select></label><label><span>代理类型</span><select id="agentType"><option>coding</option><option>business</option><option selected>custom use case</option></select></label><label><span>起点</span><select id="starting"><option>minimal</option><option>common features</option><option selected>use-case-specific</option></select></label><label><span>目标目录</span><input id="path" type="text" placeholder="例如 /Users/me/projects/support-agent"></label><label class="wide"><span>这个 Agent 要完成什么？</span><textarea id="usecase" placeholder="例如：在网页中接收退款咨询；必要时通过 AskUserQuestion 补充订单信息；流式返回处理进度。"></textarea></label></div><h3>能力（可多选）</h3><div class="capgrid" id="caps"></div><h3>补充要求</h3><div id="requirements"></div><button class="tab" id="addReq" type="button">＋ 添加一条要求</button></section>
<section id="docs"><div class="section-head"><div><h2>官方文档 · 逐 URL</h2><p>每个开关对应一个独立页面；能力选择会自动推荐相关页面。</p></div><span class="badge" id="docCount"></span></div><table class="citation-table"><thead><tr><th>页面与 URL</th><th>这页回答什么</th><th>纳入引用</th></tr></thead><tbody id="docBody"></tbody></table></section>
<section id="demos"><div class="section-head"><div><h2>Anthropic 示例 · 逐项目</h2><p>引用具体项目，不只引用仓库首页。</p></div><span class="badge" id="demoCount"></span></div><p class="warning"><strong>生产边界：</strong><a href="https://github.com/anthropics/claude-agent-sdk-demos#readme">仓库根 README</a> 明确说明这些项目仅供本地开发，不应直接部署到生产或规模化使用。</p><table class="citation-table"><thead><tr><th>项目与 URL</th><th>可借鉴的实现先例</th><th>纳入引用</th></tr></thead><tbody id="demoBody"></tbody></table></section>
<section class="panel" id="export-section"><h2>导出前检查</h2><p>导出后，<code>my-agent-sdk</code> 会把已回答需求交给 <code>new-agent-sdk</code>；后者仍负责当前文档核验、实现与验证。</p><pre class="summary" id="summary"></pre></section><p class="provenance">来源项目：my-agent-sdk · 绝对路径：__PROJECT__ · Pi session ID：__SESSION_HTML__</p></main><footer class="footerbar"><span class="status" id="status">请先填写项目名和用途。</span><button class="secondary" id="copy">复制为提示词</button><button class="primary" id="export">导出构建配置 JSON</button></footer>
<script>
const DOCS=__DOCS__,DEMOS=__DEMOS__,sessionId=__SESSION_JSON__;
const capabilities=[['streaming','流式输出'],['AskUserQuestion','AskUserQuestion'],['MCP','MCP'],['permissions','权限'],['sessions','会话'],['subagents','子代理'],['custom tools','自定义工具'],['structured outputs','结构化输出'],['hooks','Hooks'],['production hardening','生产加固']];
const mapDocs={streaming:['streaming-output','streaming-vs-single-mode','agent-loop'],AskUserQuestion:['user-input','permissions','agent-loop'],MCP:['mcp','custom-tools'],permissions:['permissions','hooks'],sessions:['sessions','session-storage'],subagents:['subagents','hooks'],['custom tools']:['custom-tools','mcp'],['structured outputs']:['structured-outputs'],hooks:['hooks'],['production hardening']:['hosting','secure-deployment','observability','cost-tracking']};
const mapDemos={streaming:['simple-chatapp'],AskUserQuestion:['ask-user-question-previews'],sessions:['hello-world-v2','simple-chatapp'],subagents:['research-agent'],hooks:['research-agent'],['custom tools']:['hello-world'],MCP:['hello-world'],['production hardening']:[]};
const capEl=document.querySelector('#caps');capabilities.forEach(([v,l])=>capEl.insertAdjacentHTML('beforeend',`<label class="cap"><input type="checkbox" value="${v}"> ${l}</label>`));
function citationRow(x,type){const key=type==='doc'?x.slug:x.project;return `<tr><td><span class="cite-title">${type==='doc'?x.title:x.project}</span><a class="url" href="${x.url}">${x.url}</a></td><td class="desc">${x.description}</td><td><label class="toggle"><input type="checkbox" data-kind="${type}" data-key="${key}"><span class="slider"></span></label></td></tr>`}
document.querySelector('#docBody').innerHTML=DOCS.map(x=>citationRow(x,'doc')).join('');document.querySelector('#demoBody').innerHTML=DEMOS.map(x=>citationRow(x,'demo')).join('');
function setChecked(kind,key,value=true){const x=document.querySelector(`input[data-kind="${kind}"][data-key="${key}"]`);if(x)x.checked=value}
['overview','quickstart','agent-loop'].forEach(x=>setChecked('doc',x));setChecked('demo','hello-world');
function recommend(){const selected=[...document.querySelectorAll('#caps input:checked')].map(x=>x.value);selected.forEach(c=>(mapDocs[c]||[]).forEach(x=>setChecked('doc',x)));selected.forEach(c=>(mapDemos[c]||[]).forEach(x=>setChecked('demo',x)));const lang=document.querySelector('#language').value;setChecked('doc',lang==='Python'?'python':'typescript');render()}
function addRequirement(value=''){const row=document.createElement('div');row.className='req';row.innerHTML=`<input type="text" value="${value.replaceAll('"','&quot;')}" placeholder="例如：30 秒超时；只允许只读工具"><button class="delete" type="button">删除</button>`;row.querySelector('input').oninput=render;row.querySelector('button').onclick=()=>{row.remove();render()};document.querySelector('#requirements').appendChild(row)}
addRequirement('不要写入真实 secret；.env 必须忽略');document.querySelector('#addReq').onclick=()=>addRequirement();
function selectedCitations(kind,data,key){const keys=[...document.querySelectorAll(`input[data-kind="${kind}"]:checked`)].map(x=>x.dataset.key);return data.filter(x=>keys.includes(x[key])).map(x=>({title:x.title||x.project,url:x.url,reason:x.description}))}
function data(){return{project_name:document.querySelector('#project').value.trim(),project_path:document.querySelector('#path').value.trim(),language:document.querySelector('#language').value,tooling:document.querySelector('#tooling').value,agent_type:document.querySelector('#agentType').value,starting_point:document.querySelector('#starting').value,use_case:document.querySelector('#usecase').value.trim(),capabilities:[...document.querySelectorAll('#caps input:checked')].map(x=>x.value),requirements:[...document.querySelectorAll('#requirements input')].map(x=>x.value.trim()).filter(Boolean),wrapper_chain:['my-agent-sdk','new-agent-sdk','agent-sdk-dev'],citations:{official_docs:selectedCitations('doc',DOCS,'slug'),demo_projects:selectedCitations('demo',DEMOS,'project'),demo_warning:'Anthropic demos are for local development only; do not deploy directly to production or at scale.'},session_id:sessionId}}
function render(){const d=data();document.querySelector('#summary').textContent=JSON.stringify(d,null,2);document.querySelector('#docCount').textContent=`已选 ${d.citations.official_docs.length} / ${DOCS.length}`;document.querySelector('#demoCount').textContent=`已选 ${d.citations.demo_projects.length} / ${DEMOS.length}`;document.querySelector('#status').textContent=d.project_name&&d.use_case?'配置完整，可以导出。':'请先填写项目名和用途。'}
function valid(){const d=data();if(!d.project_name){document.querySelector('#project').focus();return false}if(!d.use_case){document.querySelector('#usecase').focus();return false}return true}
document.querySelectorAll('input,textarea,select').forEach(x=>x.addEventListener('input',render));document.querySelector('#language').addEventListener('change',recommend);capEl.addEventListener('change',recommend);document.querySelectorAll('.toggle input').forEach(x=>x.addEventListener('change',render));
document.querySelectorAll('.tab[data-target]').forEach(b=>b.onclick=()=>{document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));b.classList.add('active');document.querySelector('#'+b.dataset.target).scrollIntoView({behavior:'smooth'})});
function blobExport(){if(!valid())return;const b=new Blob([JSON.stringify(data(),null,2)],{type:'application/json'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download='my-agent-sdk-build-intake.json';a.click();URL.revokeObjectURL(u);document.querySelector('#status').textContent='已导出。回到 Pi，告诉我“已完成”。'}
document.querySelector('#export').onclick=blobExport;document.querySelector('#copy').onclick=async()=>{if(!valid())return;await navigator.clipboard.writeText('请使用 my-agent-sdk，并将以下配置交给 new-agent-sdk：\n```json\n'+JSON.stringify(data(),null,2)+'\n```');document.querySelector('#status').textContent='已复制，可粘贴回 Pi。'};recommend();
</script></body></html>'''

if __name__ == "__main__":
    main()
