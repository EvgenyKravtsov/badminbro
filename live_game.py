import distributor
import model


class LiveGame:
    def __init__(self):
        self.players = []
        # self.players = [
        #     model.Player(name='A', rating=1500, matches_played=0, matches_won=0,
        #                  games_played_in_a_row=0, participation_in_the_last_game=False),
        #     model.Player(name='B', rating=1500, matches_played=0, matches_won=0,
        #                  games_played_in_a_row=0, participation_in_the_last_game=False),
        #     model.Player(name='C', rating=1500, matches_played=0, matches_won=0,
        #                  games_played_in_a_row=0, participation_in_the_last_game=False),
        #     model.Player(name='D', rating=1500, matches_played=0, matches_won=0,
        #                  games_played_in_a_row=0, participation_in_the_last_game=False),
        #     model.Player(name='E', rating=1500, matches_played=0, matches_won=0,
        #                  games_played_in_a_row=0, participation_in_the_last_game=False),
        #     model.Player(name='F', rating=1500, matches_played=0, matches_won=0,
        #                  games_played_in_a_row=0, participation_in_the_last_game=False),
        #     model.Player(name='G', rating=1500, matches_played=0, matches_won=0,
        #                  games_played_in_a_row=0, participation_in_the_last_game=False),
        #     model.Player(name='H', rating=1500, matches_played=0, matches_won=0,
        #                  games_played_in_a_row=0, participation_in_the_last_game=False),
        # ]
        self.active_match = []
        self.played_matches = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

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
