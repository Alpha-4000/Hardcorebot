import requests
from config import config

BASE_URL = "https://api.telegram.org/bot"  # Telegram API bazasi

def bot(method, params=None):
    """Telegram API chaqiruvi"""
    if params is None:
        params = {}
    token = config.get("bot_token")
    url = f"{BASE_URL}{token}/{method}"
    resp = requests.post(url, data=params).json()
    return resp

def send_message(chat_id, text, parse_mode="HTML"):
    return bot("sendMessage", {"chat_id": chat_id, "text": text, "parse_mode": parse_mode})

def send_channel_message(text):
    kanal_id = config.get("kanal_id")
    if kanal_id:
        return send_message(kanal_id, text)
    else:
        print("⚠ Kanal ID sozlanmagan")
        return None

def edit_message(chat_id, message_id, text, parse_mode="HTML"):
    return bot("editMessageText", {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text,
        "parse_mode": parse_mode
    })
