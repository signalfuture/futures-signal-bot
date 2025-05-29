# indicators/ema.py

def calculate_ema(data, period=200):
    """
    Menghitung Exponential Moving Average (EMA)
    data: list harga penutupan
    period: periode EMA (default 200)
    """
    if len(data) < period:
        return None
    ema = []
    k = 2 / (period + 1)
    ema.append(sum(data[:period]) / period)  # SMA pertama
    for price in data[period:]:
        ema.append((price - ema[-1]) * k + ema[-1])
    return ema
