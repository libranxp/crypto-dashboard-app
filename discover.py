import requests, os

def discover_tickers():
    url = f"https://www.alphavantage.co/query?function=LISTING_STATUS&apikey={os.getenv('API_KEY_ALPHA')}"
    r = requests.get(url).text
    lines = r.splitlines()[1:]
    tickers = []
    for line in lines:
        cols = line.split(',')
        symbol = cols[0]
        name = cols[1].lower()
        if "crypto" in name or "blockchain" in name:
            tickers.append(symbol)
    return tickers[:10]  # Limit for performance
