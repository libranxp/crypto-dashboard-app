import requests

def get_indicators(coin_id):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": 2,
            "interval": "hourly"
        }
        res = requests.get(url, params=params).json()
        prices = [p[1] for p in res.get("prices", [])]
        volumes = [v[1] for v in res.get("total_volumes", [])]

        if len(prices) < 30 or len(volumes) < 2:
            print(f"⚠️ Not enough data for {coin_id}")
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

        # RVOL
        current_volume = volumes[-1]
        avg_volume = sum(volumes[-30:-1]) / 29
        rvol = round(current_volume / avg_volume, 2)

        return {
            "price": round(prices[-1], 2),
            "RSI": rsi,
            "MACD": macd,
            "RVOL": rvol
        }

    except Exception as e:
        print(f"❌ Indicator error for {coin_id}: {e}")
        return None
