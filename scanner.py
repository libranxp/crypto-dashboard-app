import requests

def discover_tickers(limit=100):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    r = requests.get(url, params=params)
    data = r.json()

    tickers = []
    for d in data:
        symbol = d["symbol"].upper()
        id = d["id"]
        tags = fetch_tags(id)
        tickers.append({"symbol": symbol, "id": id, "tags": tags})
    return tickers

def fetch_tags(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}"
    r = requests.get(url)
    data = r.json()
    categories = data.get("categories", [])
    return categories[:3]  # top 3 tags
