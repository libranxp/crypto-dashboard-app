def enrich_indicators(ohlc_data):
    enriched = []

    for coin_id, data in ohlc_data.items():
        try:
            rsi = compute_rsi(data)
            rvol = compute_rvol(data)
            pump = detect_pump(data)

            qualified = rsi > 40 and rvol > 1 and not pump

            enriched.append({
                "symbol": coin_id,
                "rsi": rsi,
                "rvol": rvol,
                "pump": pump,
                "qualified": qualified
            })
        except Exception as e:
            print(f"❌ Error processing {coin_id}: {e}")

    return enriched
