from __future__ import annotations

import re
from dataclasses import dataclass

BANNED_PHRASES = [
    "guaranteed profit",
    "sure shot",
    "100% accurate",
    "risk free",
    "buy now",
    "sell now",
    "investment advice",
    "guaranteed return",
    "no loss",
    "will go up",
    "will go down",
    "must buy",
    "must sell",
]


RESEARCH_DISCLAIMER = "Research only. Not financial advice."
BLOCKED_TEXT = "[blocked unsafe claim]"


@dataclass(frozen=True)
class GuardResult:
    safe: bool
    blocked_phrases: list[str]
    sanitized_text: str
    disclaimer: str = RESEARCH_DISCLAIMER


def _phrase_pattern(phrase: str) -> re.Pattern[str]:
    words = phrase.strip().split()
    separator = r"[\s\-_]+"
    pattern = r"\b" + separator.join(re.escape(word) for word in words) + r"\b"
    return re.compile(pattern, flags=re.IGNORECASE)


def detect_unsafe_claims(text: str) -> list[str]:
    return [phrase for phrase in BANNED_PHRASES if _phrase_pattern(phrase).search(text)]


def sanitize_research_text(text: str) -> GuardResult:
    blocked = detect_unsafe_claims(text)
    sanitized = text

    for phrase in blocked:
        sanitized = _phrase_pattern(phrase).sub(BLOCKED_TEXT, sanitized)

    if RESEARCH_DISCLAIMER.lower() not in sanitized.lower():
        sanitized = f"{sanitized}\n\n{RESEARCH_DISCLAIMER}"

    return GuardResult(
        safe=len(blocked) == 0,
        blocked_phrases=blocked,
        sanitized_text=sanitized,
    )


def enforce_research_output(text: str) -> str:
    result = sanitize_research_text(text)
    return result.sanitized_text
