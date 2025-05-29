def calculate_ema(data, period=200):
    """
    Menghitung Exponential Moving Average (EMA).
    :param data: list harga penutupan
    :param period: periode EMA (default 200)
    :return: list nilai EMA
    """
    if len(data) < period:
        return None

    ema = []
    k = 2 / (period + 1)
    ema.append(sum(data[:period]) / period)  # EMA pertama = SMA

    for price in data[period:]:
        ema.append((price - ema[-1]) * k + ema[-1])

    return ema
