from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = '7779249464:AAFGRO9NaUSNBg5Utt2VHSHcZYfDhzke3AQ'

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Forward a video to me, and I will give you a direct link to watch it.')

def handle_video(update: Update, context: CallbackContext):
    # Log the incoming message details for debugging
    print("Received message:", update.message)

    # Check if the message contains a video
    if update.message.video:
        video_file_id = update.message.video.file_id
        file_info = context.bot.get_file(video_file_id)
        file_link = file_info.file_path
        update.message.reply_text(f'Watch the video here: {file_link}')
    elif update.message.forward_from or update.message.forward_from_chat:
        # This checks if the message is forwarded
        if update.message.video:
            video_file_id = update.message.video.file_id
            file_info = context.bot.get_file(video_file_id)
            file_link = file_info.file_path
            update.message.reply_text(f'Watch the video here: {file_link}')
        elif update.message.reply_to_message and update.message.reply_to_message.video:
            # Check if the video is in the reply
            video_file_id = update.message.reply_to_message.video.file_id
            file_info = context.bot.get_file(video_file_id)
            file_link = file_info.file_path
            update.message.reply_text(f'Watch the video here: {file_link}')
        else:
            update.message.reply_text("Please forward a video message.")
    else:
        update.message.reply_text("Please forward a video message.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.video | Filters.forwarded, handle_video))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()