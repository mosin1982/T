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


def test_sanitizes_unsafe_claims_case_insensitively():
    result = sanitize_research_text("BUY Now. This is Risk-Free.")

    assert result.safe is False
    assert "buy now" in result.blocked_phrases
    assert "risk free" in result.blocked_phrases
    assert "[blocked unsafe claim]" in result.sanitized_text
    assert "BUY Now" not in result.sanitized_text
    assert "Risk-Free" not in result.sanitized_text
    assert RESEARCH_DISCLAIMER in result.sanitized_text


def test_required_disclaimer_is_not_blocked():
    result = sanitize_research_text(RESEARCH_DISCLAIMER)

    assert result.safe is True
    assert result.blocked_phrases == []
    assert result.sanitized_text == RESEARCH_DISCLAIMER


def test_safe_text_gets_disclaimer():
    result = sanitize_research_text("This is a research observation.")

    assert result.safe is True
    assert result.blocked_phrases == []
    assert RESEARCH_DISCLAIMER in result.sanitized_text
