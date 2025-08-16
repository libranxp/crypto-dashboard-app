import json
from scanner import get_dynamic_tickers
from ohlc import fetch_ohlc_data
from indicators import compute_indicators
from news import fetch_sentiment
from resolve_symbol import resolve_symbol
from alerts import process_alert

def enrich_asset(symbol):
    print(f"🔍 Enriching {symbol}")
    try:
        ohlc = fetch_ohlc_data(symbol)
        if not ohlc:
            print(f"⚠️ Skipping {symbol}: no OHLC data")
            return None

        indicators = compute_indicators(ohlc)
        sentiment = fetch_sentiment(symbol)
        resolved = resolve_symbol(symbol)

        return {
            "symbol": symbol,
            "price": ohlc[-1]["close"],
            "indicators": indicators,
            "sentiment": sentiment,
            "resolved": resolved
        }

    except Exception as e:
        print(f"⚠️ Skipping {symbol}: {e}")
        return None

def main():
    tickers = get_dynamic_tickers()
    print(f"✅ Scanner found {len(tickers)} tickers")

    enriched = []
    for symbol in tickers:
        asset = enrich_asset(symbol)
        if asset:
            enriched.append(asset)
            process_alert(
                symbol=asset["symbol"],
                price=asset["price"],
                indicators=asset["indicators"],
                sentiment=asset["sentiment"]
            )

    with open("docs/data.json", "w") as f:
        json.dump(enriched, f, indent=2)
    print(f"✅ Saved {len(enriched)} assets to docs/data.json")

if __name__ == "__main__":
    main()
