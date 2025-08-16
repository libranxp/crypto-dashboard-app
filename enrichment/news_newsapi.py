import requests, os

API_KEY = os.getenv("API_KEY_NEWSAPI")

def get_news_score(symbol):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": symbol,
        "language": "en",
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }
    res = requests.get(url, params=params).json()
    articles = res.get("articles", [])
    return round(min(len(articles), 100) / 100, 2)
