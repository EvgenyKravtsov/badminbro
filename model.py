from enum import IntEnum


class Player:
    def __init__(self, name, rating, matches_played, matches_won, games_played_in_a_row, participation_in_the_last_game):
        self.name = name
        self.rating = rating
        self.matches_played = matches_played
        self.matches_won = matches_won
        self.games_played_in_a_row = games_played_in_a_row
        self.participation_in_the_last_game = participation_in_the_last_game

    def __eq__(self, other):
        return self.name == other.name


class WinningTeam(IntEnum):
    LEFT_TEAM = 0
    RIGHT_TEAM = 1


class Match:
    def __init__(self, players, winning_team):
        self.players = players
        self.winning_team = winning_team
