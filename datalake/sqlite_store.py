import json
import sqlite3
from pathlib import Path
from typing import Any


class SQLiteDataLake:
    def __init__(self, path: str = "data/t_datalake.sqlite3"):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(str(self.path))
        self._init()

    def _init(self) -> None:
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_type TEXT NOT NULL,
            payload TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        self.conn.commit()

    def insert(self, record_type: str, payload: dict[str, Any]) -> int:
        cur = self.conn.execute(
            "INSERT INTO records(record_type, payload) VALUES (?, ?)",
            (record_type, json.dumps(payload, ensure_ascii=False)),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def list_records(self, record_type: str | None = None) -> list[dict[str, Any]]:
        if record_type:
            rows = self.conn.execute(
                "SELECT id, record_type, payload, created_at FROM records WHERE record_type=? ORDER BY id DESC",
                (record_type,),
            ).fetchall()
        else:
            rows = self.conn.execute(
                "SELECT id, record_type, payload, created_at FROM records ORDER BY id DESC"
            ).fetchall()
        return [
            {"id": r[0], "record_type": r[1], "payload": json.loads(r[2]), "created_at": r[3]}
            for r in rows
        ]
