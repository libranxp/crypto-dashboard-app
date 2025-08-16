import time
import json
import os

def send_telegram_alert(asset):
    last_alerts = {}
    if os.path.exists("docs/alerts.json"):
        with open("docs/alerts.json") as f:
            last_alerts = json.load(f)

    now = time.time()
    last_time = last_alerts.get(asset["id"], 0)
    if now - last_time < 21600:  # 6 hours
        print(f"⏱️ Skipping duplicate alert for {asset['id']}")
        return

    # Replace with actual Telegram bot logic
    print(f"📣 Alert: {asset['id']} @ ${asset['price']} | RSI: {asset['RSI']} | RVOL: {asset['RVOL']}")

    last_alerts[asset["id"]] = now
    with open("docs/alerts.json", "w") as f:
        json.dump(last_alerts, f)
