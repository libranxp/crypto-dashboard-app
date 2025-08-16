import requests, os, numpy as np

def fetch_price_data(symbol):
    key = os.getenv("API_KEY_ALPHA")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}USD&interval=5min&apikey={key}"
    r = requests.get(url).json()
    if 'Time Series (5min)' not in r:
        raise ValueError(f"No data for {symbol}")
    return r['Time Series (5min)']

def compute_indicators(symbol):
    data = fetch_price_data(symbol)
    prices = [float(v['close']) for v in data.values()]
    latest = prices[0]
    rsi = calculate_rsi(prices)
    ema = calculate_ema(prices)
    vwap = calculate_vwap(data)
    rvol = calculate_rvol(data)
    macd = detect_macd_crossover(prices)
    tp, sl = calculate_tp_sl(prices)
    chart = prices[:30]

    return {
        'symbol': symbol,
        'price': latest,
        'RSI': rsi,
        'EMA': ema,
        'VWAP': vwap,
        'RVOL': rvol,
        'MACD': macd,
        'TP': tp,
        'SL': sl,
        'chart': chart
    }

# Indicator functions (same as before)
# calculate_rsi, calculate_ema, calculate_vwap, calculate_rvol, detect_macd_crossover, calculate_tp_sl
