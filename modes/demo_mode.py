import argparse
import csv
from pathlib import Path

from alerts.formatter import format_console_alert, format_telegram_alert
from alerts.telegram import send_telegram_message
from modes.scoring import Signal, alpha_score, build_explanation, risk_label, z_score
from paper.engine import PaperAccount
from events.event_store import JsonlEventStore, new_event

def run_demo(csv_path: str, send_telegram: bool = False) -> list[Signal]:
    path = Path(csv_path)
    volumes: list[float] = []
    signals: list[Signal] = []
    account = PaperAccount(starting_balance=10000.0)
    event_store = JsonlEventStore()

    with path.open("r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            asset = row["asset"]
            price = float(row["price"])
            volume = float(row["volume"])
            z = z_score(volume, volumes)
            alpha = alpha_score(
                z=z,
                oi_score=float(row["oi_score"]),
                sentiment_score=float(row["sentiment_score"]),
                structure_score=float(row["structure_score"]),
                whale_score=float(row["whale_score"]),
                liquidation_score=float(row["liquidation_score"]),
            )
            risk = risk_label(alpha, z)
            explanation = build_explanation(z, alpha, float(row["oi_score"]), float(row["sentiment_score"]))
            direction = "LONG_OBSERVATION" if alpha >= 70 and z >= 3 else "NO_TRADE"

            if direction != "NO_TRADE":
                signal = Signal(asset, price, z, alpha, risk, direction, explanation)
                signals.append(signal)
                event_store.append(new_event('SignalGenerated', signal.__dict__))
                print(format_console_alert(signal))
                account.open_trade(asset=asset, side="LONG", entry_price=price, risk_pct=1.0)
                if send_telegram:
                    send_telegram_message(format_telegram_alert(signal))

            volumes.append(volume)
            if len(volumes) > 50:
                volumes.pop(0)

    # Close any open paper trade at last price for demo.
    if account.open_positions:
        account.close_all(exit_price=price)

    print("\nT Paper Trading Demo Summary")
    print(account.summary())
    return signals

def main() -> None:
    parser = argparse.ArgumentParser(description="Run T Demo Mode with sample data.")
    parser.add_argument("--csv", default="data/sample/btc_demo.csv")
    parser.add_argument("--telegram", action="store_true")
    args = parser.parse_args()
    run_demo(args.csv, args.telegram)

if __name__ == "__main__":
    main()
