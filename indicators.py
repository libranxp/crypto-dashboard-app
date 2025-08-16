import requests, os

def get_indicators(symbol):
    key = os.getenv("API_KEY_ALPHA")
    if not key:
        print("⚠️ Alpha Vantage API key missing")
        return None

    try:
        # RSI
        rsi_url = "https://www.alphavantage.co/query"
        rsi_params = {
            "function": "RSI",
            "symbol": symbol,
            "interval": "60min",
            "time_period": 14,
            "series_type": "close",
            "apikey": key
        }
        rsi_res = requests.get(rsi_url, params=rsi_params).json()
        rsi_data = rsi_res.get("Technical Analysis: RSI", {})
        latest_rsi = next(iter(rsi_data.values()), {}).get("RSI")
        rsi = round(float(latest_rsi), 2) if latest_rsi else None

        # MACD
        macd_params = {
            "function": "MACD",
            "symbol": symbol,
            "interval": "60min",
            "series_type": "close",
            "apikey": key
        }
        macd_res = requests.get(rsi_url, params=macd_params).json()
        macd_data = macd_res.get("Technical Analysis: MACD", {})
        latest_macd = next(iter(macd_data.values()), {})
        macd = round(float(latest_macd.get("MACD", 0)), 2)

        # RVOL (Relative Volume)
        price_url = "https://www.alphavantage.co/query"
        price_params = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": symbol,
            "interval": "60min",
            "apikey": key
        }
        price_res = requests.get(price_url, params=price_params).json()
        series = price_res.get("Time Series (60min)", {})
        volumes = [float(v["5. volume"]) for v in series.values()]
        if len(volumes) < 2:
            print(f"⚠️ Not enough volume data for {symbol}")
            return None
        current_volume = volumes[0]
        avg_volume = sum(volumes[1:]) / len(volumes[1:])
        rvol = round(current_volume / avg_volume, 2)

        print(f"✅ Indicators for {symbol}: RSI={rsi}, MACD={macd}, RVOL={rvol}")
        return {
            "RSI": rsi,
            "MACD": macd,
            "RVOL": rvol
        }

    except Exception as e:
        print(f"❌ Indicator fetch error for {symbol}: {e}")
        return None
