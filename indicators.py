import requests

def get_indicators(coin_id):
    try:
        ohlc_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/ohlc"
        ohlc_params = {"vs_currency": "usd", "days": 1}
        ohlc_res = requests.get(ohlc_url, params=ohlc_params).json()

        if not ohlc_res or len(ohlc_res) < 30:
            print(f"⚠️ Not enough OHLC data for {coin_id}")
            return None

        closes = [c[4] for c in ohlc_res]
        volumes = [c[5] if len(c) > 5 else 0 for c in ohlc_res]

        # RSI
        deltas = [closes[i] - closes[i-1] for i in range(1, len(closes))]
        gains = [d for d in deltas if d > 0]
        losses = [-d for d in deltas if d < 0]
        avg_gain = sum(gains[-14:]) / 14 if gains else 0.01
        avg_loss = sum(losses[-14:]) / 14 if losses else 0.01
        rs = avg_gain / avg_loss
        rsi = round(100 - (100 / (1 + rs)), 2)

        # MACD
        ema12 = sum(closes[-12:]) / 12
        ema26 = sum(closes[-26:]) / 26
        macd = round(ema12 - ema26, 2)

        # EMA Alignment
        ema5 = sum(closes[-5:]) / 5
        ema13 = sum(closes[-13:]) / 13
        ema50 = sum(closes[-50:]) / 50 if len(closes) >= 50 else ema13
        ema_alignment = ema5 > ema13 > ema50

        # VWAP
        vwap = round(sum([closes[i] * volumes[i] for i in range(len(closes))]) / sum(volumes), 2)
        vwap_proximity = abs(closes[-1] - vwap) / vwap <= 0.02

        # RVOL
        current_volume = volumes[-1]
        avg_volume = sum(volumes[:-1]) / len(volumes[:-1])
        rvol = round(current_volume / avg_volume, 2)

        if not (50 <= rsi <= 70 and rvol > 2 and ema_alignment and vwap_proximity):
            return None

        return {
            "price": round(closes[-1], 2),
            "RSI": rsi,
            "MACD": macd,
            "RVOL": rvol,
            "EMA": {"EMA5": round(ema5, 2), "EMA13": round(ema13, 2), "EMA50": round(ema50, 2)},
            "VWAP": vwap
        }

    except Exception as e:
        print(f"❌ Indicator error for {coin_id}: {e}")
        return None
