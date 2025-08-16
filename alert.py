import requests, os

def send_telegram_alert(data):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    msg = (
        f"🚨 {data['symbol']} Alert\n"
        f"💰 Price: {data['price']} | TP: {data['TP']} | SL: {data['SL']}\n"
        f"📊 RSI: {data['RSI']} | EMA: {data['EMA']} | VWAP: {data['VWAP']}\n"
        f"📈 MACD: {data['MACD']} | RVOL: {data['RVOL']}\n"
        f"🧠 Sentiment Score: {data['sentiment_score']:.2f}\n"
    )
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chat_id, "text": msg})
