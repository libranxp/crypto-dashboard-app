import requests, os

API_KEY = os.getenv("API_KEY_LUNARCRUSH")

def get_lunarcrush_sentiment(symbol):
    url = f"https://api.lunarcrush.com/v2"
    params = {
        "data": "assets",
        "symbol": symbol.upper(),
        "key": API_KEY
    }
    res = requests.get(url, params=params).json()
    assets = res.get("data", [])
    if assets:
        return round(assets[0].get("galaxy_score", 0) / 100, 2)
    return None
