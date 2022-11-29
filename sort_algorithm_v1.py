import random
import string

class Player:
    def __init__(self, rank, name):
        self.rank = rank
        self.name = name

def generate_random_player():
    name_length = random.randint(4, 7)
    name = random.choice(string.ascii_letters).upper()
    for _ in range(name_length):
        name += random.choice(string.ascii_letters).lower()
    rank = random.randint(1450, 1950)
    return Player(rank, name)




num_players = 10

players = [generate_random_player() for _ in range(num_players)]

for player in players:
    print(player.name, ': ', player.rank, sep='')

