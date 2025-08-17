import requests

def fetch_coingecko_symbols():
    url = "https://api.coingecko.com/api/v3/coins/list"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        symbols = []
        for coin in data:
            if "id" in coin:
                symbols.append(coin["id"])
        return symbols

    except Exception as e:
        print(f"❌ CoinGecko symbol fetch failed: {e}")
        return []
