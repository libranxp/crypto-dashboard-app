import requests, os

def enrich_sentiment(symbol):
    key = os.getenv("API_KEY_SANTIMENT")
    url = "https://api.santiment.net/graphql"
    headers = {"Authorization": f"Bearer {key}"}
    query = {
        "query": """
        {
          getMetric(metric: "sentiment_positive_total") {
            timeseriesData(slug: "%s", from: "now-1d", to: "now", interval: "1d") {
              value
            }
          }
        }
        """ % symbol.lower()
    }
    r = requests.post(url, json=query, headers=headers).json()
    try:
        return r["data"]["getMetric"]["timeseriesData"][0]["value"]
    except:
        return 0
