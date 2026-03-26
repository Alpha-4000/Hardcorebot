# menus.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu():
    keyboard = [
        [InlineKeyboardButton("💱 Yangi almashuv", callback_data="yangi_obmen")],
        [InlineKeyboardButton("📊 Mening almashuvlarim", callback_data="my_exchanges")],
        [InlineKeyboardButton("⚙️ Sozlamalar", callback_data="settings")],
    ]
    return InlineKeyboardMarkup(keyboard)

def confirm_exchange_menu(ex_id):
    keyboard = [
        [InlineKeyboardButton("✅ Tasdiqlash", callback_data=f"confirm_{ex_id}")],
        [InlineKeyboardButton("❌ Bekor qilish", callback_data=f"cancel_{ex_id}")],
    ]
    return InlineKeyboardMarkup(keyboard)

def back_to_menu():
    keyboard = [[InlineKeyboardButton("⬅️ Orqaga", callback_data="back")]]
    return InlineKeyboardMarkup(keyboard)

def admin_panel():
    keyboard = [
        [InlineKeyboardButton("📥 Qabul qilinadigan obmenlar", callback_data="pending_exchanges")],
        [InlineKeyboardButton("📤 Yakunlangan obmenlar", callback_data="completed_exchanges")],
        [InlineKeyboardButton("⬅️ Orqaga", callback_data="back")],
    ]
    return InlineKeyboardMarkup(keyboard)
