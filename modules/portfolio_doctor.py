def portfolio_health(positions: list[dict]) -> dict:
    total = sum(float(p.get("value", 0)) for p in positions)
    if total <= 0:
        return {"health_score": 0, "risk": "UNKNOWN", "message": "No portfolio value found."}
    largest = max(float(p.get("value", 0)) for p in positions)
    concentration = largest / total
    health = max(0, 100 - concentration * 100)
    risk = "HIGH" if concentration > 0.55 else "MEDIUM" if concentration > 0.35 else "LOW"
    return {"health_score": round(health, 2), "risk": risk, "largest_position_pct": round(concentration * 100, 2)}
