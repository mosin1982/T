def capital_preservation(drawdown_pct: float, open_risk_pct: float) -> dict:
    if drawdown_pct >= 10 or open_risk_pct >= 6:
        return {"status": "DEFENSIVE", "recommendation": "Reduce position size by 50% and stop new trades."}
    if drawdown_pct >= 5 or open_risk_pct >= 3:
        return {"status": "CAUTION", "recommendation": "Reduce position size by 25%."}
    return {"status": "NORMAL", "recommendation": "Risk level acceptable."}
