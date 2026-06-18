from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    telegram_bot_token: str = os.getenv("TELEGRAM_BOT_TOKEN", "")
    telegram_chat_id: str = os.getenv("TELEGRAM_CHAT_ID", "")
    binance_symbol: str = os.getenv("BINANCE_SYMBOL", "btcusdt")
    z_score_threshold: float = float(os.getenv("Z_SCORE_THRESHOLD", "3.0"))
    app_env: str = os.getenv("APP_ENV", "development")

settings = Settings()
