class TClient:
    """Lightweight local SDK for T.

    Future versions may connect to the API Gateway.
    """

    def alpha_score(
        self,
        z: float,
        oi_score: float = 50,
        sentiment_score: float = 50,
        structure_score: float = 50,
    ) -> dict:
        from modes.scoring import alpha_score

        return {
            "alpha_score": alpha_score(
                z=z,
                oi_score=oi_score,
                sentiment_score=sentiment_score,
                structure_score=structure_score,
            )
        }

    def mission_control(self) -> dict:
        from mission_control.health import system_health

        return system_health()
