from discover import discover_tickers
from indicators import compute_indicators
from sentiment import fetch_sentiment
from alert import send_telegram_alert
from save import save_to_dashboard

def run_scan():
    tickers = discover_tickers()
    results = []
    for symbol in tickers:
        try:
            data = compute_indicators(symbol)
            data['sentiment'] = fetch_sentiment(symbol)
            send_telegram_alert(data)
            results.append(data)
        except Exception as e:
            print(f"Error for {symbol}: {e}")
    save_to_dashboard(results)

if __name__ == "__main__":
    run_scan()
