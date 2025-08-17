import requests, json, os
from datetime import datetime, timedelta

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
ALERTS_FILE = "docs/alerts.json"

def load_alerts():
    if os.path.exists(ALERTS_FILE):
        with open(ALERTS_FILE) as f:
            return json.load(f)
    return {}

def save_alerts(data):
    with open(ALERTS_FILE, "w") as f:
        json.dump(data, f)

def send_alerts(assets):
    alerts = load_alerts()
    now = datetime.utcnow()

    for a in assets:
        symbol = a["symbol"]
        last = alerts.get(symbol)
        if last and (now - datetime.fromisoformat(last)) < timedelta(minutes=30):
            continue

        msg = (
            f"📣 *{symbol}* @ ${a['price']}\n"
            f"RSI: {a['rsi']} | RVOL: {a['rvol']}\n"
            f"TP: ${a['tp_price']} | SL: ${a['sl_price']}\n"
            f"Sentiment: {a['sentiment']} | Tags: {', '.join(a['tags'])}"
        )
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"}
        requests.post(url, data=payload)

        alerts[symbol] = now.isoformat()

    save_alerts(alerts)
