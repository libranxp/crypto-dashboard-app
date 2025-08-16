from scanner import discover_tickers
from indicators import get_indicators
from news import get_news_score
from alerts import send_telegram_alert
import json

def run():
    tickers = discover_tickers()
    enriched = []

    for coin in tickers:
        coin_id = coin["id"]
        print(f"🔍 Enriching {coin_id}")

        indicators = get_indicators(coin_id)
        news = get_news_score(coin_id)

        if not indicators or not news:
            print(f"⚠️ Sk
