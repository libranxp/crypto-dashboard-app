from enrichment.sentiment_lunarcrush import get_lunarcrush_sentiment
from enrichment.sentiment_santiment import get_santiment_sentiment

def get_sentiment(symbol):
    scores = []
    lunar = get_lunarcrush_sentiment(symbol)
    if lunar is not None:
        scores.append(lunar)
    santiment = get_santiment_sentiment(symbol)
    if santiment is not None:
        scores.append(santiment)
    return round(sum(scores) / len(scores), 2) if scores else None
