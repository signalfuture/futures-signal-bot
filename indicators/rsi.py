def calculate_rsi(data, period=14):
    """
    Menghitung Relative Strength Index (RSI)
    :param data: list harga penutupan
    :param period: periode RSI (default 14)
    :return: list RSI
    """
    if len(data) < period:
        return []

    gains = []
    losses = []

    for i in range(1, period + 1):
        delta = data[i] - data[i - 1]
        gains.append(max(0, delta))
        losses.append(max(0, -delta))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    rsi_list = []

    for i in range(period, len(data)):
        delta = data[i] - data[i - 1]
        gain = max(0, delta)
        loss = max(0, -delta)

        avg_gain = (avg_gain * (period - 1) + gain) / period
        avg_loss = (avg_loss * (period - 1) + loss) / period

        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        rsi = 100 - (100 / (1 + rs)) if avg_loss != 0 else 100

        rsi_list.append(rsi)

    return rsi_list
