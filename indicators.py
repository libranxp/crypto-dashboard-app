import requests

def get_indicators(coin_id):
    try:
        # Fetch OHLC data
        ohlc_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/ohlc"
        ohlc_params = {"vs_currency": "usd", "days": 1}
        ohlc_res = requests.get(ohlc_url, params=ohlc_params).json()

        if not ohlc_res or len(ohlc_res) < 30:
            print(f"⚠️ Not enough OHLC data for {coin_id}")
            return None

        closes = [candle[4] for candle in ohlc_res]  # Close prices

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

        # Fetch current price and volume
        market_url = "https://api.coingecko.com/api/v3/coins/markets"
        market_params = {
            "vs_currency": "usd",
            "ids": coin_id,
            "order": "market_cap_desc",
            "per_page": 1,
            "page": 1,
            "sparkline": False
        }
        market_res = requests.get(market_url, params=market_params).json()
        if not market_res:
            print(f"⚠️ Market data missing for {coin_id}")
            return None

        market_data = market_res[0]
        price = round(market_data["current_price"], 2)
        volume = market_data["total_volume"]
        avg_volume = sum([candle[5] for candle in ohlc_res]) / len(ohlc_res)
        rvol = round(volume / avg_volume, 2) if avg_volume else 0.0

        return {
            "price": price,
            "RSI": rsi,
            "MACD": macd,
            "RVOL": rvol
        }

    except Exception as e:
        print(f"❌ Indicator error for {coin_id}: {e}")
        return None
