import os
import requests

def send_alerts(assets):
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if not token or not chat_id:
        print("❌ Missing Telegram credentials")
        return

    for asset in assets:
        msg = (
            f"📈 *{asset['symbol'].upper()}* Alert\n"
            f"Type: {asset['asset_type']}\n"
            f"Price: ${asset['price']}\n"
            f"RSI: {asset['rsi']} | RVOL: {asset['rvol']}\n"
            f"TP: ${asset['tp_price']} | SL: ${asset['sl_price']}\n"
            f"Risk Ratio: {asset['risk_ratio']}\n"
            f"[View on CoinGecko](https://www.coingecko.com/en/coins/{asset['symbol']})"
        )
        try:
            r = requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data={"chat_id": chat_id, "text": msg, "parse_mode": "Markdown"}
            )
            if r.status_code == 200:
                print(f"📣 Alert sent for {asset['symbol']}")
            else:
                print(f"❌ Telegram error for {asset['symbol']}: {r.text}")
        except Exception as e:
            print(f"❌ Telegram exception for {asset['symbol']}: {e}")
