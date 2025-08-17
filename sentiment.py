def enrich_sentiment(assets):
    for asset in assets:
        try:
            asset["sentiment"] = fetch_sentiment(asset["symbol"])
        except Exception as e:
            print(f"⚠️ Sentiment failed for {asset['symbol']}: {e}")
            asset["sentiment"] = "N/A"
    return assets
