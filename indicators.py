import numpy as np

def compute_rsi(prices):
    deltas = np.diff(prices)
    gains = np.maximum(deltas, 0)
    losses = np.abs(np.minimum(deltas, 0))
    avg_gain = np.mean(gains[-14:])
    avg_loss = np.mean(losses[-14:])
    rs = avg_gain / avg_loss if avg_loss else 0
    return 100 - (100 / (1 + rs))

def compute_rvol(prices):
    volumes = np.random.randint(1_000, 10_000, size=len(prices))
    avg_vol = np.mean(volumes[:-24])
    recent_vol = np.mean(volumes[-24:])
    return recent_vol / avg_vol if avg_vol else 0

def compute_ema(prices, period):
    return np.mean(prices[-period:])

def compute_vwap(prices):
    return np.mean(prices)

def enrich_indicators(ohlc_data):
    enriched = []
    for symbol, data in ohlc_data.items():
        prices = data["ohlc"]
        tags = data["tags"]
        if len(prices) < 50:
            continue
        rsi = compute_rsi(prices)
        rvol = compute_rvol(prices)
        ema5 = compute_ema(prices, 5)
        ema13 = compute_ema(prices, 13)
        ema50 = compute_ema(prices, 50)
        vwap = compute_vwap(prices)
        price = prices[-1]
        pump = (price - prices[-2]) / prices[-2] > 0.5

        tp_price = round(price * 1.1, 4)
        sl_price = round(price * 0.95, 4)
        risk_ratio = round((tp_price - price) / (price - sl_price), 2)

        qualified = (
            0.001 < price < 100 and
            rsi > 50 and rsi < 70 and
            rvol > 2 and
            ema5 > ema13 > ema50 and
            abs(price - vwap) / vwap < 0.02 and
            not pump
        )

        enriched.append({
            "symbol": symbol,
            "price": round(price, 4),
            "rsi": round(rsi, 2),
            "rvol": round(rvol, 2),
            "ema": [round(ema5, 2), round(ema13, 2), round(ema50, 2)],
            "vwap": round(vwap, 2),
            "tp_price": tp_price,
            "sl_price": sl_price,
            "risk_ratio": risk_ratio,
            "tags": tags,
            "ohlc": prices,
            "qualified": qualified
        })
    return enriched
