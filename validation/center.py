from dataclasses import dataclass

@dataclass
class SignalOutcome:
    signal_id: str
    asset: str
    alpha_score: float
    entry_price: float
    outcome_price: float
    side: str = "LONG"

    def result(self) -> dict:
        direction = 1 if self.side.upper() == "LONG" else -1
        pnl_pct = ((self.outcome_price - self.entry_price) / self.entry_price) * 100 * direction
        return {
            "signal_id": self.signal_id,
            "asset": self.asset,
            "alpha_score": self.alpha_score,
            "pnl_pct": round(pnl_pct, 2),
            "result": "WIN" if pnl_pct > 0 else "LOSS",
        }

def accuracy_report(outcomes: list[SignalOutcome]) -> dict:
    results = [o.result() for o in outcomes]
    wins = [r for r in results if r["result"] == "WIN"]
    return {
        "signals": len(results),
        "wins": len(wins),
        "win_rate_pct": round(len(wins) / len(results) * 100, 2) if results else 0,
        "results": results,
    }
