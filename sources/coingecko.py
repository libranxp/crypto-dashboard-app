import requests

def fetch_coingecko_symbols():
    url = "https://api.coingecko.com/api/v3/coins/list"
    try:
        res = requests.get(url).json()
        return [coin["symbol"].lower() for coin in res]
    except:
        return []

def fetch_ohlc_coingecko(symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart?vs_currency=usd&days=7"
    try:
        res = requests.get(url).json()
        prices = res.get("prices", [])
        volumes = res.get("total_volumes", [])
        return [
            {"timestamp": p[0], "close": round(p[1], 4), "volume": round(v[1], 2)}
            for p, v in zip(prices, volumes)
        ]
    except:
        return []
