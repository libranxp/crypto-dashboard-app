import requests

def discover_tickers():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": False
    }
    res = requests.get(url, params=params).json()
    # Return actual trading symbols like BTC, ETH
    return [coin["symbol"].upper() for coin in res if coin.get("symbol")]
