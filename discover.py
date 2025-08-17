import requests
import re

def discover_tickers():
    print("🔍 Discovering tickers from CoinGecko...")
    try:
        url = "https://api.coingecko.com/api/v3/coins/list"
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        coins = response.json()
        raw = [coin["symbol"].upper() for coin in coins if coin.get("symbol")]

        # Filter: only alphanumeric tickers, 2–10 chars
        tickers = [s for s in raw if re.match(r"^[A-Z0-9]{2,10}$", s)]

        print(f"✅ Fetched {len(tickers)} clean tickers from CoinGecko")
        return tickers[:100]  # Limit for performance
    except Exception as e:
        print(f"❌ Ticker discovery failed: {e}")
        return []
