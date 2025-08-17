import requests

def discover_tickers():
    print("🔍 Discovering tickers from CoinGecko...")
    try:
        url = "https://api.coingecko.com/api/v3/coins/list"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        coins = response.json()
        tickers = [coin["symbol"].upper() for coin in coins if coin.get("symbol")]
        print(f"✅ Fetched {len(tickers)} tickers from CoinGecko")

        return tickers[:100]  # Limit for performance; adjust as needed
    except Exception as e:
        print(f"❌ Ticker discovery failed: {e}")
        return []
