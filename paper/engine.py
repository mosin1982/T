from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class PaperTrade:
    trade_id: str
    asset: str
    side: str
    entry_price: float
    quantity: float
    risk_pct: float
    exit_price: float | None = None
    pnl: float = 0.0
    status: str = "OPEN"


@dataclass
class PaperAccount:
    starting_balance: float = 10000.0
    balance: float = 10000.0
    open_positions: list[PaperTrade] = field(default_factory=list)
    closed_trades: list[PaperTrade] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.balance = self.starting_balance

    def open_trade(
        self, asset: str, side: str, entry_price: float, risk_pct: float = 1.0
    ) -> PaperTrade:
        risk_amount = self.balance * (risk_pct / 100.0)
        quantity = risk_amount / max(
            entry_price * 0.01, 1e-9
        )  # Demo sizing: 1% stop distance assumption
        trade = PaperTrade(
            trade_id=str(uuid4()),
            asset=asset,
            side=side,
            entry_price=entry_price,
            quantity=quantity,
            risk_pct=risk_pct,
        )
        self.open_positions.append(trade)
        return trade

    def close_all(self, exit_price: float) -> None:
        for trade in list(self.open_positions):
            self.close_trade(trade.trade_id, exit_price)

    def close_trade(self, trade_id: str, exit_price: float) -> PaperTrade:
        trade = next(t for t in self.open_positions if t.trade_id == trade_id)
        direction = 1 if trade.side.upper() == "LONG" else -1
        trade.exit_price = exit_price
        trade.pnl = (exit_price - trade.entry_price) * trade.quantity * direction
        trade.status = "CLOSED"
        self.balance += trade.pnl
        self.open_positions.remove(trade)
        self.closed_trades.append(trade)
        return trade

    def summary(self) -> dict:
        wins = [t for t in self.closed_trades if t.pnl > 0]
        losses = [t for t in self.closed_trades if t.pnl <= 0]
        gross_profit = sum(t.pnl for t in wins)
        gross_loss = abs(sum(t.pnl for t in losses))
        profit_factor = (
            gross_profit / gross_loss if gross_loss else float("inf") if gross_profit else 0.0
        )
        return {
            "starting_balance": round(self.starting_balance, 2),
            "ending_balance": round(self.balance, 2),
            "closed_trades": len(self.closed_trades),
            "win_rate_pct": (
                round((len(wins) / len(self.closed_trades) * 100), 2) if self.closed_trades else 0
            ),
            "profit_factor": round(profit_factor, 2) if profit_factor != float("inf") else "inf",
            "net_pnl": round(self.balance - self.starting_balance, 2),
        }
