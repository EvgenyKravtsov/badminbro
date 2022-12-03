def rank_players(players, winning_team, storage):
    players_won = []
    players_lost = []

    if (winning_team == 0):
        players_won.append(players[0])
        players_won.append(players[1])
        players_lost.append(players[2])
        players_lost.append(players[3])
    else:
        players_won.append(players[2])
        players_won.append(players[3])
        players_lost.append(players[0])
        players_lost.append(players[1])

    players_won_combined_rating = (
        players_won[0].rating + players_won[1].rating) / 2
    players_lost_combined_rating = (
        players_lost[0].rating + players_lost[1].rating) / 2

    players_won_transformed_rating = 10**(players_won_combined_rating / 400)
    players_lost_transformed_rating = 10**(players_lost_combined_rating / 400)

    players_won_expected_score = players_won_transformed_rating / \
        (players_won_transformed_rating + players_lost_transformed_rating)
    players_lost_expected_score = players_lost_transformed_rating / \
        (players_won_transformed_rating + players_lost_transformed_rating)

    k_factor = 32

    for player in players_won:
        player.rating = int(
            player.rating + k_factor * (1 - players_won_expected_score))

    for player in players_lost:
        player.rating = int(
            player.rating + k_factor * (0 - players_lost_expected_score))

    for player in players_won:
        player.matches_played = player.matches_played + 1
        player.matches_won = player.matches_won + 1
        storage.update_player_rating(
            player.name, player.rating, player.matches_played, player.matches_won)
    for player in players_lost:
        player.matches_played = player.matches_played + 1
        storage.update_player_rating(
            player.name, player.rating, player.matches_played, player.matches_won)
