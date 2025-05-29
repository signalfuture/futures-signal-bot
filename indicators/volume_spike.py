def detect_volume_spike(volume_data, period=20, multiplier=2):
    """
    Deteksi lonjakan volume jika volume sekarang > rata-rata * multiplier
    :param volume_data: list volume
    :param period: berapa candle terakhir untuk rata-rata
    :param multiplier: berapa kali lipat dianggap spike
    :return: True jika spike, False jika tidak
    """
    if len(volume_data) < period + 1:
        return False

    avg_volume = sum(volume_data[-period-1:-1]) / period
    current_volume = volume_data[-1]

    return current_volume > avg_volume * multiplier
