def distribute_players_for_games(players):
    games_count = 8

    position_1 = [0, 0, 6, 6, 2, 2, 6, 6]
    position_2 = [1, 4, 7, 0, 0, 4, 4, 2]
    position_3 = [2, 1, 4, 7, 3, 3, 7, 7]
    position_4 = [3, 5, 5, 1, 1, 5, 5, 3]

    pairs_list = []
    length_list = []

    for i in range(games_count):
        pair = ('{{ {} & {} }} - Game {} - {{ {} & {} }}'.format(
            players[position_1[i]].name, players[position_2[i]].name, i + 1, players[position_3[i]].name, players[position_4[i]].name))
        pairs_list.append(pair)
        length_list.append(pair.index('-'))

    length_max = max(length_list)

    displayable_pairs_list = []

    for i in range(games_count):
        steps = length_max - length_list[i]
        displayable_pairs_list.append(' ' * steps + pairs_list[i])

    return ("\n".join(displayable_pairs_list))
