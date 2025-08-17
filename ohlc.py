from sources.coingecko import fetch_ohlc_coingecko
from sources.paprika import fetch_ohlc_paprika

def fetch_ohlc_data(tickers):
    data = {}
    for symbol in tickers:
        try:
            cg = fetch_ohlc_coingecko(symbol)
            if cg:
                data[symbol] = cg
                continue
            cp = fetch_ohlc_paprika(symbol)
            if cp:
                data[symbol] = cp
        except Exception as e:
            print(f"❌ OHLC error for {symbol}: {e}")
    return data
