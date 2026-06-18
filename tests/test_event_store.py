from events.event_store import JsonlEventStore, new_event

def test_event_store_roundtrip(tmp_path):
    store = JsonlEventStore(str(tmp_path / "events.jsonl"))
    event = new_event("TestEvent", {"x": 1})
    store.append(event)
    events = store.read_all()
    assert len(events) == 1
    assert events[0].event_type == "TestEvent"
    assert events[0].payload["x"] == 1
