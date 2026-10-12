#!/usr/bin/env python3
"""扫描当前目录下的 HTML 文件，提取元数据并生成 pages.json。"""
import json
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent
EXCLUDED = {"index.html", "template.html"}

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
DESC_RE = re.compile(
    r'<meta[^>]*name=["\']description["\'][^>]*content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
DATE_RE = re.compile(
    r'<meta[^>]*name=["\']date["\'][^>]*content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
TAGS_RE = re.compile(
    r'<meta[^>]*name=["\']tags["\'][^>]*content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)


def parse_page(path: Path) -> dict:
    html = path.read_text(encoding="utf-8")

    title_match = TITLE_RE.search(html)
    title = title_match.group(1).strip() if title_match else path.stem

    desc_match = DESC_RE.search(html)
    description = desc_match.group(1).strip() if desc_match else ""

    date_match = DATE_RE.search(html)
    date = date_match.group(1).strip() if date_match else ""

    tags_match = TAGS_RE.search(html)
    tags = []
    if tags_match:
        tags = [t.strip() for t in tags_match.group(1).split(",") if t.strip()]

    if not date:
        mtime = path.stat().st_mtime
        date = datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")

    return {
        "file": path.name,
        "title": title,
        "description": description,
        "date": date,
        "tags": tags,
    }


def main():
    pages = [
        parse_page(p)
        for p in sorted(ROOT.glob("*.html"))
        if p.name not in EXCLUDED
    ]
    pages.sort(key=lambda x: x["date"], reverse=True)

    output = ROOT / "pages.json"
    output.write_text(
        json.dumps(pages, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Updated {output} with {len(pages)} page(s).")


if __name__ == "__main__":
    main()
