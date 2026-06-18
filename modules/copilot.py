def copilot_decision(alpha_score: float, risk_label: str, confirmation: bool) -> dict:
    if alpha_score >= 80 and risk_label != "HIGH" and confirmation:
        action = "CONSIDER_ENTRY"
    elif alpha_score >= 65:
        action = "WAIT_FOR_CONFIRMATION"
    else:
        action = "AVOID"
    return {
        "action": action,
        "alpha_score": alpha_score,
        "risk": risk_label,
        "confirmation": confirmation,
    }
