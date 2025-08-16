import requests, os

API_KEY = os.getenv("API_KEY_ALPHA")

def get_indicators(symbol):
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol.upper(),
        "interval": "15min",
        "apikey": API_KEY
    }
    res = requests.get(url, params=params).json()
    data = res.get("Time Series (15min)", {})
    prices = [float(v["4. close"]) for v in data.values()]
    if not prices:
        return None

    # Simple mock RSI/MACD/RVOL logic
    RSI = round(30 + (prices[-1] % 40), 2)
    MACD = round(-5 + (prices[-1] % 10), 2)
    RVOL = round(0.5 + (prices[-1] % 2), 2)

    return {"RSI": RSI, "MACD": MACD, "RVOL": RVOL}
