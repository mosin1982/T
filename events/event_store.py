import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4


@dataclass(frozen=True)
class Event:
    event_id: str
    event_type: str
    timestamp: str
    payload: dict[str, Any]


def new_event(event_type: str, payload: dict[str, Any]) -> Event:
    return Event(
        event_id=str(uuid4()),
        event_type=event_type,
        timestamp=datetime.now(timezone.utc).isoformat(),
        payload=payload,
    )


class JsonlEventStore:
    def __init__(self, path: str = "data/events/events.jsonl"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def append(self, event: Event) -> None:
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(event), ensure_ascii=False) + "\n")

    def read_all(self) -> list[Event]:
        if not self.path.exists():
            return []
        events: list[Event] = []
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                obj = json.loads(line)
                events.append(Event(**obj))
        return events
