import requests

def discover_tickers(limit=100):
    print("🔍 Discovering tickers from CoinGecko...")
    try:
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "volume_desc",
            "per_page": limit,
            "page": 1,
            "sparkline": False
        }
        res = requests.get(url, params=params, timeout=10).json()
        return [coin["id"] for coin in res if coin.get("id")]
    except Exception as e:
        print(f"❌ Discovery failed: {e}")
        return []
