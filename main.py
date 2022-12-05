import storage
import live_game
from server import run_server


debug = False

storage_instance = None
if (debug):
    storage_instance = storage.LocalPostgresDatabase()
else:
    storage_instance = storage.HerokuPostgresDatabase()
live_game = live_game.LiveGame()
run_server(storage_instance, live_game)
