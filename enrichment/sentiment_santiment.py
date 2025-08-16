import requests, os

def fetch_santiment_data(symbol):
    key = os.getenv("API_KEY_SANTIMENT")
    url = "https://api.santiment.net/graphql"
    headers = {"Authorization": f"Bearer {key}"}
    query = """
    {
      getMetric(metric: "social_volume_total") {
        timeseriesData(slug: "%s", from: "now-1d", to: "now", interval: "1h") {
          datetime
          value
        }
      }
    }
    """ % symbol.lower()

    try:
        res = requests.post(url, json={'query': query}, headers=headers).json()
        data = res.get('data', {}).get('getMetric', {}).get('timeseriesData', [])
        return {'social_volume': data}
    except Exception as e:
        return {'error': str(e)}
