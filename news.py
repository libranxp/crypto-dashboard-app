import random

def enrich_sentiment(assets):
    for a in assets:
        mentions = random.randint(0, 50)
        engagement = random.randint(0, 500)
        influencer = random.choice([True, False])
        sentiment = round(random.uniform(0.3, 0.9), 2)

        a.update({
            "mentions": mentions,
            "engagement": engagement,
            "influencer": influencer,
            "sentiment": sentiment
        })

        if a["qualified"]:
            a["qualified"] = (
                mentions >= 10 and
                engagement >= 100 and
                sentiment >= 0.6
            )
    return assets
