import requests
import re

def discover_tickers():
    print("🔍 Discovering tickers from CoinGecko...")
    try:
        url = "https://api.coingecko.com/api/v3/coins/list"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        coins = response.json()
        raw = [coin["id"] for coin in coins if coin.get("id")]

        tickers = [s for s in raw if re.match(r"^[a-z0-9\-]{2,20}$", s)]
        print(f"✅ Fetched {len(tickers)} clean tickers from CoinGecko")
        return tickers[:100]
    except Exception as e:
        print(f"❌ Ticker discovery failed: {e}")
        return []
