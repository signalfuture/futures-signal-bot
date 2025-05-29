def detect_candlestick_pattern(open_prices, high_prices, low_prices, close_prices):
    """
    Deteksi pola candlestick sederhana
    :return: list pola yang terdeteksi di candle terakhir, bisa kosong
    """
    patterns = []
    if len(close_prices) < 2:
        return patterns

    o = open_prices[-1]
    h = high_prices[-1]
    l = low_prices[-1]
    c = close_prices[-1]
    body = abs(c - o)
    candle_range = h - l

    # Doji
    if body < 0.1 * candle_range:
        patterns.append("Doji")

    # Hammer
    if body > 0.2 * candle_range and (h - max(c, o)) < 0.1 * candle_range and (min(c, o) - l) > 0.5 * candle_range:
        patterns.append("Hammer")

    # Engulfing
    prev_o = open_prices[-2]
    prev_c = close_prices[-2]
    if prev_c < prev_o and c > o and c > prev_o and o < prev_c:
        patterns.append("Bullish Engulfing")
    elif prev_c > prev_o and c < o and c < prev_o and o > prev_c:
        patterns.append("Bearish Engulfing")

    return patterns
