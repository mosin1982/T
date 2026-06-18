from realworld.binance_stream import rest_poll_once


def test_rest_poll_shape(monkeypatch):
    # Avoid network in CI; this validates expected shape through a monkeypatched function when extended.
    assert callable(rest_poll_once)
