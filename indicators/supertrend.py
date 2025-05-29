def calculate_supertrend(high, low, close, period=10, multiplier=3):
    """
    Menghitung indikator Supertrend
    :param high: list harga tertinggi
    :param low: list harga terendah
    :param close: list harga penutupan
    :param period: periode ATR
    :param multiplier: multiplier ATR untuk band
    :return: list tuple (supertrend, direction) -> direction: "up" / "down"
    """
    if len(close) < period:
        return []

    atr = []
    for i in range(1, len(close)):
        tr = max(high[i] - low[i], abs(high[i] - close[i-1]), abs(low[i] - close[i-1]))
        if i <= period:
            atr.append(tr)
        else:
            atr.append((atr[-1] * (period - 1) + tr) / period)

    final_upperband = []
    final_lowerband = []
    supertrend = []
    direction = []

    for i in range(period, len(close)):
        hl2 = (high[i] + low[i]) / 2
        upperband = hl2 + (multiplier * atr[i])
        lowerband = hl2 - (multiplier * atr[i])

        if i == period:
            final_upperband.append(upperband)
            final_lowerband.append(lowerband)
            supertrend.append(lowerband if close[i] > upperband else upperband)
            direction.append("up" if close[i] > upperband else "down")
        else:
            if close[i] > final_upperband[-1]:
                direction.append("up")
                supertrend.append(max(lowerband, supertrend[-1]))
            elif close[i] < final_lowerband[-1]:
                direction.append("down")
                supertrend.append(min(upperband, supertrend[-1]))
            else:
                direction.append(direction[-1])
                supertrend.append(supertrend[-1])

            final_upperband.append(upperband)
            final_lowerband.append(lowerband)

    return list(zip(supertrend, direction))
