from sources.coingecko import fetch_coingecko_symbols

def discover_tickers():
    print("🔍 Discovering tickers from CoinGecko...")
    tickers = fetch_coingecko_symbols()

    # Optional filtering logic
    filtered = [t for t in tickers if "-" not in t and len(t) <= 15]
    print(f"✅ Discovered {len(filtered)} filtered tickers")
    return filtered
