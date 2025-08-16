import requests

def get_top_tickers(limit=50):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    res = requests.get(url, params=params).json()
    return [coin["id"] for coin in res if coin.get("id")]
