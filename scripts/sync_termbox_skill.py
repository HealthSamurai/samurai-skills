#!/usr/bin/env python3
"""Copy the Termbox agent prompts and MCP page from the published docs into the termbox skill.

The docs at https://www.health-samurai.io/docs/termbox/agents are the source of truth.
Run this after the prompts change, then bump the plugin versions:

    python3 scripts/sync_termbox_skill.py
"""
import re
import urllib.request
from pathlib import Path

BASE = "https://www.health-samurai.io/docs/termbox/"
PAGES = {
    "start-local.md": "agents/start-local.md",
    "gallery.md": "agents/gallery.md",
    "packages.md": "agents/packages.md",
    "add-content.md": "agents/add-content.md",
    "update-versions.md": "agents/update-versions.md",
    "kubernetes.md": "agents/kubernetes.md",
    "query.md": "agents/query.md",
    "connect-mcp.md": "agents/connect-mcp.md",
    "troubleshoot.md": "agents/troubleshoot.md",
    "mcp.md": "mcp.md",
}
ROOT = Path(__file__).resolve().parent.parent
TARGETS = [
    ROOT / "plugins/termbox/skills/termbox/references",
    ROOT / "plugins/samurai-skills/skills/termbox/references",
]


def fetch(path):
    with urllib.request.urlopen(BASE + path, timeout=60) as r:
        return r.read().decode("utf-8")


def strip_banner(text):
    # The site prepends "> For the complete documentation index ... ---" to every .md page.
    if text.startswith("> "):
        head, sep, rest = text.partition("\n---\n")
        if sep:
            return rest.lstrip("\n")
    return text


def fix_links(text, source):
    def repl(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"[a-z]+:", target) or target.startswith("#"):
            return m.group(0)
        path, _, anchor = target.partition("#")
        resolved = str(Path(source).parent / path)
        resolved = re.sub(r"[^/]+/\.\./", "", resolved).lstrip("./")
        name = resolved.split("/")[-1]
        if resolved.startswith("agents/") and name in PAGES or resolved == "mcp.md":
            new = name  # sibling reference file inside the skill
        else:
            published = re.sub(r"/README\.md$", ".md", resolved)
            new = BASE + published
        return f"[{label}]({new}{'#' + anchor if anchor else ''})"

    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", repl, text)


def main():
    for name, source in PAGES.items():
        text = fix_links(strip_banner(fetch(source)), source)
        for target in TARGETS:
            target.mkdir(parents=True, exist_ok=True)
            (target / name).write_text(text, encoding="utf-8")
        print(f"synced {name}")


if __name__ == "__main__":
    main()
