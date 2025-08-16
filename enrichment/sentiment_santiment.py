import requests, os

API_KEY = os.getenv("API_KEY_SANTIMENT")

def get_santiment_sentiment(symbol):
    url = f"https://api.santiment.net/graphql"
    headers = {"Authorization": f"Apikey {API_KEY}"}
    query = {
        "query": f"""
        {{
          getMetric(metric: "sentiment_positive_total") {{
            timeseriesData(
              slug: "{symbol.lower()}"
              from: "now-1d"
              to: "now"
              interval: "1d"
            ) {{
              value
            }}
          }}
        }}
        """
    }
    res = requests.post(url, json=query, headers=headers).json()
    try:
        val = res["data"]["getMetric"]["timeseriesData"][0]["value"]
        return round(float(val), 2)
    except:
        return None
