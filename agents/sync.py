#!/usr/bin/env python3
"""Regenerate agents/claude/*.md from agents/codex/*.toml (the source of truth)."""
import pathlib
import re
import sys
import tomllib

ROOT = pathlib.Path(__file__).resolve().parent
ALLOWED = {"name", "description", "model_reasoning_effort", "sandbox_mode", "developer_instructions"}
TOOLS = {
    "brag-inspector": "Read, Glob, Grep, Write, Bash",
    "brag-planner": "Read, Glob, Grep, Write, Edit",
    "brag-composer": "Read, Glob, Grep, Write, Edit, Bash",
    "brag-deliverer": "Read, Glob, Grep, Write, Edit, Bash",
}

check = "--check" in sys.argv
stale = []
for src in sorted((ROOT / "codex").glob("*.toml")):
    data = tomllib.loads(src.read_text())
    unknown = set(data) - ALLOWED
    if unknown:
        sys.exit(f"{src.name}: unknown keys {sorted(unknown)}")
    name = src.stem
    body = data["developer_instructions"].strip()
    body = body.replace(
        "${CODEX_HOME:-~/.codex}/skills/brag/`",
        "~/.claude/skills/brag/` (or `.claude/skills/brag/` in the project)",
    )
    body = re.sub(r"brag_(inspector|planner|composer|deliverer)", r"brag-\1", body)
    body = body.replace("If it is blocked by the sandbox", "If it is blocked")
    desc = data["description"].replace('"', '\\"')
    out = f'---\nname: {name}\ndescription: "{desc}"\ntools: {TOOLS[name]}\n---\n\n{body}\n'
    dst = ROOT / "claude" / f"{name}.md"
    if dst.exists() and dst.read_text() == out:
        continue
    stale.append(dst.name)
    if not check:
        dst.write_text(out)

if check and stale:
    sys.exit(f"out of sync: {', '.join(stale)} (run python3 agents/sync.py)")
print("in sync" if not stale else f"updated: {', '.join(stale)}")
