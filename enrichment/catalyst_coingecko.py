import requests

def get_price(coin_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": coin_id,
        "vs_currencies": "usd"
    }
    res = requests.get(url, params=params).json()
    return round(res.get(coin_id, {}).get("usd", 0), 2)
