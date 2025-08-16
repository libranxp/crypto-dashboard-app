import os, requests

def format_alert(data):
    return (
        f"📣 {data['symbol']} Alert\n"
        f"💰 Price: {data['price']} | TP: {data['TP']} | SL: {data['SL']}\n"
        f"📊 RSI: {data['RSI']} | EMA: {data['EMA']} | VWAP: {data['VWAP']}\n"
        f"📈 MACD: {data['MACD']} | RVOL: {data['RVOL']}\n"
        f"🧠 Sentiment: {data.get('sentiment_lunar', {}).get('galaxy_score', 'N/A')}\n"
        f"📰 News: {data.get('news', [{}])[0].get('title', 'No news')}"
    )

def send_telegram_alert(data):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    message = format_alert(data)
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={'chat_id': chat_id, 'text': message})
