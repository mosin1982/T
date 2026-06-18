from sdk import TClient
from nexus.graph import NexusGraph
from datalake.sqlite_store import SQLiteDataLake
from mission_control.health import system_health
from quality.data_quality import validate_market_tick, source_trust_score
from validation.center import SignalOutcome, accuracy_report
from benchmark.strategies import buy_and_hold_return

def test_sdk_alpha():
    client = TClient()
    assert "alpha_score" in client.alpha_score(z=3)

def test_nexus_graph():
    g = NexusGraph()
    g.add_node("BTC", "asset")
    g.add_node("WHALE", "actor")
    g.connect("BTC", "WHALE", "affected_by", weight=0.8)
    assert g.conviction_score("BTC") > 0

def test_datalake(tmp_path):
    lake = SQLiteDataLake(str(tmp_path / "lake.sqlite3"))
    row_id = lake.insert("signal", {"asset": "BTC"})
    assert row_id >= 1
    assert lake.list_records("signal")[0]["payload"]["asset"] == "BTC"

def test_mission_control():
    assert system_health()["system"] == "T"

def test_quality():
    assert validate_market_tick({"asset": "BTC", "price": 1, "volume": 2})["valid"]
    assert source_trust_score("binance") > source_trust_score("twitter")

def test_validation_center():
    report = accuracy_report([SignalOutcome("1", "BTC", 80, 100, 110)])
    assert report["win_rate_pct"] == 100

def test_benchmark():
    assert buy_and_hold_return([100, 110]) == 10
