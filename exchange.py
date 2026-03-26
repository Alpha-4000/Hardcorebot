# exchange.py
from aiogram import types
from aiogram.types import ParseMode
from datetime import datetime
from config import get_config  # configdan admin va kanal ID olish

config = get_config()  # {'bot_token': ..., 'admin_id': ..., 'kanal_id': ...}

async def send_exchange_to_channel(bot, exchange):
    """
    Kanalga yangi almashinuv xabarini yuboradi.
    exchange = {
        'id': 12345,
        'user_id': 123456789,
        'user_name': 'Ism Familya',
        'system': 'uzcard > humo',
        'amount': 95000,
        'status': '✅ Bajarildi'
    }
    """
    kanal_id = config['kanal_id']
    vaqti = datetime.now().strftime("%d.%m.%Y %H:%M")
    
    text = (
        f"🤖 <b>Yangi almashinuv (obmen):</b>\n\n"
        f"🆔 <b>Almashuv ID'si:</b> <code>{exchange['id']}</code>\n"
        f"👤 <b>Almashuvchi:</b> <a href='tg://user?id={exchange['user_id']}'>{exchange['user_name']}</a>\n"
        f"🔀 <b>Almashuv tizimi:</b> {exchange['system']}\n"
        f"📆 <b>Almashuv vaqti:</b> {vaqti}\n"
        f"🔎 <b>Status:</b> {exchange['status']}\n"
        f"💰 <b>Almashuv miqdori:</b> {exchange['amount']} so'm"
    )

    await bot.send_message(chat_id=kanal_id, text=text, parse_mode=ParseMode.HTML) 
