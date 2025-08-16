import requests

def scan_tickers():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": 250,
        "page": 1,
        "sparkline": False,
        "price_change_percentage": "1h,24h"
    }

    try:
        res = requests.get(url, params=params).json()
        filtered = []

        for coin in res:
            price = coin["current_price"]
            volume = coin["total_volume"]
            market_cap = coin["market_cap"]
            change_24h = coin["price_change_percentage_24h"]
            change_1h = coin.get("price_change_percentage_1h_in_currency", 0)

            if not all([price, volume, market_cap, change_24h]):
                continue

            if not (0.001 <= price <= 100):
                continue
            if volume < 10_000_000:
                continue
            if not (2 <= change_24h <= 20):
                continue
            if not (10_000_000 <= market_cap <= 5_000_000_000):
                continue
            if abs(change_1h) > 50:
                continue

            filtered.append(coin["id"])

        return filtered

    except Exception as e:
        print(f"❌ Scanner error: {e}")
        return []
