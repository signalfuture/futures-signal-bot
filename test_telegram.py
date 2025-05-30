import requests

BOT_TOKEN = "7572191853:AAEU5FS92jtsLmfRykBPHAeZUKqi34uLn8k"
CHAT_ID = "-1002594990660"
MESSAGE = "✅ Test berhasil! Bot trading otomatis sudah terhubung ke channel."

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": MESSAGE
}

response = requests.post(url, data=payload)

print("Status Code:", response.status_code)
print("Response Text:", response.text)
