import requests, os

def send_alert(asset):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("⚠️ Telegram credentials missing.")
        return

    msg = f"""📊 *{asset['symbol']} Alert*
Price: ${asset['price']}
RSI: {asset['RSI']} | MACD: {asset['MACD']} | RVOL: {asset['RVOL']}
Sentiment: {asset['sentiment_score']}
TP: ${asset['TP']} | SL: ${asset['SL']}"""

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": msg,
        "parse_mode": "Markdown"
    }

    r = requests.post(url, json=payload)
    if r.status_code != 200:
        print(f"❌ Telegram error: {r.text}")
    else:
        print(f"✅ Alert sent for {asset['symbol']}")
