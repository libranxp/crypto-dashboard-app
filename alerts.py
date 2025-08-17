import os
import requests

def send_alerts(assets):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("❌ Missing Telegram credentials")
        return

    if not assets:
        print("⚠️ No qualified assets to alert")
        return

    for asset in assets:
        msg = format_alert(asset)
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        payload = {"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"}

        try:
            r = requests.post(url, json=payload)
            if r.status_code == 200:
                print(f"📣 Alert sent for {asset['symbol']}")
            else:
                print(f"❌ Failed to send alert for {asset['symbol']}: {r.text}")
        except Exception as e:
            print(f"❌ Exception sending alert: {e}")

def format_alert(asset):
    return (
        f"*{asset['symbol']}* triggered:\n"
        f"Price: ${asset['price']}\n"
        f"RSI: {asset['rsi']} | RVOL: {asset['rvol']}\n"
        f"TP: ${asset['tp_price']} | SL: ${asset['sl_price']} | Risk: {asset['risk_ratio']}\n"
        f
