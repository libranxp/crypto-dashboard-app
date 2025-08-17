import requests

def fetch_coingecko_ohlc(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": "1", "interval": "hourly"}
    res = requests.get(url, params=params, timeout=10)
    res.raise_for_status()
    data = res.json()

    prices = data.get("prices", [])
    volumes = data.get("total_volumes", [])
    if not prices or not volumes:
        raise ValueError("Missing OHLC data")

    ohlc = []
    for i in range(len(prices)):
        ohlc.append({
            "timestamp": int(prices[i][0]),
            "open": prices[i][1],
            "high": prices[i][1],
            "low": prices[i][1],
            "close": prices[i][1],
            "volume": volumes[i][1]
        })
    return ohlc
