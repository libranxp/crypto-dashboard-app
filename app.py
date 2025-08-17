from scanner import discover_tickers
from ohlc import fetch_ohlc
from indicators import enrich_indicators
from news import enrich_sentiment
from alerts import send_alerts
import json

def main():
    tickers = discover_tickers()
    ohlc_data = fetch_ohlc(tickers)
    enriched = enrich_indicators(ohlc_data)
    enriched = enrich_sentiment(enriched)
    qualified = [a for a in enriched if a.get("qualified")]

    send_alerts(qualified)

    with open("docs/data.json", "w") as f:
        json.dump(qualified, f, indent=2)

if __name__ == "__main__":
    main()
