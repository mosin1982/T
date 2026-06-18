def clamp(value: float, low: float = 0, high: float = 100) -> float:
    return max(low, min(high, value))


def t_alpha_score(
    volume_score: float,
    structure_score: float,
    oi_score: float,
    sentiment_score: float,
    whale_score: float = 0,
    liquidation_score: float = 0,
) -> float:
    score = (
        volume_score * 0.30
        + structure_score * 0.20
        + oi_score * 0.20
        + sentiment_score * 0.15
        + whale_score * 0.10
        + liquidation_score * 0.05
    )
    return clamp(score)
