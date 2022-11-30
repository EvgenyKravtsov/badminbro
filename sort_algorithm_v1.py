import random
import string
import itertools

class Player:
    def __init__(self, rank, name, local_games_count):
        self.rank = rank
        self.name = name
        self.local_games_count = local_games_count

def generate_random_player():
    name_length = random.randint(4, 7)
    name = random.choice(string.ascii_letters).upper()
    for _ in range(name_length):
        name += random.choice(string.ascii_letters).lower()
    rank = random.randint(1450, 1950)
    return Player(rank, name, 0)

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

def sorting_players_for_local_game(players):
    players_in_game = [players[i] for i in range(4)] # list of players in current game
    players_number_in_game = [0, 1, 2, 3] # list for creating permutation set

    while True:
        # find rank balance between teams
        team_rank_diff = abs((players_in_game[0].rank + players_in_game[1].rank) - (players_in_game[2].rank + players_in_game[3].rank))
        perm_set = itertools.permutations(players_number_in_game)
        for i in perm_set:
            local_team_rank_diff = abs((players[i[0]].rank + players[i[1]].rank) - (players[i[2]].rank + players[i[3]].rank))
            if local_team_rank_diff <= team_rank_diff:
                team_rank_diff = local_team_rank_diff
                players_number_in_game.clear()
                players_number_in_game = [j for j in i]

        print('NOW PLAY')
        print('{} [{}] & {} [{}]'.format(players[players_number_in_game[0]].name, players[players_number_in_game[0]].rank, players[players_number_in_game[1]].name, players[players_number_in_game[1]].rank))
        print('{} [{}] & {} [{}]'.format(players[players_number_in_game[2]].name, players[players_number_in_game[2]].rank, players[players_number_in_game[3]].name, players[players_number_in_game[3]].rank))
        print()

        # update local games count
        for number in players_number_in_game:
            players[number].local_games_count += 1

        # update players in rest list
        max_games = -1
        go_rest_players_numbers_list = []
        for _ in range(2):
            for number in players_number_in_game:
                if players[number].local_games_count > max_games:
                    max_games = players[number].local_games_count
            for number in players_number_in_game:
                if players[number].local_games_count == max_games:
                    go_rest_player = players_number_in_game.pop(players_number_in_game.index(number))
                    go_rest_players_numbers_list.append(go_rest_player)
                    break

        # find players with min local games count
        two_min_games_count = []
        all_games_count = [player.local_games_count for player in players]
        for _ in range(2):
            min_count = min(all_games_count)
            two_min_games_count.append(all_games_count.pop(all_games_count.index(min_count)))

        players_number_in_rest = [i for i in range(len(players)) if i != players_number_in_game[0] and i != players_number_in_game[1]]

        # update players in game list
        while len(two_min_games_count) > 0:
            for i in range (len(players_number_in_rest)):
                if players[players_number_in_rest[i]].local_games_count == two_min_games_count[0]:
                    players_number_in_game.append(players_number_in_rest[i])
                    del two_min_games_count[0]
                    if len(two_min_games_count) == 0:
                        break

        players_in_game = [players[players_number_in_game[i]] for i in range(4)] 

        print('PLAYERS:')
        for player in players:
            print(player.name, ': ', player.local_games_count, sep='')
        print()

        continue_game = input('Next game? y/n: ')
        if continue_game == 'n':
            break
        print()


players = get_players_list()

sorting_players_for_local_game(players)
