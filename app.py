from scanner import scan_tickers
from indicators import get_indicators
from enrichment.news_newsapi import get_news_score
from alert import send_alert
from save import save_to_json

def enrich(symbol):
    print(f"🔍 Enriching {symbol}")
    try:
        indicators = get_indicators(symbol)
        news_score = get_news_score(symbol)

        if not indicators or news_score is None or news_score < 0.6:
            print(f"⚠️ Skipping {symbol} due to missing or weak data")
            return None

        TP = round(indicators["price"] * 1.1, 2)
        SL = round(indicators["price"] * 0.9, 2)

        asset = {
            "symbol": symbol,
            "price": indicators["price"],
            "RSI": indicators["RSI"],
            "MACD": indicators["MACD"],
            "RVOL": indicators["RVOL"],
            "EMA": indicators["EMA"],
            "VWAP": indicators["VWAP"],
            "news_score": news_score,
            "TP": TP,
            "SL": SL
        }

        send_alert(asset)
        return asset
    except Exception as e:
        print(f"❌ Error enriching {symbol}: {e}")
        return None

def main():
    tickers = scan_tickers()
    print(f"✅ Scanner found {len(tickers)} qualifying tickers")

    enriched = []
    for symbol in tickers:
        asset = enrich(symbol)
        if asset:
            enriched.append(asset)

    save_to_json(enriched)

if __name__ == "__main__":
    main()
