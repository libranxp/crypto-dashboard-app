import requests
import time

def fetch_ohlc_coingecko(symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "1",
        "interval": "hourly"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        ohlc = []
        for i in range(len(data["prices"])):
            ohlc.append({
                "timestamp": data["prices"][i][0],
                "open": data["prices"][i][1],
                "high": data["high_24h"][i][1] if "high_24h" in data else None,
                "low": data["low_24h"][i][1] if "low_24h" in data else None,
                "close": data["prices"][i][1],
                "volume": data["total_volumes"][i][1]
            })

        return ohlc

    except Exception as e:
        print(f"❌ CoinGecko OHLC error for {symbol}: {e}")
        return None
