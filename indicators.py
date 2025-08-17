def compute_indicators(ohlc):
    try:
        closes = [c["close"] for c in ohlc]
        volumes = [c["volume"] for c in ohlc]

        deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
        gains = [d for d in deltas if d > 0]
        losses = [-d for d in deltas if d < 0]
        avg_gain = sum(gains[-14:]) / 14 if gains else 0.01
        avg_loss = sum(losses[-14:]) / 14 if losses else 0.01
        rs = avg_gain / avg_loss
        rsi = round(100 - (100 / (1 + rs)), 2)

        ema5 = sum(closes[-5:]) / 5
        ema13 = sum(closes[-13:]) / 13
        ema50 = sum(closes[-50:]) / 50 if len(closes) >= 50 else ema13
        ema_alignment = ema5 > ema13 > ema50

        vwap = round(sum([closes[i] * volumes[i] for i in range(len(closes))]) / sum(volumes), 2)
        vwap_proximity = abs(closes[-1] - vwap) / vwap <= 0.02

        current_volume = volumes[-1]
        avg_volume = sum(volumes[:-1]) / len(volumes[:-1])
        rvol = round(current_volume / avg_volume, 2)

        spike = max(closes[-2:]) / min(closes[-2:]) > 1.5

        if not (50 <= rsi <= 70 and rvol > 2 and ema_alignment and vwap_proximity and not spike):
            return None

        return {
            "RSI": rsi,
            "RVOL": rvol,
            "EMA": {"EMA5": round(ema5, 2), "EMA13": round(ema13, 2), "EMA50": round(ema50, 2)},
            "VWAP": vwap
        }
    except Exception as e:
        print(f"❌ Indicator error: {e}")
        return None
