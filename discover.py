import requests

def discover_tickers():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": False
    }
    r = requests.get(url, params=params).json()
    tickers = [coin['symbol'].upper() for coin in r if coin['market_cap'] > 1e9]
    return tickers
