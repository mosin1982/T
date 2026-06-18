# GitHub Demo Quickstart

## 60-Second Demo

```bash
git clone <your-repo-url>
cd T
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python t_cli.py demo
```

## Docker Demo

```bash
docker compose up --build t-demo
```

## Real Market Observation

```bash
cp .env.example .env
python t_cli.py real-binance --symbol btcusdt
```

## What This Proves

- The project runs
- No API key is required for demo
- Paper trading works
- Real public market stream works
- Alerts are explainable
