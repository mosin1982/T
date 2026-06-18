from paper.engine import PaperAccount


def test_paper_account_open_close():
    account = PaperAccount(starting_balance=10000)
    trade = account.open_trade("BTC/USDT", "LONG", 100, 1)
    account.close_trade(trade.trade_id, 110)
    summary = account.summary()
    assert summary["closed_trades"] == 1
    assert summary["ending_balance"] > 10000
