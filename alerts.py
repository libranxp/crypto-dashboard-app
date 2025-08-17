import requests

TELEGRAM_TOKEN = "your_token_here"
TELEGRAM_CHAT_ID = "your_chat_id_here"

def send_alerts(assets):
    for asset in assets:
        msg = (
            f"📈 *{asset['symbol']}* Alert\n"
            f"Price: ${asset['price']}\n"
            f"RSI: {asset['rsi']} | RVOL: {asset['rvol']}\n"
            f"TP: ${asset['tp_price']} | SL: ${asset['sl_price']}\n"
            f"Risk Ratio: {asset['risk_ratio']}\n"
            f"Sentiment: {asset['sentiment_score']}\n"
            f"[View Chart](https://www.tradingview.com/symbols/{asset['symbol'].upper()}USDT)"
        )
        try:
            requests.post(
                f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
                data={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "Markdown"}
            )
        except Exception as e:
            print(f"❌ Telegram error for {asset['symbol']}: {e}")
