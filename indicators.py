import requests

def get_indicators(coin_id):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": 1,
            "interval": "hourly"
        }
        res = requests.get(url, params=params).json()
        prices = [p[1] for p in res.get("prices", [])]
        volumes = [v[1] for v in res.get("total_volumes", [])]

        if len(prices) < 30 or len(volumes) < 30:
            print(f"⚠️ Not enough market data for {coin_id}")
            return None

        # RSI
        deltas = [prices[i] - prices[i-1] for i in range(1, len(prices))]
        gains = [d for d in deltas if d > 0]
        losses = [-d for d in deltas if d < 0]
        avg_gain = sum(gains[-14:]) / 14 if gains else 0.01
        avg_loss = sum(losses[-14:]) / 14 if losses else 0.01
        rs = avg_gain / avg_loss
        rsi = round(100 - (100 / (1 + rs)), 2)

        # MACD
        ema12 = sum(prices[-12:]) / 12
        ema26 = sum(prices[-26:]) / 26
        macd = round(ema12 - ema26, 2)

        # EMA Alignment
        ema5 = sum(prices[-5:]) / 5
        ema13 = sum(prices[-13:]) / 13
        ema50 = sum(prices[-50:]) / 50 if len(prices) >= 50 else ema13
        ema_alignment = ema5 > ema13 > ema50

        # VWAP
        vwap = round(sum([prices[i] * volumes[i] for i in range(len(prices))]) / sum(volumes), 2)
        vwap_proximity = abs(prices[-1] - vwap) / vwap <= 0.02

        # RVOL
        current_volume = volumes[-1]
        avg_volume = sum(volumes[:-1]) / len(volumes[:-1])
        rvol = round(current_volume / avg_volume, 2)

        if not (50 <= rsi <= 70 and rvol > 2 and ema_alignment and vwap_proximity):
            return None

        return {
            "price": round(prices[-1], 2),
            "RSI": rsi,
            "MACD": macd,
            "RVOL": rvol,
            "EMA": {"EMA5": round(ema5, 2), "EMA13": round(ema13, 2), "EMA50": round(ema50, 2)},
            "VWAP": vwap
        }

    except Exception as e:
        print(f"❌ Indicator error for {coin_id}: {e}")
        return None
