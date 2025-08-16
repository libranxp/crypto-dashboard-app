import requests

def resolve_cc_symbol(coin_name):
    url = "https://min-api.cryptocompare.com/data/all/coinlist"
    try:
        res = requests.get(url).json()
        data = res.get("Data", {})
        for symbol, info in data.items():
            if coin_name.lower() in [info.get("Name", "").lower(), info.get("CoinName", "").lower()]:
                return symbol
        return None
    except Exception:
        return None
