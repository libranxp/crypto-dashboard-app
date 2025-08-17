import requests

def get_dynamic_tickers(limit=25):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    try:
        res = requests.get(url, params=params, timeout=10).json()
        tickers = [coin["id"] for coin in res if coin.get("id")]
        return tickers
    except Exception as e:
        print(f"⚠️ Scanner error: {e}")
        return []
