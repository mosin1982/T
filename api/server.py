"""
T API Gateway.

Optional dependency:
    pip install fastapi uvicorn

Run:
    uvicorn api.server:app --reload
"""
from typing import Any

try:
    from fastapi import FastAPI
except Exception:  # pragma: no cover
    FastAPI = None

from modes.scoring import alpha_score

if FastAPI:
    app = FastAPI(title="T API Gateway", version="0.8.0-alpha")
else:
    app = None

def calculate_alpha(payload: dict[str, Any]) -> dict[str, Any]:
    score = alpha_score(
        z=float(payload.get("z", 0)),
        oi_score=float(payload.get("oi_score", 50)),
        sentiment_score=float(payload.get("sentiment_score", 50)),
        structure_score=float(payload.get("structure_score", 50)),
        whale_score=float(payload.get("whale_score", 0)),
        liquidation_score=float(payload.get("liquidation_score", 0)),
    )
    return {"alpha_score": score, "status": "research_only"}

if app:
    @app.get("/health")
    def health() -> dict[str, str]:
        return {"status": "ok", "system": "T"}

    @app.post("/api/alpha-score")
    def api_alpha_score(payload: dict[str, Any]) -> dict[str, Any]:
        return calculate_alpha(payload)

    @app.get("/api/mission-control")
    def api_mission_control() -> dict[str, Any]:
        from mission_control.health import system_health
        return system_health()
