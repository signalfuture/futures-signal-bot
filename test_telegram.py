import os
import requests
from dotenv import load_dotenv

# Load variabel dari .env
load_dotenv()

# Ambil variabel dari file .env
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHANNEL_ID")
MESSAGE = "✅ Bot berhasil terhubung dan kirim sinyal ke Telegram!"

# Kirim pesan ke Telegram
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": MESSAGE
}

response = requests.post(url, data=payload)
print("Status:", response.status_code)
print("Respon:", response.text)
