from discover import discover_tickers
from indicators import get_indicators
from enrichment.catalyst_coingecko import get_price
from enrichment.news_newsapi import get_news_score
from alert import send_alert
from save import save_to_json

def enrich(symbol):
    print(f"🔍 Enriching {symbol}")
    try:
        price = get_price(symbol)
        indicators = get_indicators(symbol)
        news_score = get_news_score(symbol)

        if not price or not indicators or news_score is None:
            print(f"⚠️ Skipping {symbol} due to missing data")
            return None

        TP = round(price * 1.1, 2)
        SL = round(price * 0.9, 2)

        asset = {
            "symbol": symbol,
            "price": price,
            "RSI": indicators["RSI"],
            "MACD": indicators["MACD"],
            "RVOL": indicators["RVOL"],
            "news_score": news_score,
            "TP": TP,
            "SL": SL
        }

        if asset["RSI"] < 30 and asset["MACD"] > 0 and asset["RVOL"] > 2 and asset["news_score"] > 0.5:
            print(f"📣 Sending alert for {symbol}")
            send_alert(asset)

        return asset
    except Exception as e:
        print(f"❌ Error enriching {symbol}: {e}")
        return None

def main():
    tickers = discover_tickers()
    print(f"✅ Discovered {len(tickers)} tickers")

    enriched = []
    for symbol in tickers:
        asset = enrich(symbol)
        if asset:
            enriched.append(asset)

    save_to_json(enriched)
    print(f"✅ Saved {len(enriched)} assets to docs/data.json")

if __name__ == "__main__":
    main()
