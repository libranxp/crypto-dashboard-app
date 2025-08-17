from modules.utils import compute_rsi, compute_rvol, detect_pump
from sources.coingecko import fetch_asset_type

def enrich_indicators(ohlc_data):
    enriched = []
    for symbol, data in ohlc_data.items():
        try:
            if not data or all(c.get("volume", 0) == 0 for c in data):
                continue

            rsi = compute_rsi(data)
            rvol = compute_rvol(data)
            pump = detect_pump(data)
            price = data[-1]["close"]

            tp = round(price * 1.1, 4)
            sl = round(price * 0.95, 4)
            risk = round((tp - price) / max(price - sl, 0.0001), 2)
            qualified = bool(rsi > 30 and rvol > 0.5 and not pump)

            asset_type = fetch_asset_type(symbol)

            ohlc_clean = [
                {"t": int(c["timestamp"] / 1000), "c": c["close"], "v": c["volume"]}
                for c in data
            ]

            enriched.append({
                "symbol": symbol,
                "price": round(price, 4),
                "rsi": round(rsi, 2),
                "rvol": round(rvol, 2),
                "pump": pump,
                "tp_price": tp,
                "sl_price": sl,
                "risk_ratio": risk,
                "qualified": qualified,
                "asset_type": asset_type,
                "ohlc": ohlc_clean
            })
        except Exception as e:
            print(f"❌ Error processing {symbol}: {e}")
    return enriched
