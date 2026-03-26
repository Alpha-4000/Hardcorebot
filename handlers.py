from utils import send_message, send_channel_message, edit_message
from config import config

# Bu yerda barcha foydalanuvchi xabarlarini qabul qilamiz
def handle_message(update):
    message = update.get("message")
    if not message:
        return

    chat_id = message["chat"]["id"]
    text = message.get("text", "")

    # Admin buyruqlari
    if chat_id == config.get("admin_id"):
        if text.startswith("/set_channel"):
            parts = text.split()
            if len(parts) == 2:
                config["kanal_id"] = int(parts[1])
                send_message(chat_id, f"✅ Kanal ID yangilandi: {parts[1]}")
            else:
                send_message(chat_id, "⚠ To'g'ri format: /set_channel kanal_id")
            return
        if text.startswith("/status"):
            send_message(chat_id, f"Bot holati:\nKanal: {config.get('kanal_id')}\nAdmin: {config.get('admin_id')}")
            return

    # Oddiy foydalanuvchi xabarlari
    send_message(chat_id, f"Siz yubordingiz: {text}")

# Callback querylarni boshqarish
def handle_callback(update):
    callback = update.get("callback_query")
    if not callback:
        return

    chat_id = callback["message"]["chat"]["id"]
    message_id = callback["message"]["message_id"]
    data = callback.get("data")

    if data == "approve":
        edit_message(chat_id, message_id, "✅ Tasdiqlandi")
        send_channel_message(f"💡 Foydalanuvchi xabari tasdiqlandi")
    elif data == "reject":
        edit_message(chat_id, message_id, "❌ Rad etildi")
