from pathlib import Path

from backtest.engine import apply_costs, run_backtest


def test_apply_costs_for_long_trade():
    entry, exit_price = apply_costs(
        entry=100.0,
        exit=110.0,
        fee_bps=5.0,
        slippage_bps=2.0,
        side="LONG",
    )

    assert entry > 100.0
    assert exit_price < 110.0


def test_run_backtest_generates_enhanced_analytics(tmp_path: Path):
    csv_path = tmp_path / "backtest_sample.csv"
    csv_path.write_text(
        "\n".join(
            [
                (
                    "timestamp,asset,price,volume,oi_score,sentiment_score,"
                    "structure_score,whale_score,liquidation_score"
                ),
                "1,BTC/USDT,100,100,80,80,80,20,10",
                "2,BTC/USDT,101,110,80,80,80,20,10",
                "3,BTC/USDT,102,120,80,80,80,20,10",
                "4,BTC/USDT,103,130,80,80,80,20,10",
                "5,BTC/USDT,104,10000,100,100,100,50,20",
                "6,BTC/USDT,106,10500,100,100,100,50,20",
                "7,BTC/USDT,108,10600,100,100,100,50,20",
            ]
        ),
        encoding="utf-8",
    )

    result = run_backtest(str(csv_path), hold_bars=1)

    assert result.starting_balance == 10000.0
    assert result.ending_balance >= 0
    assert result.net_pnl == round(result.ending_balance - result.starting_balance, 2)

    assert result.total_trades >= 1
    assert isinstance(result.equity_curve, list)
    assert len(result.equity_curve) >= 2
    assert result.best_trade_pnl >= result.worst_trade_pnl

    assert isinstance(result.average_win, float)
    assert isinstance(result.average_loss, float)
    assert isinstance(result.average_return_pct, float)

    assert result.win_rate_pct >= 0
    assert result.max_drawdown_pct >= 0
