import requests

def fetch_ohlc_data(symbol):
    url = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}/market_chart"
    params = {
        "vs_currency": "usd",
        "days": 1,
        "interval": "hourly"
    }
    try:
        res = requests.get(url, params=params, timeout=10).json()
        prices = res.get("prices", [])
        volumes = res.get("total_volumes", [])

        if len(prices) < 30 or len(volumes) < 30:
            print(f"⚠️ Not enough OHLC data for {symbol}")
            return None

        ohlc = []
        for i in range(len(prices)):
            ohlc.append({
                "timestamp": prices[i][0],
                "close": prices[i][1],
                "volume": volumes[i][1]
            })

        return ohlc
    except Exception as e:
        print(f"❌ OHLC fetch error for {symbol}: {e}")
        return None
