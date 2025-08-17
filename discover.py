import requests
import re

def discover_tickers():
    print("🔍 Discovering tickers from CoinGecko...")
    try:
        cg_url = "https://api.coingecko.com/api/v3/coins/list"
        cg_resp = requests.get(cg_url, timeout=10)
        cg_resp.raise_for_status()
        cg_coins = cg_resp.json()
        cg_ids = {coin["id"] for coin in cg_coins}

        pp_url = "https://api.coinpaprika.com/v1/coins"
        pp_resp = requests.get(pp_url, timeout=10)
        pp_resp.raise_for_status()
        pp_coins = pp_resp.json()
        pp_ids = {coin["id"].lower().replace("-", "") for coin in pp_coins}

        # Filter to tickers supported by both
        valid = [coin["id"] for coin in cg_coins if coin["id"].replace("-", "") in pp_ids]
        tickers = [s for s in valid if re.match(r"^[a-z0-9\-]{2,20}$", s)]
        print(f"✅ Found {len(tickers)} tickers supported by both APIs")
        return tickers[:100]
    except Exception as e:
        print(f"❌ Ticker discovery failed: {e}")
        return []
