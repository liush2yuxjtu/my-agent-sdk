#!/usr/bin/env python3
"""Refresh both URL source packs in place. No arguments."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "references" / "source-packs.json"
UA = {"User-Agent": "my-agent-sdk-source-refresh"}


def fetch(url: str) -> str:
    return urlopen(Request(url, headers=UA), timeout=30).read().decode("utf-8", "ignore")


def docs(pack: dict) -> list[str]:
    page = fetch(pack["index_url"])
    prefix = pack["url_prefix"]
    found = set()
    for href in re.findall(r'href=["\']([^"\']+)', page):
        if not (href.startswith("/docs/zh-CN/agent-sdk/") or href.startswith(prefix)):
            continue
        url = urljoin(pack["index_url"], href).split("#", 1)[0].split("?", 1)[0]
        if url.startswith(prefix) and not url.endswith(".md"):
            found.add(url.rstrip("/"))
    if not found:
        raise RuntimeError("官方文档入口未发现 Agent SDK 子页面")
    return sorted(found)


def demos(pack: dict) -> list[str]:
    template = pack["project_url_template"]
    try:
        entries = json.loads(fetch(pack["contents_api_url"]))
        projects = sorted(x["name"] for x in entries if x.get("type") == "dir" and not x["name"].startswith("."))
    except Exception:
        readme = fetch(pack["readme_url"])
        projects = sorted(set(re.findall(r"\]\(\./([a-z0-9][a-z0-9-]+)\)", readme)))
    if not projects:
        raise RuntimeError("Demo 仓库未发现项目目录")
    return [template.format(project=name) for name in projects]


def main() -> None:
    data = json.loads(TARGET.read_text(encoding="utf-8"))
    packs = data["packs"]
    errors = []
    for name, loader in (("agent_sdk_docs", docs), ("agent_sdk_demos", demos)):
        try:
            packs[name]["urls"] = loader(packs[name])
        except Exception as exc:
            errors.append(f"{name}: {exc}")
    data["refreshed_at"] = datetime.now(timezone.utc).isoformat()
    data["refresh_errors"] = errors
    TARGET.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"docs={len(packs['agent_sdk_docs']['urls'])} demos={len(packs['agent_sdk_demos']['urls'])}")
    if errors:
        print("保留失败来源的上一份快照：" + " | ".join(errors))


if __name__ == "__main__":
    main()
