import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Retrieve the bot token from environment variables
TOKEN = os.getenv('7779249464:AAFGRO9NaUSNBg5Utt2VHSHcZYfDhzke3AQ')

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello! I am your bot.')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
