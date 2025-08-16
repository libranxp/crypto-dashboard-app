import requests, os

def fetch_news(symbol):
    key = os.getenv("API_KEY_NEWSAPI")
    url = f"https://newsapi.org/v2/everything?q={symbol}&apiKey={key}&language=en&sortBy=publishedAt"
    try:
        res = requests.get(url).json()
        articles = res.get('articles', [])[:3]
        return [{'title': a['title'], 'url': a['url'], 'publishedAt': a['publishedAt']} for a in articles]
    except Exception as e:
        return {'error': str(e)}
