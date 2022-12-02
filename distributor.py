import itertools


def distribute_players_for_match(players):

    fresh_players_number = [i for i in range(len(players)) if players[i].participation_in_the_last_game == False]
    played_players_number = [i for i in range(len(players)) if players[i].participation_in_the_last_game == True]

    players_in_game = []  # list of players in current game
    players_number_in_game = []  # list for creating permutation set

    # find players with min games played in a row
    min_games_count = []
    all_games_count = [players[i].games_played_in_a_row for i in played_players_number]
    for i in range(len(all_games_count)):
        min_count = min(all_games_count)
        min_games_count.append(all_games_count.pop(all_games_count.index(min_count)))
        if i == 1:
            break
    
    len_games_count = len(min_games_count)

    while len(min_games_count) > 0:
        for i in range(len(played_players_number)):
            if players[played_players_number[i]].games_played_in_a_row == min_games_count[0]:
                players_number_in_game.append(played_players_number[i])
                players_in_game.append(players[played_players_number[i]])
                del min_games_count[0]
                if len(min_games_count) == 0:
                    break

    print('pig_1:', players_number_in_game)

    all_games_count.clear()
    all_games_count = [players[i].games_played_in_a_row for i in fresh_players_number]

    for _ in range(4 - len_games_count):
        min_count = min(all_games_count)
        min_games_count.append(all_games_count.pop(all_games_count.index(min_count)))

    while len(min_games_count) > 0:
        for i in range(len(fresh_players_number)):
            if players[fresh_players_number[i]].games_played_in_a_row == min_games_count[0]:
                players_number_in_game.append(fresh_players_number[i])
                players_in_game.append(players[fresh_players_number[i]])
                del min_games_count[0]
                if len(min_games_count) == 0:
                    break

    print('pig_2:', players_number_in_game)

    # find rank balance between teams
    team_rating_diff = abs((players_in_game[0].rating + players_in_game[1].rating) - (
        players_in_game[2].rating + players_in_game[3].rating))
    perm_set = itertools.permutations(players_number_in_game)
    for i in perm_set:
        local_team_rating_diff = abs(
            (players[i[0]].rating + players[i[1]].rating) - (players[i[2]].rating + players[i[3]].rating))
        if local_team_rating_diff <= team_rating_diff:
            team_rating_diff = local_team_rating_diff
            players_number_in_game.clear()
            players_number_in_game = [j for j in i]

    # update games played in a row for each player in current match
    for player in players:
        player.participation_in_the_last_game = False


    print(players_number_in_game)

    for number in players_number_in_game:
        players[number].games_played_in_a_row += 1
        players[number].participation_in_the_last_game = True


    # # update players in rest list
    # max_games = -1
    # go_rest_players_numbers_list = []
    # for _ in range(2):
    #     for number in players_number_in_game:
    #         if players[number].games_played_in_a_row > max_games:
    #             max_games = players[number].games_played_in_a_row
    #     for number in players_number_in_game:
    #         if players[number].games_played_in_a_row == max_games:
    #             go_rest_player = players_number_in_game.pop(
    #                 players_number_in_game.index(number))
    #             go_rest_players_numbers_list.append(go_rest_player)
    #             break

    # # find players with min games played in a row
    # two_min_games_count = []
    # all_games_count = [player.games_played_in_a_row for player in players]
    # for _ in range(2):
    #     min_count = min(all_games_count)
    #     two_min_games_count.append(all_games_count.pop(
    #         all_games_count.index(min_count)))

    # players_number_in_rest = [i for i in range(len(
    #     players)) if i != players_number_in_game[0] and i != players_number_in_game[1]]

    # # update players in game list
    # while len(two_min_games_count) > 0:
    #     for i in range(len(players_number_in_rest)):
    #         if players[players_number_in_rest[i]].games_played_in_a_row == two_min_games_count[0]:
    #             players_number_in_game.append(players_number_in_rest[i])
    #             del two_min_games_count[0]
    #             if len(two_min_games_count) == 0:
    #                 break

    return [players[players_number_in_game[i]] for i in range(4)]
