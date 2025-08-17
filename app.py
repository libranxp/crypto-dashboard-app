import json
from scanner import get_dynamic_tickers
from ohlc import fetch_ohlc_data
from indicators import compute_indicators
from news import fetch_sentiment
from alerts import process_alert

def enrich_asset(symbol):
    print(f"🔍 Enriching {symbol}")
    try:
        ohlc = fetch_ohlc_data(symbol)
        if not ohlc:
            print(f"⚠️ Skipping {symbol}: no OHLC data")
            return None

        indicators = compute_indicators(ohlc)
        sentiment = fetch_sentiment(symbol)

        if not indicators or not sentiment:
            print(f"⚠️ Skipping {symbol}: failed filters")
            return None

        return {
            "symbol": symbol,
            "price": ohlc[-1]["close"],
            "indicators": indicators,
            "sentiment": sentiment
        }

    except Exception as e:
        print(f"⚠️
