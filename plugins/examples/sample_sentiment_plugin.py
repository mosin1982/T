from plugins.base import TPlugin


class SampleSentimentPlugin(TPlugin):
    name = "sample_sentiment"
    version = "0.1.0"

    def run(self, context: dict) -> dict:
        text = str(context.get("text", "")).lower()
        score = 70 if "bullish" in text else 40 if "bearish" in text else 50
        return {"sentiment_score": score}
