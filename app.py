from discover import get_top_tickers
from indicators import get_indicators
from sentiment import get_sentiment
from enrichment.catalyst_coingecko import get_price
from enrichment.news_newsapi import get_news_score
from save import save_to_json
from alert import send_alert

def enrich(coin_id):
    symbol = coin_id.upper()
    try:
        price = get_price(coin_id)
        indicators = get_indicators(symbol)
        sentiment_score = get_sentiment(symbol)
        news_score = get_news_score(symbol)

        if not indicators or not price:
            return None

        TP = round(price * 1.1, 2)
        SL = round(price * 0.9, 2)

        asset = {
            "symbol": symbol,
            "price": price,
            "RSI": indicators["RSI"],
            "MACD": indicators["MACD"],
            "RVOL": indicators["RVOL"],
            "sentiment_score": sentiment_score,
            "TP": TP,
            "SL": SL
        }

        send_alert(asset)
        return asset
    except Exception as e:
        print(f"❌ Error enriching {symbol}: {e}")
        return None

def main():
    tickers = get_top_tickers()
    enriched = []

    for coin_id in tickers:
        asset = enrich(coin_id)
        if asset:
            enriched.append(asset)

    save_to_json(enriched)
    print(f"✅ Saved {len(enriched)} assets")

if __name__ == "__main__":
    main()
