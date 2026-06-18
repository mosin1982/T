def rebalance_hint(health_score: float) -> str:
    if health_score < 45:
        return "Portfolio is concentrated. Consider reducing oversized exposure."
    if health_score < 70:
        return "Portfolio is moderate. Review correlation and hedge risk."
    return "Portfolio structure is healthy."
