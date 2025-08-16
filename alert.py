import requests, os

def send_telegram_alert(data):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("⚠️ Telegram credentials missing.")
        return

    msg = (
        f"🚨 {data['symbol']} Alert\n"
        f"💰 Price: {data['price']} | TP: {data['TP']} | SL: {data['SL']}\n"
        f"📊 RSI: {data['RSI']} | EMA: {data['EMA']} | VWAP: {data['VWAP']}\n"
        f"📈 MACD: {data['MACD']} | RVOL: {data['RVOL']}\n"
        f"🧠 Sentiment Score: {data['sentiment_score']:.2f}\n"
    )

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    r = requests.post(url, data={"chat_id": chat_id, "text": msg})
    if r.status_code != 200:
        print(f"❌ Telegram alert failed: {r.text}")
