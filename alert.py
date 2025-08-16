import requests, os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_alert(asset):
    msg = f"""📊 *{asset['symbol'].upper()} Alert*
Price: ${asset['price']}
RSI: {asset['RSI']} | MACD: {asset['MACD']} | RVOL: {asset['RVOL']}
Sentiment: {asset['sentiment_score']}
TP: ${asset['TP']} | SL: ${asset['SL']}"""
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)
