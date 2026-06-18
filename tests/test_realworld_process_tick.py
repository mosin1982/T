from realworld.binance_stream import BinancePublicStream

def test_process_tick_detects_signal_when_history_exists():
    stream = BinancePublicStream(symbol="btcusdt", threshold=1.0, cooldown_seconds=0)
    stream.minute_volumes.extend([100, 110, 95, 105, 100, 98, 102])
    stream.current_minute = 1
    stream.current_volume = 500
    signal = stream.process_tick(price=70000, volume=10, event_time_ms=2 * 60000)
    assert signal is not None
    assert signal.asset == "BTCUSDT"
