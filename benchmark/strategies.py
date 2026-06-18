def buy_and_hold_return(prices: list[float]) -> float:
    if len(prices) < 2:
        return 0.0
    return round((prices[-1] - prices[0]) / prices[0] * 100, 2)


def simple_momentum_signal(prices: list[float], lookback: int = 3) -> str:
    if len(prices) <= lookback:
        return "NO_SIGNAL"
    return "LONG" if prices[-1] > prices[-lookback] else "WAIT"
