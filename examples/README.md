# Examples

| Example | What it demonstrates |
|---|---|
| `minimal-run/` | one card through all four gates |
| `multi-card/` | three sequential cards, each gated independently |
| `decision/` | Decision request -> independent approval -> replay |
| `rollback/` | Shadow -> Lite -> Shadow with an append-only ledger |
| `two-seat-handoff/` | producer handoff + independent reviewer join |

All examples are self-contained and clean up their temporary files.

Run them directly:

```bash
python3 examples/minimal-run/run_demo.py
python3 examples/multi-card/run_demo.py
python3 examples/decision/run_demo.py
python3 examples/rollback/run_demo.py
python3 examples/two-seat-handoff/run_demo.py
```
