import json
import os
import model
import ranking_engine
from flask import Flask, Response, request
from flask_cors import CORS


debug = False


def run_server(storage, live_game):
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def get_players_ratings():
        players_cursor = storage.get_players()
        keys = ['name', 'rating', 'matches_played', 'matches_won']

        data = [dict(zip(keys, user)) for user in players_cursor]
        players_json = json.dumps(data, indent=4)

        return Response(players_json, mimetype='application/json')

    @app.route('/get_live_game')
    def get_live_game():
        live_game_json = json.dumps(live_game, default=vars)
        return Response(live_game_json, mimetype='application/json')

    @app.route('/add_player_to_live_game')
    def add_player_to_live_game():
        params = request.args
        player_name_param = params.get('player_name')

        playerFromStorage = storage.get_player(player_name_param)
        player = model.Player(
            playerFromStorage[0], playerFromStorage[1], playerFromStorage[2], playerFromStorage[3], playerFromStorage[4], playerFromStorage[5])

        live_game.add_player(player)

        players_json = json.dumps([ob.__dict__ for ob in live_game.players])

        return Response(players_json, mimetype='application/json')

    @app.route('/start_live_game')
    def start_live_game():
        players = live_game.start()
        players_json = json.dumps([ob.__dict__ for ob in players])
        return Response(players_json, mimetype='application/json')

    @app.route('/get_players_for_next_match')
    def get_players_for_next_match():
        params = request.args
        winning_team_param = params.get('winning_team')
        ranking_engine.rank_players(
            live_game.active_match, winning_team_param, storage)  # 0 - left team won, 1 - right team won
        active_match = live_game.next_match()
        played_matches = live_game.played_matches
        response = GetPlayersForNextMatchResponse(active_match, played_matches)
        response_json = json.dumps(response, default=vars)
        return Response(response_json, mimetype='application/json')

    if (debug):
        if __name__ == 'server':
            app.run(port=8000)
    else:
        if __name__ == 'server':
            port = int(os.environ.get("PORT", 5000))
            app.run(host='0.0.0.0', port=port)


class GetPlayersForNextMatchResponse:
    def __init__(self, active_match, played_matches):
        self.active_match = active_match
        self.played_matches = played_matches
