import pandas as pd
from indicators.ema import calculate_ema
from indicators.macd import calculate_macd
from indicators.rsi import calculate_rsi
from indicators.volume_spike import detect_volume_spike  # ✅ Perbaikan di sini
from indicators.supertrend import calculate_supertrend
from indicators.fibonacci import calculate_fibonacci_levels
from indicators.candlestick import detect_candlestick_pattern
from binance.client import Client
from config import BINANCE_API_KEY, BINANCE_API_SECRET

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def analyze_symbol(symbol):
    try:
        klines = client.get_klines(symbol=symbol, interval=Client.KLINE_INTERVAL_1HOUR, limit=100)
        df = pd.DataFrame(klines, columns=[
            'timestamp', 'open', 'high', 'low', 'close', 'volume',
            'close_time', 'quote_asset_volume', 'number_of_trades',
            'taker_buy_base_volume', 'taker_buy_quote_volume', 'ignore'
        ])
        df['open'] = df['open'].astype(float)
        df['high'] = df['high'].astype(float)
        df['low'] = df['low'].astype(float)
        df['close'] = df['close'].astype(float)
        df['volume'] = df['volume'].astype(float)
        return analyze_strategy(df)
    except Exception as e:
        print(f"Error analyzing {symbol}: {e}")
        return None

def analyze_strategy(df):
    result = {
        "entry_signal": None,
        "strength": 0,
        "details": []
    }

    # 1. EMA 200
    ema200 = calculate_ema(df['close'], 200)
    if df['close'].iloc[-1] > ema200.iloc[-1]:
        result["strength"] += 1
        result["details"].append("✅ Harga di atas EMA200")
    else:
        result["details"].append("❌ Harga di bawah EMA200")

    # 2. MACD
    macd_signal = calculate_macd(df)
    if macd_signal == "buy":
        result["strength"] += 1
        result["details"].append("✅ MACD: Sinyal Buy")
    else:
        result["details"].append("❌ MACD: Bukan Sinyal Buy")

    # 3. RSI
    rsi = calculate_rsi(df['close'])
    if rsi.iloc[-1] < 30:
        result["strength"] += 1
        result["details"].append("✅ RSI Oversold")
    else:
        result["details"].append("❌ RSI bukan oversold")

    # 4. Volume Spike ✅ (perbaikan sesuai request)
    if detect_volume_spike(df):
        result["strength"] += 1
        result["details"].append("✅ Volume Spike Terdeteksi")
    else:
        result["details"].append("❌ Tidak ada Volume Spike")

    # 5. Supertrend
    supertrend_signal = calculate_supertrend(df)
    if supertrend_signal == "buy":
        result["strength"] += 1
        result["details"].append("✅ Supertrend: Buy")
    else:
        result["details"].append("❌ Supertrend: Bukan Buy")

    # 6. Fibonacci
    fib_signal = calculate_fibonacci_levels(df)
    if fib_signal == "support":
        result["strength"] += 1
        result["details"].append("✅ Dekat Support Fibonacci")
    else:
        result["details"].append("❌ Tidak di support Fibonacci")

    # 7. Candlestick Pattern
    pattern = detect_candlestick_pattern(df)
    if pattern == "bullish":
        result["strength"] += 1
        result["details"].append("✅ Pola Candlestick Bullish")
    else:
        result["details"].append("❌ Tidak ada pola bullish")

    # Kesimpulan Entry
    if result["strength"] >= 5:
        result["entry_signal"] = "STRONG BUY"
    elif result["strength"] >= 3:
        result["entry_signal"] = "WEAK BUY"
    else:
        result["entry_signal"] = "NO ENTRY"

    return result
