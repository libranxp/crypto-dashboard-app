import requests

def fetch_paprika_symbols():
    url = "https://api.coinpaprika.com/v1/coins"
    try:
        res = requests.get(url).json()
        return [coin["symbol"].lower() for coin in res if coin["type"] == "coin"]
    except:
        return []

def fetch_ohlc_paprika(symbol):
    url = f"https://api.coinpaprika.com/v1/tickers/{symbol}-usd/historical?start=2023-01-01&interval=1d"
    try:
        res = requests.get(url).json()
        return [
            {"timestamp": d["timestamp"], "close": d["price"], "volume": d["volume"]}
            for d in res
        ]
    except:
        return []
