import requests
import time

def fetch_paprika_ohlc(coin_id):
    # Convert CoinGecko ID to CoinPaprika ID format
    coin_id = coin_id.replace("-", "")
    url = f"https://api.coinpaprika.com/v1/coins"
    coins = requests.get(url, timeout=10).json()
    match = next((c for c in coins if c["id"].lower().replace("-", "") == coin_id), None)
    if not match:
        raise ValueError("Coin not found on CoinPaprika")

    symbol = match["id"]
    url = f"https://api.coinpaprika.com/v1/coins/{symbol}/ohlcv/historical"
    params = {"start": time.strftime("%Y-%m-%d"), "limit": 24}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    ohlc = []
    for entry in data:
        ohlc.append({
            "timestamp": int(time.mktime(time.strptime(entry["time_open"][:19], "%Y-%m-%dT%H:%M:%S")) * 1000),
            "open": entry["open"],
            "high": entry["high"],
            "low": entry["low"],
            "close": entry["close"],
            "volume": entry["volume"]
        })

    return ohlc
