import distributor
import model


class LiveGame:
    def __init__(self):
        #self.players = []
        self.players = [
            model.Player('A', 1543, 0, False),
            model.Player('B', 1522, 0, False),
            model.Player('C', 1456, 0, False),
            model.Player('D', 1643, 0, False),
            model.Player('E', 1743, 0, False),
            model.Player('F', 1343, 0, False),
            model.Player('G', 1233, 0, False),
            model.Player('H', 1513, 0, False),
        ]

    def add_player(self, player):
        self.players.append(player)

    def start(self):
        return distributor.distribute_players_for_match(self.players)
