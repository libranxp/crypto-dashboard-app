from sources.coingecko import fetch_coingecko_symbols

def discover_tickers(limit=50):
    symbols = fetch_coingecko_symbols()
    return symbols[:limit] if symbols else []
