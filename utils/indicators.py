import numpy as np

def compute_rsi(data, period=14):
    closes = [c["close"] for c in data]
    if len(closes) < period + 1:
        return 0
    deltas = np.diff(closes)
    gains = np.maximum(deltas, 0)
    losses = np.abs(np.minimum(deltas, 0))
    avg_gain = np.mean(gains[-period:])
    avg_loss = np.mean(losses[-period:])
    rs = avg_gain / avg_loss if avg_loss else 0.01
    return round(100 - (100 / (1 + rs)), 2)

def compute_rvol(data, window=20):
    volumes = [c["volume"] for c in data]
    if len(volumes) < window:
        return 0
    recent = volumes[-1]
    avg = np.mean(volumes[-window:])
    return round(recent / avg, 2) if avg else 0

def detect_pump(data, threshold=1.2):
    closes = [c["close"] for c in data]
    if len(closes) < 2:
        return False
    return closes[-1] / closes[-2] > threshold
