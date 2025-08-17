import requests

def fetch_sentiment(symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}"
    try:
        res = requests.get(url).json()
        up = res.get("sentiment_votes_up_percentage", 0)
        down = res.get("sentiment_votes_down_percentage", 0)
        score = round((up - down) / 100, 3)  # Normalize to range [-1, 1]
        return score
    except Exception as e:
        print(f"❌ Sentiment fetch failed for {symbol}: {e}")
        return 0

def enrich_sentiment(assets):
    for asset in assets:
        score = fetch_sentiment(asset["symbol"])
        asset["sentiment_score"] = score
    return assets
