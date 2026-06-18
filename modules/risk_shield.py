def risk_grade(alpha_score: float, volatility_score: float, macro_risk: float) -> dict:
    risk = (volatility_score * 0.45) + (macro_risk * 0.35) + ((100 - alpha_score) * 0.20)
    if risk >= 75:
        label = "HIGH"
        suggested_risk = "0.25% - 0.50%"
    elif risk >= 50:
        label = "MEDIUM"
        suggested_risk = "0.50% - 1.00%"
    else:
        label = "LOW"
        suggested_risk = "1.00% - 2.00%"
    return {"risk_score": round(risk, 2), "risk_label": label, "suggested_risk": suggested_risk}
