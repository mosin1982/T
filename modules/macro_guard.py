HIGH_IMPACT_EVENTS = ["CPI", "FOMC", "FED", "RBI", "NFP", "GDP", "INFLATION"]


def macro_guard(event_title: str, minutes_to_event: int) -> dict:
    title = event_title.upper()
    high_impact = any(keyword in title for keyword in HIGH_IMPACT_EVENTS)
    avoid_new_positions = high_impact and minutes_to_event <= 60
    return {
        "event": event_title,
        "minutes_to_event": minutes_to_event,
        "high_impact": high_impact,
        "avoid_new_positions": avoid_new_positions,
    }
