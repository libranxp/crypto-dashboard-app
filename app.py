from discover import discover_tickers
from sources.ohlc import fetch_ohlc_data
from modules.indicators import enrich_indicators
from sentiment import enrich_sentiment
from alerts import send_alerts
from dashboard import save_dashboard

print("🚀 Starting enrichment pipeline...")

tickers = discover_tickers()
print(f"✅ Discovered {len(tickers)} tickers")

ohlc_data = fetch_ohlc_data(tickers)
enriched = enrich_indicators(ohlc_data)
enriched = enrich_sentiment(enriched)
qualified = [a for a in enriched if a["qualified"]]

send_alerts(qualified)
save_dashboard(enriched)

print(f"📊 Final dashboard contains {len(enriched)} assets")
print("✅ Pipeline complete")
