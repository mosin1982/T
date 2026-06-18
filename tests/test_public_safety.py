from pathlib import Path

BANNED_PHRASES = [
    "guaranteed profit",
    "100% profit",
    "risk free trading",
    "sure shot",
]


def test_no_banned_profit_claims_in_readme():
    text = Path("README.md").read_text(encoding="utf-8").lower()
    for phrase in BANNED_PHRASES:
        assert phrase not in text
