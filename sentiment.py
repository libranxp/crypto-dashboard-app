import requests

def fetch_sentiment(symbol):
    url = f"https://api.coingecko.com/api/v3/search/trending"
    r = requests.get(url).json()
    trending = [coin['item']['symbol'].upper() for coin in r['coins']]
    score = 1 if symbol in trending else 0
    return score
