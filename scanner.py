import requests

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"
EXCLUDE = {"usdt", "usdc", "busd", "dai", "tusd", "gusd"}

def get_dynamic_tickers(limit=25):
    try:
        response = requests.get(COINGECKO_URL, params={
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": limit,
            "page": 1,
            "sparkline": False
        }, timeout=10)
        response.raise_for_status()
        data = response.json()
        tickers = [coin["symbol"].upper() for coin in data if coin["symbol"].lower() not in EXCLUDE]
        return tickers
    except Exception as e:
        print(f"⚠️ Scanner error: {e}")
        return []
