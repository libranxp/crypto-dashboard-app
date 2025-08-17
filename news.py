def fetch_sentiment(symbol):
    try:
        mentions = 12
        engagement = 150
        sentiment_score = 0.65
        influencer_flag = True

        if mentions >= 10 and engagement >= 100 and sentiment_score >= 0.6 and influencer_flag:
            return {
                "score": sentiment_score,
                "mentions": mentions,
                "engagement": engagement,
                "influencer": influencer_flag
            }
    except Exception:
        pass
    return None
