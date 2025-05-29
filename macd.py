def calculate_macd(data, fast_period=12, slow_period=26, signal_period=9):
    """
    Menghitung MACD dan garis sinyal.
    :param data: list harga penutupan
    :param fast_period: periode EMA cepat (default 12)
    :param slow_period: periode EMA lambat (default 26)
    :param signal_period: periode sinyal (default 9)
    :return: tuple (macd_line, signal_line, histogram)
    """
    if len(data) < slow_period:
        return None, None, None

    def ema(values, period):
        k = 2 / (period + 1)
        ema_list = [sum(values[:period]) / period]
        for price in values[period:]:
            ema_list.append((price - ema_list[-1]) * k + ema_list[-1])
        return ema_list

    slow_ema = ema(data, slow_period)
    fast_ema = ema(data[-len(slow_ema):], fast_period)
    macd_line = [f - s for f, s in zip(fast_ema, slow_ema)]

    signal_line = ema(macd_line, signal_period)
    histogram = [m - s for m, s in zip(macd_line[-len(signal_line):], signal_line)]

    return macd_line[-len(signal_line):], signal_line, histogram
