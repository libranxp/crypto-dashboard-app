import requests

def fetch_ohlc(ticker_objs):
    result = {}
    for obj in ticker_objs:
        symbol = obj["symbol"]
        coin_id = obj["id"]
        try:
            url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
            params = {"vs_currency": "usd", "days": "1", "interval": "hourly"}
            r = requests.get(url, params=params)
            prices = r.json().get("prices", [])
            if prices:
                ohlc = [p[1] for p in prices[-50:]]
                result[symbol] = {
                    "ohlc": ohlc,
                    "tags": obj["tags"]
                }
        except Exception:
            continue
    return result
