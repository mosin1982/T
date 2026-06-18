from backtest.engine import apply_costs, run_backtest
from backtest.report import save_backtest_report

def test_apply_costs_long():
    entry, exit_ = apply_costs(100, 110, fee_bps=5, slippage_bps=5, side="LONG")
    assert entry > 100
    assert exit_ < 110

def test_run_backtest_and_save(tmp_path):
    result = run_backtest("data/sample/btc_demo.csv", alpha_threshold=50, z_threshold=1)
    assert result.starting_balance == 10000
    assert isinstance(result.trades, list)
    out = save_backtest_report(result, str(tmp_path / "report.json"))
    assert out.endswith("report.json")
