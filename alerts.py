import json
import os
import time
from datetime import datetime, timedelta
import requests

ALERTS_PATH = "docs/alerts.json"
COOLDOWN_MINUTES = 30

def load_alerts():
    if not os.path.exists(ALERTS_PATH):
        return {}
    with open(ALERTS_PATH, "r") as f:
        return json.load(f)

def save_alerts(alerts):
    with open(ALERTS_PATH, "w") as f:
        json.dump(alerts, f, indent=2)

def should_alert(symbol, price, alerts):
    now = datetime.utcnow()
    history = alerts.get(symbol, {
        "last_alert_price": 0,
        "last_alert_time": "2000-01-01T00:00:00Z"
    })

    last_time = datetime.fromisoformat(history["last_alert_time"].replace("Z", ""))
    if now - last_time < timedelta(minutes=COOLDOWN_MINUTES):
        return False

    if abs(price - history["last_alert_price"]) < 0.5:
        return False

    return True

def update_alert_history(symbol, price, alerts):
    alerts[symbol] = {
        "last_alert_price": price,
        "last_alert_time": datetime.utcnow().isoformat() + "Z"
    }

def send_telegram_alert(symbol, price, indicators, sentiment):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        print("❌ Missing Telegram credentials")
        return

    message = f"""
📣 *Alert: {symbol}*
Price: `${price:.2f}`
RSI: {indicators.get("RSI", "N/A")}
RVOL: {indicators.get("RVOL", "N/A")}
Sentiment: {sentiment.get("score", "N/A")}
""".strip()

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print(f"✅ Alert sent for {symbol}")
        else:
            print(f"⚠️ Telegram error: {response.text}")
    except Exception as e:
        print(f"❌ Telegram exception: {e}")

def process_alert(symbol, price, indicators, sentiment):
    alerts = load_alerts()
    if should_alert(symbol, price, alerts):
        send_telegram_alert(symbol, price, indicators, sentiment)
        update_alert_history(symbol, price, alerts)
        save_alerts(alerts)
    else:
        print(f"⏸ Skipping alert for {symbol} (cooldown or minor move)")
