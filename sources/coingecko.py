import requests

def fetch_coingecko_symbols():
    url = "https://api.coingecko.com/api/v3/coins/list"
    try:
        res = requests.get(url, timeout=10)
        res.raise_for_status()
        coins = res.json()
        return [coin["id"] for coin in coins if coin.get("id")]
    except Exception as e:
        print(f"❌ Error fetching CoinGecko symbols: {e}")
        return []

def fetch_asset_type(symbol):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}"
        res = requests.get(url, timeout=10).json()
        categories = res.get("categories", [])
        return categories[0].lower() if categories else "unknown"
    except Exception:
        return "unknown"
