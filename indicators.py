import numpy as np

def compute_rsi(data, period=14):
    closes = [c["close"] for c in data]
    if len(closes) < period + 1:
        return 0

    deltas = np.diff(closes)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)

    avg_gain = np.mean(gains[-period:])
    avg_loss = np.mean(losses[-period:])

    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    return round(rsi, 2)

def compute_rvol(data, window=20):
    volumes = [c["volume"] for c in data]
    if len(volumes) < window + 1:
        return 0

    recent = volumes[-1]
    avg = np.mean(volumes[-window:])
    if avg == 0:
        return 0
    rvol = recent / avg
    return round(rvol, 2)

def detect_pump(data, threshold=1.2):
    closes = [c["close"] for c in data]
    if len(closes) < 2:
        return False

    change = closes[-1] / closes[-2]
    return change > threshold

def enrich_indicators(ohlc_data):
    enriched = []

    for coin_id, data in ohlc_data.items():
        try:
            rsi = compute_rsi(data)
            rvol = compute_rvol(data)
            pump = detect_pump(data)

            price = data[-1]["close"]
            tp = round(price * 1.1, 4)
            sl = round(price * 0.95, 4)
            risk = round((tp - price) / (price - sl), 2)

            qualified = rsi > 40 and rvol > 1 and not pump

            enriched.append({
                "symbol": coin_id,
                "price": round(price, 4),
                "rsi": rsi,
                "rvol": rvol,
                "pump": pump,
                "tp_price": tp,
                "sl_price": sl,
                "risk_ratio": risk,
                "qualified": qualified
            })
        except Exception as e:
            print(f"❌ Error processing {coin_id}: {e}")

    return enriched
