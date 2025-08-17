from discover import discover_tickers
from sources.ohlc import fetch_ohlc_data
from modules.indicators import enrich_indicators
from alerts import send_alerts
import json

def main():
    print("🚀 Discovering tickers...")
    tickers = discover_tickers()
    print(f"✅ Found {len(tickers)} tickers")

    print("📊 Fetching OHLC data...")
    ohlc_data = fetch_ohlc_data(tickers)

    print("🧠 Enriching indicators...")
    enriched = enrich_indicators(ohlc_data)

    print("📣 Sending alerts...")
    send_alerts([a for a in enriched if a["qualified"]])

    print("💾 Saving dashboard data...")
    with open("docs/data.json", "w") as f:
        json.dump(enriched, f, indent=2)

if __name__ == "__main__":
    main()
