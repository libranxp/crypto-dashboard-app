import requests

def discover_tickers():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    try:
        res = requests.get(url, params=params).json()
        tickers = [coin["symbol"].upper() for coin in res if coin.get("symbol")]
        print(f"✅ Fetched {len(tickers)} tickers from CoinGecko")
        return tickers
    except Exception as e:
        print(f"❌ Failed to fetch tickers: {e}")
        return []
