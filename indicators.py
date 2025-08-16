import requests, numpy as np, os

def fetch_price_data(symbol):
    key = os.getenv("API_KEY_ALPHA")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}USD&interval=5min&apikey={key}"
    r = requests.get(url).json()
    if 'Time Series (5min)' not in r:
        raise ValueError(f"No data for {symbol}")
    return r['Time Series (5min)']

# RSI, EMA, VWAP, RVOL, MACD, TP/SL logic as before...
