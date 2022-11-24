def distribute_players_for_games(players):
    games_count = 8

    position_1 = [0, 0, 6, 6, 2, 2, 6, 6]
    position_2 = [1, 4, 7, 0, 0, 4, 4, 2]
    position_3 = [2, 1, 4, 7, 3, 3, 7, 7]
    position_4 = [3, 5, 5, 1, 1, 5, 5, 3]

    pairs1_list = []
    pairs2_list = []
    length_list = []
    games_list = []

    for i in range(games_count):
        pare1 = ('{{ {} & {} }}'.format(
            players[position_1[i]].name, players[position_2[i]].name))
        pare2 = ('{{ {} & {} }}'.format(
            players[position_3[i]].name, players[position_4[i]].name))
        pairs1_list.append(pare1)
        pairs2_list.append(pare2)
        length_list.append(len(pare1))
        length_list.append(len(pare2))
        games_list.append('Game ' + str(i + 1))

    length_max = max(length_list)

    displayable_pairs_list = []

    for i in range(games_count):
        displayable_pairs_list.append('-' * length_max)
        steps1 = (length_max - len(pairs1_list[i])) // 2
        displayable_pairs_list.append(' ' * steps1 + pairs1_list[i])
        stepsG = (length_max - len(games_list[i])) // 2
        displayable_pairs_list.append(' ' * stepsG + games_list[i])
        steps2 = (length_max - len(pairs2_list[i])) // 2
        displayable_pairs_list.append(' ' * steps2 + pairs2_list[i])
        displayable_pairs_list.append('-' * length_max)

    return ("\n".join(displayable_pairs_list))
