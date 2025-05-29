import requests
from indicators.ema import calculate_ema
from indicators.macd import calculate_macd
from indicators.rsi import calculate_rsi
from indicators.volume_spike import detect_volume_spike
from indicators.supertrend import calculate_supertrend
from indicators.fibonacci import get_fibonacci_levels
from indicators.candlestick import detect_candlestick_pattern

# === Konfigurasi ===
symbol = "BTCUSDT"
interval = "1h"
limit = 100

def get_klines(symbol, interval, limit=100):
    url = f"https://fapi.binance.com/fapi/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"
    res = requests.get(url).json()
    o, h, l, c, v = [], [], [], [], []
    for candle in res:
        o.append(float(candle[1]))
        h.append(float(candle[2]))
        l.append(float(candle[3]))
        c.append(float(candle[4]))
        v.append(float(candle[5]))
    return o, h, l, c, v

def analyze():
    open_prices, high_prices, low_prices, close_prices, volumes = get_klines(symbol, interval, limit)
    signal_score = 0
    signal_details = []

    # EMA200
    ema200 = calculate_ema(close_prices, 200)
    if close_prices[-1] > ema200[-1]:
        signal_score += 1
        signal_details.append("✅ Above EMA200 (Uptrend)")
    else:
        signal_details.append("❌ Below EMA200 (Downtrend)")

    # MACD
    macd_hist = calculate_macd(close_prices)
    if macd_hist[-1] > 0:
        signal_score += 1
        signal_details.append("✅ MACD Histogram > 0 (Bullish)")
    else:
        signal_details.append("❌ MACD Histogram < 0 (Bearish)")

    # RSI
    rsi = calculate_rsi(close_prices)
    if rsi[-1] < 30:
        signal_score += 1
        signal_details.append("✅ RSI Oversold (<30)")
    elif rsi[-1] > 70:
        signal_details.append("❌ RSI Overbought (>70)")
    else:
        signal_details.append("✅ RSI Normal")

    # Volume Spike
    if detect_volume_spike(volumes):
        signal_score += 1
        signal_details.append("✅ Volume Spike Detected")
    else:
        signal_details.append("❌ No Volume Spike")

    # Supertrend
    supertrend_data = calculate_supertrend(high_prices, low_prices, close_prices)
    if supertrend_data and supertrend_data[-1][1] == "up":
        signal_score += 1
        signal_details.append("✅ Supertrend Up")
    else:
        signal_details.append("❌ Supertrend Down")

    # Fibonacci
    levels = get_fibonacci_levels(max(high_prices), min(low_prices))
    price_now = close_prices[-1]
    near_fibo = any(abs(price_now - levels[level]) / price_now < 0.01 for level in ['50.0%', '61.8%'])
    if near_fibo:
        signal_score += 1
        signal_details.append("✅ Near Fibonacci Level (0.5 / 0.618)")
    else:
        signal_details.append("❌ Not near Fibonacci key levels")

    # Candlestick
    patterns = detect_candlestick_pattern(open_prices, high_prices, low_prices, close_prices)
    if patterns:
        signal_score += 1
        signal_details.append(f"✅ Candlestick Pattern: {', '.join(patterns)}")
    else:
        signal_details.append("❌ No Candlestick Pattern")

    # Final Signal
    signal = "BUY" if signal_score >= 5 else "NO SIGNAL"
    strength = f"{signal_score}/7 indikator aktif"
    return signal, strength, signal_details

if __name__ == "__main__":
    signal, strength, details = analyze()
    print(f"\n📊 Sinyal: {signal} ({strength})")
    for d in details:
        print("•", d)
