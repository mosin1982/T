from datetime import datetime, timezone

def source_trust_score(source: str) -> int:
    source = source.lower()
    if source in {"binance", "nse", "zerodha", "dhan", "bybit", "okx"}:
        return 90
    if source in {"twitter", "x", "reddit", "telegram"}:
        return 45
    return 30

def validate_market_tick(tick: dict) -> dict:
    issues = []
    if float(tick.get("price", 0)) <= 0:
        issues.append("invalid_price")
    if float(tick.get("volume", 0)) < 0:
        issues.append("invalid_volume")
    if "asset" not in tick:
        issues.append("missing_asset")

    return {
        "valid": not issues,
        "issues": issues,
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }

def freshness_score(age_seconds: float) -> int:
    if age_seconds <= 5:
        return 100
    if age_seconds <= 60:
        return 80
    if age_seconds <= 300:
        return 50
    return 10
