def fetch_ohlc(tickers):
    result = {}
    for symbol in tickers:
        try:
            result[symbol] = fetch_from_primary(symbol)
        except:
            try:
                result[symbol] = fetch_from_fallback(symbol)
            except Exception as e:
                print(f"❌ OHLC fetch failed for {symbol}: {e}")
    return result
