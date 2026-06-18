def institutional_probability(
    oi_surge: float, whale_score: float, funding_extreme: float, liquidation_cluster: float
) -> float:
    score = (
        oi_surge * 0.35 + whale_score * 0.30 + funding_extreme * 0.20 + liquidation_cluster * 0.15
    )
    return round(max(0, min(100, score)), 2)
