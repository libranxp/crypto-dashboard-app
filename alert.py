import requests
import os

def send_telegram_alert(data):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("Telegram credentials missing.")
        return

    msg = f"🚨 Signal: {data['symbol']}\n"
    msg += f"📈 RSI: {data['rsi']:.2f}\n"
    msg += f"📊 MACD: {data['macd']:.2f}\n"
    msg += f"🧠 Sentiment: {data['sentiment_score']:.2f}\n"
    msg += f"🔗 [View Chart](https://www.tradingview.com/symbols/{data['symbol']})"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Telegram error: {response.text}")
