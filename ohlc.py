import requests
import os
from resolve_symbol import resolve_cc_symbol

def get_ohlc_from_coingecko(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": 1, "interval": "hourly"}
    try:
        res = requests.get(url, params=params).json()
        prices = [p[1] for p in res.get("prices", [])]
        volumes = [v[1] for v in res.get("total_volumes", [])]
        if len(prices) >= 30 and len(volumes) >= 30:
            return prices, volumes
    except Exception:
        pass
    return None, None

def get_ohlc_from_cryptocompare(symbol):
    url = f"https://min-api.cryptocompare.com/data/v2/histohour"
    headers = {"authorization": f"Apikey {os.getenv('CRYPTOCOMPARE_API_KEY')}"}
    params = {"fsym": symbol.upper(), "tsym": "USD", "limit": 50}
    try:
        res = requests.get(url, headers=headers, params=params).json()
        data = res.get("Data", {}).get("Data", [])
        prices = [c["close"] for c in data]
        volumes = [c["volumeto"] for c in data]
        if len(prices) >= 30:
            return prices, volumes
    except Exception:
        pass
    return None, None

def get_ohlc(coin_id):
    prices, volumes = get_ohlc_from_coingecko(coin_id)
    if prices: return prices, volumes

    cc_symbol = resolve_cc_symbol(coin_id)
    if cc_symbol:
        prices, volumes = get_ohlc_from_cryptocompare(cc_symbol)
        if prices: return prices, volumes

    return None, None
