from ohlc import get_ohlc

def get_indicators(coin_id):
    prices, volumes = get_ohlc(coin_id)
    if not prices or not volumes:
        print(f"⚠️ Not enough market data for {coin_id}")
        return None

    deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
    gains = [d for d in deltas if d > 0]
    losses = [-d for d in deltas if d < 0]
    avg_gain = sum(gains[-14:]) / 14 if gains else 0.01
    avg_loss = sum(losses[-14:]) / 14 if losses else 0.01
    rs = avg_gain / avg_loss
    rsi = round(100 - (100 / (1 + rs)), 2)

    ema5 = sum(prices[-5:]) / 5
    ema13 = sum(prices[-13:]) / 13
    ema50 = sum(prices[-50:]) / 50 if len(prices) >= 50 else ema13
    ema_alignment = ema5 > ema13 > ema50

    vwap = round(sum([prices[i] * volumes[i] for i in range(len(prices))]) / sum(volumes), 2)
    vwap_proximity = abs(prices[-1] - vwap) / vwap <= 0.02

    current_volume = volumes[-1]
    avg_volume = sum(volumes[:-1]) / len(volumes[:-1])
    rvol = round(current_volume / avg_volume, 2)

    spike = max(prices[-2:]) / min(prices[-2:]) > 1.5

    if not (50 <= rsi <= 70 and rvol > 2 and ema_alignment and vwap_proximity and not spike):
        return None

    return {
        "price": round(prices[-1], 2),
        "RSI": rsi,
        "RVOL": rvol,
        "EMA": {"EMA5": round(ema5, 2), "EMA13": round(ema13, 2), "EMA50": round(ema50, 2)},
        "VWAP": vwap
    }
