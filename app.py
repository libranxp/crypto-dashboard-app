from flask import Flask, jsonify, request
from indicators import compute_indicators
from alert import send_telegram_alert
from discover import discover_tickers

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    tickers = request.json.get('tickers') or discover_tickers()
    results = []
    for symbol in tickers:
        try:
            data = compute_indicators(symbol)
            send_telegram_alert(data)
            results.append(data)
        except Exception as e:
            results.append({'symbol': symbol, 'error': str(e)})
    return jsonify(results)

@app.route('/')
def home():
    return "Dashboard backend is running."

if __name__ == '__main__':
    app.run(debug=False)
