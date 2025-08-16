import requests

def discover_tickers():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    try:
        r = requests.get(url, params=params).json()
        return [coin["symbol"].upper() for coin in r if coin.get("symbol")]
    except Exception as e:
        print(f"⚠️ Ticker discovery failed: {e}")
        return []
