# indicators/volume_spike.py

def detect_volume_spike(df):
    """
    Deteksi apakah volume spike terjadi.
    Volume spike dianggap terjadi jika volume candle terakhir
    > 1.5x rata-rata volume 20 candle sebelumnya.
    """
    if df is None or df.empty or len(df) < 22:
        return False

    recent_volume = df['volume'].iloc[-1]
    average_volume = df['volume'].iloc[-21:-1].mean()

    return recent_volume > 1.5 * average_volume
