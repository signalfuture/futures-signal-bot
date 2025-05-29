# main.py

import requests
from config import BINANCE_API_KEY, BINANCE_API_SECRET

def get_price(symbol="BTCUSDT", interval="5m", limit=10):
    url = f"https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    response = requests.get(url, params=params)
    data = response.json()
    return data

if __name__ == "__main__":
    candles = get_price()
    for c in candles:
        print(f"Time: {c[0]}, Open: {c[1]}, High: {c[2]}, Low: {c[3]}, Close: {c[4]}")
