import os
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import distributor
import ranking_engine
import storage
import server

badminbro_bot_token = "5898643664:AAG7eDcktsFFNQAwK1DE5I6uBcK0TlAMQUQ"

updater = Updater(token=badminbro_bot_token, use_context=True)
dispatcher = updater.dispatcher

debug = False


def start(update, context):
    chat_id = update.effective_chat.id

    replied_message = update.effective_message.reply_to_message.text
    players = __parse_players_from_replied_message(replied_message)

    context.bot.send_message(
        chat_id=chat_id, text=distributor.distribute_players_for_games(players))


def rank(update, context):
    chat_id = update.effective_chat.id

    replied_message = update.effective_message.reply_to_message.text
    players = __parse_players_from_replied_message(replied_message)

    player_numbers_to_rank = update.effective_message.text.split(" ")[1]

    rankedPlayers = []
    for i, player_number_to_rank in enumerate(player_numbers_to_rank):
        for player in players:
            if (player.number) == player_number_to_rank:
                rankedPlayers.append(
                    ranking_engine.RankedPlayer(player, i <= 1))

    storageInstance = None
    if (debug):
        storageInstance = storage.LocalPostgresDatabase()
    else:
        storageInstance = storage.HerokuPostgresDatabase()

    displayable_updated_ratings = ranking_engine.rank_players(
        rankedPlayers, storage=storageInstance)

    context.bot.send_message(chat_id=chat_id, text=displayable_updated_ratings)


def __parse_players_from_replied_message(replied_message):
    replied_message_strings = replied_message.split("\n")

    def string_to_player(player_as_string):
        number = player_as_string.split(".")[0].strip()
        if number.isnumeric():
            name = player_as_string.split(".")[1].strip()
            return Player(number, name)

    return list(filter(lambda item: item is not None, list(
        map(string_to_player, replied_message_strings))))


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("rank", rank))

if (debug):
    updater.start_polling()
else:
    updater.start_webhook(listen="0.0.0.0",
                          port=int(os.environ.get('PORT', 5000)),
                          url_path=badminbro_bot_token,
                          webhook_url="https://badminbro.herokuapp.com/" + badminbro_bot_token
                          )

storageInstance = None
if (debug):
    storageInstance = storage.LocalPostgresDatabase()
else:
    storageInstance = storage.HerokuPostgresDatabase()
server.run_server(storageInstance)


class Player:
    def __init__(self, number, name):
        self.number = number
        self.name = name
