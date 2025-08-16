import requests

def get_price(symbol):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": symbol.lower(),
        "vs_currencies": "usd"
    }
    try:
        res = requests.get(url, params=params).json()
        price = res.get(symbol.lower(), {}).get("usd")
        if price:
            print(f"✅ Price for {symbol}: ${price}")
        return price
    except Exception as e:
        print(f"❌ Price fetch error for {symbol}: {e}")
        return None
