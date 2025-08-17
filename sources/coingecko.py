import requests

def fetch_coingecko_ohlc(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": "1", "interval": "hourly"}
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()
    prices = data.get("prices", [])
    volumes = data.get("total_volumes", [])

    if not prices or not volumes:
        raise ValueError("Missing OHLC data")

    ohlc = []
    for i in range(len(prices)):
        ts = int(prices[i][0])
        close = float(prices[i][1])
        volume = float(volumes[i][1])
        ohlc.append({
            "timestamp": ts,
            "open": close,
            "high": close,
            "low": close,
            "close": close,
            "volume": volume
        })

    return ohlc
