import asyncio
import storage
import game
import server


debug = True

storage_implementation = None
if (debug):
    storage_implementation = storage.LocalPostgresDatabase()
else:
    storage_implementation = storage.HerokuPostgresDatabase()

game = game.Game()

asyncio.run(server.run_server(storage_implementation, game))
