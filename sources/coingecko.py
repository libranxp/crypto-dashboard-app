import requests

def fetch_asset_type(symbol):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}"
        res = requests.get(url, timeout=10).json()
        categories = res.get("categories", [])
        if not categories:
            return "unknown"
        return categories[0].lower()
    except Exception:
        return "unknown"
