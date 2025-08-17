from sources.coingecko import fetch_coingecko_ohlc
from sources.paprika import fetch_paprika_ohlc

def fetch_ohlc_data(tickers):
    result = {}
    for coin_id in tickers:
        try:
            result[coin_id] = fetch_coingecko_ohlc(coin_id)
        except Exception as e1:
            print(f"⚠️ CoinGecko failed for {coin_id}: {e1}")
            try:
                result[coin_id] = fetch_paprika_ohlc(coin_id)
                print(f"✅ Fallback success for {coin_id} via CoinPaprika")
            except Exception as e2:
                print(f"❌ OHLC fetch failed for {coin_id}: {e2}")
    return result
