import os
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import distributor

badminbro_bot_token = "5898643664:AAG7eDcktsFFNQAwK1DE5I6uBcK0TlAMQUQ"

updater = Updater(token=badminbro_bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    chat_id = update.effective_chat.id

    replied_message = update.effective_message.reply_to_message.text
    replied_message_strings = replied_message.split("\n")

    def string_to_player(player_as_string):
        number = player_as_string.split(".")[0].strip()
        if number.isnumeric():
            name = player_as_string.split(".")[1].strip()
            return Player(number, name)

    players = list(filter(lambda item: item is not None, list(
        map(string_to_player, replied_message_strings))))

    context.bot.send_message(
        chat_id=chat_id, text=distributor.distribute_players_for_games(players))


dispatcher.add_handler(CommandHandler("start", start))

# updater.start_polling()
updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path=badminbro_bot_token,
                      webhook_url="https://badminbro.herokuapp.com/" + badminbro_bot_token
                      )


####

class Player:
    def __init__(self, number, name):
        self.number = number
        self.name = name
