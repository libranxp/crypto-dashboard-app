from sources.coingecko import fetch_coingecko_symbols
from sources.paprika import fetch_paprika_symbols

def discover_tickers():
    cg = fetch_coingecko_symbols()
    cp = fetch_paprika_symbols()
    combined = sorted(set(cg + cp))
    return [s for s in combined if len(s) >= 3]
