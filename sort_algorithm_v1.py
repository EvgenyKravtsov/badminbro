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

def get_players_list():
    print()
    while True:
        request = input('How many players in game (4 - 20)?: ')
        if request.isnumeric():
            num = int(request)
            if num < 4:
                print()
                print('Too little :(')
                print()
            elif num > 20:
                print()
                print('Too much :(')
                print()
            else:
                num_players_in_game = num
                break
        else:
            print()
            print('Please, insert a number.')
            print()

    players = [generate_random_player() for _ in range(num_players_in_game)]

    print()
    print('PLAYERS:')
    for player in players:
        print(player.name, ': ', player.rank, sep='')
    print()

    return players



players = get_players_list()

# sorting

