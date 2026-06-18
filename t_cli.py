import argparse
import asyncio

from modes.demo_mode import run_demo
from backtest.engine import run_backtest
from backtest.report import format_backtest_summary, save_backtest_report
from realworld.binance_stream import BinancePublicStream, rest_poll_once

def main() -> None:
    parser = argparse.ArgumentParser(description="T command line runner")
    sub = parser.add_subparsers(dest="command", required=True)

    demo = sub.add_parser("demo", help="Run no-key demo mode")
    demo.add_argument("--csv", default="data/sample/btc_demo.csv")
    demo.add_argument("--telegram", action="store_true")

    real = sub.add_parser("real-binance", help="Run real-world Binance public WebSocket mode")
    real.add_argument("--symbol", default="btcusdt")
    real.add_argument("--threshold", type=float, default=3.0)
    real.add_argument("--telegram", action="store_true")
    real.add_argument("--max-runtime", type=int, default=None, help="Optional seconds before clean exit")

    rest = sub.add_parser("rest-check", help="Check Binance public REST connectivity")
    rest.add_argument("--symbol", default="BTCUSDT")

    backtest = sub.add_parser("backtest", help="Run historical sample backtest")
    backtest.add_argument("--csv", default="data/sample/btc_demo.csv")
    backtest.add_argument("--alpha-threshold", type=float, default=65.0)
    backtest.add_argument("--z-threshold", type=float, default=2.0)
    backtest.add_argument("--hold-bars", type=int, default=2)
    backtest.add_argument("--fee-bps", type=float, default=5.0)
    backtest.add_argument("--slippage-bps", type=float, default=3.0)

    mission = sub.add_parser("mission-control", help="Show T system health")

    args = parser.parse_args()

    if args.command == "demo":
        run_demo(args.csv, args.telegram)
    elif args.command == "real-binance":
        asyncio.run(
            BinancePublicStream(
                symbol=args.symbol,
                threshold=args.threshold,
                telegram=args.telegram,
                max_runtime_seconds=args.max_runtime,
            ).run()
        )
    elif args.command == "rest-check":
        print(rest_poll_once(args.symbol))
    elif args.command == "backtest":
        result = run_backtest(
            csv_path=args.csv,
            alpha_threshold=args.alpha_threshold,
            z_threshold=args.z_threshold,
            hold_bars=args.hold_bars,
            fee_bps=args.fee_bps,
            slippage_bps=args.slippage_bps,
        )
        print(format_backtest_summary(result))
        print(f"Saved: {save_backtest_report(result)}")
    elif args.command == "mission-control":
        from mission_control.health import system_health
        print(system_health())

if __name__ == "__main__":
    main()
