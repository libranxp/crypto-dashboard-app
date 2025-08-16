import requests, os, numpy as np

def fetch_price_data(symbol):
    key = os.getenv("API_KEY_ALPHA")
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}USD&interval=5min&apikey={key}"
    r = requests.get(url).json()
    if 'Time Series (5min)' not in r:
        raise ValueError(f"No data for {symbol}")
    return r['Time Series (5min)']

def calculate_rsi(prices, period=14):
    deltas = np.diff(prices)
    seed = deltas[:period]
    up = seed[seed > 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down if down != 0 else 0
    return round(100 - (100 / (1 + rs)), 2)

def calculate_ema(prices, period=20):
    weights = np.exp(np.linspace(-1., 0., period))
    weights /= weights.sum()
    ema = np.convolve(prices, weights, mode='valid')[-1]
    return round(ema, 2)

def calculate_vwap(data):
    total_volume = 0
    total_price_volume = 0
    for v in data.values():
        price = (float(v['high']) + float(v['low']) + float(v['close'])) / 3
        volume = float(v['volume'])
        total_price_volume += price * volume
        total_volume += volume
    return round(total_price_volume / total_volume, 2)

def calculate_rvol(data):
    volumes = [float(v['volume']) for v in data.values()]
    latest = volumes[0]
    avg = np.mean(volumes[1:])
    return round(latest / avg, 2)

def detect_macd_crossover(prices):
    short_ema = calculate_ema(prices, 12)
    long_ema = calculate_ema(prices, 26)
    macd = short_ema - long_ema
    signal = calculate_ema([macd] + prices[:8], 9)
    return "Bullish" if macd > signal else "Bearish"

def calculate_tp_sl(prices):
    tp = round(prices[0] * 1.05, 2)
    sl = round(prices[0] * 0.95, 2)
    return tp, sl

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
