def explain_signal(signal: dict) -> str:
    reasons = signal.get("reasons", [])
    invalidation = signal.get("invalidation", "Price closes below invalidation zone.")
    lines = ["Why this signal triggered:"]
    for reason in reasons:
        lines.append(f"- {reason}")
    lines.append(f"Invalidation: {invalidation}")
    return "\n".join(lines)
