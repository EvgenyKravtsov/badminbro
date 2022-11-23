import os
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

badminbro_bot_token = "5898643664:AAG7eDcktsFFNQAwK1DE5I6uBcK0TlAMQUQ"

updater = Updater(token=badminbro_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id, text="Jack is a King of Badminton")


dispatcher.add_handler(CommandHandler("start", start))

# updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=badminbro_bot_token,
                      webhook_url="https://badminbro.herokuapp.com/" + badminbro_bot_token
                      )
