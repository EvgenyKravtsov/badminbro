from flask import Flask
from flask import Response
from flask_cors import CORS
import json
import os

debug = False


def run_server(storage):
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def get_players_ratings():
        players_cursor = storage.get_players()
        keys = ['name', 'rating']

        data = [dict(zip(keys, user)) for user in players_cursor]
        players_json = json.dumps(data, indent=4)

        return Response(players_json, mimetype='application/json')

    if (debug):
        if __name__ == 'server':
            app.run(port=8000)
    else:
        if __name__ == 'server':
            port = int(os.environ.get("PORT", 5000))
            app.run(host='0.0.0.0', port=port)
