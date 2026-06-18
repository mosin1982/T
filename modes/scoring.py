import statistics
from dataclasses import dataclass


@dataclass
class Signal:
    asset: str
    price: float
    z_score: float
    alpha_score: float
    risk_label: str
    direction: str
    explanation: str


def clamp(value: float, low: float = 0.0, high: float = 100.0) -> float:
    return max(low, min(high, value))


def z_score(current_volume: float, history: list[float]) -> float:
    if len(history) < 3:
        return 0.0
    mean = statistics.mean(history)
    std = statistics.pstdev(history)
    if std == 0:
        return 0.0
    return (current_volume - mean) / std


def alpha_score(
    z: float,
    oi_score: float,
    sentiment_score: float,
    structure_score: float,
    whale_score: float = 0.0,
    liquidation_score: float = 0.0,
) -> float:
    volume_score = clamp(z * 25.0)
    score = (
        volume_score * 0.30
        + structure_score * 0.20
        + oi_score * 0.20
        + sentiment_score * 0.15
        + whale_score * 0.10
        + liquidation_score * 0.05
    )
    return round(clamp(score), 2)


def risk_label(alpha: float, z: float) -> str:
    if z > 5:
        return "HIGH"
    if alpha >= 75:
        return "LOW"
    if alpha >= 55:
        return "MEDIUM"
    return "HIGH"


def build_explanation(z: float, alpha: float, oi_score: float, sentiment_score: float) -> str:
    reasons = []
    if z >= 3:
        reasons.append(f"Volume anomaly confirmed with Z-score {z:.2f}.")
    if alpha >= 75:
        reasons.append(f"T Alpha Score strong at {alpha}/100.")
    if oi_score >= 70:
        reasons.append("Open interest proxy is supportive.")
    if sentiment_score >= 65:
        reasons.append("Sentiment proxy is positive.")
    if not reasons:
        reasons.append("No high-conviction setup detected.")
    reasons.append("This is research output, not financial advice.")
    return " ".join(reasons)
