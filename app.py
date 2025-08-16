from discover import discover_tickers
from indicators import compute_indicators
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
            data = compute_indicators(symbol)
            data['sentiment_lunar'] = fetch_lunarcrush_sentiment(symbol)
            data['sentiment_santiment'] = fetch_santiment_data(symbol)
            data['news'] = fetch_news(symbol)
            data['catalyst'] = fetch_catalysts(symbol)
            send_telegram_alert(data)
            results.append(data)
        except Exception as e:
            results.append({'symbol': symbol, 'error': str(e)})

    save_to_dashboard(results)

if __name__ == "__main__":
    run_scan()
