import json
import os
import model
from flask import Flask, Response, request
from flask_cors import CORS


debug = True


def run_server(storage, live_game):
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def get_players_ratings():
        players_cursor = storage.get_players()
        keys = ['name', 'rating']

        data = [dict(zip(keys, user)) for user in players_cursor]
        players_json = json.dumps(data, indent=4)

        return Response(players_json, mimetype='application/json')

    @app.route('/get_live_game_players')
    def get_live_game_players():
        players = live_game.players
        players_json = json.dumps([ob.__dict__ for ob in players])
        return Response(players_json, mimetype='application/json')

    @app.route('/add_player_to_live_game')
    def add_player_to_live_game():
        params = request.args
        player_name_param = params.get('player_name')

        player = storage.get_player(player_name_param)

        live_game.add_player(player)

        players = []
        for player_tuple in live_game.players:
            players.append(model.Player(player_tuple[0], player_tuple[1]))

        players_json = json.dumps([ob.__dict__ for ob in players])

        return Response(players_json, mimetype='application/json')

    @app.route('/start_live_game')
    def start_live_game():
        players = live_game.start()
        players_json = json.dumps([ob.__dict__ for ob in players])
        return Response(players_json, mimetype='application/json')

    if (debug):
        if __name__ == 'server':
            app.run(port=8000)
    else:
        if __name__ == 'server':
            port = int(os.environ.get("PORT", 5000))
            app.run(host='0.0.0.0', port=port)
