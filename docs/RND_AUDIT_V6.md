# T R&D Audit v6

## Problems Found and Solved

1. Demo docker service depended on `.env.example`; fixed to run without env.
2. `asyncio` was listed as a dependency even though it is Python standard library; removed.
3. Real-world mode had no clean smoke-test exit; added `--max-runtime`.
4. Event sourcing was roadmap-only; added lightweight JSONL event store.
5. CI Python path could fail in some runners; added `pythonpath = ["."]`.
6. Public launch needed clearer limitation boundaries; docs and disclaimers retained.

## Current Reality

T v6 is strong for:
- GitHub demo
- Paper trading demo
- Public Binance observation
- Explainable alerts
- Event logging foundation
- Docker demo

Still not production-live-trading ready:
- No live order execution
- No broker auth layer
- No slippage model
- No exchange-specific risk controls
- No certified financial-advice compliance layer
- No full backtest engine yet

## Next Engineering Hardening

1. Backtest engine with historical replay.
2. Slippage + fees model.
3. Strategy configuration system.
4. SQLite/Postgres event store option.
5. Dashboard screenshot/demo video.
6. CI secret scanning with gitleaks action.
