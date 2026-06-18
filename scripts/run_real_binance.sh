#!/usr/bin/env bash
set -e
python t_cli.py real-binance --symbol "${BINANCE_SYMBOL:-btcusdt}" --threshold "${Z_SCORE_THRESHOLD:-3.0}"
