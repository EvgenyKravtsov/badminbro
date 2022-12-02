import itertools


def distribute_players_for_match(players):
    players_in_game = [players[i]
                       for i in range(4)]  # list of players in current game
    players_number_in_game = [0, 1, 2, 3]  # list for creating permutation set

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
    for number in players_number_in_game:
        players[number].games_played_in_a_row += 1

    # update players in rest list
    max_games = -1
    go_rest_players_numbers_list = []
    for _ in range(2):
        for number in players_number_in_game:
            if players[number].games_played_in_a_row > max_games:
                max_games = players[number].games_played_in_a_row
        for number in players_number_in_game:
            if players[number].games_played_in_a_row == max_games:
                go_rest_player = players_number_in_game.pop(
                    players_number_in_game.index(number))
                go_rest_players_numbers_list.append(go_rest_player)
                break

    # find players with min games played in a row
    two_min_games_count = []
    all_games_count = [player.games_played_in_a_row for player in players]
    for _ in range(2):
        min_count = min(all_games_count)
        two_min_games_count.append(all_games_count.pop(
            all_games_count.index(min_count)))

    players_number_in_rest = [i for i in range(len(
        players)) if i != players_number_in_game[0] and i != players_number_in_game[1]]

    # update players in game list
    while len(two_min_games_count) > 0:
        for i in range(len(players_number_in_rest)):
            if players[players_number_in_rest[i]].games_played_in_a_row == two_min_games_count[0]:
                players_number_in_game.append(players_number_in_rest[i])
                del two_min_games_count[0]
                if len(two_min_games_count) == 0:
                    break

    return [players[players_number_in_game[i]] for i in range(4)]
