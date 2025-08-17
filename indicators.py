def enrich_indicators(ohlc_data):
    enriched = []

    for symbol, data in ohlc_data.items():
        try:
            rsi = compute_rsi(data)
            rvol = compute_rvol(data)
            pump = detect_pump(data)

            qualified = rsi > 40 and rvol > 1 and not pump

            enriched.append({
                "symbol": symbol,
                "rsi": rsi,
                "rvol": rvol,
                "pump": pump,
                "qualified": qualified
            })
        except Exception as e:
            print(f"❌ Error processing {symbol}: {e}")

    return enriched
