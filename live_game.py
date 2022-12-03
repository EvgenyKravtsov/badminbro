import distributor
import model


class LiveGame:
    def __init__(self):
        #self.players = []
        self.players = [
            model.Player('A', 1543, 0),
            model.Player('B', 1522, 0),
            model.Player('C', 1456, 0),
            model.Player('D', 1643, 0),
            model.Player('E', 1743, 0),
            model.Player('F', 1343, 0),
            model.Player('G', 1233, 0),
            model.Player('H', 1513, 0),
        ]
        self.active_match = []
        self.played_matches = []

    def add_player(self, player):
        self.players.append(player)

    def start(self):
        # return distributor.distribute_players_for_match(self.players)
        active_match = self.players[0:4]
        self.active_match.clear
        self.active_match.extend(active_match)
        return active_match

    def next_match(self):
        # return distributor.distribute_players_for_match(self.players)
        played_match = []
        for player in self.active_match:
            played_match.append(player)
        self.played_matches.append(played_match)
        active_match = self.players[4:8]
        self.active_match.clear()
        self.active_match.extend(active_match)
        return active_match
