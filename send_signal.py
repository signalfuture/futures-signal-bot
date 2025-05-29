import subprocess
import telegram
import os

# === Konfigurasi ===
TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")  # atau langsung isi 'token' jika tidak pakai .env
CHANNEL_ID = os.getenv("CHANNEL_ID")     # contoh: '@namachannelkamu'

def get_signal():
    result = subprocess.run(["python3", "strategy.py"], capture_output=True, text=True)
    return result.stdout

def send_to_telegram(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    signal_text = get_signal()
    print("Mengirim sinyal ke Telegram...")
    send_to_telegram(signal_text)
