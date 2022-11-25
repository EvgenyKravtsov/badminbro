def rank_players(rankedPlayers, storage):
    for rankedPlayer in rankedPlayers:
        rankedPlayer.current_rating = storage.get_player_rating(
            rankedPlayer.player.name)

    players_won = []
    players_lost = []

    for player in rankedPlayers:
        if player.won:
            players_won.append(player)
        else:
            players_lost.append(player)

    players_won_combined_rating = (
        players_won[0].current_rating + players_won[1].current_rating) / 2
    players_lost_combined_rating = (
        players_lost[0].current_rating + players_lost[1].current_rating) / 2

    players_won_transformed_rating = 10**(players_won_combined_rating / 400)
    players_lost_transformed_rating = 10**(players_lost_combined_rating / 400)

    players_won_expected_score = players_won_transformed_rating / \
        (players_won_transformed_rating + players_lost_transformed_rating)
    players_lost_expected_score = players_lost_transformed_rating / \
        (players_won_transformed_rating + players_lost_transformed_rating)

    k_factor = 32

    for player in players_won:
        player.updated_rating = int(
            player.current_rating + k_factor * (1 - players_won_expected_score))

    for player in players_lost:
        player.updated_rating = int(
            player.current_rating + k_factor * (0 - players_lost_expected_score))

    displayble_result = ["Updated ratings:"]

    for ranked_player in rankedPlayers:
        storage.update_player_rating(ranked_player.player.name, ranked_player.updated_rating)
        displayble_result.append(
            f"{ranked_player.player.name} - {ranked_player.updated_rating}")

    return "\n".join(displayble_result)


class RankedPlayer:
    current_rating = 0
    updated_rating = 0

    def __init__(self, player, won):
        self.player = player
        self.won = won
