import requests

def fetch_catalysts(symbol):
    try:
        url = f"https://api.coingecko.com/api/v3/coins/{symbol.lower()}/events"
        res = requests.get(url).json()
        events = res.get('data', [])[:3]
        return [{'title': e['title'], 'description': e['description'], 'date': e['start_date']} for e in events]
    except Exception as e:
        return {'error': str(e)}
