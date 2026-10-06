# brag-codex

Codex skill `/brag` (skills/brag/) that turns a project into a launch video with Hyperframes, plus per-step pipeline agents (agents/).

## Save context: delegate

- Lookups across files → `scout` agent (haiku). Don't read whole files yourself to find something.
- Noisy commands (validators, `npx hyperframes …`, scripts) → `runner` agent (haiku); you get pass/fail + error lines.
- Decided, mechanical multi-file edits → `mechanic` agent (sonnet).
- Do small single-file reads/edits yourself; spawning costs more than it saves.

## Rules

- Never read media (`*.mp3`, `*.wav`, `*.mp4`, `*.png`, `*.jpg`) or `uv.lock`.
- `agents/codex/*.toml` is the source of truth; regenerate Claude versions with `python3 agents/sync.py` (`--check` to verify).
- Skill validator: `uv run --with pyyaml python ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/brag`.
