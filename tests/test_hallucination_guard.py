from quality.hallucination_guard import (
    RESEARCH_DISCLAIMER,
    detect_unsafe_claims,
    sanitize_research_text,
)


def test_detects_banned_profit_claims():
    text = "This is guaranteed profit and 100% accurate."
    blocked = detect_unsafe_claims(text)

    assert "guaranteed profit" in blocked
    assert "100% accurate" in blocked


def test_sanitizes_unsafe_claims():
    result = sanitize_research_text("Buy now. This is financial advice.")

    assert result.safe is False
    assert "buy now" in result.blocked_phrases
    assert "financial advice" in result.blocked_phrases
    assert "[blocked unsafe claim]" in result.sanitized_text
    assert RESEARCH_DISCLAIMER in result.sanitized_text


def test_safe_text_gets_disclaimer():
    result = sanitize_research_text("This is a research observation.")

    assert result.safe is True
    assert result.blocked_phrases == []
    assert RESEARCH_DISCLAIMER in result.sanitized_text
