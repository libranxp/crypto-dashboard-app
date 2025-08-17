import requests
import time

def fetch_paprika_ohlc(coin_id):
    coin_id = coin_id.replace("-", "")
    coins = requests.get("https://api.coinpaprika.com/v1/coins", timeout=10).json()
    match = next((c for c in coins if c["id"].replace("-", "") == coin_id), None)
    if not match:
        raise ValueError("Coin not found")

    symbol = match["id"]
    url = f"https://api.coinpaprika.com/v1/coins/{symbol}/ohlcv/historical"
    params = {"start": time.strftime("%Y-%m-%d"), "limit": 24}
    res = requests.get(url, params=params, timeout=10)
    res.raise_for_status()
    data = res.json()

    ohlc = []
    for entry in data:
        if not isinstance(entry, dict):
            continue
        ohlc.append({
            "timestamp": int(time.mktime(time.strptime(entry["time_open"][:19], "%Y-%m-%dT%H:%M:%S")) * 1000),
            "open": entry.get("open", 0),
            "high": entry.get("high", 0),
            "low": entry.get("low", 0),
            "close": entry.get("close", 0),
            "volume": entry.get("volume", 0)
        })

    if not ohlc or all(c["volume"] == 0 for c in ohlc):
        raise ValueError("No valid volume data")

    return ohlc
