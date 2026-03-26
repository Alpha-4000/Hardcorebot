from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler, Filters, CallbackContext
from config import config
from handlers import handle_message, handle_callback

bot = Bot(token=config["bot_token"])

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 Bot ishga tushdi!")

def message_router(update: Update, context: CallbackContext):
    handle_message(update.to_dict())

def callback_router(update: Update, context: CallbackContext):
    handle_callback(update.to_dict())

def main():
    updater = Updater(token=config["bot_token"], use_context=True)
    dp = updater.dispatcher

    # /start buyrug‘i
    dp.add_handler(CommandHandler("start", start))

    # Foydalanuvchi xabarlari
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_router))

    # Callback querylar
    dp.add_handler(CallbackQueryHandler(callback_router))

    # Botni ishga tushurish
    updater.start_polling()
    print("Bot ishga tushdi...")
    updater.idle()

if __name__ == "__main__":
    main()
