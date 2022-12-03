import distributor
import model


class LiveGame:
    def __init__(self):
        self.players = []
        self.active_match = []
        self.played_matches = []

    def add_player(self, player):
        self.players.append(player)

    def start(self):
        active_match = distributor.distribute_players_for_match(self.players)
        self.active_match.clear
        self.active_match.extend(active_match)
        return active_match

    def next_match(self):
        played_match = []
        for player in self.active_match:
            played_match.append(player)
        self.played_matches.append(played_match)
        active_match = distributor.distribute_players_for_match(self.players)
        self.active_match.clear()
        self.active_match.extend(active_match)
        return active_match
