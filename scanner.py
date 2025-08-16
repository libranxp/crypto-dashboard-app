import requests

def discover_tickers():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": 250,
        "page": 1,
        "sparkline": False
    }
    try:
        res = requests.get(url, params=params).json()
        tickers = []
        for coin in res:
            price = coin.get("current_price", 0)
            volume = coin.get("total_volume", 0)
            change = coin.get("price_change_percentage_24h", 0)
            mcap = coin.get("market_cap", 0)

            if (
                0.001 <= price <= 100 and
                volume >= 10_000_000 and
                2 <= change <= 20 and
                10_000_000 <= mcap <= 5_000_000_000
            ):
                tickers.append({
                    "id": coin["id"],
                    "symbol": coin["symbol"],
                    "name": coin["name"],
                    "price": price,
                    "volume": volume,
                    "change": change,
                    "market_cap": mcap
                })
        print(f"✅ Scanner found {len(tickers)} qualifying tickers")
        return tickers
    except Exception as e:
        print(f"❌ Scanner error: {e}")
        return []
