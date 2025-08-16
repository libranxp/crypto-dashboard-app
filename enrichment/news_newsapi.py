import requests, os

def get_news_score(symbol):
    key = os.getenv("API_KEY_NEWSAPI")
    if not key:
        print("⚠️ NEWSAPI key missing")
        return None

    query = f"{symbol} crypto"
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&pageSize=10&apiKey={key}"

    try:
        res = requests.get(url).json()
        articles = res.get("articles", [])
        score = sum(1 for a in articles if a.get("title") and "bullish" in a["title"].lower())
        normalized = round(score / max(len(articles), 1), 2)
        print(f"✅ News score for {symbol}: {normalized}")
        return normalized
    except Exception as e:
        print(f"❌ NewsAPI error for {symbol}: {e}")
        return None
