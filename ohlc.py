from sources.coingecko import fetch_coingecko_ohlc

def fetch_ohlc(tickers):
    result = {}
    for coin_id in tickers:
        try:
            result[coin_id] = fetch_coingecko_ohlc(coin_id)
        except Exception as e:
            print(f"❌ OHLC fetch failed for {coin_id}: {e}")
    return result
