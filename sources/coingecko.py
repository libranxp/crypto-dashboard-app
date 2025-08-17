import requests

def fetch_ohlc_coingecko(symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "1",
        "interval": "hourly"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        prices = data.get("prices", [])
        volumes = data.get("total_volumes", [])

        if not prices or not volumes:
            raise ValueError("Missing OHLC data")

        ohlc = []
        for i in range(len(prices)):
            ohlc.append({
                "timestamp": prices[i][0],
                "open": prices[i][1],
                "high": prices[i][1],
                "low": prices[i][1],
                "close": prices[i][1],
                "volume": volumes[i][1]
            })

        return ohlc

    except Exception as e:
        print(f"❌ CoinGecko OHLC error for {symbol}: {e}")
        return None
