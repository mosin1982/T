from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

from modes.scoring import alpha_score, z_score


@dataclass
class BacktestTrade:
    asset: str
    entry_price: float
    exit_price: float
    side: str
    pnl: float
    return_pct: float
    alpha: float
    z: float


@dataclass
class BacktestResult:
    trades: list[BacktestTrade]
    starting_balance: float
    ending_balance: float
    max_drawdown_pct: float
    win_rate_pct: float
    profit_factor: float
    net_pnl: float
    total_trades: int
    average_win: float
    average_loss: float
    best_trade_pnl: float
    worst_trade_pnl: float
    average_return_pct: float
    equity_curve: list[float]


def apply_costs(
    entry: float,
    exit: float,
    fee_bps: float,
    slippage_bps: float,
    side: str,
) -> tuple[float, float]:
    cost = (fee_bps + slippage_bps) / 10000

    if side.upper() == "LONG":
        return entry * (1 + cost), exit * (1 - cost)

    return entry * (1 - cost), exit * (1 + cost)


def run_backtest(
    csv_path: str,
    starting_balance: float = 10000.0,
    risk_per_trade: float = 0.10,
    fee_bps: float = 5.0,
    slippage_bps: float = 2.0,
) -> BacktestResult:
    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(f"Backtest CSV not found: {csv_path}")

    trades: list[BacktestTrade] = []
    volume_history: list[float] = []
    balance = starting_balance
    equity_peak = starting_balance
    max_drawdown_pct = 0.0
    equity_curve = [round(balance, 2)]

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            volume = float(row["volume"])
            volume_history.append(volume)

            if len(volume_history) < 3:
                continue

            z = z_score(volume, volume_history[:-1])
            alpha = alpha_score(
                z,
                float(row["price_change_pct"]),
                float(row["liquidity_score"]),
                float(row["risk_score"]),
            )

            if alpha < 70:
                continue

            entry = float(row["entry_price"])
            exit_price = float(row["exit_price"])

            adj_entry, adj_exit = apply_costs(
                entry=entry,
                exit=exit_price,
                fee_bps=fee_bps,
                slippage_bps=slippage_bps,
                side="LONG",
            )

            position_size = balance * risk_per_trade
            units = position_size / max(adj_entry, 1e-9)
            pnl = (adj_exit - adj_entry) * units
            balance += pnl
            equity_curve.append(round(balance, 2))

            return_pct = pnl / max(starting_balance, 1e-9) * 100

            trades.append(
                BacktestTrade(
                    asset=row["asset"],
                    entry_price=round(adj_entry, 4),
                    exit_price=round(adj_exit, 4),
                    side="LONG",
                    pnl=round(pnl, 2),
                    return_pct=round(return_pct, 4),
                    alpha=round(alpha, 4),
                    z=round(z, 4),
                )
            )

            equity_peak = max(equity_peak, balance)
            drawdown_pct = (equity_peak - balance) / max(equity_peak, 1e-9) * 100
            max_drawdown_pct = max(max_drawdown_pct, drawdown_pct)

    wins = [trade for trade in trades if trade.pnl > 0]
    losses = [trade for trade in trades if trade.pnl <= 0]

    gross_profit = sum(trade.pnl for trade in wins)
    gross_loss = abs(sum(trade.pnl for trade in losses))

    if gross_loss:
        profit_factor = gross_profit / gross_loss
    elif gross_profit:
        profit_factor = float("inf")
    else:
        profit_factor = 0.0

    total_trades = len(trades)
    average_win = round(gross_profit / len(wins), 2) if wins else 0.0
    average_loss = round(sum(trade.pnl for trade in losses) / len(losses), 2) if losses else 0.0
    best_trade_pnl = round(max((trade.pnl for trade in trades), default=0.0), 2)
    worst_trade_pnl = round(min((trade.pnl for trade in trades), default=0.0), 2)
    average_return_pct = (
        round(sum(trade.return_pct for trade in trades) / total_trades, 4) if total_trades else 0.0
    )

    win_rate_pct = round(len(wins) / total_trades * 100, 2) if total_trades else 0.0
    net_pnl = round(balance - starting_balance, 2)

    return BacktestResult(
        trades=trades,
        starting_balance=round(starting_balance, 2),
        ending_balance=round(balance, 2),
        max_drawdown_pct=round(max_drawdown_pct, 2),
        win_rate_pct=win_rate_pct,
        profit_factor=round(profit_factor, 4) if profit_factor != float("inf") else profit_factor,
        net_pnl=net_pnl,
        total_trades=total_trades,
        average_win=average_win,
        average_loss=average_loss,
        best_trade_pnl=best_trade_pnl,
        worst_trade_pnl=worst_trade_pnl,
        average_return_pct=average_return_pct,
        equity_curve=equity_curve,
    )
