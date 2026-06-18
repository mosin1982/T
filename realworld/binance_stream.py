import asyncio
import json
import os
import time
import urllib.request
from collections import deque
from typing import Optional

from alerts.formatter import format_console_alert, format_telegram_alert
from alerts.telegram import send_telegram_message
from modes.scoring import Signal, alpha_score, build_explanation, risk_label, z_score

try:
    import websockets
except ImportError:  # pragma: no cover
    websockets = None

PUBLIC_REST_URL = "https://api.binance.com/api/v3/trades?symbol={symbol}&limit=1000"

class BinancePublicStream:
    """Observation-only Binance public market stream.

    This class never places orders and never requires exchange API secrets.
    """

    def __init__(
        self,
        symbol: str = "btcusdt",
        threshold: float = 3.0,
        telegram: bool = False,
        cooldown_seconds: int = 300,
        max_runtime_seconds: Optional[int] = None,
    ):
        self.symbol = symbol.lower()
        self.threshold = threshold
        self.telegram = telegram
        self.cooldown_seconds = cooldown_seconds
        self.max_runtime_seconds = max_runtime_seconds
        self.minute_volumes = deque(maxlen=50)
        self.current_minute = None
        self.current_volume = 0.0
        self.last_price = 0.0
        self.last_alert_ts = 0.0

    async def run(self) -> None:
        if websockets is None:
            raise RuntimeError("Install websockets or run REST polling mode.")
        url = f"wss://stream.binance.com:9443/ws/{self.symbol}@aggTrade"
        print(f"[T Real-World Mode] Binance public WebSocket online: {self.symbol.upper()}")
        started = time.time()

        while True:
            if self.max_runtime_seconds and time.time() - started >= self.max_runtime_seconds:
                print("[T Real-World Mode] max runtime reached. Exiting cleanly.")
                return

            try:
                async with websockets.connect(url, ping_interval=20, ping_timeout=20) as ws:
                    async for message in ws:
                        self.process_message(message)
                        if self.max_runtime_seconds and time.time() - started >= self.max_runtime_seconds:
                            print("[T Real-World Mode] max runtime reached. Exiting cleanly.")
                            return
            except Exception as exc:
                print(f"[stream] reconnecting after error: {exc}")
                await asyncio.sleep(3)

    def process_message(self, message: str) -> None:
        data = json.loads(message)
        price = float(data["p"])
        volume = float(data["q"])
        event_time_ms = int(data["T"])
        self.process_tick(price, volume, event_time_ms)

    def process_tick(self, price: float, volume: float, event_time_ms: int) -> Optional[Signal]:
        minute = event_time_ms // 60000
        self.last_price = price
        if self.current_minute is None:
            self.current_minute = minute

        if minute == self.current_minute:
            self.current_volume += volume
            return None

        completed_volume = self.current_volume
        z = z_score(completed_volume, list(self.minute_volumes))
        alpha = alpha_score(
            z=z,
            oi_score=50,
            sentiment_score=50,
            structure_score=65 if price > 0 else 50,
            whale_score=0,
            liquidation_score=0,
        )

        signal = None
        if z >= self.threshold and time.time() - self.last_alert_ts > self.cooldown_seconds:
            risk = risk_label(alpha, z)
            explanation = build_explanation(z, alpha, 50, 50)
            signal = Signal(
                asset=self.symbol.upper(),
                price=price,
                z_score=z,
                alpha_score=alpha,
                risk_label=risk,
                direction="LONG_OBSERVATION",
                explanation=explanation,
            )
            print(format_console_alert(signal))
            if self.telegram:
                send_telegram_message(format_telegram_alert(signal))
            self.last_alert_ts = time.time()

        self.minute_volumes.append(completed_volume)
        self.current_volume = volume
        self.current_minute = minute
        return signal

def rest_poll_once(symbol: str = "BTCUSDT") -> dict:
    """Public no-key REST fallback for basic connectivity testing."""
    url = PUBLIC_REST_URL.format(symbol=symbol.upper())
    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.loads(response.read().decode("utf-8"))
    last = data[-1]
    return {"symbol": symbol.upper(), "price": float(last["price"]), "qty": float(last["qty"]), "trades": len(data)}

async def main() -> None:
    symbol = os.getenv("BINANCE_SYMBOL", "btcusdt")
    threshold = float(os.getenv("Z_SCORE_THRESHOLD", "3.0"))
    telegram = os.getenv("TELEGRAM_ENABLED", "false").lower() == "true"
    await BinancePublicStream(symbol=symbol, threshold=threshold, telegram=telegram).run()

if __name__ == "__main__":
    asyncio.run(main())
