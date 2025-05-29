import subprocess
import telegram

# === Token dan Channel langsung ditulis di sini ===
TELEGRAM_TOKEN = '7572191853:AAEU5FS92jtsLmfRykBPHAeZUKqi34uLn8k'
CHANNEL_ID = '-1002594990660'  # pakai tanda minus (-) di depan kalau ID numerik

def get_signal():
    # Jalankan strategy.py untuk ambil sinyal
    result = subprocess.run(["python3", "strategy.py"], capture_output=True, text=True)
    return result.stdout

def send_to_telegram(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    signal_text = get_signal()
    print("Mengirim sinyal ke Telegram...")
    send_to_telegram(signal_text)
