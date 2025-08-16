import requests, os

def fetch_lunarcrush_sentiment(symbol):
    key = os.getenv("API_KEY_LUNARCRUSH")
    url = f"https://api.lunarcrush.com/v2?data=assets&key={key}&symbol={symbol}"
    try:
        res = requests.get(url).json()
        asset = res.get('data', [{}])[0]
        return {
            'galaxy_score': asset.get('galaxy_score'),
            'alt_rank': asset.get('alt_rank'),
            'volatility': asset.get('volatility'),
            'social_score': asset.get('social_score')
        }
    except Exception as e:
        return {'error': str(e)}
