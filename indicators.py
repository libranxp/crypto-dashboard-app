from utils.indicators import compute_rsi, compute_rvol, detect_pump

def enrich_indicators(ohlc_data):
    enriched = []
    for symbol, data in ohlc_data.items():
        try:
            if not data or all(c["volume"] == 0 for c in data):
                continue
            rsi = compute_rsi(data)
            rvol = compute_rvol(data)
            pump = detect_pump(data)
            price = data[-1]["close"]
            tp = round(price * 1.1, 4)
            sl = round(price * 0.95, 4)
            risk = round((tp - price) / (price - sl), 2)
            qualified = rsi > 30 and rvol > 0.5 and not pump
            enriched.append({
                "symbol": symbol,
                "price": price,
                "rsi": rsi,
                "rvol": rvol,
                "pump": pump,
                "tp_price":
