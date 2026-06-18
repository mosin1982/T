# T Real-World Mode

Real-World Mode connects to Binance public market data.

## Important

This mode uses public market data only. It does not place real trades.

## Run WebSocket Mode

```bash
cp .env.example .env
python t_cli.py real-binance --symbol btcusdt --threshold 3.0
```

## Docker

```bash
cp .env.example .env
docker compose --profile real up --build t-real-binance
```

## Telegram Optional

Set in `.env`:

```bash
TELEGRAM_ENABLED=true
TELEGRAM_BOT_TOKEN=your_token
TELEGRAM_CHAT_ID=your_chat
```

## Safety

Real-world mode is observation only. It is not financial advice and does not execute live orders.
