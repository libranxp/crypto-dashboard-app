from sources.coingecko import fetch_ohlc_coingecko
from sources.paprika import fetch_ohlc_paprika

def fetch_ohlc_data(tickers):
    result = {}
    for symbol in tickers:
        try:
            data = fetch_ohlc_coingecko(symbol)
            if data:
                result[symbol] = data
                continue
            data = fetch_ohlc_paprika(symbol)
            if data:
                result[symbol] = data
        except Exception as e:
            print(f"❌ OHLC fetch failed for {symbol}: {e}")
    return result
