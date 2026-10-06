# brag agents

Four subagents, one per `/brag` step. The same instructions ship in two formats:

- `codex/*.toml` — Codex custom agents (`~/.codex/agents/` or `.codex/agents/`)
- `claude/*.md` — Claude Code subagents (`~/.claude/agents/` or `.claude/agents/`)

| Agent | Step | Reads | Writes (in `<output-dir>/`) |
|---|---|---|---|
| inspector | 1. Inspect | project code | `project-notes.md` (9-question rubric, palette, fonts, verbatim copy) |
| planner | 2. Plan | `project-notes.md` | `brag-plan.md` (angle, hook, 15–25s storyboard, audio) |
| composer | 3. Compose | notes + plan | `composition-brief.md`, `composition/` (lint-clean) |
| deliverer | 4. Deliver | `composition/` | `share-copy.txt`, `brag.mp4` (only when render is approved) |

The orchestrating `/brag` skill runs them in order, checks each gate, and owns the user-facing preview/approval step. Each agent reads its step's reference from the installed brag skill, so the `skills/brag/references/` files stay the single source of truth.

Keep both formats in sync when editing: the Claude files are the Codex `developer_instructions` with Claude paths (`~/.claude/skills/brag/`) and hyphenated names.
