import json
from discover import discover_tickers
from indicators import compute_indicators
from sentiment import enrich_sentiment
from enrichment.sentiment_lunarcrush import fetch_lunarcrush_sentiment
from enrichment.sentiment_santiment import fetch_santiment_data
from enrichment.news_newsapi import fetch_news
from enrichment.catalyst_coingecko import fetch_catalysts
from alert import send_telegram_alert
from save import save_to_dashboard

def run_scan():
    tickers = discover_tickers()
    results = []

    for symbol in tickers:
        try:
            indicators = compute_indicators(symbol)
            sentiment = enrich_sentiment(symbol)
            lunar = fetch_lunarcrush_sentiment(symbol)
            santiment = fetch_santiment_data(symbol)
            news = fetch_news(symbol)
            catalysts = fetch_catalysts(symbol)

            enriched = {
                **indicators,
                "sentiment_score": sentiment,
                "lunarcrush": lunar,
                "santiment": santiment,
                "news": news,
                "catalysts": catalysts
            }

            if indicators["RSI"] < 30 and indicators["MACD"] == "Bullish" and indicators["RVOL"] > 2 and sentiment > 0.5:
                send_telegram_alert(enriched)

            results.append(enriched)

        except Exception as e:
            results.append({"symbol": symbol, "error": str(e)})

    save_to_dashboard(results)

if __name__ == "__main__":
    run_scan()
