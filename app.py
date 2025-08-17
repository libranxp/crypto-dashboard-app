import json
from discover import discover_tickers
from ohlc import fetch_ohlc
from indicators import enrich_indicators
from sentiment import enrich_sentiment
from alerts import send_alerts

def main():
    print("🚀 Starting enrichment pipeline...")

    tickers = discover_tickers()
    print(f"✅ Discovered {len(tickers)} tickers")

    if not tickers:
        print("⚠️ No tickers found. Exiting.")
        return

    ohlc_data = fetch_ohlc(tickers)
    print(f"✅ Fetched OHLC for {len(ohlc_data)} assets")

    enriched = enrich_indicators(ohlc_data)
    print(f"✅ Indicators computed for {len(enriched)} assets")

    enriched = enrich_sentiment(enriched)
    qualified = [a for a in enriched if a.get("qualified")]
    print(f"✅ Qualified assets: {len(qualified)}")

    send_alerts(qualified)

    with open("docs/data.json", "w") as f:
        json.dump(qualified, f, indent=2)
    print("✅ Saved dashboard data to docs/data.json")

if __name__ == "__main__":
    main()
