import os
import asyncio
import websockets
import json
import model
import ranking_engine

debug = True


async def run_server(storage, game):
    async def handler(websocket, path):
        while True:
            data = await websocket.recv()
            reply = __handle_message_from_client(data)
            await websocket.send(reply)

    def __handle_message_from_client(message):
        messageComponents = message.split(':')
        event = messageComponents[0]
        if (len(messageComponents) > 1):
            parameter = message.split(':')[1]
        match event:
            case 'init':
                players_cursor = storage.get_players()
                keys = ['name', 'rating', 'matches_played', 'matches_won']

                data = [dict(zip(keys, user)) for user in players_cursor]
                players_json = json.dumps(data, indent=4)

                return players_json
            case 'get_game':
                game_json = json.dumps(game, default=vars)
                return game_json
            case 'add_player_to_game':
                playerFromStorage = storage.get_player(parameter)
                player = model.Player(playerFromStorage[0], playerFromStorage[1], playerFromStorage[2],
                                      playerFromStorage[3], playerFromStorage[4], playerFromStorage[5])

                game.add_player(player)

                game_json = json.dumps(game, default=vars)
                return game_json
            case 'remove_player_from_game':
                playerFromStorage = storage.get_player(parameter)
                player = model.Player(playerFromStorage[0], playerFromStorage[1], playerFromStorage[2],
                                      playerFromStorage[3], playerFromStorage[4], playerFromStorage[5])

                game.remove_player(player)

                game_json = json.dumps(game, default=vars)
                return game_json
            case 'start_game':
                game.start()
                game_json = json.dumps(game, default=vars)
                return game_json
            case 'get_next_match':
                winning_team_param = int(parameter)
                ranking_engine.rank_players(
                    game.active_match, winning_team_param, storage)  # 0 - left team won, 1 - right team won

                winning_team = model.WinningTeam.LEFT_TEAM
                if (winning_team_param == 0):
                    winning_team = model.WinningTeam.LEFT_TEAM
                elif (winning_team_param == 1):
                    winning_team = model.WinningTeam.RIGHT_TEAM
                game.get_next_match(winning_team)

                game_json = json.dumps(game, default=vars)
                return game_json

    if (debug):
        async with websockets.serve(handler, 'localhost', 8000):
            await asyncio.Future()
    else:
        port = int(os.environ.get('PORT', 5000))
        async with websockets.serve(handler, '0.0.0.0', port):
            await asyncio.Future()
